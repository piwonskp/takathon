import copy
import logging
from dataclasses import InitVar, dataclass, field
from types import FunctionType

from lark import Token

from takathon.interpreter.ast_interpreter.builtins import BUILTINS
from takathon.interpreter.ast_interpreter.common_stmt import (
    CommonInterpreter,
    TestedFunction,
)
from takathon.interpreter.ast_interpreter.count_tests import count_tests
from takathon.interpreter.ast_interpreter.exceptions import (
    UserException,
    WrongMockPathException,
)
from takathon.interpreter.ast_interpreter.test_case import TestCaseInterpreter
from takathon.output import clear_line
from takathon.result import tests_failed


def print_results(function_id, results):
    logging.info(
        f"{function_id}: {results.passed} tests passed, {results.failed} failed"
    )


def interpret(module, function, title, description, *ast):
    interpreter = Interpreter(module, TestedFunction(function), title, description)
    interpreter.interpret(ast)

    print_results(interpreter.target.function_id, interpreter.target.results)


@dataclass
class Interpreter(CommonInterpreter):
    scope: dict = field(default_factory=lambda: copy.copy(BUILTINS), init=False)
    title: Token
    description: Token

    def __post_init__(self):
        self.test_info()

    def test_info(self):
        clear_line()
        if self.title:
            logging.info(self.title)
        else:
            logging.info(f"{self.target.function_id}:")

    def unsafe_interpret(self, ast):
        for node in ast:
            if node.data == "test_case":
                self.test_case(*node.children)
            else:
                self.stmt(node)

    def count_remaining_tests(self, exc, ast):
        if type(exc) == WrongMockPathException:
            return count_tests(exc.subtree)
        return count_tests(ast)

    def interpret(self, ast):
        ast = iter(ast)
        try:
            self.unsafe_interpret(ast)
        except UserException as e:
            self.failed(self.count_remaining_tests(e, ast))
            e.print()

    def failed(self, remaining_tests):
        self.target.results.failed += remaining_tests
        tests_failed(remaining_tests)

    def test_case(self, arguments, title, description, *subtree):
        return TestCaseInterpreter(
            self.module,
            copy.deepcopy(self.scope),
            self.target,
            arguments,
            title,
            description,
        ).interpret(subtree)
