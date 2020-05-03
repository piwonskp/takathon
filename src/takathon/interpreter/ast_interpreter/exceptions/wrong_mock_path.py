import inspect
from dataclasses import InitVar, dataclass
from traceback import FrameSummary, StackSummary
from types import FunctionType

from lark import Token, Tree

from takathon.interpreter.ast_interpreter.exceptions.user_exception import (
    UserException,
    docs_start_lineno,
)
from takathon.output import fail_description


@dataclass
class WrongMockPathException(UserException):
    path: Token
    subtree: [Tree]
    function: InitVar[FunctionType]
    test_id: InitVar[str]

    def __post_init__(self, function, test_id):
        file_frame = FrameSummary(
            inspect.getfile(function),
            docs_start_lineno(function) + self.path.line,
            function.__name__,
            lookup_line=False,
        )
        dynamic_frame = FrameSummary(
            test_id, 1, function.__name__, lookup_line=False, line=self.path
        )
        self.stack = StackSummary.from_list([file_frame, dynamic_frame])

    def format(self):
        return self.stack.format()

    def print(self):
        super().print()
        fail_description(f"Incorrect mock path: {self.path}")
