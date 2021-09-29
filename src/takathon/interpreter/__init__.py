import inspect

from takathon.interpreter.ast_interpreter import interpret
from takathon.interpreter.ast_interpreter.class_interpreter import interpret_method
from takathon.interpreter.parser import make_procedure_ast
from takathon.interpreter.parser.class_parser.method_parser import make_method_ast


def run_function_tests(module, function):
    docs = inspect.cleandoc(function.__doc__)
    interpret(module, function, *make_procedure_ast(module.__name__, docs))


def run_method_tests(module, cls, method):
    docs = inspect.cleandoc(method.__doc__)
    interpret_method(module, method, cls, *make_method_ast(module.__name__, docs))
