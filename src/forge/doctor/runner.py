from __future__ import annotations

from forge.doctor.models import CheckResult, DoctorReport


class DoctorRunner:
    """Execute doctor checks."""

    def __init__(self) -> None:
        self._checks: list[CheckResult] = []

    def add(
        self,
        name: str,
        ok: bool,
        message: str,
    ) -> None:
        """Add a completed check."""
        self._checks.append(
            CheckResult(
                name=name,
                ok=ok,
                message=message,
            )
        )

    def report(self) -> DoctorReport:
        """Build the final report."""
        return DoctorReport(
            checks=tuple(self._checks),
        )

    def clear(self) -> None:
        """Reset all collected checks."""
        self._checks.clear()