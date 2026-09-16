# AGENTS.md

This repository is the persistent project memory and source of truth for the Agency Foundation program.

## Required reading before work
1. `PROJECT_STATE.md`
2. `docs/00-meta/source-of-truth.md`
3. `docs/00-meta/operating-model.md`
4. the active workstream spec under `docs/08-plans/workstreams/`
5. relevant ADRs under `docs/07-decisions/`

## Core rules
- Never treat research, generated assets, or workbench material as approved canon.
- Never change a FROZEN decision without an explicit reopening ADR.
- Work only inside the scope assigned to your workstream/task.
- Prefer small branches and PRs; do not write directly to `main`.
- State what you intentionally did **not** change.
- Preserve traceability: sources, assumptions, risks, tests, and decisions.
- Never commit secrets, tokens, credentials, private keys, or `.env` files.
- Generated assets belong in `assets/generated/`; approved assets belong in `assets/approved/` only after review.
- Experimental code belongs in `labs/`; production code belongs in `apps/` or `packages/` only after approval.
- **Before opening a PR**, run `python3 scripts/repo-health/validate_repo.py` locally to verify repository health and ensure no secrets or broken links are introduced.

## Status model
`DRAFT -> REVIEW -> APPROVED -> FROZEN -> SUPERSEDED/DEPRECATED`

## Ownership summary
- ChatGPT / human creative direction: `docs/03-brand/`
- Claude/CoWork: `docs/02-strategy/`, `docs/04-operations/`, `docs/06-validation/`, `docs/08-plans/`
- Gemini Asset Factory: `asset-factory/`, `assets/generated/`
- Codex: `apps/`, `packages/`, `scripts/`, `infra/`, approved technical docs
- Antigravity: primarily `labs/`
- Jules: issue-scoped repo changes through branch + PR

See `docs/00-meta/agent-contracts.md` for full contracts.
