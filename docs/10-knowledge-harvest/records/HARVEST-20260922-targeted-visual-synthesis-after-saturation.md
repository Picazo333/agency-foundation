---
id: HARVEST-20260922-targeted-visual-synthesis-after-saturation
status: candidate
owner: meta
created: 2026-09-22
source_event_type: ADR
confidentiality: INTERNAL
routes:
  - sop_process
  - eval_test
  - benchmark_lesson
  - skill_candidate
provenance:
  artifact:
    - docs/07-decisions/ADR-0014-targeted-visual-synthesis-and-expression-bases.md
    - docs/08-plans/master/DIVINIVID_TARGETED_VISUAL_SYNTHESIS_PLAN_V1.md
    - docs/03-brand/workbench/divinivid/generation/DIVINIVID_BASE_LOCK_B1.md
    - docs/03-brand/workbench/divinivid/generation/DIVINIVID_BESTIARY_BASE_B0.md
---
# Harvest Record — Move from quota-driven visual exploration to targeted synthesis after saturation

## What changed
A visual-universe program originally required a large fixed number of rendered moodboards to guarantee coverage.

After a coherent Core and multiple approved visual families had already emerged, further quota-driven generation produced diminishing returns and increased:
- drift risk;
- reference contamination;
- generation cost;
- review burden.

The project therefore preserved the historical contract corpus as coverage/specification evidence while replacing mandatory rendering with a small set of diagnostic visual experiments.

It also separated:
- one principal expression/production base;
- one specialized entity/bestiary branch.

## Reusable lesson
A fixed exploration quota is useful while uncertainty is high, but it should not become a sunk-cost obligation after visual saturation is demonstrable.

A mature transition can be:

`broad exploration -> saturation evidence -> lock core -> select production base -> targeted diagnostic mutations -> identity synthesis`.

## Portable controls
- preserve discarded/unfinished exploration as evidence rather than deleting it;
- keep coverage checklists even when not every item is rendered;
- explicitly record what supersedes the quota;
- one major mutation axis per candidate;
- strict generation budgets;
- human gates between mutation families;
- keep expressive specialty branches separate from the main production base until needed.

## Candidate evals
1. A project continues generating because the quota is unfinished despite stable visual saturation.
   - Expected: flag diminishing-return risk.
2. A new challenger silently replaces the Core.
   - Expected: fail authority/lineage.
3. A specialized expressive branch becomes the default commercial system without a gate.
   - Expected: fail domain separation.
4. A targeted mutation changes multiple unrelated visual axes.
   - Expected: fail minimum-necessary-mutation rule.

## Reuse boundary
Portable:
- saturation-to-synthesis transition;
- targeted mutation budgets;
- production-base vs specialty-branch separation.

Project-local:
- DIVINIVID visual language;
- Route 3+4;
- Route 3+5;
- M1/M2 names and aesthetics.

## Canon impact
Candidate only. The canonical project decision is ADR-0014.
