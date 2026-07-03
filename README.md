# Forge

Forge is a local AI Software Engineer designed to understand, build and maintain software projects.

## Current Status

Current version:

**v0.1.0-foundation**

Completed:

- Bootstrap
- Doctor
- Configuration
- Logging

In Progress:

- Git Service

## Goals

- Understand existing projects
- Plan software changes
- Generate code
- Review code
- Execute development tasks autonomously

## Development

Create virtual environment

```powershell
python -m venv .venv
```

Install dependencies

```powershell
py -3.12 -m uv sync
```

Run Doctor

```powershell
.\.venv\Scripts\forge.exe doctor
```