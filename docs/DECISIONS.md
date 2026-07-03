# Architecture Decisions

## ADR-0001

Decision

Use layered architecture.

Status

Accepted

Reason

Clear separation between business logic and infrastructure.

---

## ADR-0002

Decision

Services are implemented as classes.

Status

Accepted

Reason

Dependency Injection and testing.

---

## ADR-0003

Decision

Use Providers instead of calling external libraries directly.

Status

Accepted

Reason

Infrastructure can be replaced without changing business logic.

---

## ADR-0004

Decision

Forge works with engineering domains rather than technologies.

Status

Accepted

Reason

AI should reason about repositories, workspaces and tasks rather than Git commands.