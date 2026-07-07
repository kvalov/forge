from __future__ import annotations

import ast
from pathlib import Path

from forge.python.import_graph import ImportGraph
from forge.python.imports import Import


class ImportVisitor(ast.NodeVisitor):
    """Collect import statements from a Python AST."""

    def __init__(self, module: Path) -> None:
        self._module = module
        self._graph = ImportGraph()

    @property
    def graph(self) -> ImportGraph:
        return self._graph

    def visit_Import(
        self,
        node: ast.Import,
    ) -> None:

        for alias in node.names:
            self._graph.add(
                Import(
                    module=self._module,
                    target=alias.name,
                    line=node.lineno,
                )
            )

        self.generic_visit(node)

    def visit_ImportFrom(
        self,
        node: ast.ImportFrom,
    ) -> None:

        module = node.module or ""

        for alias in node.names:
            target = (
                f"{module}.{alias.name}"
                if module
                else alias.name
            )

            self._graph.add(
                Import(
                    module=self._module,
                    target=target,
                    line=node.lineno,
                )
            )

        self.generic_visit(node)