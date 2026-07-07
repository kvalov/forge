from __future__ import annotations

from forge.doctor.models import CheckResult, DoctorReport


class DoctorRunner:
    """Execute doctor checks."""

    def __init__(self) -> None:
        self._checks: list[CheckResult] = []

    def add(self, result: CheckResult) -> None:
        """Add a completed check."""
        self._checks.append(result)

    def report(self) -> DoctorReport:
        """Build the final report."""
        return DoctorReport(
            checks=tuple(self._checks),
        )

    def clear(self) -> None:
        """Reset collected checks."""
        self._checks.clear()