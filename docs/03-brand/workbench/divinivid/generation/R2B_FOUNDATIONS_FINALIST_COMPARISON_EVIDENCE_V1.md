---
status: approved
owner: brand
created: 2026-09-23
updated: 2026-09-23
authority: evidence
human_approved: true
depends_on:
  - docs/03-brand/workbench/divinivid/generation/R2A_FOUNDATIONS_TECHNICAL_VALIDATION_V1.md
  - docs/03-brand/workbench/divinivid/generation/R1_SIGNATURE_SYSTEM_LOCK_SBE_V1.md
  - docs/08-plans/master/DIVINIVID_CURRENT_EXECUTION_PLAN_V2.md
---
# R2-B Foundations — Finalist Comparison Evidence V1

## Purpose

Resolve the production typography finalist while preserving all already-approved identity variables.

R2-B does not reopen:
- P1 typographic direction;
- R1 S-BE signature architecture;
- P2 Minimal / No-Icons;
- color semantics;
- composition/hero/density/motion locks.

## R2-A input

R2-A passed technical validation and produced the bounded shortlist:

1. **Newsreader + IBM Plex Sans**
2. **Bodoni Moda + IBM Plex Sans**
3. **Source Serif 4 + IBM Plex Sans**

Fixed:
- operational sans: **IBM Plex Sans**;
- signature architecture: **S-BE Bilateral Body + Glyph-Class Logic**;
- candidate production color set;
- content;
- layout/proof conditions.

Only the display serif changes.

## Figma evidence

- file: `DIVINIVID — PRE-LOCK VISUAL LAB`;
- page: `R2 — FOUNDATIONS`;
- page id: `26:2`;
- comparison root: `26:3`.

Direct node URL:
`https://www.figma.com/design/bqcKhEQHs4EEQgnn6lNU8O/?node-id=26-3`

## Comparison matrix

### A — Newsreader + IBM Plex Sans

Question:
Can the existing R1 construction substrate mature into the production display serif while preserving authority and macro/micro behavior?

Expected strength:
- continuity;
- optical-size range;
- lower risk of generic fashion/luxury drift.

Expected failure mode:
- insufficient monumentality or excessive literary softness.

### B — Bodoni Moda + IBM Plex Sans

Question:
Can maximum display monumentality strengthen DIVINIVID without converting the identity into fashion/editorial luxury?

Expected strength:
- dramatic high-contrast authority;
- strongest natural monumentality.

Expected failure mode:
- generic luxury/fashion reading;
- fragile micro behavior.

### C — Source Serif 4 + IBM Plex Sans

Question:
Can maximum production robustness preserve enough identity when paired with the locked S-BE architecture?

Expected strength:
- broad editorial/system flexibility;
- implementation robustness;
- long-form usability.

Expected failure mode:
- rationality/genericity that weakens signature character.

## Proof conditions

Each finalist is tested on the same:
- S-BE wordmark architecture;
- black-on-ivory wordmark;
- ivory-on-black wordmark;
- hero statement;
- operational sans navigation;
- annotation/data;
- body copy;
- CTA;
- 32px wordmark;
- 16px wordmark;
- Spanish character proof;
- candidate production color set.

## Font assertion

Read-back validation confirmed:

- A contains only `Newsreader` + `IBM Plex Sans`;
- B contains only `Bodoni Moda` + `IBM Plex Sans`;
- C contains only `Source Serif 4` + `IBM Plex Sans`.

No proxy serif was substituted.

## Candidate production color set under review

- `darkness/950 #060604`
- `ivory/100 #E8DDC9`
- `ivory/200 #CEB39A`
- `crimson/ui #C15B4D`
- `crimson/matter #601C16`
- `gold/text #BDA16F`
- `gold/instrument #856A47`
- `ultramar/ui #6984B4`
- `ultramar/matter #102139` remains documented in R2-A even though it is not a primary swatch in every proof surface.

The color set is one candidate implementation of already-approved color semantics, not a new palette direction.

## Visual QA

Initial construction exposed two deterministic layout defects:
1. unintended white fills on structural auto-layout containers;
2. clipped/overlapping proof copy.

Both were corrected without changing the comparison variables.

The latest screenshot is the valid evidence state.

## Human typography decision

**A — Newsreader + IBM Plex Sans: PASS / SELECTED**

The human creative owner selected Newsreader as the production display-serif direction.

Locked typography result inside R2:
- display serif: `NEWSREADER`;
- operational sans: `IBM_PLEX_SANS`.

Bodoni Moda and Source Serif 4 remain rejected comparison evidence and are no longer active finalists.

This closes the typography decision inside R2 but does **not** yet close Foundations.

## Bounded color-role coverage repair — 2026-09-23

A deterministic review found one documentation/proof gap: R2-A required light/dark surface behavior, but the measured table only quantified the palette against `darkness/950`.

This was repaired **without changing any primitive color value and without creating a second palette**.

Figma proof:
- root remains `26:3`;
- bounded repair node: `31:2` — `R2B-COLOR-ROLE-PROOF-V1`.

### Measured light-surface behavior

| Token | vs `ivory/100 #E8DDC9` | vs `ivory/200 #CEB39A` | Authorized light-surface behavior |
|---|---:|---:|---|
| `darkness/950 #060604` | 15.08:1 | 10.18:1 | primary/default text |
| `crimson/matter #601C16` | 9.32:1 | 6.29:1 | crimson accent alias on light; not default body copy |
| `ultramar/matter #102139` | 12.03:1 | 8.12:1 | rare ultramar accent alias on light |
| `gold/instrument #856A47` | 3.76:1 | 2.54:1 | non-text only on ivory/100; restricted on ivory/200 |
| `crimson/ui #C15B4D` | 3.21:1 | 2.16:1 | not normal text on ivory surfaces |
| `gold/text #BDA16F` | 1.84:1 | 1.24:1 | dark-surface text token only |
| `ultramar/ui #6984B4` | 2.81:1 | 1.90:1 | dark-surface UI/text token only |

Semantic clarification:
- on Living Darkness, use the existing `*/ui` and `gold/text` roles exactly as already specified;
- on ivory surfaces, default readable text is `darkness/950`;
- `crimson/matter` may act as semantic alias `accent/crimson/on-light`;
- `ultramar/matter` may act as semantic alias `accent/ultramar/on-light`;
- these aliases add **roles only**, not new primitives;
- color must never be the sole carrier of meaning.

Repair status:
`COMPLETE_READY_FOR_HUMAN_REVIEW`.

## Human color decision

**PASS — candidate production color mapping approved.**

The human creative owner approved the candidate color mapping after the bounded light-surface role repair.

R2-B is closed.

Review the single candidate production mapping:

- `darkness/950 #060604`
- `ivory/100 #E8DDC9`
- `ivory/200 #CEB39A`
- `crimson/ui #C15B4D`
- `crimson/matter #601C16`
- `gold/text #BDA16F`
- `gold/instrument #856A47`
- `ultramar/ui #6984B4`
- `ultramar/matter #102139`

No second aesthetic palette is authorized by default.

Promotion consequence executed:
1. `DIVINIVID_FOUNDATIONS_LOCK_V1` created;
2. R2 marked `COMPLETE_PASS`;
3. R3/R4/R5 Formalization Cluster entered.

## Promotion consequence

If typography and color pass:
1. create `DIVINIVID_FOUNDATIONS_LOCK_V1`;
2. close R2;
3. enter the R3/R4/R5 Formalization Cluster.

If a bounded failure is identified:
- mutate only the named typography/color variable;
- do not add new font families or palettes without material evidence.
