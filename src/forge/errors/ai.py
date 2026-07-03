from forge.errors.base import ErrorInfo, ForgeError


class AIError(ForgeError):
    def __init__(
        self,
        message: str,
        hint: str = "Verify AI model configuration.",
    ):
        super().__init__(
            ErrorInfo(
                code="AI001",
                message=message,
                hint=hint,
            )
        )