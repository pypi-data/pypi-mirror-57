# -*- coding: utf-8 -*-
import atexit
import logging
import os
import re
import signal
import sys

import pexpect
from plumbum import local, ProcessExecutionError

from frutils.exceptions import FrklException
from frutils.frutils import execute_external_comand

log = logging.getLogger("frutils")

SSH_OUTPUT_REGEX = re.compile(
    "SSH_AUTH_SOCK=(?P<socket>[^;]+).*SSH_AGENT_PID=(?P<pid>\\d+)",
    re.MULTILINE | re.DOTALL,
)


def start_ssh_agent(sock_path=None, kill_at_exit=True):

    ssh_agent_command = "ssh-agent"
    args = ["-s"]

    if sock_path is not None:

        if os.path.exists(sock_path):
            raise Exception("Custom ssh socket already exists: {}".format(sock_path))

        sock_path = os.path.realpath(sock_path)
        dir_name = os.path.dirname(sock_path)
        os.makedirs(dir_name, exist_ok=True)

        args.append("-a")
        args.append(sock_path)

    rc, stdout, stderr = execute_external_comand(ssh_agent_command, args)
    match = SSH_OUTPUT_REGEX.search(stdout)
    if not match:
        raise Exception("Invalid ssh-agent output: {}".format(stdout))

    details = match.groupdict()
    os.environ["SSH_AUTH_SOCK"] = details["socket"]
    os.environ["SSH_AGENT_PID"] = details["pid"]
    if kill_at_exit:
        atexit.register(kill_ssh_agent)
        signal.signal(signal.SIGTERM, kill_ssh_agent)
        # signal.signal(signal.SIGINT, kill_ssh_agent)

    return details


def kill_ssh_agent(*args, **kwargs):

    sock = os.environ.get("SSH_AUTH_SOCK", None)
    pid = os.environ.get("SSH_AGENT_PID", None)
    with local.env(SSH_AUTH_SOCK=sock, SSH_AGENT_PID=pid):
        if sock is not None:
            log.debug("Killing ssh agent...")
            ssh_agent = local["ssh-agent"]
            ssh_agent(["-k"])

    if sock is not None:
        del os.environ["SSH_AUTH_SOCK"]
    if pid is not None:
        del os.environ["SSH_AGENT_PID"]


def get_default_ssh_key():

    ssh_key_path = os.path.join(os.path.expanduser("~"), ".ssh", "id_rsa")
    return ssh_key_path


def add_default_ssh_key_to_agent(
    start_agent=True,
    kill_agent_at_exit=True,
    password_callback=None,
    ssh_agent_sock_path=None,
):

    default_key_path = get_default_ssh_key()

    if not os.path.exists(default_key_path):
        raise FrklException(
            msg="Can't add default ssh key.",
            reason="No default ssh key available (on: {})".format(default_key_path),
            solution="Create an ssh key, e.g.:\n\n    ssh-keygen -t rsa -b 4096 -C 'your_email@example.com'",
            references={
                "digital ocean blog post": "https://www.digitalocean.com/docs/droplets/how-to/add-ssh-keys/create-with-openssh/"
            },
        )

    return add_ssh_key_to_agent(
        default_key_path,
        start_agent=start_agent,
        kill_agent_at_exit=kill_agent_at_exit,
        password_callback=password_callback,
        ssh_agent_sock_path=ssh_agent_sock_path,
    )


def add_ssh_key_to_agent(
    key_path,
    start_agent=True,
    kill_agent_at_exit=True,
    password_callback=None,
    ssh_agent_sock_path=None,
):

    key_path = os.path.realpath(key_path)

    try:
        # check whether key needs a password
        rc, stdout, stderr = execute_external_comand(
            "ssh-keygen", ["-y", "-f", key_path, "-P", ""]
        )

        if rc == 0:
            password = False
        else:
            password = True
    except (ProcessExecutionError) as e:
        log.debug(e, exc_info=1)
        password = True

    if not password:
        return

    if not os.environ.get("SSH_AUTH_SOCK", None):

        if os.path.exists(ssh_agent_sock_path):
            os.environ["SSH_AUTH_SOCK"] = ssh_agent_sock_path

            keys = get_agent_ssh_keys()
            if key_path in keys:
                return
        else:

            if start_agent:
                start_ssh_agent(
                    sock_path=ssh_agent_sock_path, kill_at_exit=kill_agent_at_exit
                )
            else:
                raise FrklException(
                    msg="Can't add ssh key to ssh agent.",
                    reason="No ssh-agent process running, or SSH_AUTH_SOCK environment variable not set.",
                    solution='Start ssh-agent and export the relevant environment variables, e.g.:\n\n    eval "$(ssh-agent -s)"',
                    references={
                        "GitHub blog post": "https://help.github.com/en/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent"
                    },
                )

    try:
        success = False
        retry_bad_password = True

        while not success:
            child = pexpect.spawn(
                "ssh-add",
                args=[key_path],
                env={"SSH_AUTH_SOCK": os.environ["SSH_AUTH_SOCK"]},
            )
            child.expect("Enter passphrase for {}:".format(key_path))

            if password_callback is None:

                def default_pw_callback():

                    raise Exception(
                        "ssh key needs password, but no password callback specified."
                    )

                password_callback = default_pw_callback

            password = password_callback()

            child.sendline(password)

            i = child.expect(
                ["Bad passphrase.*", "Identity added.*", "Error connecting to agent.*"]
            )
            if i == 0:
                child.kill(0)
            elif i == 1:
                child.wait()
            else:
                child.kill(0)

            rc = child.exitstatus
            if rc != 0:
                if i == 0:
                    if retry_bad_password:
                        print(
                            "Bad passphrase, please try again (or enter Ctrl-C to quit).\n"
                        )
                        continue
                    else:
                        raise FrklException(
                            msg="Could not add ssh key to ssh-agent.",
                            reason="Bad passphrase.",
                            solution="Try again with the correct passphrase.",
                        )
                else:
                    raise FrklException(
                        msg="Could not add ssh key to ssh-agent.",
                        reason="ssh-agent not running, or not discoverable.",
                    )
            else:
                success = True
    except (KeyboardInterrupt):
        print("User interrupted process, exiting...")
        sys.exit(1)
    except (FrklException) as fe:
        raise fe
    except (Exception) as e:
        raise FrklException(
            "Could not add ssh key to ssh-agent.",
            solution="Check existing ssh-agent processes, and your SSH_AUTH_SOCK environment variable, you may have that variable set, but the ssh-agent process is gone. In that case, delete the file SSH_AUTH_SOCK points to.",
            reason=str(e),
        )

    return success


def agent_is_available(sock=None):

    if sock is None:
        sock = os.environ.get("SSH_AUTH_SOCK", None)

    if sock is None:
        return False

    return os.path.exists(sock)


def get_agent_ssh_keys(sock=None):

    if sock is None:
        sock = os.environ.get("SSH_AUTH_SOCK", None)

    if not sock:
        return []

    with local.env(
        SSH_AUTH_SOCK=sock,
        # SSH_AGENT_PID=os.environ["SSH_AGENT_PID"],
    ):

        try:
            rc, stdout, stderr = execute_external_comand("ssh-add", ["-l"])

            if rc != 0:
                raise Exception("Could not list agent ssh keys: {}".format(stderr))

            result = []
            for line in stdout.split("\n"):
                if not line:
                    continue
                tokens = line.split(" ")
                result.append(tokens[2])
        except (ProcessExecutionError):
            result = []

        return result
