from forge.cli.project import app


def test_project_cli_exists():
    assert app is not None