# Forge Architecture

> Architecture is a set of rules that allow Forge to evolve without becoming difficult to maintain.

---

# Vision

Forge is **not** a Git client.

Forge is **not** an AI wrapper.

Forge is an **AI Software Engineer**.

The purpose of Forge is to understand software projects, plan work, implement changes, review code and execute software engineering tasks autonomously.

External technologies (Git, filesystem, terminal, AI models) are implementation details.

---

# Core Principles

## 1. Domain First

Forge is organized around engineering domains, not technologies.

Good:

- Repository
- Workspace
- Analysis
- Planning
- Tasks
- AI

Avoid:

- Git
- OS
- subprocess
- OpenAI

Technologies belong to Infrastructure.

---

## 2. Services contain business logic

Business rules belong only to Services.

Services answer questions like:

- Can this repository be published?
- Is the workspace ready?
- Can a task start?

Services never contain CLI code.

Services never print to the console.

Services never know about Typer.

---

## 3. Providers communicate with external systems

Providers expose abstract capabilities.

Examples:

- RepositoryProvider
- WorkspaceProvider
- TerminalProvider
- AIProvider

Providers never contain business rules.

---

## 4. Infrastructure contains implementations

Infrastructure implements Providers.

Examples:

- GitPythonProvider
- LocalFilesystemProvider
- LocalTerminalProvider
- OpenAIProvider

Infrastructure may depend on third-party libraries.

Business logic must never depend directly on those libraries.

---

## 5. Models describe the domain

Models contain data.

Models do not perform work.

Models should be immutable whenever possible.

Preferred:

- dataclass(frozen=True)
- Pydantic models when validation is required

---

## 6. CLI is only an interface

CLI responsibilities:

- Parse commands
- Call services
- Display results

CLI never contains business logic.

---

## 7. Error handling is centralized

Every expected error derives from ForgeError.

Unexpected exceptions should be logged.

Expected errors should display:

- error code
- message
- hint

without a Python traceback.

---

## 8. Logging is centralized

Every module uses:

```python
logger = get_logger(__name__)
```

No module configures logging itself.

---

## 9. Testing

Every new feature must include tests.

Quality gate:

- pytest
- ruff
- mypy
- forge doctor

must pass before merging.

---

# Layered Architecture

```
            CLI
             │
             ▼
         Services
             │
             ▼
         Providers
             │
             ▼
      Infrastructure
             │
             ▼
     External Systems
```

Dependencies always point downward.

Reverse dependencies are forbidden.

---

# Domain Model

Forge should think in engineering concepts.

Preferred:

- Repository
- Workspace
- Task
- Analysis
- Plan
- Review

Avoid exposing implementation details such as Git commands to higher layers.

---

# Future Domains

Repository

- RepositoryService
- RepositoryProvider
- RepositoryState

Workspace

- WorkspaceService
- WorkspaceProvider
- WorkspaceState

Analysis

- Analyzer
- SymbolIndex
- AST

Planning

- Planner
- TaskEngine

AI

- AIProvider
- PromptEngine
- Memory

---

# Architectural Rules

Never:

- print() from Services
- call GitPython directly from CLI
- call subprocess from Services
- return dictionaries from Services
- duplicate business rules

Always:

- use Models
- use Providers
- use Services
- raise ForgeError
- keep modules focused on one responsibility

---

# Long-Term Goal

Forge should evolve from a command-line tool into an autonomous software engineering platform.

Every architectural decision should support that goal.