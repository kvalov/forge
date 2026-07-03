from forge.errors.base import ErrorInfo, ForgeError


class GitError(ForgeError):
    def __init__(
        self,
        message: str,
        hint: str = "Verify that the current directory is a Git repository.",
    ):
        super().__init__(
            ErrorInfo(
                code="GIT001",
                message=message,
                hint=hint,
            )
        )