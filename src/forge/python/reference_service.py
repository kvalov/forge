from __future__ import annotations

from pathlib import Path

from forge.python.reference_graph import ReferenceGraph
from forge.python.reference_indexer import ReferenceIndexer


class ReferenceService:
    """Application service for symbol references."""

    def __init__(
        self,
        indexer: ReferenceIndexer | None = None,
    ) -> None:
        self._indexer = indexer or ReferenceIndexer()

    def analyze(
        self,
        files: tuple[Path, ...],
    ) -> ReferenceGraph:
        return self._indexer.build(files)

    def references(
        self,
        files: tuple[Path, ...],
        symbol: str,
    ):
        graph = self.analyze(files)

        return graph.references(symbol)