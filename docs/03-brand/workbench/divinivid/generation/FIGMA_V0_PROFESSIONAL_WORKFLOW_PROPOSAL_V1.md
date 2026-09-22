---
status: proposal
owner: brand
created: 2026-09-22
authority: workbench
depends_on:
  - docs/03-brand/workbench/divinivid/generation/POSTMORTEM_2026-09-22_ACTIVE_VISUAL_CONDITIONING_FAILURE.md
  - docs/03-brand/workbench/divinivid/generation/EXECUTION_STYLE_ANCHOR_SET_V1.md
  - docs/03-brand/workbench/divinivid/generation/SURFACE_LOCK_V1.md
---
# DIVINIVID — Figma + v0 Professional Visual Production Workflow V1

## Decision intent
Introduce Figma as the **visual-system and composition control plane** and v0 as a **code/prototype implementation accelerator**, without replacing repository authority, human approval, Canon, or the generative image layer.

This document is a proposal. Adoption requires human approval.

## Authority model

### Repository
Owns:
- contracts;
- semantic Canon;
- Anti-Canon;
- execution-style anchor registry;
- Surface Lock;
- generation state;
- lineage;
- acceptance status;
- production specifications.

### Figma
Owns, once approved:
- operational visual tokens;
- board shells;
- layout primitives;
- typography hierarchy;
- reusable diagram/annotation components;
- composition variants;
- editable final board assembly;
- UI/website design system;
- design QA surfaces.

Figma does **not** decide Canon independently.

### Image generators
Own:
- bounded imagery;
- specimens;
- environments;
- textures;
- visual transformations;
- candidate illustrations.

They do not own exact typography, exact diagrams, lifecycle logic, DAG correctness or governance state.

### v0
Owns:
- fast interactive implementation from approved Figma/code-system inputs;
- UI experiments;
- component prototypes;
- responsive behavior exploration;
- production-oriented React/Next.js drafts;
- implementation PR candidates.

v0 does not become design authority.

### Production code repository
Owns the deployable implementation.

## Core topology

```
Repo contracts / Canon
        |
        v
Figma tokens + components + approved board shells
        |
        +-------------------------+
        |                         |
        v                         v
bounded image generation      deterministic diagrams/text
        |                         |
        +------------+------------+
                     v
              Figma assembly
                     |
                 visual QA
                     |
                human gate
                     |
          approved design artifact
                     |
            v0 implementation
                     |
          code review / repo / CI
                     |
                 production
```

## Why this architecture

The 2026-09-22 incident showed that monolithic image generation can satisfy superficial palette/style while failing:
- exact composition;
- Anti-Canon;
- typography;
- semantic correctness;
- graph correctness;
- stable reference conditioning.

Figma removes high-precision design tasks from probabilistic image generation while preserving generative richness where it is valuable.

## Figma file architecture

Create one team/project space for DIVINIVID with separate files:

### 00 — DIVINIVID / Design System
Pages:
1. `FOUNDATIONS`
2. `TOKENS`
3. `TYPOGRAPHY`
4. `COLOR + MATERIAL`
5. `GRID + SPACING`
6. `INSTRUMENTATION`
7. `ANNOTATION`
8. `DIAGRAMS`
9. `BOARD COMPONENTS`
10. `UI COMPONENTS`
11. `DEPRECATED / QUARANTINE`

### 01 — DIVINIVID / Visual Universe Boards
Pages:
- `ROOT ANCHORS`
- `A SERIES`
- `B SERIES`
- ...
- `CHECKPOINTS`
- `QUARANTINE`

### 02 — DIVINIVID / Product + Web
Pages:
- information architecture;
- landing;
- workbench/product concepts;
- responsive frames;
- prototypes.

### 03 — DIVINIVID / Production Handoff
Pages:
- approved screens;
- component mapping;
- implementation annotations;
- code links;
- QA snapshots.

## Token model

Do not start with hundreds of tokens.

Start with the minimum stable layer:

### Color
- `surface/living-darkness`
- `surface/ivory-counterform`
- `signal/living-crimson`
- `instrument/aged-gold`
- `support/ultramar`

Use semantic roles, not hexadecimal names, as the primary naming layer.

### Typography
Define:
- display;
- editorial heading;
- body;
- annotation;
- micro-label;
- numeric/index;
- caption.

Each should include:
- family;
- size;
- line-height;
- tracking;
- casing;
- optical behavior;
- minimum readable size.

### Spatial
Define:
- board outer margin;
- content gutter;
- micro-gap;
- specimen gap;
- section gap;
- macro field separation.

### Stroke / instrumentation
Define:
- hairline;
- standard;
- emphasis;
- measured line;
- lineage edge;
- negative/rejected marker.

## Component model

Initial component families:

- `DVV/Board/Header`
- `DVV/Board/Footer`
- `DVV/Board/SectionLabel`
- `DVV/Specimen/Window`
- `DVV/Specimen/Caption`
- `DVV/Annotation/Callout`
- `DVV/Diagram/Node`
- `DVV/Diagram/Edge`
- `DVV/Diagram/Legend`
- `DVV/State/Badge`
- `DVV/Lineage/Marker`
- `DVV/Negative/RejectedEvidence`
- `DVV/Storyboard/Frame`
- `DVV/Storyboard/Strip`

Create variants for A/B/H intensity only where structure genuinely changes. Do not make intensity a cosmetic theme switch.

## Root-anchor reconstruction

Rebuild STYLE-S01-S05 in Figma as **analysis overlays**, not pixel-for-pixel redraws.

For each anchor:
- place original image;
- overlay measured content zones;
- mark dominant black field;
- identify hierarchy levels;
- estimate text-to-image ratio;
- identify frame/stroke density;
- identify image windows;
- identify crimson matter paths;
- identify gold instrumentation;
- record macro/micro rhythm.

Output:
`EXECUTION_GRAMMAR_V1`

This is a measurable translation of approved visual evidence, not a new aesthetic.

## A11 golden-board pilot

A11 becomes the pilot.

### Step 1 — contract decomposition
Convert exact A11 contract into:
- fixed text/data;
- required diagrams;
- required storyboard states;
- image-required slots;
- optional atmospheric slots.

### Step 2 — Figma skeleton
Build layout with no generated imagery.

Acceptance:
- all contract fields fit;
- hierarchy works at 25% zoom;
- no spreadsheet gestalt;
- Living Darkness remains dominant;
- storyboard remains legible;
- board resembles the structural rhythm of STYLE-S01-S05.

### Step 3 — image slots
Generate only bounded assets where a generative model adds value.

Each image job receives approved root anchors, not generated siblings.

### Step 4 — per-asset QA
Reject:
- generic gothic shortcuts;
- unapproved religious/classical shorthand;
- skull/heart/eclipse substitutions;
- premium-gothic filler;
- irrelevant symmetry;
- stylistic drift.

### Step 5 — assembly
Place approved assets into Figma.
All text, arrows, labels, metrics and diagrams remain native/editable.

### Step 6 — whole-board QA
Evaluate separately:
- CONTRACT_FIDELITY;
- SURFACE_FIDELITY;
- ANTI_CANON;
- HIERARCHY;
- THUMBNAIL_GESTALT;
- READABILITY;
- REFERENCE_LINEAGE.

### Step 7 — human gate
Only an approved A11 becomes the golden board template for structured technical boards.

## Two production modes

### Mode G — Generative Board
Use when:
- atmosphere/composition is the primary discovery;
- exact diagrams/text are low-risk;
- generative accidents are desirable.

Process:
`root anchors -> image generation -> QA -> human`

### Mode S — Structured Board
Use when:
- exact text matters;
- there is a DAG/state machine/matrix/provenance system;
- correctness and reproducibility matter;
- typography/diagram accuracy is contractual.

Process:
`contract -> Figma skeleton -> bounded generation -> assembly -> QA -> human`

A board may be Hybrid, but one mode must own the composition.

## v0 integration

### Use v0 after Figma intent is stable
v0 should not discover the core DIVINIVID visual language.

Use it to:
- convert approved Figma frames/components into React/Next.js prototypes;
- explore responsive behavior;
- implement interaction/motion;
- validate component reuse;
- create production PR candidates.

### Componentized import
Never send one giant page if smaller components can be isolated.

Preferred:
`Figma component/frame -> v0 implementation -> visual diff -> repo`

### Design-system grounding
The long-term target is:
- Figma variables/components;
- code tokens;
- Tailwind/CSS variables;
- shadcn-compatible branded primitives where useful;
- a reusable component registry;
- v0 consuming the same primitives as production.

### No screenshot-as-source-of-truth
Screenshots may be evidence but must not become the canonical handoff when native Figma structure exists.

## Figma MCP

The preferred architecture should support Figma MCP so agents can read:
- components;
- variables;
- layout;
- design metadata.

When write-to-canvas is available and authorized, agents may draft native Figma structures, but:
- human approval remains mandatory for visual promotion;
- write actions should target a workbench page/file before approved libraries;
- generated nodes must carry provisional naming/status.

## Code Connect
If the plan level supports it later, use Code Connect to map approved Figma components to real repo components.

Do not make Code Connect a prerequisite for Phase 1.

## Failure-prevention gates

### Gate F0 — authority
No frame without exact source contract.

### Gate F1 — visual roots
Approved root anchors visible and identified.

### Gate F2 — skeleton
Exact information fits before image generation.

### Gate F3 — bounded generation
Image model receives only the task needed for the slot.

### Gate F4 — anti-drift
Candidate compared against roots, not last generation.

### Gate F5 — assembly
No rasterized text/diagram where native construction is feasible.

### Gate F6 — human
No Canon or style-anchor promotion automatically.

### Gate F7 — code
v0 output must pass repo review, accessibility and implementation QA.

## Initial adoption sequence

### Phase 0 — setup
- create Figma project/files;
- connect MCP;
- establish naming/version rules;
- import STYLE-S01-S05;
- create quarantine page.

### Phase 1 — execution grammar
- measure anchors;
- create initial variables;
- build board primitives;
- recreate structural rhythm.

### Phase 2 — A11 golden pilot
- skeleton;
- bounded assets;
- assembly;
- QA;
- human approval.

### Phase 3 — A12-A15
Use structured mode by default because they contain lifecycle, provenance, negative-evidence and DAG logic.

### Phase 4 — system hardening
- component library;
- token export;
- visual regression snapshots;
- board templates;
- MCP operating rules.

### Phase 5 — v0 bridge
- import selected Figma frames;
- prototype web/UI;
- map branded components;
- validate responsive/motion implementation;
- move accepted code to repo through PRs.

## Definition of Done for adoption
Figma integration is considered proven only if:
1. one A11 board reaches human approval with stronger surface consistency than failed monolithic attempts;
2. exact contract content remains editable;
3. A12-A15 can reuse primitives without looking templated;
4. rejected imagery cannot silently become root context;
5. a new conversation can recover design intent from repo + Figma without relying on chat memory;
6. at least one approved frame can be implemented through v0 and reconciled back to production code without material visual drift.

## Non-goals
- replacing creative image generation;
- turning DIVINIVID into a generic design-system aesthetic;
- making Figma the semantic source of truth;
- letting v0 publish directly without repo review;
- universalizing DIVINIVID-specific visual tokens into Noema or Skill Foundry.
