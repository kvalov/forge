from forge.cli.repository import app


def test_repository_cli_exists():
    assert app is not None