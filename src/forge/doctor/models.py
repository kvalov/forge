from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CheckResult:
    """Result of a single doctor check."""

    name: str
    ok: bool
    message: str


@dataclass(frozen=True, slots=True)
class DoctorReport:
    """Complete doctor report."""

    checks: tuple[CheckResult, ...]

    @property
    def healthy(self) -> bool:
        return all(check.ok for check in self.checks)

    @property
    def failed(self) -> tuple[CheckResult, ...]:
        return tuple(
            check
            for check in self.checks
            if not check.ok
        )

    @property
    def passed(self) -> tuple[CheckResult, ...]:
        return tuple(
            check
            for check in self.checks
            if check.ok
        )