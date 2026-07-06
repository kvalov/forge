from pathlib import Path

import pytest

from forge.errors import GitError
from forge.infrastructure.git.gitpython_adapter import GitPythonAdapter


def test_invalid_repository():
    adapter = GitPythonAdapter(Path("X:/this/path/does/not/exist"))

    with pytest.raises(GitError):
        adapter.state()