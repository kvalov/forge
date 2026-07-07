# Forge Roadmap

> Long-term engineering roadmap.

---

# Vision

Forge aims to become an AI-native software engineering platform capable of understanding, analyzing and evolving large software systems.

The project is intentionally developed in phases.

Each phase builds the foundation for the next.

---

# Guiding Principle

Every new capability must be built on understanding.

```
Understand

↓

Analyze

↓

Plan

↓

Review

↓

Generate

↓

Automate
```

AI is the final step.

Understanding is the first.

---

# Phase 1 — Foundation

Status

✅ Completed

Objective

Build a clean, testable engineering platform.

Delivered

- Bootstrap
- Configuration
- Logging
- Error Model
- Repository Service
- Workspace Service
- Project Scanner
- Project Analyzer
- Python Parser
- Symbol Index
- Doctor Framework

Quality

- Ruff
- MyPy
- Pytest
- Clean Architecture

---

# Phase 2 — Code Intelligence

Status

🚧 In Progress

Objective

Build a semantic understanding of Python projects.

Planned

## Import Graph

Understand module dependencies.

```
Module A

↓

Module B
```

---

## Reference Graph

Locate symbol usages.

```
WorkspaceService

↓

ProjectService

↓

RepositoryService
```

---

## Call Graph

Understand runtime call relationships.

```
main()

↓

ProjectService

↓

PythonIndexer

↓

SymbolVisitor
```

---

## Dependency Graph

Understand component dependencies.

---

## Architecture Graph

Produce a complete structural model of the project.

---

# Phase 3 — Engineering Intelligence

Objective

Reason about software.

Planned

## Planner

Plan implementation steps.

---

## Reviewer

Review pull requests.

---

## Refactoring Assistant

Suggest safe architectural improvements.

---

## Documentation Generator

Generate technical documentation automatically.

---

## Test Impact Analysis

Determine which tests are affected by code changes.

---

# Phase 4 — AI Engineering

Objective

Introduce AI-assisted software engineering.

Planned

- AI Planner
- AI Reviewer
- AI Coder
- AI Documentation
- AI Architecture Advisor

Every AI component will operate on the semantic model produced during Phase 2.

---

# Phase 5 — Autonomous Engineering

Objective

Execute engineering workflows with minimal human intervention.

Planned

- Task Engine
- Job Scheduler
- Autonomous Pull Requests
- Automated Refactoring
- Continuous Architecture Monitoring

---

# Technical Debt

Known improvements.

## Doctor

- JSON output
- Machine-readable reports

---

## Python

- Method indexing
- Qualified names
- Line numbers
- Decorator analysis

---

## Repository

- Diff analysis
- Commit graph
- Branch comparison

---

## Workspace

- Incremental scanning
- Cache
- File watching

---

# Quality Goals

Every release should maintain:

- 100% passing tests
- Zero Ruff issues
- Zero MyPy issues

---

# Release Strategy

## v0.2 Alpha

Foundation complete.

---

## v0.3 Alpha

Code Intelligence.

---

## v0.4 Alpha

Engineering Intelligence.

---

## v0.5 Beta

AI-assisted development.

---

## v1.0

Stable engineering platform.

---

# Long-Term Goal

Forge should eventually answer questions such as:

- What does this project do?
- How is the architecture organized?
- What will break if this class changes?
- Which components depend on this module?
- Which tests should run after this change?
- How should this feature be implemented?

The ultimate objective is to build an engineering platform capable of reasoning about software systems before modifying them.