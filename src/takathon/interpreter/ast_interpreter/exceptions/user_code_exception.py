import inspect
import sys
from dataclasses import dataclass
from traceback import FrameSummary, TracebackException

import click

from takathon.interpreter.ast_interpreter.exceptions.user_exception import (
    UserException,
    docs_start_lineno,
)


def construct_user_code_exc(
    function, lineno, executed_code, exc_type, exc_value, exc_traceback
):
    """Not generic enough to make it a real class constructor"""
    exc_traceback = exc_traceback.tb_next.tb_next

    exc = TracebackException(exc_type, exc_value, exc_traceback)
    exc.stack[0]._line = executed_code

    first = FrameSummary(
        inspect.getfile(function),
        docs_start_lineno(function) + lineno,
        function.__name__,
        lookup_line=False,
    )
    exc.stack.insert(0, first)

    return UserCodeException(exc)


@dataclass
class UserCodeException(UserException):
    original_exc: TracebackException

    def format(self, *args, **kwargs):
        return self.original_exc.format(*args, **kwargs)
