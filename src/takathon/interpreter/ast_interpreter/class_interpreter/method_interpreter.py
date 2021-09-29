import copy
import inspect
from dataclasses import dataclass

from takathon.interpreter.ast_interpreter.procedure_interpreter.common_stmt import (
    CommonInterpreter,
    TestedFunction,
)
from takathon.interpreter.ast_interpreter.procedure_interpreter.procedure_interpreter import (
    ProcedureInterpreter,
    print_results,
)
from takathon.interpreter.ast_interpreter.procedure_interpreter.test_case import (
    TestCaseInterpreter,
)


def interpret_method(module, function, cls, title, description, *ast):
    interpreter = MethodInterpreter(
        module, TestedMethod(function, cls), title, description
    )
    interpreter.interpret(ast)

    print_results(interpreter.target.id, interpreter.target.results)


@dataclass
class TestedMethod(TestedFunction):
    cls: type

    @property
    def id(self):
        return f"{inspect.getfile(self.function)}#{self.cls.__name__}.{self.function.__name__}"


@dataclass
class CommonMethodInterpreter(CommonInterpreter):
    def stmt(self, node):
        if node.data == "new":
            self.new(*node.children)
            return

        super().stmt(node)

    def new(self, args):
        self.scope["object_under_test"] = self.eval(
            f"{self.target.cls.__name__}({args})", args.line
        )


@dataclass
class MethodTestCaseInterpreter(TestCaseInterpreter, CommonMethodInterpreter):
    def construct_call(self):
        return (
            "object_under_test."
            + super(MethodTestCaseInterpreter, self).construct_call()
        )


@dataclass
class MethodInterpreter(ProcedureInterpreter, CommonMethodInterpreter):
    def __post_init__(self):
        super().__post_init__()
        self.scope["object_under_test"] = self.target.cls

    def test_case(self, arguments, title, description, *subtree):
        return MethodTestCaseInterpreter(
            self.module,
            copy.deepcopy(self.scope),
            self.target,
            arguments,
            title,
            description,
        ).interpret(subtree)
