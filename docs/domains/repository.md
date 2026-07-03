# Repository Domain

## Purpose

The Repository domain represents the lifecycle of a software project stored in a version control system.

Forge does not interact with Git directly.

Forge interacts with a Repository.

Git is only one possible implementation.

---

# Ubiquitous Language

Repository

A version-controlled software project.

Workspace

The working tree of the repository.

Changes

Modified, staged or untracked files.

Feature

A unit of planned work.

Publication

Publishing work to the remote repository.

Snapshot

A saved state of the repository.

Recovery

Returning the repository to a consistent state.

---

# Entities

Repository

Represents a software repository.

RepositoryState

Represents the current repository status.

Branch

Represents a development branch.

Commit

Represents a repository snapshot.

Remote

Represents a remote repository.

---

# Value Objects

RepositoryName

BranchName

CommitHash

RemoteName

TagName

---

# Services

RepositoryService

Responsibilities

- inspect repository
- prepare workspace
- save progress
- publish work
- recover repository

RepositoryProvider

Responsibilities

- communicate with Git
- expose repository information

---

# Repository State

A RepositoryState contains:

- repository name
- current branch
- default branch
- clean state
- ahead commits
- behind commits
- modified files
- staged files
- untracked files
- merge conflicts
- detached head
- remote availability

---

# Use Cases

Read repository state

Prepare workspace

Save progress

Publish changes

Start feature

Finish feature

Recover repository

Create tag

Create release

---

# Business Rules

Services never expose GitPython.

Services never execute subprocess.

Services never return dictionaries.

RepositoryState is immutable.

Business logic belongs only to RepositoryService.

---

# Future Extensions

Multi-repository workspace

Submodules

Worktrees

Git LFS

Alternative providers

Cloud repositories