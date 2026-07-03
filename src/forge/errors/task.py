from forge.errors.base import ErrorInfo, ForgeError


class TaskError(ForgeError):
    """Task exception."""

    def __init__(
        self,
        message: str,
        *,
        code: str = "TASK001",
        hint: str = "Verify task execution.",
    ) -> None:
        super().__init__(
            ErrorInfo(
                code=code,
                message=message,
                hint=hint,
            )
        )