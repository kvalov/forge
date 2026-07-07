from pathlib import Path

from forge.python.reference_indexer import ReferenceIndexer


def test_reference_indexer(tmp_path: Path) -> None:
    source = tmp_path / "example.py"

    source.write_text(
        """
from pathlib import Path

path = Path(".")

print(path)
""",
        encoding="utf-8",
    )

    graph = ReferenceIndexer().build((source,))

    assert graph.contains("Path")
    assert graph.contains("path")
    assert graph.contains("print")

    assert len(graph.references("path")) == 2