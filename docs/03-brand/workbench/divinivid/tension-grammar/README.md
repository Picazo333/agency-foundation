---
status: review
owner: brand
updated: 2026-09-16
authority: workbench
depends_on:
  - ../reference-atlas/README.md
---
# DIVINIVID Tension Grammar

## State
Phase 4 scaffold. Do not fill from memory before the Reference Atlas is approved.

## Purpose
Translate source references into portable visual rules so later production no longer depends on artist/film names.

## Required grammar domains
- light
- color
- body
- grotesque
- geometry
- composition
- texture/material
- annotation/information
- symbolism
- motion
- narrative
- density

## Record format
For every retained mechanism:

```text
GRAMMAR_RULE_ID:
source_reference_ids:
master_tension:
observed_mechanism:
abstract_rule:
allowed_use:
misuse_or_limit:
proof_needed:
status: CANDIDATE / PASSED / MUTATE / KILLED
```

## Translation rule
Never write “make it look like [artist/film]” as a production instruction. Translate the observable mechanism first.

A rule is useful only if another capable designer can reproduce the mechanism without having to copy the source work.

## Phase gate
`DIVINIVID_VISUAL_GRAMMAR_V0` may be declared only after:
- all five positive Atlas boards pass;
- redundant rules are deduplicated;
- every rule maps to at least one master tension;
- every rule includes misuse/limit guidance;
- the human creative owner approves the grammar as sufficient to begin Route 01 territory production.
