from forge.doctor.checks import (
    GitCheck,
    PythonCheck,
    UvCheck,
    WorkspaceCheck,
)


def test_python_check():
    result = PythonCheck().run()

    assert result.ok
    assert result.name == "Python"


def test_git_check():
    result = GitCheck().run()

    assert result.name == "Git"


def test_uv_check():
    result = UvCheck().run()

    assert result.name == "uv"


def test_workspace_check():
    result = WorkspaceCheck().run()

    assert result.name == "Workspace"