from forge.errors.base import ErrorInfo, ForgeError


class TerminalError(ForgeError):
    """Terminal exception."""

    def __init__(
        self,
        message: str,
        *,
        code: str = "TERM001",
        hint: str = "Verify terminal execution.",
    ) -> None:
        super().__init__(
            ErrorInfo(
                code=code,
                message=message,
                hint=hint,
            )
        )