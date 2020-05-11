import os

from lark import lark
from lark.indenter import Indenter

from takathon.interpreter.parser.to_ast import ToAST


GRAMMAR_PATH = os.path.join(os.path.dirname(__file__), "grammar", "takathon.lark")


class GrammarIndenter(Indenter):
    NL_type = "_NEWLINE"
    OPEN_PAREN_types = []
    CLOSE_PAREN_types = []
    INDENT_type = "_INDENT"
    DEDENT_type = "_DEDENT"
    tab_len = 8


def parse(spec):
    parser = lark.Lark(
        open(GRAMMAR_PATH),
        parser="lalr",
        postlex=GrammarIndenter(),
        maybe_placeholders=True,
        propagate_positions=True,
    )
    return parser.parse(spec)


def make_ast(module_name, spec):
    return ToAST(module_name, spec, visit_tokens=True).transform(parse(spec))
