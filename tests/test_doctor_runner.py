from forge.doctor.models import CheckResult
from forge.doctor.runner import DoctorRunner


def test_runner_collects_checks() -> None:
    runner = DoctorRunner()

    runner.add(
        CheckResult(
            name="Python",
            ok=True,
            message="Python found",
        )
    )

    runner.add(
        CheckResult(
            name="Git",
            ok=True,
            message="Git found",
        )
    )

    report = runner.report()

    assert report.healthy
    assert len(report.checks) == 2


def test_runner_clear() -> None:
    runner = DoctorRunner()

    runner.add(
        CheckResult(
            name="Python",
            ok=True,
            message="Python found",
        )
    )

    runner.clear()

    report = runner.report()

    assert len(report.checks) == 0
    assert report.healthy