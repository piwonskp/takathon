"""
TODO: Remove this file once lark adds support for validation without building subtree for imported nodes. 
Hacks in this file are strong.
"""
from lark import Token, Transformer, Tree, v_args
from lark.load_grammar import load_grammar

rename = lambda name: f"_{name}"
is_python_rule = lambda name: name.startswith("python__")

imported_rules = ["testlist", "arguments", "import_stmt", "dotted_name", "test"]


def inline_python_rules(rule):
    name, tree, opts = rule
    if is_python_rule(name):
        name = rename(name)
        opts.expand1 = False
        opts.keep_all_tokens = True
    elif name in imported_rules:
        opts.keep_all_tokens = True

    tree = FlattenPythonGrammar(visit_tokens=True).transform(tree)

    return name, tree, opts


def flatten_python_subtree(*args, **kwargs):
    grammar = load_grammar(*args, **kwargs)
    grammar.rule_defs = list(map(inline_python_rules, grammar.rule_defs))

    return grammar


@v_args(tree=True)
class FlattenPythonGrammar(Transformer):
    def alias(self, tree):
        return tree.children[0]

    def RULE(self, token):
        if is_python_rule(token.value):
            return token.update(value=rename(token.value))
        return token


@v_args(tree=True)
class MergePythonTokens(Transformer):
    def __getattr__(self, name):
        if name in imported_rules:
            return self.replace_node_with_token
        raise AttributeError

    def replace_node_with_token(self, node):
        return self.merge_tokens(node.children)

    def merge_children(self, tree):
        tree.children = [self.merge_tokens(tree.children)]
        return tree

    def merge_tokens(self, children):
        # Due to maybe_placeholders=True
        children = filter(lambda tok: tok is not None, children)
        first = next(children)

        value = first.value
        token = None
        for token in children:
            value = f"{value} {token.value}"
        last_token = first if token is None else token

        return Token(
            "PYTHON_CODE",
            value,
            first.pos_in_stream,
            first.line,
            first.column,
            last_token.end_line,
            last_token.end_column,
            last_token.end_pos,
        )

    import_stmt = merge_children

    def dotted_name(self, node):
        token = self.replace_node_with_token(node)
        return token.update(value=token.value.replace(" ", ""))
