from forge.errors.base import ErrorInfo, ForgeError


class AIError(ForgeError):
    """AI exception."""

    def __init__(
        self,
        message: str,
        *,
        code: str = "AI001",
        hint: str = "Verify AI configuration.",
    ) -> None:
        super().__init__(
            ErrorInfo(
                code=code,
                message=message,
                hint=hint,
            )
        )