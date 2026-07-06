from pathlib import Path

from forge.python.index import SymbolIndex
from forge.python.symbols import Symbol, SymbolKind


def test_add_symbol() -> None:
    index = SymbolIndex()

    symbol = Symbol(
        name="WorkspaceService",
        kind=SymbolKind.CLASS,
        module=Path("workspace/service.py"),
        line=10,
    )

    index.add(symbol)

    assert len(index) == 1
    assert index.contains("WorkspaceService")
    assert index.get("WorkspaceService") == symbol


def test_classes() -> None:
    index = SymbolIndex()

    index.add(
        Symbol(
            "A",
            SymbolKind.CLASS,
            Path("a.py"),
            1,
        )
    )

    index.add(
        Symbol(
            "func",
            SymbolKind.FUNCTION,
            Path("a.py"),
            10,
        )
    )

    assert len(index.classes()) == 1
    assert len(index.functions()) == 1


def test_unknown_symbol() -> None:
    index = SymbolIndex()

    assert index.get("Missing") is None