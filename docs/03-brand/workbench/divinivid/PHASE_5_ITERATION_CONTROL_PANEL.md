---
status: active
owner: brand
updated: 2026-09-17
authority: workbench
phase: 5
version: 2
inherits:
  - DIVINIVID_VISUAL_GRAMMAR_V0.md
  - PHASE_5_ITERATION_CONTRACT.md
  - PHASE_5_RECONCILIATION_PLAN.md
  - PHASE_5_NEGATIVE_EVIDENCE_LEDGER.md
---
# DIVINIVID — Phase 5 Iteration Control Panel v2

## Purpose
Provide a persistent control surface for visual discovery while preventing vague iteration, visual contamination, repeated morphology and premature identity-board generation.

The panel is not an identity generator. It records experimental state.

---

# 1. Canonical controls

| Control | 0 | 100 |
|---|---|---|
| `X1` Anatomical ↔ Symbolic | evidentiary anatomy | metaphysical symbol |
| `X2` Revealed ↔ Withheld | luminous/exposed | concealed/delayed |
| `X3` Grotesque intensity | nearly neutral | practical ceiling ≈75 |
| `X4` Rational ↔ Oneiric | physically coherent | dream-logical |
| `X5` Scientific ↔ Ritual | treatise/observation | ceremonial/liturgical |
| `X6` Editorial ↔ Pictorial | information structure | image/atmosphere |
| `X7` Silent ↔ Dramatic | quiet tension | visual event |
| `X8` System ↔ Hero | repeatable system | singular hero |
| `X9` Human ↔ Specimen | human threshold | classified organism |

These axes describe intensity. They do **not** prove that two outputs are meaningfully different.

---

# 2. Mandatory structural controls

Every creature/organism experiment must additionally declare:

```text
M1 MORPHOLOGY FAMILY:
M2 SILHOUETTE:
M3 SYMMETRY:
M4 APPENDAGE LOGIC:
M5 POSTURE / ORIENTATION:
M6 MATERIAL LOGIC:
M7 PHYSICAL IMPOSSIBILITY:
```

For a divergence set, at least three of `M1–M5` must differ visibly between candidates unless the explicit question requires them to stay constant.

A batch that repeats the same underlying creature with different lighting/layout is invalid.

---

# 3. Evidence-type control

Before generation, declare exactly one output type:

- `INGREDIENT_MORPHOLOGY`
- `INGREDIENT_LIGHT`
- `INGREDIENT_LITURGICAL_ILLUSTRATION`
- `INGREDIENT_ANNOTATION`
- `COMPARISON_ASSEMBLY`
- `SYSTEM_PROOF_HERO`
- `SYSTEM_PROOF_EDITORIAL`
- `SYSTEM_PROOF_OPERATIONAL`

Do not mix output types in one comparison set.

In particular, `INGREDIENT_*` generations must not invent website mockups, final typography or full identity boards.

---

# 4. Required iteration card

No visual generation proceeds without this card:

```text
ID:
LINEAGE:
OUTPUT_TYPE:
QUESTION:
LOCKED:
MUTATE:
AXIS_BEFORE:
AXIS_AFTER:
STRUCTURAL_CONTROLS:
SOURCE_PRINCIPLES:
NEGATIVE_EVIDENCE_CHECK:
EXPECTED_LEARNING:
KNOWN_RISK:
DECISION: pending / PASS / MUTATE / KILL
```

## Anti-contamination declaration
Also state:

```text
PRIOR_GENERATED_PIXELS_USED_AS_REFERENCE: NO
```

The only valid `YES` requires explicit human approval naming exactly what is being preserved.

---

# 5. Human feedback modes

The owner may use numbers or ordinary language.

Examples:

```text
X4 70 → 85
X5 20 → 35
```

or

```text
more surreal, less taxonomic, keep the elegance
```

or

```text
keep the material, kill the creature silhouette
```

The operator must translate qualitative feedback into explicit state changes before the next generation.

---

# 6. Current positive-evidence lineages

## OA-01 — Oneiric Anatomy
Status: `RETAINED POSITIVE EVIDENCE / SECONDARY LINEAGE`

Original profile:
```text
X1 75
X2 40
X3 35
X4 85
X5 70
X6 80
X7 65
X8 85
X9 25
```

Preserve only as principles:
- solemn oneiric threshold;
- impossible interior;
- crimson as semantic event;
- strong ivory/dark tension;
- monumental pictorial pull.

Do not automatically preserve the human figure, exact architecture or composition.

## BS-01 → BS-04 — Bestiary / Surreal Dislocation
Status: `PRIMARY CURRENT LINEAGE`

BS-04 target profile:
```text
X1 35
X2 20
X3 45
X4 70
X5 20
X6 30
X7 30
X8 20
X9 90
```

Strongest retained signals:
- impossible organism;
- organic materiality;
- marked surrealism;
- serious observation/classification;
- editorial containment;
- non-fantasy intent.

Desired but not yet proven against this lineage:
- Dark Revelation behavior;
- liturgical/manuscript illustration compatibility.

---

# 7. Obsolete planned mutations

The old Round-B plan `OA-02/03/04 + BS-02/03/04` is historical evidence, not the active next gate.

Results:
- OA mutations produced insufficient structural independence and were less favored than the original OA signal;
- BS-04 produced the strongest later positive signal;
- subsequent bestiary/identity-board rounds suffered morphology lock and invalid comparisons.

Do not continue numbering from those failed boards as if they were valid parents.

---

# 8. Batch preflight

Before showing any batch to the owner, operator checks:

1. Same output type across set?
2. Same approximate polish/information burden?
3. Declared question visible in the differences?
4. At least three structural differences when divergence is intended?
5. Any repeated dragon/wyvern/fantasy default?
6. Any generated typography masquerading as a type decision?
7. Any premature website/application design?
8. Any generic Gothic / occult / pseudo-luxury contamination?
9. Any prior generated image acting as an undeclared seed?
10. Does the batch add new learning?

If 1–9 fail materially, reject internally before human review.

---

# 9. Current next experiment

## `ORG-PROBE-01 — Oneiric Organic Morphology Divergence`

Question:
> Which non-fantasy families of impossible organic form preserve the human pull of BS-04 while avoiding morphology lock?

Output type: `INGREDIENT_MORPHOLOGY`.

Locked:
- elegant;
- solemn;
- oneiric HIGH;
- organic materiality HIGH;
- non-traumatic;
- compatible with ivory / black / crimson;
- no sci-fi gloss;
- no typography;
- no layout;
- no website mockup;
- no liturgical decoration yet.

Mutate:
- morphology family;
- silhouette;
- symmetry;
- appendage logic;
- physical impossibility.

Success:
- candidates remain recognizably inside one Brand universe while being structurally different at thumbnail size;
- at least one candidate receives genuine human `PULL`;
- no candidate defaults to dragon/wyvern/dinosaur/fantasy-character anatomy.

After human selection only:
1. test Dark Revelation lighting as a separate controlled probe;
2. test liturgical illustration as a separate controlled probe;
3. assemble approved mechanisms into editable system-proof surfaces.

---

# 10. Persistent state

`phase5_iteration_state.yaml` is authoritative for machine-readable Phase-5 state.

The workflow is now:

`CONTROL CARD → ISOLATED PROBE → SET-LEVEL CURATION → HUMAN SIGNAL → STATE UPDATE → NEXT PROBE`

not:

`PROMPT → FULL IDENTITY BOARD → VAGUE FEEDBACK → PROMPT`.
