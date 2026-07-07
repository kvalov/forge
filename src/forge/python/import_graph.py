from __future__ import annotations

from collections import defaultdict
from pathlib import Path

from forge.python.imports import Import


class ImportGraph:
    """Stores Python module dependencies."""

    def __init__(self) -> None:
        self._imports: list[Import] = []

        self._by_module: dict[Path, list[Import]] = defaultdict(list)

        self._by_target: dict[str, list[Import]] = defaultdict(list)

    def add(
        self,
        import_: Import,
    ) -> None:

        self._imports.append(import_)

        self._by_module[import_.module].append(import_)

        self._by_target[import_.target].append(import_)

    def all(self) -> tuple[Import, ...]:
        return tuple(self._imports)

    def imports(
        self,
        module: Path,
    ) -> tuple[Import, ...]:

        return tuple(
            self._by_module.get(
                module,
                (),
            )
        )

    def imported_by(
        self,
        target: str,
    ) -> tuple[Import, ...]:

        return tuple(
            self._by_target.get(
                target,
                (),
            )
        )

    def modules(self) -> tuple[Path, ...]:

        return tuple(
            sorted(self._by_module.keys())
        )

    def targets(self) -> tuple[str, ...]:

        return tuple(
            sorted(self._by_target.keys())
        )

    def contains(
        self,
        target: str,
    ) -> bool:

        return target in self._by_target

    def __len__(self) -> int:
        return len(self._imports)