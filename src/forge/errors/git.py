from forge.errors.base import ErrorInfo, ForgeError


class GitError(ForgeError):
    """Base Git exception."""

    def __init__(
        self,
        message: str,
        *,
        code: str = "GIT001",
        hint: str = "Verify that the current directory is a Git repository.",
    ) -> None:
        super().__init__(
            ErrorInfo(
                code=code,
                message=message,
                hint=hint,
            )
        )