from __future__ import annotations

import ast
from pathlib import Path

from forge.python.import_graph import ImportGraph
from forge.python.import_visitor import ImportVisitor


class ImportIndexer:
    """Build an ImportGraph for a collection of Python files."""

    def build(
        self,
        files: tuple[Path, ...],
    ) -> ImportGraph:

        graph = ImportGraph()

        for file in files:

            tree = ast.parse(
                file.read_text(
                    encoding="utf-8",
                )
            )

            visitor = ImportVisitor(file)

            visitor.visit(tree)

            for item in visitor.graph.all():
                graph.add(item)

        return graph