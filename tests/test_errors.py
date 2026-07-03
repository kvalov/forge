from forge.errors import (
    AIError,
    ConfigurationError,
    ErrorInfo,
    FilesystemError,
    ForgeError,
    GitError,
    TaskError,
    TerminalError,
    ValidationError,
)


def test_error_info():
    error = ErrorInfo(
        code="TEST001",
        message="Something went wrong",
        hint="Try again",
    )

    assert error.code == "TEST001"
    assert error.message == "Something went wrong"
    assert error.hint == "Try again"


def test_forge_error():
    error = ForgeError(
        ErrorInfo(
            code="TEST001",
            message="Failure",
            hint="Retry",
        )
    )

    assert error.code == "TEST001"
    assert error.message == "Failure"
    assert error.hint == "Retry"
    assert str(error) == "[TEST001] Failure"


def test_git_error():
    error = GitError("Repository not found")

    assert error.code == "GIT001"
    assert str(error) == "[GIT001] Repository not found"


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