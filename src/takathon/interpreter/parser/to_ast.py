from dataclasses import dataclass

from lark import Lark, Token, Transformer, Tree, v_args
from lark.reconstruct import Reconstructor

is_mock = lambda node: type(node) == Tree and node.data == "mock_stmt"


def transform_mock(children):
    new_children = []
    for node in reversed(children):
        if is_mock(node):
            new_children = [Tree("mock_stmt", node.children + new_children)]
        else:
            new_children.insert(0, node)
    return new_children


@v_args(inline=True)
class ToAST(Transformer):
    def __init__(self, module_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.module_name = module_name

    def mock_current_module(self, token):
        return token.update(value=f"{self.module_name}.{token}")

    mock_path_absolute = lambda self, path: path

    def domain_stmt(self, arguments, stmts):
        if arguments.type == "BLANK_DOMAIN_STMT":
            arguments = arguments.update(value="")

        flattened_children = (arguments,) + stmts
        return Tree("test_case", transform_mock(flattened_children))

    def inline_test(self, *children):
        docs = (None, None)
        return docs + children

    multiline_test = lambda self, *children: children

    RAW_TEXT = lambda self, t: t.strip()

    def start(self, *children):
        return transform_mock(children)
