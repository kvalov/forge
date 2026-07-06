from pathlib import Path

from forge.workspace.ignore import is_ignored


def test_git_is_ignored():
    assert is_ignored(Path(".git/config"))


def test_venv_is_ignored():
    assert is_ignored(Path(".venv/Lib/site-packages/a.py"))


def test_pycache_is_ignored():
    assert is_ignored(Path("__pycache__/main.pyc"))


def test_python_source_is_not_ignored():
    assert not is_ignored(Path("src/forge/main.py"))