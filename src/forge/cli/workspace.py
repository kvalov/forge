from __future__ import annotations

import typer

from forge.infrastructure.filesystem.local_filesystem_adapter import (
    LocalFilesystemAdapter,
)
from forge.workspace.service import WorkspaceService

app = typer.Typer(
    help="Workspace commands",
)


@app.command("info")
def info() -> None:
    """Display workspace information."""

    service = WorkspaceService(
        LocalFilesystemAdapter()
    )

    state = service.state()

    typer.echo()
    typer.echo("Workspace")
    typer.echo("─" * 40)

    typer.echo(f"Project      : {state.project_name}")
    typer.echo(f"Root         : {state.root}")

    typer.echo()
    typer.echo(f"Files        : {state.file_count}")
    typer.echo(f"Directories  : {state.directory_count}")
    typer.echo(f"Python Files : {state.python_files}")

    typer.echo()
    typer.echo(f"Git          : {'YES' if state.has_git else 'NO'}")
    typer.echo(f"pyproject    : {'YES' if state.has_pyproject else 'NO'}")
    typer.echo(f"README       : {'YES' if state.has_readme else 'NO'}")
    typer.echo(f"Tests        : {'YES' if state.has_tests else 'NO'}")