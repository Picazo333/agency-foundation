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

### Current visual strategy
ADR-0014 supersedes mandatory rendering of the full historical 100-board program.

The 100-contract corpus remains coverage/specification evidence, but current visual production follows targeted synthesis.

Mandatory authority order for current visual work:

`CURRENT_GENERATION_STATE -> CORE_LOCK -> ACTIVE_EXPRESSION_BASE -> TARGETED_PHASE_CONTRACT -> VISUAL_CANON -> ANTI_CANON -> EXECUTION -> QA -> HUMAN_GATE -> DURABLE_CLOSEOUT`.

Current locked hierarchy:
- `DIVINIVID_CORE_LOCK_V1` — frozen visual DNA;
- `BASE_LOCK_B1` — Route 3+4, principal expression/production base;
- `BESTIARY_BASE_B0` — Route 3+5, specialized bestiary/apparition branch.

Current approved sequence:
`M1-A Anatomía Celeste -> M1-B Topografía Orgánica -> human comparison -> optional bounded synthesis -> M2-Soft -> M2-Hard -> human comparison -> MAIN_SYSTEM_B2`.

Do not automatically generate the next candidate. Every material candidate requires an explicit human trigger.

### Visual-generation invariants
- Bind only approved positive references appropriate to the active phase.
- Keep `REFERENCE_AVAILABLE != REFERENCE_BOUND != REFERENCE_EFFECTIVE` explicit.
- Do not use rejected or recent unapproved generations as positive references.
- Keep the bestiary branch out of the principal B1 evolution until its deferred phase is explicitly opened.
- Use minimum-necessary mutation: one major development axis per candidate.
- Do not reopen the Core or silently replace B1/B0.
- Executor substitution requires a capability check.
- Generated output remains `EVIDENCE_PENDING` until human approval.

The governing current details live in:
- `docs/03-brand/workbench/divinivid/generation/CURRENT_GENERATION_STATE.yaml`;
- `docs/03-brand/workbench/divinivid/generation/DIVINIVID_CORE_LOCK_V1.md`;
- `docs/03-brand/workbench/divinivid/generation/DIVINIVID_BASE_LOCK_B1.md`;
- `docs/03-brand/workbench/divinivid/generation/DIVINIVID_BESTIARY_BASE_B0.md`;
- `docs/08-plans/master/DIVINIVID_TARGETED_VISUAL_SYNTHESIS_PLAN_V1.md`;
- `docs/07-decisions/ADR-0014-targeted-visual-synthesis-and-expression-bases.md`.

The older Visual Universe meta-plan, 100-board spec/contracts and runtime-lock artifacts remain historical evidence and reusable coverage material where relevant.

Do not silently skip preflight, acceptance criteria or human gates.

## Project Harvest
At the end of a meaningful PR, ADR, milestone, experiment, incident or delivery, perform a quick harvest assessment using `docs/10-knowledge-harvest/PROJECT_HARVEST_PROTOCOL.md`.

Routine work creates no record. Harvest is non-blocking, does not change canon and does not authorize publication.

## Status model
`DRAFT -> REVIEW -> APPROVED -> FROZEN -> SUPERSEDED/DEPRECATED`

## Current state
Use `PROJECT_STATE.md` only when the selected context mode/task needs current operating state. It is a freshness-sensitive projection, not a stronger authority than ADRs, frozen plans or explicit evidence.
