from pathlib import Path

from forge.python.import_indexer import ImportIndexer


def test_import_indexer(tmp_path: Path) -> None:

    source = tmp_path / "example.py"

    source.write_text(
        """
import logging
from pathlib import Path
""",
        encoding="utf-8",
    )

    graph = ImportIndexer().build((source,))

    assert len(graph) == 2

    assert graph.contains("logging")

    assert graph.contains("pathlib.Path")