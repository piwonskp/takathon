import logging
from dataclasses import dataclass

from lark import Token

from takathon.interpreter.ast_interpreter.exceptions import (
    UserException,
    construct_user_code_exc,
)
from takathon.interpreter.ast_interpreter.procedure_interpreter.common_stmt import (
    CommonInterpreter,
)
from takathon.output import fail
from takathon.result import test_failed, test_passed

INCORRECT_RESULT = "\tExpected {} got {}".format
REJECTED_RESULT = "\tFunction {} rejected result {}".format
IMPROPER_EXCEPTION = "\tImproper exception. Expected {} got {}".format
MISSING_EXCEPTION = "\tExpected exception {}. No exception has been raised".format


@dataclass
class TestCaseInterpreter(CommonInterpreter):
    arguments: Token
    title: Token
    description: Token

    def unsafe_interpret(self, children):
        for node in children:
            if node.data == "results_stmt":
                self.results(*node.children)
            elif node.data == "result_by_function_stmt":
                self.result_by_function(*node.children)
            elif node.data == "throws_stmt":
                self.throws(*node.children)
            else:
                self.stmt(node)

    def interpret(self, children):
        try:
            self.unsafe_interpret(children)
        except UserException as e:
            self.failed()
            e.print()

    def construct_call(self):
        return f"{self.target.function.__name__}({self.arguments})"

    def call_fun(self):
        return self.eval(self.construct_call(), self.arguments.line)

    def results(self, expected_result):
        result = self.call_fun()
        expected_result = self.eval(expected_result, expected_result.line)
        try:
            assert result == expected_result
            self.passed()
        except AssertionError:
            self.failed()
            fail(INCORRECT_RESULT(expected_result, result))

    def result_by_function(self, validator_function):
        result = self.call_fun()
        validator = self.eval(validator_function, validator_function.line)
        try:
            assert validator(result)
            self.passed()
        except AssertionError:
            self.failed()
            fail(REJECTED_RESULT(validator_function, result))

    def get_exception(self, exception_str):
        exception = self.eval(exception_str, exception_str.line)
        if type(exception) == type:
            return exception()
        return exception

    def compare_exceptions(self, raised, expected_exception):
        expected = self.get_exception(expected_exception)
        try:
            assert type(raised) is type(expected) and raised.args == expected.args
            self.passed()
        except AssertionError:
            self.failed()
            fail(IMPROPER_EXCEPTION(type(expected), type(raised)))
            construct_user_code_exc(
                self.target.function,
                expected_exception.line,
                self.construct_call(),
                type(raised),
                raised,
                raised.__traceback__,
            ).print()

    def throws(self, expected_exception):
        try:
            self.unsafe_eval(self.construct_call())
        except Exception as raised:
            self.compare_exceptions(raised, expected_exception)
        else:
            self.failed()
            fail(MISSING_EXCEPTION(expected_exception))

    def failed_info(self):
        if self.title:
            print(f"\t{self.title}", end="")
        else:
            print(f"\tDomain {self.arguments}", end="")
        fail(" FAILED", bold=True)

    def passed_info(self):
        if self.title:
            logging.info(f"\t{self.title} PASSED")
        else:
            logging.info(f"\tDomain {self.arguments} PASSED")

    def passed(self):
        self.target.results.passed += 1
        test_passed()
        self.passed_info()

    def failed(self):
        self.target.results.failed += 1
        test_failed()
        self.failed_info()
