---
status: approved
owner: meta
updated: 2026-09-15
authority: canon
depends_on:
  []
---
# Agent Contracts

## Core rule
Workstream authority belongs to the **capability contract**, not to the name of the tool that first received the task. Executors may be substituted when this reduces complexity without reducing scope, validation or Definition of Done.

## ChatGPT / Brand Direction
Owns: `docs/03-brand/` proposals, synthesis and brand reviews.
Must not silently freeze business strategy.

## Claude Code / Agency Master Plan
Owns proposals under `docs/02-strategy/`, `docs/04-operations/`, `docs/06-validation/` and strategy planning outputs under `docs/08-plans/` as governed by Issue #2.
Must treat Brand workbench as context, not fixed commercial truth.

## Jules
Current active executor for three isolated workstreams:

1. **Asset Factory Architecture** — Issue #3 — branch `asset/jules-asset-factory-architecture`.
2. **Neutral Technical Foundation** — Issue #4 — branch `tech/jules-technical-foundation`.
3. **Repo Hardening / CI** — Issue #6 — branch `tech/jules-repo-hardening`.

Rules:
- one Issue/workstream per isolated task/branch;
- never work directly on `main`;
- no silent cross-workstream edits;
- each task returns its own PR;
- executor reuse does not merge scopes;
- no self-merge.

## Gemini
Not an active foundation-phase executor. Retained as an optional future asset-generation provider after Brand V1 and after the Asset Factory contract is approved. Gemini must consume Brand/Asset Factory contracts rather than redefine them.

## Antigravity
Not an active foundation-phase dependency. Retained as an optional later experimentation environment for motion/interaction/multi-agent prototypes when its incremental benefit justifies setup complexity. Experimental results do not enter production automatically.

## Codex / other implementation agents
May later own implementation surfaces such as `apps/`, `packages/`, `scripts/`, `infra/` under explicit Issues/specs. Prefer branch/worktree isolation and PR delivery.

## Human owner
Final authority over canonical decisions and merges that alter frozen strategy/brand.
