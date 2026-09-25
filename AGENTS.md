# Project Agent Entry Point

This repository is the persistent project memory and source of truth for **DIVINIVID**. The stable Noema project ID is `agency-foundation`; the intended repository slug is `divinivid`.

Read, in this order:
1. this file;
2. `noema.project.yaml`;
3. the current task/work order.
For image-generation calls, run the local reference-binding preflight described in `docs/03-brand/workbench/divinivid/evaluations/REFERENCE_BINDING_LOCAL_GUARD.md` before treating a request as Brand evidence.

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
ADR-0015 inserts a bounded Pre-Lock Exploration Program before final expression lock.

The historical 100-contract corpus remains coverage/specification evidence.

Mandatory authority order for current visual work:

`CURRENT_GENERATION_STATE -> CORE_LOCK -> BASE_LOCK_B1 -> M1-B_WORKING_ANCHOR -> CURRENT_MODULE_CONTRACT -> VISUAL_CANON -> ANTI_CANON -> EXECUTION -> QA -> HUMAN_GATE -> DURABLE_CLOSEOUT`.

Current authority hierarchy:
- `DIVINIVID_CORE_LOCK_V1` — frozen visual DNA;
- `BASE_LOCK_B1` — Route 3+4, principal expression/production base;
- `M1-B_TOPOGRAFIA_ORGANICA` — human-approved pre-lock working anchor;
- `BESTIARY_BASE_B0` — Route 3+5, specialized bestiary/apparition branch, excluded from default positive context during pre-lock exploration.

Current approved sequence:

`P1 Typography -> P2 Iconography -> P3 Hero -> P4 Density -> P5 Motion -> P6 Digital Behavior -> P7 Application Stress -> P8 Final Synthesis -> Independent Red Team -> Human Final Gate -> DIVINIVID_FINAL_EXPRESSION_LOCK_V1`.

Do not automatically generate the next candidate. Every material candidate requires an explicit human trigger.

### Pre-lock invariants
- Test one system variable at a time.
- Default context packet is only Core + B1 + M1-B + current module contract.
- Do not infer typography, iconography, labels or component rules from incidental details in M1-B.
- Do not use rejected/recent unapproved generations as positive references.
- Keep `REFERENCE_AVAILABLE != REFERENCE_BOUND != REFERENCE_EFFECTIVE` explicit.
- Keep BESTIARY_BASE_B0 out of default pre-lock context unless the active module explicitly requires the bestiary branch.
- Preserve minimum-necessary mutation.
- Do not reopen Core/B1 silently.
- Executor substitution requires a capability check.
- Generated output remains `EVIDENCE_PENDING` until human approval.

The governing current details live in:
- `docs/03-brand/workbench/divinivid/generation/CURRENT_GENERATION_STATE.yaml`;
- `docs/03-brand/workbench/divinivid/generation/DIVINIVID_CORE_LOCK_V1.md`;
- `docs/03-brand/workbench/divinivid/generation/DIVINIVID_BASE_LOCK_B1.md`;
- `docs/08-plans/master/DIVINIVID_PRE_LOCK_EXPLORATION_V1.md`;
- `docs/07-decisions/ADR-0015-pre-lock-exploration-before-final-expression-lock.md`.

Historical targeted-synthesis and Visual Universe documents remain reusable evidence but do not define the next active gate.

Do not silently skip preflight, acceptance criteria or human gates.

## Project Harvest
At the end of a meaningful PR, ADR, milestone, experiment, incident or delivery, perform a quick harvest assessment using `docs/10-knowledge-harvest/PROJECT_HARVEST_PROTOCOL.md`.

Routine work creates no record. Harvest is non-blocking, does not change canon and does not authorize publication.

## Status model
`DRAFT -> REVIEW -> APPROVED -> FROZEN -> SUPERSEDED/DEPRECATED`

## Current state
Use `PROJECT_STATE.md` only when the selected context mode/task needs current operating state. It is a freshness-sensitive projection, not a stronger authority than ADRs, frozen plans or explicit evidence.
