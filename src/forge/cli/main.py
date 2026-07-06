from __future__ import annotations

import typer

from forge.cli.repository import app as repository_app
from forge.services.doctor import DoctorService
from forge.cli.workspace import app as workspace_app
app = typer.Typer(
    help="Forge AI Software Engineer",
)

app.add_typer(
    repository_app,
    name="repository",
)

app.add_typer(
    workspace_app,
    name="workspace",
)

@app.command()
def doctor() -> None:
    """Run diagnostics."""

    raise typer.Exit(
        DoctorService().check()
    )


def main() -> None:
    app()