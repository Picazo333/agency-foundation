---
status: approved
owner: brand
updated: 2026-09-20
authority: workbench
depends_on:
  - archive/VISUAL_ARCHIVE_V1_INVENTORY.md
  - VISUAL_UNIVERSE_CHECKPOINT_2026-09-20.md
  - REFERENCE_CANON.md
  - ANTI_CANON.md
---
# DIVINIVID — Phase 2 Canon + Lineage Reconciliation Plan

## Objective
Promote Archive V1 evidence into durable visual authority without reconstructing approvals from memory or allowing polished but unapproved generations to become canon by repetition.

Phase 2 separates:
- **CANON** — principle-defining visual evidence;
- **APPROVED_SUPPORT** — approved application/reference evidence;
- **NEGATIVE_CANON** — explicit failures/forbidden directions worth preserving;
- **SUPERSEDED_DUPLICATE** — duplicate/copy evidence retained only for traceability;
- **PENDING_HUMAN_REVIEW** — ambiguous material that cannot be promoted safely.

## Candidate pass generated from Archive V1

The current machine-assisted candidate layer contains 277 visual records:

| Candidate state | Count |
|---|---:|
| `APPROVED_SUPPORT_CANDIDATE` | 206 |
| `PENDING_HUMAN_REVIEW` | 39 |
| `NEGATIVE_EVIDENCE_CANDIDATE` | 3 |
| `NEGATIVE_CANON` | 15 |
| `SUPERSEDED_DUPLICATE` | 6 |
| `APPROVED_SUPPORT_EVIDENCE` | 6 |
| `EVIDENCE_ONLY` | 2 |

Only 29 records currently have enough evidence to avoid a human promotion decision. The remaining 248 are intentionally not auto-promoted.

## Evidence-backed positive set
Six records have a mapped positive-evidence basis:
- five corrected Motion 21–25 boards explicitly accepted after the rejected first attempt;
- one earlier editorial board that can be linked to positive conversation evidence, but its precise preference rank remains weaker than the Motion evidence.

The sixth remains support evidence, not a principle-defining Canon artifact, until the relationship is reconciled.

## Review method — batch, not 248 individual approvals

Human review should operate by **visual family sheet** with exception naming.

Review sheets are organized as:
1. Core Identity / Visual Universe
2. Anatomy / Specimens / Transformations
3. Bestiary / Entities
4. Environments / Impossible Geometry
5. Digital / Web / Mobile UI
6. Motion Master Language
7. Editorial / Typography / Information
8. Communication / Physical
9. Asset Factory Bridge
10. Experiments / Potential Drift

Each tile exposes stable `DVV-VIS-####` ID + filename.

### Default family decision
For sheets 1–9, the available human decisions are:
- **APPROVE SUPPORT** — promote the sheet to `APPROVED_SUPPORT`, naming any exceptions;
- **MIXED** — approve only named ranges/IDs;
- **HOLD** — keep the sheet pending;
- **NEGATIVE** — route the family/output subset to negative evidence.

For Sheet 10:
- **KEEP EXPERIMENTAL**
- **PROMOTE NAMED IDs**
- **NEGATIVE NAMED IDs**

This avoids asking the owner to review 248 YAML rows.

## Canon promotion rule
A family-level “APPROVE SUPPORT” decision does **not** make every image a master Canon artifact.

After support promotion, the reconciliation pass selects the smallest set of principle-defining artifacts necessary to evidence:
- Living Darkness;
- Living Crimson;
- ivory editorial counterform;
- aged-gold instrument/ritual logic;
- selective ultramar;
- anatomy-by-analogy;
- medieval entity/bestiary logic;
- living environments;
- impossible geometry;
- A/B/H intensity system;
- motion-as-behavior;
- scientific/editorial information order.

The goal is a small, legible Canon with a much larger Approved Support library.

## Lineage requirements
Every promoted record must preserve:
- archive ID;
- original filename;
- family;
- approval source;
- parent/source artifacts when known;
- superseded-by / replaces relationships;
- negative-evidence relationship when a corrected board replaces a failed one;
- downstream production families unlocked.

## Specific correction lineage
The rejected first Motion 21–25 set must point to the corrected accepted replacements rather than merely remaining as isolated failures.

## Anti-canon relationship
Negative evidence is not a trash folder. Where a failure expresses a reusable prohibited mechanism, it should reference the relevant Anti-Canon rule:
- condensed five-in-one outputs;
- aesthetic drift;
- parchment/dark-academy/fantasy shortcut;
- overcompression of visual systems;
- low-quality document-like motion boards.

## Phase 2 gate
PASS only when:
1. all 277 archive records have a durable terminal/review state;
2. all promoted support has human authority evidence;
3. a compact principle-level Canon set is identified;
4. negative evidence and supersession are linked;
5. the resulting registry can seed the 100-board specification without loading chat history.

## Next handoff
After Phase 2 PASS:
`VISUAL_UNIVERSE_EXPANSION` specification of the 100-board program.


---

# Human decision — 2026-09-20

The human owner approved the Phase 2 review sheets.

Interpretation applied:
- sheets 01–09: promote all non-negative, non-duplicate candidate material to `APPROVED_SUPPORT`;
- sheet 10: approval confirms retention/classification of experiments and drift candidates, but does **not** convert drift/experimental material into positive support;
- explicit failures remain `NEGATIVE_CANON`;
- duplicate copies remain `SUPERSEDED_DUPLICATE`.

A compact principle-level Canon was then selected from the approved support corpus. This is intentionally much smaller than the support library.

## Final Phase 2 counts

| Final state | Count |
|---|---:|
| `APPROVED_SUPPORT` | 193 |
| `CANON` | 19 |
| `EXPERIMENT` | 39 |
| `NEGATIVE_CANON` | 18 |
| `SUPERSEDED_DUPLICATE` | 6 |
| `EVIDENCE_ONLY` | 2 |

## Canon-set rule

The 19 Canon artifacts are not "the only good images." They are the smallest current evidence set that anchors principle-level behavior across:
- identity mother / invisible-world grammar;
- Living Darkness;
- color semantics;
- anatomy-by-analogy;
- specimen duality;
- transformative structure;
- medieval Bestiary;
- infernal and harlequin/liminal families;
- living environments;
- impossible geometry;
- digital application;
- Abyssal intensity;
- motion;
- typographic motion;
- annotation and measurement;
- typography;
- Asset Factory family map.

The larger `APPROVED_SUPPORT` corpus remains available for breadth, application detail and future production references.

## Phase 2 verdict

**PASS.**

The archive can now seed the 100-board specification without requiring chat-history reconstruction.
