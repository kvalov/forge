from pathlib import Path

from forge.python.symbols import Symbol, SymbolKind


def test_symbol():
    symbol = Symbol(
        name="WorkspaceService",
        kind=SymbolKind.CLASS,
        module=Path("workspace/service.py"),
        line=12,
    )

    assert symbol.name == "WorkspaceService"
    assert symbol.kind is SymbolKind.CLASS
    assert symbol.line == 12