# ADR-0005 — Capability-first workstreams and executor substitution

Status: APPROVED
Date: 2026-09-15

## Context
The Agency Foundation program intentionally experimented with multiple AI execution surfaces. Gemini/Gemini CLI was assigned to Asset Factory Architecture and Antigravity to the Neutral Technical Foundation. In practice, introducing additional local/CLI setup and authentication paths increased coordination cost before those tools provided unique value for the current tasks.

The workstream scopes themselves remain valid. The problem is executor complexity, not capability need.

## Decision
Define workstreams by their capability contract, not by the tool originally assigned to them.

Reassign current execution as follows:

- Issue #3 — Asset Factory Architecture -> Jules -> `asset/jules-asset-factory-architecture`.
- Issue #4 — Neutral Technical Foundation -> Jules -> `tech/jules-technical-foundation`.
- Issue #6 — Repo Hardening -> Jules -> `tech/jules-repo-hardening`.
- Issue #2 — Agency Master Plan -> Claude Code.
- Brand Direction remains human + ChatGPT.

Jules may execute #3, #4 and #6 in parallel only as separate isolated tasks/branches/PRs. Scope boundaries remain independent.

Gemini and Antigravity remain available later as optional execution providers, not project dependencies.

## Why
- Reduce setup/authentication/local-environment overhead.
- Reduce context switching while the project is still in foundation/decision stages.
- Preserve parallelism through isolated Jules tasks instead of through additional products.
- Keep the project architecture tool-agnostic.
- Avoid making learning a new tool a dependency for completing a capability that another connected executor can already deliver.
- Preserve the option to reintroduce specialized tools when they provide a measurable advantage.

## Alternatives considered

### Keep Gemini CLI for Issue #3
Rejected for the current phase because the task is primarily architecture/specification work and does not require Gemini-specific generation capability yet.

### Keep Antigravity for Issue #4
Rejected for the current phase because local/worktree setup adds operational friction and the required neutral foundations can be delivered through a scoped repo agent.

### Collapse #3, #4 and #6 into one Jules task
Rejected. Using one executor does not justify merging separate capability contracts. The workstreams have different scopes, files, risks and Definitions of Done.

## Consequences
- Fewer active tool surfaces to configure and supervise.
- Jules becomes a shared executor but not a shared workstream.
- Branch/Issue/PR isolation becomes more important because one executor is performing multiple concurrent tasks.
- Asset Factory architecture must remain generator-agnostic; Gemini may later plug into it.
- Technical Foundation must remain environment/tool-agnostic; Antigravity may later consume or extend it.
- Existing legacy branches/files mentioning Gemini/Antigravity may be retained for history where renaming would create unnecessary churn, but active execution uses Jules-named branches.

## Non-regression requirements
The reassignment must not reduce:
- scope;
- validation/audit depth;
- provenance/security requirements;
- branch isolation;
- PR review;
- Definitions of Done;
- future compatibility with Gemini or Antigravity.

## Reopen if
- Jules cannot perform a required capability without substantial quality loss;
- Gemini or Antigravity offers a unique capability that materially improves the workstream;
- concurrency limits or execution constraints make executor consolidation slower or less reliable than separate tools;
- a later production phase benefits from specialized local/interactive tooling enough to justify the added setup cost.
