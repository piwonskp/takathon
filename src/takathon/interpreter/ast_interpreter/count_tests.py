from dataclasses import dataclass, field

from lark import Tree, Visitor


def count_tests(children):
    visitor = Count()
    visitor.visit(Tree("start", children))
    return visitor.tests_number


@dataclass
class Count(Visitor):
    tests_number: int = field(default=0, init=False)

    def test_case(self, *args):
        self.tests_number += 1
