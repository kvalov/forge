from forge.errors.base import ErrorInfo, ForgeError


class ValidationError(ForgeError):
    """Validation exception."""

    def __init__(
        self,
        message: str,
        *,
        code: str = "VALID001",
        hint: str = "Verify input data.",
    ) -> None:
        super().__init__(
            ErrorInfo(
                code=code,
                message=message,
                hint=hint,
            )
        )