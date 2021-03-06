from enum import Enum

Color = Enum("Color", ("BLUE", "CYAN", "GREEN", "YELLOW", "RED"))


def is_red(color):
    """
    spec:
        domain any_of(Color.BLUE, Color.CYAN, Color.GREEN, Color.YELLOW):
            results False
        domain Color.RED: results True
    """
    return color == Color.RED
