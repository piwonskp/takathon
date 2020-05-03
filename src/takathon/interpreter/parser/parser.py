import os

from lark import lark
from lark.indenter import Indenter

from takathon.interpreter.parser.inline_python import (
    MergePythonTokens,
    flatten_python_subtree,
)
from takathon.interpreter.parser.to_ast import ToAST

GRAMMAR_PATH = os.path.join(os.path.dirname(__file__), "grammar", "takathon.lark")


lark.load_grammar = flatten_python_subtree


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
        transformer=MergePythonTokens(),
        maybe_placeholders=True,
    )
    return parser.parse(spec)


def make_ast(module_name, spec):
    return ToAST(module_name, visit_tokens=True).transform(parse(spec))
