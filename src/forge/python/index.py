from __future__ import annotations

from forge.python.symbols import Symbol, SymbolKind


class SymbolIndex:
    """In-memory index of Python symbols."""

    def __init__(self) -> None:
        self._symbols: dict[str, Symbol] = {}

    def add(self, symbol: Symbol) -> None:
        """Add or replace a symbol."""
        self._symbols[symbol.name] = symbol

    def get(self, name: str) -> Symbol | None:
        """Return a symbol by name."""
        return self._symbols.get(name)

    def contains(self, name: str) -> bool:
        """Return True if the symbol exists."""
        return name in self._symbols

    def all(self) -> tuple[Symbol, ...]:
        """Return all indexed symbols."""
        return tuple(self._symbols.values())

    def classes(self) -> tuple[Symbol, ...]:
        """Return all class symbols."""
        return tuple(
            symbol
            for symbol in self._symbols.values()
            if symbol.kind is SymbolKind.CLASS
        )

    def functions(self) -> tuple[Symbol, ...]:
        """Return all function symbols."""
        return tuple(
            symbol
            for symbol in self._symbols.values()
            if symbol.kind is SymbolKind.FUNCTION
        )

    def methods(self) -> tuple[Symbol, ...]:
        """Return all method symbols."""
        return tuple(
            symbol
            for symbol in self._symbols.values()
            if symbol.kind is SymbolKind.METHOD
        )

    def __len__(self) -> int:
        return len(self._symbols)

    def __contains__(self, name: object) -> bool:
        if not isinstance(name, str):
            return False

        return self.contains(name)