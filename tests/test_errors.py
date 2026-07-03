from forge.errors import ErrorInfo, ForgeError


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