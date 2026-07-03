from forge.errors.base import ErrorInfo, ForgeError


class TerminalError(ForgeError):
    def __init__(
        self,
        message: str,
        hint: str = "Verify terminal execution.",
    ):
        super().__init__(
            ErrorInfo(
                code="TERM001",
                message=message,
                hint=hint,
            )
        )