from __future__ import annotations

import typer

from forge.infrastructure.filesystem.local_filesystem_adapter import (
    LocalFilesystemAdapter,
)
from forge.python.indexer import PythonIndexer
from forge.workspace.service import WorkspaceService

app = typer.Typer(
    help="Python symbol commands.",
)


def _index():
    workspace = WorkspaceService(
        LocalFilesystemAdapter()
    )

    return PythonIndexer(workspace).build()


@app.command()
def list() -> None:
    """List all indexed symbols."""

    index = _index()

    typer.echo()
    typer.echo("Symbols")
    typer.echo("─" * 40)

    typer.echo()
    typer.echo("Classes")
    typer.echo("-" * 20)

    for symbol in sorted(
        index.classes(),
        key=lambda s: s.name,
    ):
        typer.echo(symbol.name)

    typer.echo()
    typer.echo("Functions")
    typer.echo("-" * 20)

    for symbol in sorted(
        index.functions(),
        key=lambda s: s.name,
    ):
        typer.echo(symbol.name)


@app.command()
def find(name: str) -> None:
    """Find a symbol."""

    index = _index()

    symbol = index.get(name)

    if symbol is None:
        typer.echo(f"Symbol '{name}' not found.")
        raise typer.Exit(1)

    typer.echo()
    typer.echo(symbol.name)
    typer.echo("─" * 40)
    typer.echo(f"Kind    : {symbol.kind.value}")
    typer.echo(f"Module  : {symbol.module}")
    typer.echo(f"Line    : {symbol.line}")