---
status: complete
owner: brand
created: 2026-09-23
authority: audit
human_approved: true
depends_on:
  - docs/08-plans/workstreams/DIVINIVID_VISUAL_IDENTITY_MASTER_PLAN.md
  - docs/08-plans/master/DIVINIVID_CURRENT_EXECUTION_PLAN_V2.md
  - docs/07-decisions/ADR-0013-visual-universe-to-asset-factory-sequencing.md
  - docs/07-decisions/ADR-0014-targeted-visual-synthesis-and-expression-bases.md
  - docs/07-decisions/ADR-0015-pre-lock-exploration-before-final-expression-lock.md
  - docs/03-brand/workbench/divinivid/generation/CURRENT_GENERATION_STATE.yaml
---
# DIVINIVID R0 Requirement Matrix V1

## Purpose

Audit the frozen Visual Identity Master Plan against the actually approved DIVINIVID evidence before any new visual-tool call.

R0 does not generate new identity material.

It answers only:

> Which original identity-system requirements are already satisfied, which are partial, and which are genuinely missing?

## Status vocabulary

- `SATISFIED` — approved evidence closes the requirement without new creative work.
- `PARTIAL` — approved evidence resolves part of the requirement but an operational gap remains.
- `MISSING` — no valid approved evidence closes the requirement.
- `NOT_APPLICABLE` — conditional requirement is not currently justified and should not be manufactured.
- `HISTORICAL_ONLY` — useful context whose former phase/gate semantics were superseded.

## Audit rule

A requirement is not marked SATISFIED because:
- a moodboard happens to depict it;
- a proxy artifact suggests it;
- a generated result is visually attractive;
- an old document contains an unresolved proposal.

SATISFIED requires approved evidence or a later approved decision that clearly supersedes the older requirement.

---

# 1. Prerequisite integrity

| Requirement / authority | Status | Evidence / interpretation |
|---|---|---|
| Brand thesis and hierarchy exist | SATISFIED | Creative Direction, Brand State, Master Plan |
| Clean reference canon / anti-canon exists | SATISFIED | REFERENCE_CANON + ANTI_CANON |
| Core expression exists | SATISFIED | DIVINIVID_CORE_LOCK_V1 |
| Primary production expression base exists | SATISFIED | BASE_LOCK_B1 |
| Current morphology anchor exists | SATISFIED | M1-B Topografía Orgánica |
| Specialized bestiary branch is separated | SATISFIED | BESTIARY_BASE_B0 |
| P1 typographic visual direction | SATISFIED | imposing dual-editorial direction |
| P2 sign grammar | SATISFIED | Minimal / No-Icons |
| P3 hero behavior | SATISFIED | H-B Editorial / Systemic |
| P4 density/intensity default | SATISFIED | D2 Controlled / Expressive Mosaic |
| P5 motion behavior | SATISFIED | Registration + Negative Revelation |
| Tool/capability governance for next phases | SATISFIED | TOOL_EXECUTION_CONTRACTS_V1 |
| Old Phase-4 Tension Grammar human-gate metadata | HISTORICAL_ONLY | ADR-0013 explicitly superseded the old Reference Atlas / Tension Grammar / route-production sequence as active execution gating. Its mechanisms remain useful evidence, but its stale `human_gate: pending` metadata is not a current blocker. |

## R0 prerequisite conclusion

There is no reason to reopen:
- reference discovery;
- Core;
- B1;
- M1;
- P1-P5;
- the old 100-board quota program.

The real gaps begin at identity formalization.

---

# 2. R1 — Signature System audit

Frozen Master Plan requirement:
build a signature that survives without historical imagery.

| Required proof | Status | Existing evidence | Gap |
|---|---|---|---|
| Primary DIVINIVID wordmark | MISSING | P1 establishes typographic character only | no formal wordmark construction |
| Signature architecture | MISSING | palindrome/bilateral ideas exist in earlier grammar/research | no approved signature system |
| Symbol/glyph where justified | NOT_APPLICABLE | P2 explicitly rejects decorative icon systems | only create if R1 proves functional need |
| Monogram/reduced mark where justified | MISSING | none approved | small/reduced brand behavior unresolved |
| Micro-mark/favicon | MISSING | none approved | no small-size identity proof |
| Black one-color | MISSING | direction implies monochrome viability but no proof | needs explicit test |
| Reversed one-color | MISSING | no proof | needs explicit test |
| 16px/small-size behavior | MISSING | no proof | needs deterministic size test |
| Horizontal behavior | MISSING | no formal signature | unresolved |
| Vertical behavior where justified | NOT_APPLICABLE pending R1 architecture | no need to manufacture without structural reason |
| Palindrome mechanics described, not decorated | PARTIAL | brand naming history and bilateral/mirror grammar support the concept | no approved formal application |

## R1 result

**OVERALL: MISSING**

R1 is a real creative gap and cannot be closed by documentation alone.

### Minimum valid R1 work
The frozen plan calls for five meaningful signature architectures:
1. Palindromic Axis
2. Bilateral Body
3. Sacred Inscription
4. Mirrored Cut
5. Custom Letterform Logic

P1 must remain fixed as the typographic personality authority.
P2 prevents gratuitous symbol invention.

### Tool implication
Figma is justified for R1 because the unresolved question is deterministic:
- letterform geometry;
- alignment;
- symmetry/asymmetry;
- small-size;
- monochrome;
- exact comparison.

Image generation is not the default R1 engine.

---

# 3. R2 — Foundations audit

## 3.1 Typography

| Requirement | Status | Existing evidence | Gap |
|---|---|---|---|
| role architecture | PARTIAL | P1 strongly implies display + severe operational secondary logic | roles need explicit operational names |
| actual font family/families | MISSING | P1 is visual direction only | candidate families unresolved |
| maximum two-family default | MISSING | plan rule exists | no selected pair |
| ES/EN coverage | MISSING | required by Master Plan / Canon | not validated |
| readability | PARTIAL | P1 visually reviewed; no production tests | needs real font testing |
| weights/styles | MISSING | not mapped |
| web delivery | MISSING | not verified |
| print delivery | MISSING | not verified |
| licensing | MISSING | not verified |
| fallbacks | MISSING | not defined |
| scale / line-height / measure | MISSING | no production system |

**Typography foundations: PARTIAL, with substantial implementation gaps.**

Important:
R2 must resolve production typography without reopening P1's approved visual direction.

## 3.2 Color

| Requirement | Status | Existing evidence | Gap |
|---|---|---|---|
| Living Darkness semantic role | SATISFIED | Core / Canon / Surface behavior |
| Ivory/bone role | SATISFIED | Core / Canon |
| Living Crimson role | SATISFIED | Core / Canon |
| Residual ultramar discipline | SATISFIED | Core / current DNA |
| Aged-gold/instrument role | PARTIAL | historical/current Canon evidence | final retention and operational budget need confirmation |
| exact production values | MISSING | no final values |
| tonal scale / neutrals | MISSING | no operational scale |
| semantic mappings | PARTIAL | semantic roles exist; mappings incomplete |
| light/dark surface rules | PARTIAL | dark dominance is strong; full operational pairing incomplete |
| accessibility contrast | MISSING | no measured final pairings |

**Color foundations: PARTIAL but conceptually mature.**

## 3.3 Other foundations

| Requirement | Status | Existing evidence | Gap |
|---|---|---|---|
| spacing logic | PARTIAL | H-B/D2 imply rhythm and hierarchy | no operational values/rules |
| frame/border behavior | PARTIAL | printed-evidence/editorial grammar exists | no minimal reusable spec |
| line/stroke behavior | PARTIAL | P2 and B1 constrain it | no operational scale |
| texture budget | PARTIAL | anti-global-distress rules + D1-D4 exist | needs mode-specific operationalization |
| annotation hierarchy | PARTIAL | P2 removes fake notation; earlier grammar supports real evidence labels | needs explicit hierarchy |
| foundational tokens | MISSING | intentionally deferred | only minimum necessary should be created |

## R2 result

**OVERALL: PARTIAL**

R2 is necessary, but most work is translation/validation rather than aesthetic rediscovery.

---

# 4. R3 — Composition Grammar audit

Frozen Master Plan calls for five composition modes:
1. Contemplative
2. Anatomical Plate
3. Illuminated Page
4. Dramatic Revelation
5. Information-Dense

Current evidence is strong but not fully formalized.

| Requirement | Status | Evidence | Gap |
|---|---|---|---|
| primary event + subordinate evidence + recovery zone | SATISFIED as principle | Visual Grammar V0 |
| editorial/systemic hierarchy | SATISFIED | P3 H-B |
| order <-> creativity tension | SATISFIED | P4 D2 |
| mosaic/puzzle assembly | SATISFIED as default behavior | P4 approved refinement |
| density modes D1-D4 | SATISFIED | P4 |
| quiet vs dense localization | SATISFIED as principle | Visual Grammar / P4 |
| Contemplative mode | PARTIAL | D1 / quiet-field rules support it | not formally specified |
| Anatomical Plate mode | PARTIAL | B1 + M1-B strongly support it | not operationally specified |
| Illuminated Page mode | PARTIAL | historical grammar exists | must be reconciled with current B1, not revived literally |
| Dramatic Revelation mode | PARTIAL | H-A evidence + P5 reveal | not formally specified as composition mode |
| Information-Dense mode | PARTIAL | H-B + D2 | exact information hierarchy not specified |
| reproducibility without copying anchor | PARTIAL | rules exist | not yet demonstrated/closed as a system spec |

## R3 result

**OVERALL: PARTIAL / HIGH EVIDENCE**

R3 should begin by synthesizing existing approved evidence into rules.

### Default execution rule
No new image generation unless the synthesis reveals a genuine visual ambiguity.

A Figma comparison is optional, not automatic.

---

# 5. R4 — Image / Illustration Language audit

Current project evidence already contains unusually strong visual-matter learning.

## Existing approved/working families evidenced

- porous marrow / bone-like structure;
- topographic / coastal / geological ambiguity;
- membrane / cavity / active void;
- celestial / planetary mass by analogy;
- fibrous / branching structures;
- tectonic / vascular crimson transitions;
- printed-evidence / erosion / transfer;
- sculptural/figurative material when it does not become classical-statue shorthand;
- bestiary/entity branch separated into B0.

| Master requirement | Status | Evidence | Gap |
|---|---|---|---|
| coherent anatomy family | PARTIAL | B1 + M1-B |
| illumination behavior | PARTIAL | Core + reveal logic |
| grotesque family | PARTIAL | Canon / B0 boundary |
| cosmology/diagram relation | PARTIAL | macro/micro grammar |
| cinematic/material behavior | PARTIAL | Core / approved anchors |
| USE WHEN | MISSING as family contract | implied only |
| DO NOT USE WHEN | PARTIAL | Anti-Canon gives global rejects |
| crop rules | MISSING |
| light rules by family | MISSING |
| color rules by family | PARTIAL |
| detail rules | MISSING |
| material/treatment rules | PARTIAL |
| source/generation requirements | PARTIAL | runtime/reference rules exist globally |
| rights state | PARTIAL | provenance policy exists but not family-specific |
| permanent Asset Cut List | PARTIAL | negative evidence exists, not yet normalized to R4 families |

## R4 result

**OVERALL: PARTIAL / HIGH EVIDENCE**

R4 is primarily a classification/specification task.

### Default execution rule
Do **not** generate new image families by default.
Generate only if a specific family cannot be specified from existing approved evidence.

---

# 6. R5 — Temporal Identity audit

Frozen Master Plan behavior set:
- REVEAL
- DISSECTION
- ILLUMINATION
- MIRROR
- ABERRATION -> RECONCILIATION

Approved P5 behavior:
- M-C Negative Revelation — primary reveal;
- M-B Registration — structural transition;
- optional M-A Breathing Matter;
- optional M-D Instrument Response;
- choreography: `OBSCURE -> MISREGISTER -> REVEAL -> RESOLVE`.

| Original behavior | Status | P5 mapping | Gap |
|---|---|---|---|
| REVEAL | SATISFIED | Negative Revelation |
| DISSECTION | PARTIAL | can be expressed by segmented/misregistered layers | not explicitly named/bounded |
| ILLUMINATION | PARTIAL | revelation semantics cover disclosure; color/light behavior exists in Core | temporal rule not explicitly mapped |
| MIRROR | PARTIAL | registration/alignment can support mirror relations | not explicitly bounded |
| ABERRATION -> RECONCILIATION | SATISFIED | misregister -> resolve |
| motion expresses grammar, not spectacle | SATISFIED | P5 hard fails |
| timing/easing after behavior approval | SATISFIED as sequencing rule | intentionally deferred |
| reduced-motion alternative | SATISFIED as principle | P5 accessibility requirement |
| production timing/easing values | NOT_APPLICABLE at R5 conceptual stage | correctly deferred |

## R5 result

**OVERALL: PARTIAL BUT CLOSE**

R5 probably requires **documentation/mapping only**, not new motion generation.

Runway is not justified unless the mapping reveals a continuous-motion question that cannot be judged from existing P5 evidence.

---

# 7. Aggregate requirement state

| Block | R0 status | New visual creation required? | Likely tool burden |
|---|---|---:|---|
| R1 Signature | MISSING | **Yes** | one controlled Figma comparison + targeted refinement |
| R2 Foundations | PARTIAL | limited deterministic comparison | font/licensing research + Figma |
| R3 Composition | PARTIAL / high evidence | probably no | repo synthesis; Figma only if ambiguity |
| R4 Image/Illustration | PARTIAL / high evidence | probably no | repo classification; image gen only for a proven gap |
| R5 Temporal | PARTIAL / close | probably no | repo mapping; no Runway by default |
| P6 Digital Brand Specimen | BLOCKED | later | Figma after R1-R5 |
| P7 Application Stress | BLOCKED | later | mixed |
| P8 Final Synthesis | BLOCKED | later | synthesis |

## Main R0 finding

The project does **not** need another broad aesthetic exploration cycle.

It needs one genuinely new design block — **Signature System** — followed by increasingly deterministic formalization of already-discovered evidence.

That is a materially smaller scope than rebuilding the identity.

---

# 8. What R0 explicitly rejects

R0 finds no evidence-based reason to:
- regenerate Core;
- reopen B1;
- reopen M1-B;
- rerun P1;
- create an icon family;
- regenerate hero directions;
- re-explore density;
- regenerate motion storyboards;
- return to 100 moodboards;
- build a product dashboard;
- begin Website IA;
- begin v0;
- industrialize the full Figma system.

---

# 9. Next exact gate

`R1 — DIVINIVID Signature System`

## R1 preflight before any Figma write

The first material R1 Figma call must declare:

- `ACTIVE_PHASE: R1_SIGNATURE_SYSTEM`
- `QUESTION: which signature architecture can make DIVINIVID distinctive without imagery while preserving P1 authority?`
- `WHY_FIGMA: exact wordmark geometry, alignment, monochrome and small-size comparison require deterministic editable construction`
- `SOURCE_OF_TRUTH: Core + B1 + M1-B + P1 + P2 + R0`
- `VARIABLE_UNDER_TEST: signature architecture`
- `FIXED_VARIABLES: approved visual personality, no decorative icon invention, no new palette, no new image language`
- `EXPECTED_OUTPUT: one five-up signature comparison`
- `BUDGET: one comparison + one targeted repair`
- `PROMOTION_RULE: evidence pending until human review`

No R1 tool call should occur until its exact five hypotheses are specified in text and checked for meaningful distinction.

---

# 10. R0 Definition of Done result

R0 PASS conditions:

- [x] original Master Plan identity requirements mapped;
- [x] each requirement classified with evidence;
- [x] no moodboard depiction treated as automatic system proof;
- [x] real missing work separated from already-approved evidence;
- [x] no visual-generation or Figma call used;
- [x] next exact gate identified;
- [x] downstream P6/v0/web boundaries preserved.

**R0 RESULT: PASS**

**NEXT: R1 SIGNATURE SYSTEM**
