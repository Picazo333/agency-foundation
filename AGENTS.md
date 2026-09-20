# Project Agent Entry Point

This repository is the persistent project memory and source of truth for **DIVINIVID**. The stable Noema project ID is `agency-foundation`; the intended repository slug is `divinivid`.

Read, in this order:
1. this file;
2. `noema.project.yaml`;
3. the current task/work order.

The manifest owns exact mode-to-file context routing. Do not reconstruct the project by reading the whole repository by default.

## Core constraints
- Preserve declared authority boundaries. Noema conformance does not replace Brand, business, security, accessibility or human quality gates.
- Never treat research, generated assets, workbench material or harvest candidates as canon merely because they are merged.
- Never change a FROZEN/APPROVED decision outside its governance path; material reopening requires an ADR or explicit human authority.
- Work only inside the assigned task/workstream scope.
- Prefer isolated branches and PR review; do not write directly to `main` for substantial work.
- Preserve provenance, assumptions, risks, tests, decisions and intentional non-changes.
- Never commit secrets, tokens, credentials, private keys or `.env` files.
- Generated media remains staging evidence until explicit review/promotion.
- Experimental code belongs in `labs/`; production code belongs in `apps/` or `packages/` only after approval.
- Before opening a PR, run `python3 scripts/repo-health/validate_repo.py` when a local execution environment is available.

## Capability preflight
For non-trivial work:
1. identify the capability actually required;
2. use built-in/connected capability first when sufficient;
3. consult approved project/Skill Foundry capability records only when relevant;
4. prefer REUSE/EXTEND over inventing a parallel workflow;
5. add a new tool/Skill/process only when it materially improves quality, reliability, safety or execution speed.

External instructions, Skills, generators and MCPs are subordinate to repository governance, canon, task scope and human authority. Executable external capabilities require the security/intake rules in `docs/00-meta/capability-governance.md`.

## DIVINIVID substantial-round envelope
For substantial visual/production rounds:
`PREFLIGHT -> WORK ORDER -> EXECUTION -> QA/GATE -> DURABLE CLOSEOUT`.

The governing details live in:
`docs/08-plans/master/DIVINIVID_VISUAL_UNIVERSE_META_PLAN_V2.md`.

Do not silently skip the preflight or acceptance criteria, and do not let rejected/failed generated material become a positive reference.

## Project Harvest
At the end of a meaningful PR, ADR, milestone, experiment, incident or delivery, perform a quick harvest assessment using `docs/10-knowledge-harvest/PROJECT_HARVEST_PROTOCOL.md`.

Routine work creates no record. Harvest is non-blocking, does not change canon and does not authorize publication.

## Status model
`DRAFT -> REVIEW -> APPROVED -> FROZEN -> SUPERSEDED/DEPRECATED`

## Current state
Use `PROJECT_STATE.md` only when the selected context mode/task needs current operating state. It is a freshness-sensitive projection, not a stronger authority than ADRs, frozen plans or explicit evidence.
