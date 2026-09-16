---
status: approved
owner: brand
updated: 2026-09-16
authority: workbench
depends_on:
  - ../routes/01-kirograf/EVALUATION_PROTOCOL.md
  - ../../../../08-plans/workstreams/DIVINIVID_VISUAL_IDENTITY_MASTER_PLAN.md
---
# DIVINIVID Evaluations

Store material phase/route gate records here.

## Naming
`YYYY-MM-DD_PHASE_<NN>_<short-name>.md`

Examples:
- `2026-09-XX_PHASE_01_CREATIVE_DIRECTION_GATE.md`
- `2026-09-XX_PHASE_03_REFERENCE_ATLAS_GATE.md`
- `2026-09-XX_PHASE_07_SIGNATURE_GATE.md`

## Required decision state
Every record ends in exactly one:
- `PASS`
- `MUTATE`
- `KILL`

Do not use ambiguous states such as “pretty good”, “approved-ish”, “close enough”, “maybe” or an unbounded “continue exploring”.

## Plan deviation records
Material changes to the frozen Master Plan belong here as `PLAN_DEVIATION` records and require explicit human approval.

Template:

```text
PLAN_DEVIATION
phase:
requested_change:
reason:
evidence_or_new_constraint:
impact_on_downstream_phases:
what_remains_frozen:
rollback_path:
human_approval:
```

A new tool or attractive reference is not, by itself, enough reason to alter the frozen method.
