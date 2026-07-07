from pathlib import Path

from forge.python.import_graph import ImportGraph
from forge.python.imports import Import


def test_import_graph_lookup() -> None:

    graph = ImportGraph()

    graph.add(
        Import(
            module=Path("service.py"),
            target="logging",
            line=1,
        )
    )

    graph.add(
        Import(
            module=Path("service.py"),
            target="ast",
            line=2,
        )
    )

    assert graph.contains("logging")

    assert not graph.contains("json")

    assert len(
        graph.imports(
            Path("service.py")
        )
    ) == 2

    assert len(
        graph.imported_by("logging")
    ) == 1

    assert "logging" in graph.targets()

    assert Path("service.py") in graph.modules()