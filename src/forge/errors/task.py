from forge.errors.base import ErrorInfo, ForgeError


class TaskError(ForgeError):
    def __init__(
        self,
        message: str,
        hint: str = "Verify the requested task.",
    ):
        super().__init__(
            ErrorInfo(
                code="TASK001",
                message=message,
                hint=hint,
            )
        )