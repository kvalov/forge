from __future__ import annotations

import ast
from pathlib import Path

from forge.python.index import SymbolIndex
from forge.python.symbols import Symbol, SymbolKind


class SymbolVisitor(ast.NodeVisitor):
    """Collect Python symbols from an AST."""

    def __init__(self, module: Path) -> None:
        self._module = module
        self._index = SymbolIndex()

    @property
    def index(self) -> SymbolIndex:
        return self._index

    def visit_ClassDef(self, node: ast.ClassDef) -> None:
        self._index.add(
            Symbol(
                name=node.name,
                kind=SymbolKind.CLASS,
                module=self._module,
                line=node.lineno,
            )
        )

        self.generic_visit(node)

    def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
        self._index.add(
            Symbol(
                name=node.name,
                kind=SymbolKind.FUNCTION,
                module=self._module,
                line=node.lineno,
            )
        )

        self.generic_visit(node)

    def visit_AsyncFunctionDef(
        self,
        node: ast.AsyncFunctionDef,
    ) -> None:
        self._index.add(
            Symbol(
                name=node.name,
                kind=SymbolKind.FUNCTION,
                module=self._module,
                line=node.lineno,
            )
        )

        self.generic_visit(node)