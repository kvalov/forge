from __future__ import annotations

from forge.python.index import SymbolIndex
from forge.python.index_builder import IndexBuilder
from forge.workspace.service import WorkspaceService

class PythonIndexer:
    """Build a symbol index for the current workspace."""

    def __init__(
        self,
        workspace: WorkspaceService,
        builder: IndexBuilder | None = None,
    ) -> None:
        self._workspace = workspace
        self._builder = builder or IndexBuilder()

    def build(self) -> SymbolIndex:
        root = self._workspace.state().root

        files = tuple(
            root / file.path
            for file in self._workspace.python_files()
        )

        return self._builder.build(files)