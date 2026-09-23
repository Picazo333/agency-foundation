---
status: approved
owner: brand
created: 2026-09-23
updated: 2026-09-23
authority: module_lock
human_approved: true
depends_on:
  - docs/03-brand/workbench/divinivid/generation/R2A_FOUNDATIONS_TECHNICAL_VALIDATION_V1.md
  - docs/03-brand/workbench/divinivid/generation/R2B_FOUNDATIONS_FINALIST_COMPARISON_EVIDENCE_V1.md
  - docs/03-brand/workbench/divinivid/generation/R1_SIGNATURE_SYSTEM_LOCK_SBE_V1.md
  - docs/08-plans/master/DIVINIVID_CURRENT_EXECUTION_PLAN_V2.md
---
# DIVINIVID Foundations Lock V1

## Decision

The human creative owner approved the R2 Foundations candidate on 2026-09-23.

This closes **R2 — Foundations**.

No prior lock is reopened by this decision.

## Production typography

### Display serif
**Newsreader**

Role:
- display/editorial authority;
- signature substrate for the locked S-BE architecture;
- macro/micro display behavior;
- high-value headings and editorial statements.

### Operational sans
**IBM Plex Sans**

Role:
- navigation;
- body/UI copy;
- data;
- annotations;
- operational and clinical/B2B-sensitive surfaces.

Typography policy:
- maximum default: two production families;
- no proxy substitution may silently replace either family;
- fallback stacks remain implementation concerns, not identity redesign opportunities.

## Signature constraint

Typography must preserve:

**S-BE — Bilateral Body + Glyph-Class Logic**

- S-B controls bilateral global wordmark architecture and central-spine balance;
- S-E controls repeatable D/I/V/N glyph-class behavior;
- no decorative monogram or icon is authorized by default;
- palindrome remains structural rather than ornamental.

## Production color primitives

| Token | Value | Primary role |
|---|---|---|
| `darkness/950` | `#060604` | dominant field; primary text on ivory |
| `ivory/100` | `#E8DDC9` | primary readable text on darkness; high-contrast light field |
| `ivory/200` | `#CEB39A` | secondary readable text; material/counterform |
| `crimson/ui` | `#C15B4D` | functional signal on Living Darkness |
| `crimson/matter` | `#601C16` | matter, rupture, marrow, transformation; light-surface crimson accent |
| `gold/text` | `#BDA16F` | rare text-capable aged gold on darkness |
| `gold/instrument` | `#856A47` | rule, measurement, instrumentation, hierarchy |
| `ultramar/ui` | `#6984B4` | rare functional ultramar on darkness |
| `ultramar/matter` | `#102139` | rare material/celestial depth; light-surface ultramar accent |

These are one locked production mapping of already-approved visual semantics, not permission to create parallel palettes.

## Dark-surface behavior

Against `darkness/950`:
- `ivory/100`: 15.08:1 — normal text PASS;
- `ivory/200`: 10.18:1 — normal text PASS;
- `crimson/ui`: 4.70:1 — normal text PASS, but remains a signal/accent role;
- `gold/text`: 8.20:1 — normal text PASS;
- `gold/instrument`: 4.01:1 — large/non-text only by default;
- `ultramar/ui`: 5.37:1 — normal text PASS;
- `crimson/matter`: matter only on darkness;
- `ultramar/matter`: matter only on darkness.

Color never carries meaning alone.

## Light-surface behavior

The R2-B bounded repair validated the same primitives against ivory surfaces without changing any primitive value.

### On `ivory/100`
- `darkness/950`: 15.08:1 — primary/default text;
- `crimson/matter`: 9.32:1 — permitted crimson accent alias;
- `ultramar/matter`: 12.03:1 — permitted rare ultramar accent alias;
- `gold/instrument`: 3.76:1 — non-text only;
- `crimson/ui`, `gold/text`, `ultramar/ui`: not normal-text tokens.

### On `ivory/200`
- `darkness/950`: 10.18:1 — primary/default text;
- `crimson/matter`: 6.29:1 — permitted crimson accent alias;
- `ultramar/matter`: 8.12:1 — permitted rare ultramar accent alias;
- aged-gold and dark-surface UI variants remain restricted unless a later implementation test establishes a valid non-text use.

The light-surface aliases add semantic roles only; they do not add new primitives.

## Other foundations

R2 intentionally does **not** create the production design system.

The following foundation logic is authorized at minimum:
- spacing follows editorial hierarchy rather than decorative uniformity;
- frames/rules are sparse and semantic;
- line/stroke behavior is instrumentation, evidence framing or hierarchy—not ornament for its own sake;
- textures remain subordinate to hierarchy and legibility;
- annotations use IBM Plex Sans and require real semantic content;
- P2 Minimal / No-Icons remains controlling authority;
- fake coordinates, meaningless scales, arbitrary scientific marks, decorative plate metadata and untargeted lines remain prohibited.

Exact component tokens, responsive values and a production component library remain downstream implementation work.

## Figma evidence

File:
`DIVINIVID — PRE-LOCK VISUAL LAB`

R2 comparison root:
`26:3`

Human-selected typography:
- Newsreader + IBM Plex Sans.

Bounded color-role coverage proof:
`31:2 — R2B-COLOR-ROLE-PROOF-V1`

No palette primitive changed during the bounded repair.

## R2 Definition of Done

R2 is closed because:
- licensing and technical viability were validated before aesthetic selection;
- Newsreader + IBM Plex Sans received explicit human approval;
- production color primitives and semantic roles are explicit;
- dark-surface contrast behavior is measured;
- light-surface behavior is measured and role-bounded;
- color never carries meaning alone;
- imagery is not required for the foundations to remain functional;
- no speculative production component library was created;
- the human owner explicitly passed the color mapping.

## Frozen consequence

From this point, R3/R4/R5 may **use** these foundations but may not silently mutate them.

A material foundation failure discovered downstream must be:
1. named;
2. evidenced;
3. bounded to the failing token/role;
4. explicitly reopened by human authority.

## Next handoff

Enter the approved **R3/R4/R5 Formalization Cluster**:

- R3 — Composition Grammar;
- R4 — Image / Illustration Language;
- R5 — Temporal Mapping Audit.

Default:
`FORMALIZE_EXISTING_APPROVED_EVIDENCE_FIRST`.

New visual generation:
`PROHIBITED_UNLESS_A_NAMED_GAP_REQUIRES_IT`.

None of R3/R4/R5 independently unlocks P6.

Required closure:
`CROSS-CONSISTENCY AUDIT -> SYSTEM FORMALIZATION GATE -> P6`.
