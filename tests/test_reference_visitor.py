import ast
from pathlib import Path

from forge.python.reference_visitor import ReferenceVisitor


def test_reference_visitor() -> None:
    tree = ast.parse(
        """
workspace = WorkspaceService()

logger.info(workspace)

print(workspace)
"""
    )

    visitor = ReferenceVisitor(Path("demo.py"))

    visitor.visit(tree)

    graph = visitor.graph

    assert graph.contains("WorkspaceService")
    assert graph.contains("workspace")
    assert graph.contains("logger")
    assert graph.contains("print")

    assert len(graph.references("workspace")) == 3