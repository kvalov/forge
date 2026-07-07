from __future__ import annotations

from abc import ABC, abstractmethod

from forge.doctor.models import CheckResult


class DoctorCheck(ABC):
    """Base class for doctor checks."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Human readable check name."""

    @abstractmethod
    def run(self) -> CheckResult:
        """Execute the check."""