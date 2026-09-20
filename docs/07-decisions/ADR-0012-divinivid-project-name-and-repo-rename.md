# ADR-0012 — Adopt DIVINIVID as project display name and plan repository slug rename

Status: APPROVED
Date: 2026-09-20

## Context
The repository began as `agency-foundation` while the agency name and identity were unresolved. The human owner has now selected **DIVINIVID** as the project/brand name for the current identity and has explicitly requested that the repository identity reflect it.

Git repository names and Noema project identifiers serve different purposes. Renaming both simultaneously would create avoidable provenance and cross-project relation churn.

## Decision
1. The human-facing project/brand name is **DIVINIVID**.
2. The intended GitHub repository slug is `divinivid`.
3. The stable Noema `project.id` remains `agency-foundation` during the rename so historical relations, manifests and provenance do not break.
4. Documentation should use DIVINIVID for the project/brand except where a historical repository identifier is technically required.
5. Legal/trademark/domain diligence remains a separate commercial gate; it does not reopen visual work unless it finds a real blocker.

## Alternatives considered
- Keep the public project name as Agency Foundation indefinitely.
- Change both repository slug and Noema project ID at once.
- Create a new repository and abandon history.

## Why
The selected identity is now mature enough that the working repository name is misleading. Preserving a stable machine identity while changing the human-facing name follows Noema's separation of durable identity from storage/provider location.

## Consequences
### Positive
- clearer project identity;
- less naming ambiguity for agents and collaborators;
- repository rename can occur without breaking the Noema graph.

### Trade-offs
- for a period, repository slug and project display name may differ;
- historical links/documentation may continue to contain `agency-foundation`.

## Evidence / assumptions
Human owner instruction on 2026-09-20; current DIVINIVID Brand workbench and approved visual baseline.

## Reopen if
- commercial diligence blocks use of DIVINIVID;
- a future ecosystem migration requires changing the stable project ID.
