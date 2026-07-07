from pathlib import Path

from forge.python.reference_graph import ReferenceGraph
from forge.python.references import Reference


def test_reference_graph() -> None:

    graph = ReferenceGraph()

    graph.add(
        Reference(
            module=Path("service.py"),
            symbol="WorkspaceService",
            line=12,
        )
    )

    assert graph.contains(
        "WorkspaceService"
    )

    assert len(
        graph.references(
            "WorkspaceService"
        )
    ) == 1

    assert len(
        graph.module(
            Path("service.py")
        )
    ) == 1