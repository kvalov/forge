# Forge Architecture

## High Level Architecture

```
                User
                  │
                  ▼
        CLI / GUI / VS Code
                  │
                  ▼
           Command Dispatcher
                  │
        ┌─────────┼─────────┐
        ▼         ▼         ▼
     Services  Planner  Reviewer
        │
        ▼
     Providers
        │
        ▼
 Infrastructure
```

## Layers

### CLI

Responsible only for parsing commands and displaying output.

### Services

Contains all business logic.

### Providers

Access external systems such as Git, filesystem and terminal.

### Infrastructure

Lowest layer responsible for operating system integration.

---

## Rules

- CLI never contains business logic.
- Services never call CLI.
- Providers never know about the CLI.
- Every service should be testable.
- Prefer dependency injection over global state.