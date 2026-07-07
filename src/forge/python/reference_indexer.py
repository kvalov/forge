from __future__ import annotations

import ast
from pathlib import Path

from forge.python.reference_graph import ReferenceGraph
from forge.python.reference_visitor import ReferenceVisitor


class ReferenceIndexer:
    """Build a ReferenceGraph for a collection of Python files."""

    def build(
        self,
        files: tuple[Path, ...],
    ) -> ReferenceGraph:

        graph = ReferenceGraph()

        for file in files:
            tree = ast.parse(
                file.read_text(
                    encoding="utf-8",
                )
            )

            visitor = ReferenceVisitor(file)

            visitor.visit(tree)

            for reference in visitor.graph.all():
                graph.add(reference)

        return graph