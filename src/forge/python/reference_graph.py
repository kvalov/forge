from __future__ import annotations

from collections import defaultdict
from pathlib import Path

from forge.python.references import Reference


class ReferenceGraph:

    def __init__(self) -> None:

        self._references: list[Reference] = []

        self._by_symbol: dict[
            str,
            list[Reference],
        ] = defaultdict(list)

        self._by_module: dict[
            Path,
            list[Reference],
        ] = defaultdict(list)

    def add(
        self,
        reference: Reference,
    ) -> None:

        self._references.append(reference)

        self._by_symbol[
            reference.symbol
        ].append(reference)

        self._by_module[
            reference.module
        ].append(reference)

    def references(
        self,
        symbol: str,
    ) -> tuple[Reference, ...]:

        return tuple(
            self._by_symbol.get(
                symbol,
                (),
            )
        )

    def module(
        self,
        path: Path,
    ) -> tuple[Reference, ...]:

        return tuple(
            self._by_module.get(
                path,
                (),
            )
        )

    def contains(
        self,
        symbol: str,
    ) -> bool:

        return symbol in self._by_symbol

    def all(self) -> tuple[Reference, ...]:

        return tuple(
            self._references
        )

    def __len__(self) -> int:

        return len(
            self._references
        )