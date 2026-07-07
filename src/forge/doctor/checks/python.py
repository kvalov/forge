from __future__ import annotations

import sys

from forge.doctor.checks.base import DoctorCheck
from forge.doctor.models import CheckResult


class PythonCheck(DoctorCheck):

    @property
    def name(self) -> str:
        return "Python"

    def run(self) -> CheckResult:
        return CheckResult(
            name=self.name,
            ok=True,
            message=sys.version.split()[0],
        )