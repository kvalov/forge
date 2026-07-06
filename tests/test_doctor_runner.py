from forge.doctor.runner import DoctorRunner


def test_runner_collects_checks() -> None:
    runner = DoctorRunner()

    runner.add(
        "Python",
        True,
        "Python found",
    )

    runner.add(
        "Git",
        True,
        "Git found",
    )

    report = runner.report()

    assert report.healthy
    assert len(report.checks) == 2


def test_runner_clear() -> None:
    runner = DoctorRunner()

    runner.add(
        "Python",
        True,
        "Python found",
    )

    runner.clear()

    report = runner.report()

    assert len(report.checks) == 0
    assert report.healthy