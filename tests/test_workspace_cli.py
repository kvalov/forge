from forge.cli.workspace import app


def test_workspace_cli_exists():
    assert app is not None