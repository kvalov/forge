from __future__ import annotations

import typer

from forge.infrastructure.git.gitpython_adapter import GitPythonAdapter
from forge.repository.service import RepositoryService

app = typer.Typer(
    help="Repository commands",
)


@app.command("status")
def status() -> None:
    """Show repository status."""

    service = RepositoryService(
        GitPythonAdapter()
    )

    state = service.state()

    typer.echo()
    typer.echo(f"Repository : {state.repository}")
    typer.echo(f"Branch     : {state.branch.name}")

    typer.echo()
    typer.echo("Status")
    typer.echo("-" * 30)

    typer.echo(f"Clean           : {'YES' if state.clean else 'NO'}")
    typer.echo(f"Modified files  : {len(state.modified_files)}")
    typer.echo(f"Staged files    : {len(state.staged_files)}")
    typer.echo(f"Untracked files : {len(state.untracked_files)}")
    typer.echo(f"Remote          : {'YES' if state.remote_available else 'NO'}")
    typer.echo(f"Detached HEAD   : {'YES' if state.detached_head else 'NO'}")