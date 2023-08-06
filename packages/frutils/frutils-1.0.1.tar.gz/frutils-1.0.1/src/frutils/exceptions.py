# -*- coding: utf-8 -*-
import textwrap

import click
from colorama import Fore, Style
import sys

import logging

log = logging.getLogger("frutils")


def handle_exception(exc, exit=True, exit_code=1, logger=None):

    if logger is None:
        logger = log

    log.debug(exc, exc_info=1)
    # click.echo("Can't create context: {}".format(e))

    if hasattr(exc, "root_exc"):

        root_exc = exc.root_exc
        if isinstance(root_exc, FrklException):
            exc = root_exc
        else:
            exc = FrklException(parent=exc)
    if not isinstance(exc, FrklException) and not issubclass(
        exc.__class__, FrklException
    ):
        exc = FrklException(exc)

    click.echo()
    exc.print_message()

    if exit:
        sys.exit(exit_code)


def generate_exception_dict(exc):

    if hasattr(exc, "root_exc"):
        root_exc = exc.root_exc
        if isinstance(root_exc, FrklException):
            exc = root_exc
        else:
            exc = FrklException(parent=exc)
    if not isinstance(exc, FrklException) and not issubclass(
        exc.__class__, FrklException
    ):
        exc = FrklException(exc)

    result = {"msg": exc.msg, "solution": exc.solution, "reason": exc.reason}
    return result


def handle_exc(func, exit=True, exit_code=1):
    def func_wrapper(*args, **kwargs):

        try:
            return func(*args, **kwargs)
        except (Exception) as e:
            handle_exception(e, exit=exit, exit_code=exit_code)

    return func_wrapper


class FrklException(Exception):
    """Base exception class for nsbl."""

    def __init__(
        self, msg=None, solution=None, references=None, reason=None, parent=None, *args
    ):

        if isinstance(msg, Exception):
            if parent is None:
                parent = msg
            msg = str(msg)

        if msg is None:
            msg = "freckles internal error"

        super(FrklException, self).__init__(msg, *args)
        self.msg = msg
        self.solution = solution
        self.reason = reason
        self.references = references
        self.parent = parent

    @property
    def message(self):

        msg = self.msg
        if not msg.endswith("."):
            msg = msg + "."

        msg = msg + "\n"

        if self.reason:
            msg = msg + "\n  Reason: {}".format(self.reason)
        if self.solution:
            msg = msg + "\n  Solution: {}".format(self.solution)
        if self.references:
            if len(self.references) == 1:
                url = self.references[list(self.references.keys())[0]]
                msg = msg + "\n  Reference: {}".format(url)
            else:
                msg = msg + "\n  References\n"
                for k, v in self.references.items():
                    msg = msg + "\n    {}: {}".format(k, v)

        return msg.rstrip()

    def print_message(self):

        from frutils import get_terminal_size, reindent
        from frutils.frutils_cli import output_to_terminal

        cols, _ = get_terminal_size()

        msg = Fore.RED + "Error: " + Style.RESET_ALL + self.msg
        for m in msg.split("\n"):
            m = textwrap.fill(m, width=cols, subsequent_indent="       ")
            output_to_terminal(m)
        click.echo()
        if self.reason:
            output_to_terminal(Style.BRIGHT + "  Reason: " + Style.RESET_ALL)
            msg = reindent(self.reason, 4)
            for m in msg.split("\n"):
                m = textwrap.fill(m, width=cols, subsequent_indent="    ")
                output_to_terminal(m)
            click.echo()
        if self.solution:
            output_to_terminal(Style.BRIGHT + "  Solution: " + Style.RESET_ALL)
            msg = reindent(self.solution, 4)
            for m in msg.split("\n"):
                m = textwrap.fill(m, width=cols, subsequent_indent="    ")
                output_to_terminal(m)
            click.echo()
        if self.references:
            if len(self.references) == 1:
                url = self.references[list(self.references.keys())[0]]
                output_to_terminal(
                    Style.BRIGHT + "  Reference: " + Style.RESET_ALL + url
                )
            else:
                output_to_terminal(Style.BRIGHT + "  References:" + Style.RESET_ALL)
                for k, v in self.references.items():
                    output_to_terminal(
                        "    " + Style.DIM + k + ": " + Style.RESET_ALL + v
                    )

        click.echo()

    def __str__(self):
        return self.message


class FrklParseException(FrklException):
    def __init__(
        self,
        content,
        msg=None,
        solution=None,
        references=None,
        reason=None,
        content_origin=None,
        exception_map=None,
    ):
        self.content = content
        self.content_origin = content_origin
        self.exception_map = exception_map
        super(FrklParseException, self).__init__(
            msg=msg, solution=solution, references=references, reason=reason
        )


class CnfException(FrklException):
    def __init__(self, msg, cnf):

        super(CnfException, self).__init__(msg)

        self.cnf = cnf


class CnfValidationException(CnfException):
    def __init__(self, cnf, cnf_key=None, errors="n/a"):
        if cnf_key is None:
            msg = "Config error: {}".format(errors)
        else:
            msg = "Error with config key '{}': {}".format(cnf_key, errors)

        super(CnfValidationException, self).__init__(msg=msg, cnf=cnf)
        self.cnf_key = cnf_key
        self.cnf = cnf
        self.errors = errors
