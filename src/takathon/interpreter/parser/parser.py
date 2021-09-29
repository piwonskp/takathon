from lark import lark
from lark.indenter import Indenter


class GrammarIndenter(Indenter):
    NL_type = "_NEWLINE"
    OPEN_PAREN_types = []
    CLOSE_PAREN_types = []
    INDENT_type = "_INDENT"
    DEDENT_type = "_DEDENT"
    tab_len = 8


def make_parser(grammar_path):
    return lark.Lark(
        open(grammar_path),
        parser="lalr",
        postlex=GrammarIndenter(),
        maybe_placeholders=True,
        propagate_positions=True,
    )
