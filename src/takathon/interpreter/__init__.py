import inspect

from takathon.interpreter.ast_interpreter import interpret
from takathon.interpreter.parser import make_ast


def run_tests(module, function):
    docs = inspect.cleandoc(function.__doc__)
    interpret(module, function, *make_ast(module.__name__, docs))
