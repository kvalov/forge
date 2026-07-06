from pathlib import Path
import ast

from forge.python.symbol_visitor import SymbolVisitor


def test_symbol_visitor() -> None:

    tree = ast.parse(
        """
class Demo:
    pass

def hello():
    pass
"""
    )

    visitor = SymbolVisitor(Path("demo.py"))

    visitor.visit(tree)

    index = visitor.index

    assert index.contains("Demo")
    assert index.contains("hello")

    assert index.get("Demo").line == 2