import sys
from unittest.mock import patch

from takathon.interpreter.ast_interpreter.exceptions import (
    WrongMockPathException,
    construct_user_code_exc,
)


class CommonInterpreter:
    def stmt(self, node):
        if node.data == "mock_stmt":
            self.mock(*node.children)
        elif node.data == "import_stmt":
            self.import_stmt(*node.children)

    def mock(self, path, value, *children):
        patcher = patch(path, self.eval(value, value.line))
        try:
            patcher.start()
        except ModuleNotFoundError as e:
            raise WrongMockPathException(
                path, children, self.target.function, self.get_test_id()
            )
        self.interpret(children)
        patcher.stop()

    def import_stmt(self, stmt):
        self.exec(stmt, stmt.line)

    def get_test_id(self):
        return f"<takathon {self.target.function_id}>"

    def unsafe_eval(self, expr):
        return eval(compile(expr, self.get_test_id(), "eval"), *self.scope())

    def eval(self, expr, lineno):
        try:
            return self.unsafe_eval(expr)
        except Exception:
            raise construct_user_code_exc(
                self.target.function, lineno, expr, *sys.exc_info()
            )

    def unsafe_exec(self, stmt):
        return exec(compile(stmt, self.get_test_id(), "exec"), *self.scope())

    def exec(self, stmt, lineno):
        try:
            return self.unsafe_exec(stmt)
        except Exception:
            raise construct_user_code_exc(
                stmt, self.target.function, lineno, *sys.exc_info()
            )
