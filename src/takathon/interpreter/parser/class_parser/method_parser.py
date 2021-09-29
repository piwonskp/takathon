import os

from lark import Transformer, Tree

from takathon.interpreter.parser.parser import make_parser
from takathon.interpreter.parser.procedure_parser import ToAST

GRAMMAR_PATH = os.path.join(
    os.path.dirname(os.path.dirname(__file__)), "grammar", "method.lark"
)


remove = lambda string: string.removeprefix("procedure__")


class DropProcedurePrefix(Transformer):
    def __default__(self, data, children, meta):
        return Tree(remove(data), children, meta)

    def __default_token__(self, token):
        token.type = remove(token.type)
        return token


def parse(spec):
    parser = make_parser(GRAMMAR_PATH)
    return parser.parse(spec)


def make_method_ast(module_name, spec):
    dropped_procedure = DropProcedurePrefix(visit_tokens=True).transform(parse(spec))
    return ToAST(module_name, spec, visit_tokens=True).transform(dropped_procedure)
