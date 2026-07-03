from forge.errors import GitError


def test_git_error():
    error = GitError("Repository not found")

    assert error.code == "GIT001"
    assert error.message == "Repository not found"
    assert error.hint != ""