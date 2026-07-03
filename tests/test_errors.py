from forge.errors import (
    AIError,
    ConfigurationError,
    FilesystemError,
    GitError,
    TaskError,
    TerminalError,
    ValidationError,
)


def test_git_error():
    error = GitError("Repository not found")
    assert error.code == "GIT001"


def test_configuration_error():
    error = ConfigurationError("Missing configuration")
    assert error.code == "CONFIG001"


def test_filesystem_error():
    error = FilesystemError("File not found")
    assert error.code == "FS001"


def test_terminal_error():
    error = TerminalError("Command failed")
    assert error.code == "TERM001"


def test_task_error():
    error = TaskError("Task failed")
    assert error.code == "TASK001"


def test_ai_error():
    error = AIError("Model unavailable")
    assert error.code == "AI001"


def test_validation_error():
    error = ValidationError("Invalid input")
    assert error.code == "VALID001"