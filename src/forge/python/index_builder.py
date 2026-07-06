from __future__ import annotations

import ast
from pathlib import Path

from forge.python.index import SymbolIndex
from forge.python.symbol_visitor import SymbolVisitor


class IndexBuilder:
    """Build a symbol index directly from Python source files."""

    def build(
        self,
        files: tuple[Path, ...],
    ) -> SymbolIndex:

        index = SymbolIndex()

        for file in files:
            source = file.read_text(
                encoding="utf-8",
            )

            tree = ast.parse(
                source,
                filename=str(file),
            )

            visitor = SymbolVisitor(file)

            visitor.visit(tree)

            for symbol in visitor.index.all():
                index.add(symbol)

        return index