from forge.doctor.models import (
    CheckResult,
    DoctorReport,
)


def test_doctor_report_healthy() -> None:
    report = DoctorReport(
        checks=(
            CheckResult(
                name="Python",
                ok=True,
                message="Python found",
            ),
            CheckResult(
                name="Git",
                ok=True,
                message="Git found",
            ),
        )
    )

    assert report.healthy
    assert len(report.passed) == 2
    assert len(report.failed) == 0


def test_doctor_report_failed() -> None:
    report = DoctorReport(
        checks=(
            CheckResult(
                name="Python",
                ok=True,
                message="Python found",
            ),
            CheckResult(
                name="Git",
                ok=False,
                message="Git missing",
            ),
        )
    )

    assert not report.healthy
    assert len(report.passed) == 1
    assert len(report.failed) == 1