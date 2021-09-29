import os

from lark import Token, Transformer, Tree, v_args

from takathon.interpreter.parser.parser import make_parser

GRAMMAR_PATH = os.path.join(os.path.dirname(__file__), "grammar", "procedure.lark")
is_mock = lambda node: type(node) == Tree and node.data == "mock_stmt"


def transform_mock(children):
    new_children = []
    for node in reversed(children):
        if is_mock(node):
            new_children = [Tree("mock_stmt", node.children + new_children)]
        else:
            new_children.insert(0, node)
    return new_children


def inline(method):
    return lambda self, tree: method(self, *tree.children)


@v_args(tree=True)
class ToAST(Transformer):
    def __init__(self, module_name, spec, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.module_name = module_name
        self.spec = spec

    @v_args(inline=True)
    def mock_current_module(self, token):
        return token.update(value=f"{self.module_name}.{token}")

    @v_args(inline=True)
    def mock_path_absolute(self, path):
        return path

    def multiline_docs(self, tree):
        tree.children = ["\n".join(tree.children)]
        return tree

    @v_args(inline=True)
    def domain_stmt(self, arguments, stmts):
        if arguments.type == "BLANK_DOMAIN_STMT":
            arguments = arguments.update(value="")

        flattened_children = [arguments] + stmts
        return Tree("test_case", transform_mock(flattened_children))

    def inline_test(self, tree):
        docs = [None, None]
        return docs + tree.children

    multiline_test = lambda self, tree: tree.children

    @v_args(inline=True)
    def RAW_TEXT(self, t):
        return t.strip()

    def start(self, tree):
        return transform_mock(tree.children)

    def get_original_text(self, tree):
        original = self.spec[tree.meta.start_pos : tree.meta.end_pos]
        return Token.new_borrow_pos("PYTHON_CODE", original, tree.meta)

    def set_children_as_original_text(self, tree):
        tree.children = [self.get_original_text(tree)]
        return tree

    arguments = get_original_text
    dotted_name = get_original_text
    import_stmt = set_children_as_original_text
    python_expr = get_original_text
    testlist = get_original_text


def parse(spec):
    parser = make_parser(GRAMMAR_PATH)
    return parser.parse(spec)


def make_procedure_ast(module_name, spec):
    return ToAST(module_name, spec, visit_tokens=True).transform(parse(spec))
