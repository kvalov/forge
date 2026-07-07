import ast
from pathlib import Path

from forge.python.import_visitor import ImportVisitor


def test_import_visitor() -> None:

    tree = ast.parse(
        """
import logging
import ast

from pathlib import Path
from forge.workspace.service import WorkspaceService
"""
    )

    visitor = ImportVisitor(Path("demo.py"))

    visitor.visit(tree)

    graph = visitor.graph

    assert len(graph) == 4

    imports = {
        item.target
        for item in graph.all()
    }

    assert "logging" in imports
    assert "ast" in imports
    assert "pathlib.Path" in imports
    assert (
        "forge.workspace.service.WorkspaceService"
        in imports
    )