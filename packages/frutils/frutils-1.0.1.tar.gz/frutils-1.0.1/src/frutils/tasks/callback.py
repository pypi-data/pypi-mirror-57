# -*- coding: utf-8 -*-
import abc
import inspect
import io
import json
import logging
import os
import sys
import threading

import click
import fasteners
import six
import stevedore
from colorama import Fore, Style
from halo import Halo
from stevedore import ExtensionManager

from frutils import get_terminal_size
from frutils.doc import Doc

log = logging.getLogger("frutils")


CURSOR_UP_ONE = "\x1b[1A"
ERASE_LINE = "\x1b[2K"

BOLD = "\033[1m"
UNBOLD = "\033[0m"

ARC_DOWN_RIGHT = u"\u256d"
ARC_UP_RIGHT = u"\u2570"
ARC_UP_LEFT = u"\u256f"
VERTICAL_RIGHT = u"\u251C"
VERTICAL_LEFT = u"\u2528"
VERTICAL = u"\u2502"
HORIZONTAL = u"\u2500"
END = u"\u257C"
ARROW = u"\u279B"
OK = u"\u2713"
ARROR_RESULT = u"\u257C"


def output_to_terminal(line, nl=True, no_output=False, err=False):

    if no_output:
        return

    click.echo(line.encode("utf-8"), nl=nl, err=err)


def delete_last_line(no_display=False, err=False):

    if no_display:
        return

    if not err:
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)
    else:
        sys.stderr.write(CURSOR_UP_ONE)
        sys.stderr.write(ERASE_LINE)


def get_all_callback_classes():
    """Load all callback classes."""

    log2 = logging.getLogger("stevedore")
    out_hdlr = logging.StreamHandler(sys.stdout)
    out_hdlr.setFormatter(
        logging.Formatter("load callback classes plugin error -> %(message)s")
    )
    out_hdlr.setLevel(logging.DEBUG)
    log2.addHandler(out_hdlr)
    log2.setLevel(logging.INFO)

    log.debug("Loading callback classes...")

    mgr = ExtensionManager(
        namespace="frutils.callbacks",
        invoke_on_load=True,
        propagate_map_exceptions=True,
    )

    result = {}
    for plugin in mgr:
        name = plugin.name
        ep = plugin.entry_point
        adapter = ep.load()
        result[name] = adapter()

    return result


def get_callback_doc(callback_class):

    doc_content = callback_class.__doc__
    if not doc_content:
        doc_content = ""
    doc_content = inspect.cleandoc(doc_content)
    doc = Doc(doc_content)
    return doc


def load_callback(callback_name, callback_config=None):
    """Loading a freckles callback extension.

    Returns:
      frutils.tasks.callback.TasksCallback: the callback object
    """

    if callback_config is None:
        callback_config = {}

    log2 = logging.getLogger("stevedore")
    out_hdlr = logging.StreamHandler(sys.stdout)
    out_hdlr.setFormatter(logging.Formatter("task plugin plugin error -> %(message)s"))
    out_hdlr.setLevel(logging.DEBUG)
    log2.addHandler(out_hdlr)
    log2.setLevel(logging.INFO)

    log.debug("Loading freckles callback...")

    mgr = stevedore.driver.DriverManager(
        namespace="frutils.callbacks",
        name=callback_name,
        invoke_on_load=True,
        invoke_kwds=callback_config,
    )
    log.debug(
        "Registered plugins: {}".format(", ".join(ext.name for ext in mgr.extensions))
    )

    return mgr.driver


def colorize_status(status, ignore_errors=False):

    if status == "ok":
        result = Fore.GREEN + status + Style.RESET_ALL
    elif status == "no change" or status == "unchanged":
        result = Fore.GREEN + status + Style.RESET_ALL
    elif status == "skipped":
        result = Fore.YELLOW + status + Style.RESET_ALL
    elif status == "failed":
        if not ignore_errors:
            result = Fore.RED + status + Style.RESET_ALL
        else:
            result = Fore.YELLOW + "{} (ignored)".format(status) + Style.RESET_ALL
    else:
        result = status

    return result


@six.add_metaclass(abc.ABCMeta)
class TasksCallback(object):
    def __init__(self, **kwargs):

        if "use_stderr" in kwargs.keys():
            self._use_stderr = kwargs["use_stderr"]
        else:
            self._use_stderr = False

        if "silent" in kwargs.keys():
            self._silent = kwargs["silent"]
        else:
            self._silent = False

        pass

    @property
    def use_stderr(self):

        return self._use_stderr

    @use_stderr.setter
    def use_stderr(self, use_stderr):
        self._use_stderr = use_stderr

    @abc.abstractmethod
    def task_started(self):

        pass

    @abc.abstractmethod
    def task_finished(self):

        pass

    def task_paused(self):

        pass

    def task_resumed(self):

        pass

    def finished(self):

        pass

    def output_to_terminal(self, line, nl=True):

        if self._silent:
            return

        output_to_terminal(line, nl=nl, no_output=self._silent, err=self._use_stderr)


class TasksCallbackSilent(TasksCallback):
    """Task callback that displays no output.
    """

    def __init__(self, **kwargs):

        super(TasksCallbackSilent, self).__init__(**kwargs)

    def task_started(self, task):

        pass

    def task_finished(self, task):

        pass


class TasksCallbackLog(TasksCallback):
    """Callback to add events to the application log."""

    def __init__(self, **kwargs):

        super(TasksCallbackLog, self).__init__(**kwargs)

        profile = kwargs.get("profile", "DEBUG")
        self._logger = log
        try:
            self._log_level = logging._nameToLevel[profile]
        except (Exception):
            self._log_level = 10

    def task_started(self, task):
        self._logger.log(self._log_level, "task started: {}".format(task.msg))

    def task_finished(self, task):
        self._logger.log(self._log_level, "task finished: {}".format(task.msg))


class TasksCallbackJson(TasksCallback):
    """Callback to output json messages for events.

    Each event outputs one one-line json string.
    """

    def __init__(self, **kwargs):

        super(TasksCallbackJson, self).__init__(**kwargs)

    def task_started(self, task):

        json_string = json.dumps({"output_type": "run_log", "value": task.to_dict()})
        self.output_to_terminal(json_string)

    def task_finished(self, task):

        json_string = json.dumps({"output_type": "run_log", "value": task.to_dict()})
        self.output_to_terminal(json_string)


class TasksCallbackLogfile(TasksCallback):
    """Callback to write events to a log file.

    By default, logs are written to a file 'tasks_log.json' in the current directory. The json format is the same
    as for the 'json' callback.
    """

    def __init__(self, **kwargs):

        super(TasksCallbackLogfile, self).__init__(**kwargs)
        self.log_file = kwargs.get("path", os.path.join(os.getcwd(), "tasks_log.json"))
        self._keep_file_open = True
        self._file_handle = None
        if self._keep_file_open:
            self._file_handle = io.open(
                self.log_file, "w", encoding="utf-8", buffering=1
            )
        self._lock = threading.Lock()

    def finish(self):

        if self._keep_file_open:
            self._file_handle.close()

    @fasteners.locked
    def _write(self, task):

        task_dict = {"output_type": "run_log", "value": task.to_dict()}

        if not self._keep_file_open:
            with io.open(self.log_file, "a", encoding="utf-8") as f:
                json.dump(task_dict, f)
                f.write("\n")
        else:
            json.dump(task_dict, self._file_handle)
            self._file_handle.write("\n")

    def task_started(self, task):

        self._write(task)

    def task_finished(self, task):

        self._write(task)


class TasksCallbackPlain(TasksCallback):
    """Callback with plain string output for task events."""

    def __init__(self, **kwargs):

        super(TasksCallbackPlain, self).__init__(**kwargs)

        self._parent_task_open = False
        self._detail_level = 10
        self._debug = kwargs.get("debug", False)

    def task_started(self, task):

        if task.detail_level > self._detail_level:
            return

        if not self._debug:
            padding = "  " * task.level
            if self._parent_task_open:
                click.echo()
            self.output_to_terminal(u"{}- {}".format(padding, task.msg), nl=False)
            self._parent_task_open = True
        else:
            padding = "-" * task.level
            self.output_to_terminal(
                u"-{} STARTING ({}): {}".format(padding, task.id, task.msg), nl=True
            )

    def task_finished(self, task):

        if task.detail_level > self._detail_level:
            return

        if task.success:
            if task.skipped is True:
                status = "skipped"
            else:
                if task.changed is True:
                    status = "ok"
                else:
                    status = "no change"
        else:
            status = "failed"

        status = colorize_status(status, task.ignore_errors)

        if not self._debug:
            if not self._parent_task_open:
                return

            self.output_to_terminal(u" -> {}".format(status))
            self._parent_task_open = False
        else:
            padding = "-" * task.level
            self.output_to_terminal(
                u"-{} FINISHED {} ({}) -> {}".format(
                    padding, task.msg, task.id, status
                ),
                nl=True,
            )

        # if not task.success:
        #     reindent_level = (2 * (task.level+2))
        #     if task.get_messages():
        #         if "\n" not in task.get_messages().strip():
        #             click.echo(reindent("msg: {}".format(task.get_messages().strip()), reindent_level))
        #         else:
        #             click.echo(reindent(u"msg:", reindent_level))
        #             click.echo(reindent(task.get_messages(), reindent_level+2))
        #     if task.get_error_messages():
        #         if "\n" not in task.get_error_messages().strip():
        #             click.echo(reindent("error: {}".format(task.get_error_messages().strip()), reindent_level))
        #         else:
        #             click.echo(reindent(u"error:", reindent_level))
        #             click.echo(reindent(task.get_error_messages(), reindent_level+2))

    def task_paused(self):

        pass
        # click.echo()

    def task_resumed(self):

        pass


PROFILE_MAP = {"full": {"show_skipped": True, "show_no_change": True, "show_msg": True}}


def get_callback_config_value(key, config, default, profile_name=None):

    if config.get(key, None) is not None:
        return config[key]

    if profile_name is not None:
        profile = PROFILE_MAP.get(profile_name, None)
        if profile is not None:
            if profile.get(key, None) is not None:
                return profile[key]

    return default


class TasksCallbackDefault(TasksCallback):
    """Fancypants task event outputs.

    This outputs escape characters, so it is not supported by all terminals."""

    def __init__(self, **kwargs):

        super(TasksCallbackDefault, self).__init__(**kwargs)

        self._detail_level = 10
        self.last_level = 0

        self.started_tasks = {}

        profile_name = kwargs.pop("profile", None)

        self.show_skipped = get_callback_config_value(
            key="show_skipped", config=kwargs, default=False, profile_name=profile_name
        )
        self.show_no_change = get_callback_config_value(
            key="show_no_change",
            config=kwargs,
            default=False,
            profile_name=profile_name,
        )
        self.show_msg = get_callback_config_value(
            key="show_msg", config=kwargs, default=False, profile_name=profile_name
        )

    def get_task_started_string(self, task):

        current_level = task.level

        if current_level == 0:
            msg = u"{}{} {}".format(ARC_DOWN_RIGHT, END, task.msg)
        else:
            if current_level == 1:
                padding = ""
            else:
                padding = u"  {}".format(VERTICAL) * (current_level - 1)

            padding = padding + u"  {}".format(VERTICAL_RIGHT)
            msg = u"{}{}{} {}".format(VERTICAL, padding, END, task.msg)

        return msg

    def get_finished_padding(self, task):

        padding = u"  {}".format(VERTICAL) * task.level
        return padding

    def get_task_finished_status(self, task):

        if task.success:
            if task.skipped is True:
                status = "skipped"
            else:
                if task.changed is True:
                    status = "ok"
                else:
                    status = "no change"
        else:
            status = "failed"
        status = colorize_status(status, task.ignore_errors)

        msg = u"{}{}  {}{} {}".format(
            VERTICAL,
            self.get_finished_padding(task),
            ARC_UP_RIGHT,
            ARROR_RESULT,
            status,
        )

        return msg

    def get_msg_string(self, task):

        padding = self.get_finished_padding(task)

        if "\n" not in task.get_messages().strip():
            msg = u"{}{}  {} msg: {}".format(
                VERTICAL, padding, VERTICAL_RIGHT, task.get_messages().strip()
            )
        else:
            msg = u"{}{}  {} msg:".format(VERTICAL, padding, VERTICAL_RIGHT)

            for line in task.get_messages().strip().split("\n"):
                msg = msg + u"\n{}{}  {}   {}".format(VERTICAL, padding, VERTICAL, line)

        return msg

    def get_error_msg_string(self, task):

        padding = self.get_finished_padding(task)

        if "\n" not in task.get_error_messages().strip():
            msg = u"{}{}  {} {}error{}: {}".format(
                VERTICAL,
                padding,
                VERTICAL_RIGHT,
                Fore.RED,
                Style.RESET_ALL,
                task.get_error_messages().strip(),
            )
        else:

            msg = u"{}{}  {} {}error{}:".format(
                VERTICAL, padding, VERTICAL_RIGHT, Fore.RED, Style.RESET_ALL
            )
            for line in task.get_error_messages().strip().split("\n"):
                msg = msg + u"\n{}{}  {}   {}".format(VERTICAL, padding, VERTICAL, line)

        return msg

    def get_task_conclusion(self, task):

        if task.success:
            tasks_status = "ok"
        else:
            tasks_status = "failed"

        tasks_status = colorize_status(tasks_status)

        msg = u"{}{} {}".format(ARC_UP_RIGHT, ARROR_RESULT, tasks_status)
        return msg

    def task_started(self, task):

        if task.detail_level > self._detail_level:
            return

        msg = self.get_task_started_string(task)
        self.print_msg(task, msg)

    def print_msg(self, task, msg):
        self.output_to_terminal(msg)

        self.started_tasks.setdefault(task.id, []).append(msg)

    def remove_printed_lines(self, task):

        msgs = self.started_tasks.get(task.id, None)
        if msgs is None:
            return

        new_lines = 0
        for msg in msgs:
            new_lines = new_lines + 1
            new_lines = new_lines + msg.count("\n")
            width = get_terminal_size()[0]
            if len(msg) > get_terminal_size()[0]:
                extra_lines = int(len(msg) / width)
                new_lines = new_lines + extra_lines

        if new_lines < 1:
            return

        for i in range(0, new_lines):
            delete_last_line(err=self.use_stderr)

    def task_finished(self, task):

        if task.detail_level > self._detail_level:
            return

        try:
            if (task.success or not task.success and task.ignore_errors) and (
                task.level != 0 or task._tasks.is_utility_task
            ):
                skip = False
                if task.skipped and not self.show_skipped:
                    skip = True

                if not task.changed and not self.show_no_change:
                    skip = True

                if task.get_messages(detail_level=0) or (
                    self.show_msg and task.get_messages()
                ):
                    skip = False

                if skip:
                    self.remove_printed_lines(task)
                    return
                if self.show_msg or task.get_messages(detail_level=0):
                    if task.get_messages():
                        msg = self.get_msg_string(task)
                        self.print_msg(task, msg)

            if not task.success and (task.get_messages() or task.get_error_messages()):

                if task.get_messages():
                    msg = self.get_msg_string(task)
                    self.print_msg(task, msg)

                if task.get_error_messages():
                    msg = self.get_error_msg_string(task)
                    self.print_msg(task, msg)

            msg = self.get_task_finished_status(task)
            self.print_msg(task, msg)

        finally:

            if task.level == 0:

                if not task._tasks.is_utility_task:
                    msg = self.get_task_conclusion(task)
                    self.output_to_terminal(msg)
                elif task._tasks.is_utility_task and task.changed:
                    msg = self.get_task_conclusion(task)
                    self.output_to_terminal(msg)
                elif task._tasks.is_utility_task and not task.skipped:
                    msg = self.get_task_conclusion(task)
                    self.output_to_terminal(msg)
                elif task._tasks.is_utility_task and task.skipped and self.show_skipped:
                    msg = self.get_task_conclusion(task)
                    self.output_to_terminal(msg)
                elif (
                    task._tasks.is_utility_task
                    and not task.changed
                    and self.show_no_change
                ):
                    msg = self.get_task_conclusion(task)
                    self.output_to_terminal(msg)

                self.started_tasks = {}

    def task_paused(self):

        pass
        # click.echo()

    def task_resumed(self):

        pass


class TasksCallbackAuto(TasksCallback):
    """Wrapper callback that auto-selects a callback based on the terminal properties.

    If 'utf-8' is present in the 'LANG' environment variable value and the command is not piped, one of the fancy
    human-readable callbacks is used. If the current command is piped, the 'plain' callback is selected.
     If 'utf-8' is not present the 'default' callback is used.
    """

    def __init__(self, **kwargs):

        super(TasksCallbackAuto, self).__init__(**kwargs)

        lang = os.environ.get("LANG", "").lower()

        if "utf-8" in lang:
            if not self.use_stderr:
                if sys.stdout.isatty():
                    callback = "spinner"
                else:
                    callback = "plain"
            else:
                if sys.stderr.isatty():
                    callback = "default"
                else:
                    callback = "plain"
        else:
            callback = "default"

        if callback == "default":
            self.callback = TasksCallbackDefault(**kwargs)
        elif callback == "spinner":
            self.callback = TasksCallbackSpinner(**kwargs)
        elif callback == "plain":
            self.callback = TasksCallbackPlain(**kwargs)
        else:
            self.callback = TasksCallbackDefault(**kwargs)

    def __getattr__(self, name):

        return getattr(self.callback, name)

    def task_paused(self):

        self.callback.task_paused()

    def task_resumed(self):

        self.callback.task_resumed()

    def task_started(self, task):

        self.callback.task_started(task)

    def task_finished(self, task):

        self.callback.task_finished(task)


class TasksCallbackSpinner(TasksCallbackDefault):
    """Fancypants task event outputs with spinner.

    This outputs escape characters, so it is not supported by all terminals."""

    def __init__(self, **kwargs):

        super(TasksCallbackSpinner, self).__init__(**kwargs)

        self._spinner_dict = self.get_spinner_dict()
        self._spinner = None

        self.current_tasks = []
        # self.already_printed = {}

    @property
    def spinner(self):

        if self._spinner is not None:
            return self._spinner

        if not self.use_stderr:
            self._spinner = Halo(
                text="Initiating...",
                spinner=self._spinner_dict,
                color="grey",
                animation="bounce",
            )
        else:
            self._spinner = Halo(
                text="Initiating...",
                spinner=self._spinner_dict,
                color="grey",
                animation="bounce",
                stream=sys.stderr,
            )
        return self._spinner

    def task_started(self, task):

        if task.detail_level > self._detail_level:
            return
        if self.current_tasks:
            self.stop_spinner()
            self.print_current_tasks()
        self.start_spinner(task)
        self.current_tasks.append(task)
        # self.already_printed[task.id] = {"task": task}

    def print_current_tasks(self):

        for t in self.current_tasks:
            self.print_msg(t, self.get_task_started_string(t))
            # self.output_to_terminal(self.get_task_started_string(t))

        self.current_tasks = []

    def task_finished(self, task):

        self.stop_spinner()
        self.print_current_tasks()

        try:

            if (task.success or not task.success and task.ignore_errors) and (
                task.level != 0 or task._tasks.is_utility_task
            ):

                skip = False
                if task.skipped and not self.show_skipped:
                    skip = True

                if not task.changed and not self.show_no_change:
                    skip = True

                if task.get_messages(detail_level=0):
                    skip = False

                if skip:
                    self.remove_printed_lines(task)
                    return

                if self.show_msg or task.get_messages(detail_level=0):

                    if task.get_messages():
                        msg = self.get_msg_string(task)
                        self.print_msg(task, msg)

            if not task.success and (task.get_messages() or task.get_error_messages()):

                if task.get_messages():
                    msg = self.get_msg_string(task)
                    self.print_msg(task, msg)

                if task.get_error_messages():
                    msg = self.get_error_msg_string(task)
                    self.print_msg(task, msg)

            finished_msg = self.get_task_finished_status(task)
            self.print_msg(task, finished_msg)
            # self.already_printed[task.id].setdefault("output", []).append(finished_msg)

        finally:
            if task.level == 0:
                if not task._tasks.is_utility_task or task.changed or not task.skipped:
                    msg = self.get_task_conclusion(task)
                    self.output_to_terminal(msg)

                self.spinner.stop()
                self.current_tasks = []
                self.started_tasks = {}

    def start_spinner(self, task=None):

        if task is not None:
            self.spinner.spinner = self.get_spinner_dict(task)
            if isinstance(task.msg, six.string_types):
                m = task.msg
            else:
                m = str(task.msg)
            self.spinner.text = m
        else:
            self.spinner.text = ""
        self.spinner.start()

    def stop_spinner(self):

        self.spinner.stop()

    def get_spinner_dict(self, task=None):

        if task is None:
            level = 0
        else:
            level = task.level

        padding = u"{}  ".format(VERTICAL) * level

        result = []

        # spinner_list = Spinners.pipe.value.get("frames")
        if level == 0:
            return "dots"
        else:
            # spinner_list = ["└", "├", "│", "┤", "┘", "┴"]
            spinner_list = [ARC_UP_RIGHT, VERTICAL, ARC_UP_LEFT, VERTICAL]

            for character in spinner_list:
                c = "{}{}".format(padding, character)
                result.append(c)

            return {"interval": 240, "frames": result}

    def task_paused(self):

        self.spinner.stop()
        # click.echo()

    def task_resumed(self):

        # click.echo()
        self.spinner.start()
