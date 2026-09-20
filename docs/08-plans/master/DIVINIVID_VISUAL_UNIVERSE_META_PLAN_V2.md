---
status: review
owner: meta
updated: 2026-09-20
authority: plan
depends_on:
  - ../../../PROJECT_STATE.md
  - ../../00-meta/source-of-truth.md
  - ../../03-brand/workbench/divinivid/BRAND_STATE.md
  - ../../03-brand/workbench/divinivid/REFERENCE_CANON.md
  - ../../03-brand/workbench/divinivid/ANTI_CANON.md
  - ../../../asset-factory/spec/01-brand-pack-contract.md
---
# DIVINIVID — Visual Universe to Asset Factory Meta-Plan V2

## 0. Purpose

Turn the human-approved DIVINIVID visual universe into a production-grade, auditable, reusable identity system and complete agency brandbook without asking the production executor to rediscover the aesthetic.

The program deliberately separates:

`DISCOVERY -> COVERAGE -> SPECIFICATION -> PILOT -> INDUSTRIAL PRODUCTION -> BRAND GOVERNANCE`

More output is not automatically better. Every round must remove uncertainty, increase usable coverage, or prove production readiness.

This plan is a **review baseline**. It becomes the frozen production program only after the Noema migration and Skill Foundry pass are reconciled and the human owner approves the post-protocol verification.

---

# 1. Program invariants

1. **Domain authority remains in DIVINIVID.** Noema governs coordination/conformance; Skill Foundry owns reusable capabilities; neither may silently redefine Brand canon.
2. **Generated work is evidence until promoted.** Human-approved visual work may enter canon only through the archive/registry process.
3. **Negative evidence is preserved.** Failed, condensed, recycled, low-quality and aesthetically drifting generations are retained and classified rather than deleted.
4. **Exploration ends before factory production.** The production executor receives explicit visual contracts, not an invitation to improvise a new direction.
5. **100 moodboards are a target corpus, not a vanity number.** A redundant or failed board does not count. Every accepted board must add coverage.
6. **Complexity must pay rent.** New schemas, automation or review layers are adopted only when they reduce ambiguity, risk, manual reconstruction or production error.
7. **Capability before executor.** Gemini is the intended factory executor but the production contract must remain portable enough to survive executor substitution.
8. **Rights/provenance are first-class.** Reference material, generated media, fonts, production assets and derived outputs must have traceable rights/provenance state.
9. **Accessibility and reduced-motion are part of identity quality**, not post-production patches.
10. **Human creative authority remains explicit.** Structural and deterministic checks may automate; material creative changes require the human gate.

---

# 2. Round envelope — mandatory for every substantial round

Every round, regardless of phase, uses the same lightweight envelope.

## R0 — Preflight
- identify phase, round ID and exact objective;
- load the smallest Noema context required for the task;
- check governing canon, anti-canon and current checkpoint;
- run capability preflight against existing Skills/tools;
- check whether the round duplicates already-covered territory;
- state write scope and forbidden scope;
- define acceptance criteria before generation/build.

## R1 — Work order
Create a compact work order containing:
- inputs;
- required outputs;
- dependencies;
- visual/technical constraints;
- provenance requirements;
- QA method;
- stop condition.

## R2 — Execute
Perform the round without reopening upstream decisions unless an explicit contradiction is discovered.

## R3 — QA / gate
Evaluate:
- conformance to canon;
- coverage gain;
- redundancy;
- production usefulness;
- accessibility/rights where relevant;
- failure signatures from Anti-Canon.

Possible outcomes:
`PASS / MUTATE / REJECT / BLOCKED`.

## R4 — Durable closeout
- update checkpoint/registry;
- record decisions;
- perform Project Harvest assessment;
- route only high-signal reusable findings to Skill Foundry/Noema;
- define the exact next action.

Routine rounds should remain low-friction; not every round creates a harvest record.

---

# 3. Stage I — DISCOVERY COMPLETION

## Phase 1 — Archive, archaeology and evidence inventory

### Objective
Know exactly what has been generated before using it as production evidence.

### Required outputs
- complete file inventory;
- stable archive IDs;
- original filename retention;
- checksum manifest;
- source/tool/model where recoverable;
- human status;
- lineage;
- family tags;
- duplicate/near-duplicate detection;
- failure classification.

### Status vocabulary
- `CANON`
- `APPROVED_SUPPORT`
- `EXPERIMENT`
- `FAILED`
- `COMPOSITE_FAILURE`
- `AESTHETIC_DRIFT`
- `DUPLICATE_NEAR_DUPLICATE`
- `UNASSESSED`

### Required archive package
`DIVINIVID_VISUAL_UNIVERSE_ARCHIVE_V1.zip`

It must contain:
- canon;
- approved support;
- experiments;
- negative evidence;
- failures;
- applications;
- motion;
- communication/physical;
- asset-factory bridge material;
- `MANIFEST.csv`;
- `MANIFEST.json`;
- `CHECKSUMS.txt`;
- `ARCHIVE_VERSION.json`;
- `CANON_INDEX.md`;
- naming convention.

### Gate P1
No material image remains unclassified. Every promoted reference has provenance and an explicit human-status field.

---

## Phase 2 — Canon promotion and lineage registry

### Objective
Convert the explored universe into an explicit visual evidence graph without making chat history a dependency.

### Required outputs
- `VISUAL_CANON_REGISTRY`;
- `NEGATIVE_EVIDENCE_REGISTRY`;
- lineage ledger;
- asset-family taxonomy;
- relationship map between core DNA, systems and applications;
- supersession records for rejected/obsolete directions.

### Critical distinction
A generated moodboard can be:
- canon for a visual principle;
- support for an application;
- negative evidence;
- or merely historical.

Approval of one property does not automatically approve every detail inside the image.

### Gate P2
A future agent can answer “what visual evidence is authoritative for this decision?” without reconstructing the conversation.

---

# 4. Stage II — CONTROLLED UNIVERSE EXPANSION

## Phase 3 — 100-moodboard specification program

### Objective
Specify the expansion corpus **before generation**.

The five macrofamilies remain:

1. **Asset Family Master Map — 20**
2. **Structural Asset Library — 20**
3. **Illustration & Entity Asset Library — 20**
4. **Cross-Medium Stress Test — 20**
5. **Brandbook / Final Universe System — 20**

### Board contract
Each of the 100 specifications must define:
- `moodboard_id`;
- objective;
- question answered;
- canonical input references;
- required visual families;
- required new coverage;
- composition;
- density;
- A/B/H intensity mode;
- Living Darkness role;
- Living Crimson role;
- aged-gold role;
- ultramar permission;
- typography behavior;
- anatomical abstraction level;
- oneiric intensity;
- entity/specimen/environment requirements;
- implied motion;
- target medium;
- production outputs unlocked;
- dependencies;
- explicit exclusions;
- anti-pattern checks;
- acceptance criteria;
- lineage destination.

### Gate P3
100/100 board specs exist before the first expansion board is generated.

---

## Phase 4 — 100-moodboard generation

### Execution pattern
`20 rounds x 5 boards`.

A round is not complete until all five boards have individual outputs and individual evaluation results.

### Coverage rule
An accepted board must add at least one:
- new family;
- new combination;
- new scale;
- new behavior;
- new application;
- new transformation;
- new limit/exception;
- new cross-system relationship.

Pure cosmetic variation is rejected and does not count toward 100.

### Saturation checkpoints
After boards 20, 40, 60 and 80:
- run redundancy check;
- inspect family imbalance;
- reallocate remaining specs only when the change increases coverage without reopening aesthetic DNA.

### Gate P4
100 accepted high-signal boards, with failed/rejected boards preserved separately.

---

## Phase 5 — Coverage audit and targeted gap expansion

### Objective
Determine whether the universe is actually complete enough to specify production.

Build a multidimensional coverage matrix across:
- family;
- medium;
- scale;
- state;
- behavior;
- A/B/H intensity;
- color state;
- motion;
- accessibility;
- production format.

Audit domains include:
- typography and letterforms;
- marks/logos/lockups where applicable;
- symbols and seals;
- ornament/marginalia;
- grids/frames/dividers;
- textures/materials;
- specimens/vessels/Petri/cross-sections;
- bestiary;
- angelic/infernal/harlequin/celestial families;
- anatomical transformations;
- living environments;
- impossible geometry;
- data visualization;
- editorial;
- web/mobile;
- motion;
- campaigns;
- presentations;
- physical/packaging/environmental;
- accessibility/reduced motion;
- production constraints.

### Classification
- `GREEN` — sufficient for specification;
- `YELLOW` — partial; targeted expansion needed;
- `RED` — insufficient/absent.

### Gap loop
Generate only the additional moodboards justified by YELLOW/RED findings.

No fixed quota. The loop stops when:
- no material RED remains;
- critical YELLOW items are resolved;
- additional boards add negligible information.

### Gate P5
Coverage report passes human review.

---

# 5. Stage III — INDUSTRIALIZATION

## Phase 6 — Visual Spec, Visual Matrix and Asset Ontology

### Objective
Translate the visual universe into production contracts.

### Visual Spec
Must formalize:
- color roles/tokens;
- typography roles and licensing/fallbacks;
- grids;
- spacing;
- composition;
- strokes;
- borders/radii;
- texture/material behavior;
- image rules;
- anatomy rules;
- entity construction;
- symbol geometry;
- illumination;
- contrast;
- motion;
- responsive behavior;
- accessibility;
- prohibited combinations.

### Visual Matrix
Machine-readable relationships across:
`asset family x medium x intensity x color state x scale x behavior x motion x format`.

### Asset Ontology
Stable family/subfamily IDs and inheritance rules.

### Production Matrix
Every row becomes a candidate production order with:
- asset ID;
- family/subtype;
- variants;
- states;
- dimensions;
- format;
- visual constraints;
- motion compatibility;
- responsive needs;
- accessibility;
- provenance;
- expected files.

### Gate P6
A production order can be written without making a material creative decision.

---

## Phase 7 — Golden-set factory pilot and contract hardening

### Why this phase exists
A complete-looking spec can still fail when translated to real SVG/vector production. This pilot prevents mass-producing hundreds of structurally wrong assets.

### Pilot set
Select a deliberately difficult cross-section, approximately 15–30 assets, spanning:
- structural primitives;
- typography-adjacent assets;
- symbols/seals;
- one bestiary family;
- one specimen family;
- one complex environment/geometry asset;
- web/app implementation;
- print/physical use;
- motion-ready asset;
- reduced-motion/accessibility equivalent.

### Test
For each pilot asset:
- generation fidelity;
- SVG/vector cleanliness;
- editability;
- responsive scaling;
- layer naming;
- accessibility;
- rendering portability;
- file-size/performance;
- color-token compliance;
- provenance;
- round-trip editability;
- visual-coherence eval.

### Output
- hardened Visual Spec;
- hardened Production Matrix;
- exporter constraints;
- Gemini-specific adapter;
- executor-neutral core contract;
- golden reference asset pack;
- failure/repair playbook.

### Gate P7
Pilot assets can be generated, validated, repaired and exported without reopening visual direction.

---

# 6. Stage IV — PRODUCTION

## Phase 8 — Asset Factory production

### Factory rule
Gemini executes contracts; it does not explore identity.

Pipeline:
`Production Order -> Generate -> Validate -> Repair -> Export -> Register`.

### Outputs
As applicable:
- master SVG;
- simplified SVG;
- monochrome;
- responsive variants;
- raster fallback;
- motion-ready layers;
- icon/pattern systems;
- illustration/entity families;
- diagrams/templates;
- print-ready resources.

### Quality
Automate deterministic checks; use model/human review only where judgment remains material.

### Gate P8
All required asset families are complete, registered and pass their contracts.

---

## Phase 9 — Brandbook assembly

### Objective
Assemble approved upstream artifacts without reopening them.

Required sections:
1. philosophy/essence;
2. identity architecture;
3. color/material;
4. typography;
5. composition;
6. structural grammar;
7. symbols/seals;
8. illustration/entities;
9. bestiary;
10. specimens/anatomy;
11. environments/geometry;
12. motion;
13. digital;
14. editorial/data;
15. communication/campaign;
16. physical/environmental;
17. accessibility;
18. asset library;
19. production rules;
20. DO/DON'T;
21. governance/versioning.

### Gate P9
A designer, writer or agent can execute from the brandbook without the originating chat.

---

## Phase 10 — Final QA, release and governance

### Final stress tests
- cross-medium consistency;
- minimum-size behavior;
- monochrome behavior;
- high/low-density layouts;
- localization/ES-EN coverage;
- responsive behavior;
- motion/reduced motion;
- print/digital conversion;
- dark/ivory surface behavior;
- accessibility;
- asset provenance and rights;
- executor portability.

### Release package
- Brandbook;
- canonical asset library;
- design tokens;
- Visual Spec;
- Visual Matrix;
- Asset Ontology;
- Production Matrix;
- negative evidence/anti-pattern pack;
- governance guide;
- changelog/version manifest;
- archive snapshot.

### Final acceptance question
> Can an external agency or agent work for six months with DIVINIVID without needing to rediscover how the brand should look or behave?

### Gate P10
Human release approval + versioned baseline.

---

# 7. Cross-cutting control planes

## Noema
Noema governs:
- project composition;
- progressive context;
- authority boundaries;
- provenance contracts;
- conformance;
- durable relations;
- recoverability.

Noema does **not** approve visual quality or own DIVINIVID canon.

## Skill Foundry
Skill Foundry receives only high-signal harvested capabilities. It evaluates:
`REUSE -> EXTEND -> MODE -> DEPENDENT_SKILL -> NEW_SKILL -> NO_SKILL`.

It does not receive every moodboard or routine generation event.

High-value candidate capability areas currently include:
- visual-universe coverage audit;
- moodboard specification/contracts;
- negative-evidence-driven visual QA;
- visual-spec-to-production-order translation;
- asset-factory QA/repair loop;
- brandbook readiness audit.

These are candidates, not approved new Skills.

## Project Harvest
Capture once, route many times. A harvest record never changes project canon.

---

# 8. Naming and repository identity

The human-selected project/brand name is **DIVINIVID**.

For continuity:
- Noema stable project ID remains `agency-foundation` unless a separate migration explicitly changes it.
- The intended GitHub repository slug is `divinivid`.
- Repository slug changes must not break provenance, links, relations or historical references.
- Legal/trademark/domain clearance remains a separate commercial diligence gate and does not reopen the current visual work unless a real blocker appears.

---

# 9. Immediate sequence from this checkpoint

1. complete Noema selective migration;
2. capture visual-production pipeline harvest evidence;
3. run Skill Foundry G0–G5 on the harvested capability cluster;
4. perform one post-Noema/Foundry meta-plan verification;
5. human approves any material deltas;
6. Phase 1 inventory/archive;
7. Phase 2 canon/lineage registry;
8. Phase 3 detailed 100-board specification;
9. continue through gates P4–P10.

No mass asset generation is authorized before P7 pilot PASS.
