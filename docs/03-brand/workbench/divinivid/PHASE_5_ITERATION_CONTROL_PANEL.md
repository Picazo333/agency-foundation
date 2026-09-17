---
status: active
owner: brand
updated: 2026-09-17
authority: workbench
phase: 5
inherits:
  - DIVINIVID_VISUAL_GRAMMAR_V0.md
  - PHASE_5_ITERATION_CONTRACT.md
---
# DIVINIVID — Phase 5 Iteration Control Panel

## Purpose
Provide a compact, persistent control surface for original visual iteration without requiring a bespoke HTML tool.

The human owner can adjust the identity in conversation using percentages, plain-language comments, or both. The operator translates that input into controlled mutations and records the resulting state.

The panel exists to prevent vague iteration such as `make it better` or `make it more artistic`.

---

# 1. Canonical controls

All axes are represented from `0–100` for convenience in conversation, while preserving the semantics of the Phase-4 grammar.

| Control | 0 | 100 |
|---|---|---|
| `X1` Anatomical ↔ Symbolic | anatomical / evidentiary | symbolic / metaphysical |
| `X2` Revealed ↔ Withheld | exposed / luminous | concealed / delayed revelation |
| `X3` Grotesque intensity | absent / nearly neutral | prohibited extreme; practical working ceiling ≈ 75 |
| `X4` Rational ↔ Oneiric | physically coherent | dream-logical / surreal |
| `X5` Scientific ↔ Ritual | plate / treatise / observation | ceremonial / iconic / liturgical |
| `X6` Editorial ↔ Pictorial | information structure dominates | image / atmosphere dominates |
| `X7` Silent ↔ Dramatic | restrained / quiet tension | confrontational visual event |
| `X8` System ↔ Hero | repeatable system surface | singular hero-image emphasis |
| `X9` Human ↔ Specimen | human subject / threshold | classified organism / object of study |

`X8` and `X9` are Phase-5 convenience controls. They do not replace the Phase-4 grammar; they make route mutation easier to discuss and record.

---

# 2. How the owner can operate it

The owner may respond in any of these forms.

## A. Direct numeric move
```text
OA: X4 85 → 65
OA: X6 80 → 55
Keep composition.
```

## B. Relative move
```text
OA: surreal -15, editorial +20, darkness +10.
```

The operator maps natural-language controls onto the canonical axes.

## C. Pure qualitative feedback
```text
More anatomical.
Keep the body-threshold idea.
Less cathedral.
More silent.
```

The operator must translate qualitative feedback into explicit axis deltas before producing the next artifact.

## D. Locked invariant + mutation
```text
LOCK: central monumental figure, crimson interior, ivory field.
MUTATE: more anatomical, less pictorial.
```

---

# 3. Required mutation card

Every generated iteration must carry a short card:

```text
ID:
PARENT:
QUESTION:
LOCKED:
MUTATE:
AXIS BEFORE:
AXIS AFTER:
COMMENTS:
EXPECTED LEARNING:
KNOWN RISK:
DECISION: pending / PASS / MUTATE / KILL
```

No image should be generated unless `QUESTION`, `LOCKED`, and `MUTATE` are explicit.

---

# 4. Initial survivor baselines

These profiles describe the first serious original artifacts approximately. They are control-state estimates, not measurements of pixels.

## OA-01 — Oneiric Anatomy

```text
X1 Anatomical→Symbolic   75
X2 Revealed→Withheld     40
X3 Grotesque intensity   35
X4 Rational→Oneiric      85
X5 Scientific→Ritual     70
X6 Editorial→Pictorial   80
X7 Silent→Dramatic       65
X8 System→Hero           85
X9 Human→Specimen        25
```

### Preserve candidates
- monumental human figure;
- body as threshold / impossible interior;
- crimson as interior semantic event;
- solemn surrealism;
- strong ivory field / dark-red contrast;
- explicit relation between anatomy, architecture and inner realm.

### Current risks
- may remain a poster rather than become a system;
- architecture could overpower anatomical logic;
- high pictoriality may make repeatability expensive;
- surrealism could become spectacle if raised indiscriminately.

---

## BS-01 — Bestiary of Systems

```text
X1 Anatomical→Symbolic   35
X2 Revealed→Withheld     20
X3 Grotesque intensity   45
X4 Rational→Oneiric      45
X5 Scientific→Ritual     20
X6 Editorial→Pictorial   20
X7 Silent→Dramatic       30
X8 System→Hero           20
X9 Human→Specimen        90
```

### Preserve candidates
- dossier/specimen logic;
- bilateral organism;
- classification + observation language;
- generous ivory surface;
- crimson as evidentiary marker;
- evidence panels / annotations;
- impossible organism presented as if scientifically ordinary.

### Current risks
- may become clinical/science-fiction adjacent;
- could lose sacred/symbolic charge;
- creature may become a repeated logo-like motif;
- too much UI structure could weaken mystery.

---

# 5. Recommended Round-B mutations

The following are controlled experiments, not mandatory final directions.

## OA-02 — Anatomical Reinforcement
**Question:** does Oneiric Anatomy become stronger if the human body remains the main impossible architecture but explicit cathedral/architectural language is reduced?

- `X1`: 75 → 55
- `X4`: keep 85
- `X5`: 70 → 55
- `X6`: keep 80
- `X8`: keep 85

**Lock:** monumental figure, surreal interior, crimson event, ivory field.

**Mutate:** more sectional/anatomical interior; less literal architecture.

---

## OA-03 — Editorialization
**Question:** can Oneiric Anatomy preserve emotional pull while behaving more like a repeatable identity system?

- `X6`: 80 → 50
- `X8`: 85 → 55
- `X7`: 65 → 50

**Lock:** core image concept and oneiric intensity.

**Mutate:** stronger annotation, plate logic, caption hierarchy, secondary evidence fields.

---

## OA-04 — Dark Revelation
**Question:** does stronger concealment improve the Macario/threshold quality without collapsing into generic black luxury or cinematic darkness?

- `X2`: 40 → 75
- `X7`: 65 → 70
- `X5`: keep 70
- `X4`: 85 → 75

**Lock:** body threshold and surreal relation.

**Mutate:** reveal less; semantic illumination targets anatomy/interior only.

---

## BS-02 — Corporeal Escalation
**Question:** can Bestiary become more bodily/grotesque without losing classification rigor?

- `X3`: 45 → 60
- `X1`: 35 → 45
- `X9`: keep 90

**Lock:** dossier layout, bilateral specimen, annotation.

**Mutate:** more biological materiality and interpretably impossible anatomy.

---

## BS-03 — Ritual Infusion
**Question:** can Bestiary gain sacred weight without becoming occult, Gothic, or pseudo-luxury?

- `X5`: 20 → 50
- `X2`: 20 → 35
- `X7`: 30 → 40

**Lock:** scientific observation and information hierarchy.

**Mutate:** ceremonial axis, restrained symbolic geometry, more solemn material behavior.

---

## BS-04 — Surreal Dislocation
**Question:** can Bestiary incorporate dream logic while preserving the credibility of the classification system?

- `X4`: 45 → 70
- `X3`: keep 45
- `X6`: 20 → 30

**Lock:** specimen/dossier system.

**Mutate:** one dominant physical impossibility, repeated/reciprocal behavior, or spatial contradiction.

---

# 6. Conversation display convention

Before every new generation, show the owner a compact state card like:

```text
OA-03 · Editorialization
Anatomical 45% ████░░░░░░ Symbolic 55%
Revealed   60% ██████░░░░ Withheld 40%
Grotesque  35% ███░░░░░░░
Rational   15% ██░░░░░░░░ Oneiric 85%
Scientific 30% ███░░░░░░░ Ritual 70%
Editorial  50% █████░░░░░ Pictorial 50%
Silent     50% █████░░░░░ Dramatic 50%
System     45% ████░░░░░░ Hero 55%
Human      75% ███████░░░ Specimen 25%

LOCK: body-threshold + crimson interior + solemnity
MUTATE: stronger information system
COMMENT: keep the emotional pull; reduce poster-dependence
```

The bars are a conversational display, not a precision measurement.

---

# 7. State authority

The machine-readable companion file `phase5_iteration_state.yaml` is the persistent state of the iteration loop.

Rules:
1. the current parent profile is recorded before generation;
2. user comments are appended as evidence;
3. numeric changes are recorded as deltas;
4. rejected variants remain in history but never seed future work unless a preserved invariant is explicitly named;
5. only `PASS` or explicit `preserve` signals may become inputs to convergence.

---

# 8. Why not an HTML slider app yet?

A slider app would be useful later, but building it now introduces interface work before the control vocabulary has stabilized.

For Round B the preferred system is:

`CHAT CONTROL CARD ↔ YAML STATE ↔ GENERATED ARTIFACT ↔ HUMAN FEEDBACK`

If the vocabulary survives several rounds, it can later become a Figma component, lightweight local control panel, or Brand tooling surface without changing the underlying data model.
