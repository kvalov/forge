from __future__ import annotations

import ast
from pathlib import Path

from forge.python.reference_graph import ReferenceGraph
from forge.python.references import Reference


class ReferenceVisitor(ast.NodeVisitor):
    """Collect symbol references from a Python AST."""

    def __init__(self, module: Path) -> None:
        self._module = module
        self._graph = ReferenceGraph()

    @property
    def graph(self) -> ReferenceGraph:
        return self._graph

    def visit_Name(self, node: ast.Name) -> None:
        self._graph.add(
            Reference(
                module=self._module,
                symbol=node.id,
                line=node.lineno,
            )
        )

        self.generic_visit(node)