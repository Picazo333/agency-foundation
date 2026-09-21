---
status: approved
owner: brand
updated: 2026-09-21
authority: execution-control
depends_on:
  - ../VISUAL_CANON_V1.md
  - ../ANTI_CANON.md
  - DIVINIVID_100_MOODBOARD_EXPANSION_SPEC_V1.md
  - DIVINIVID_MOODBOARD_CONTRACTS_V1.yaml
  - CANON_ANCHOR_SET_V1.md
  - EXECUTION_STYLE_ANCHOR_SET_V1.md
  - SURFACE_LOCK_V1.md
  - CURRENT_GENERATION_STATE.yaml
---
# DIVINIVID — Generation Runtime Lock V1

## Purpose
Prevent visual drift while executing the locked 100-moodboard program.

This file does not change the approved aesthetic or the 100-board plan. It changes only **how generation is allowed to run**.

The core failure this lock prevents is:
`generated output -> implicit positive reference -> next generation -> compounded drift`.

Generation must instead run:
`CURRENT STATE -> EXACT CONTRACT -> EXECUTION STYLE ANCHORS -> SURFACE LOCK -> VISUAL CANON -> SEMANTIC ANCHORS -> ANTI-CANON -> GENERATE -> QA -> HUMAN GATE -> STATE UPDATE`.

## 1. Absolute source hierarchy

For every expansion moodboard, authority order is:

1. `CURRENT_GENERATION_STATE.yaml` — exact cursor and allowed next IDs.
2. `DIVINIVID_MOODBOARD_CONTRACTS_V1.yaml` — exact board contract.
3. `EXECUTION_STYLE_ANCHOR_SET_V1.md` — latest human-approved execution appearance; controls tonal gravity and rendering character.
4. `SURFACE_LOCK_V1.md` — explicit dark-surface constraints.
5. `VISUAL_CANON_V1.md` — semantic and principle authority.
6. `CANON_ANCHOR_SET_V1.md` — principle/semantic positive references.
7. `ANTI_CANON.md` — binding exclusions.
8. `DIVINIVID_100_MOODBOARD_EXPANSION_SPEC_V1.md` — human-readable program context.
9. Approved Support only when the exact contract requires additional evidence.

No lower-authority source may override a higher-authority source.

## 2. No self-referential generation

### Hard rule
A newly generated board is **not** a positive reference for any later board merely because it is recent, attractive, coherent or part of the same round.

A generated board can become a positive reference only after:
1. individual QA PASS;
2. explicit human approval;
3. registry/state promotion.

### Forbidden
- using the immediately previous generation as a style anchor;
- using a whole recent round as visual context before human approval;
- extracting a new "DIVINIVID style" from unapproved generations;
- allowing repeated generator defaults to become canon through frequency.

## 3. Style Lock vs Board Content

Every run has two separate layers.

### STYLE LOCK — immutable during Phase 4
- Living Darkness is the default spatial/material field.
- Ivory is editorial counterform, illumination and legibility; it is not an automatic page background.
- Living Crimson means matter, signal, marrow, fracture, transformation, active state or rupture.
- Aged gold means instrument, hierarchy, annotation, measurement or liturgical order; never generic luxury.
- Ultramar is selective and strongest only in approved medieval/bestiary/celestial domains.
- Anatomy works by analogy and transformation, not decorative literal anatomy.
- Sacred beauty must remain in tension with anomaly/horror/impossible life.
- Information order remains surgical/editorial.
- A/B/H intensity changes amplitude, not identity.
- Motion expresses behavior, not spectacle.

### BOARD CONTENT — contract-specific
The board objective may change structure, examples, medium, states or technical content.

**Board content may not rewrite the Style Lock.**

Examples:
- an accessibility board does not become a white corporate accessibility infographic;
- a factory-readiness board does not become a SaaS dashboard;
- a typography board does not become generic luxury editorial;
- a structural board does not become Gothic-architecture decoration.

## 4. Positive image-reference policy

Default positive image context is **not** the full Canon Anchor Set.

For appearance, load 2–3 images from `EXECUTION_STYLE_ANCHOR_SET_V1.md`.
For semantics/content, add only the Canon anchors required by the exact contract.

If the image tool supports explicit reference selection, explicitly pass only those approved style anchors plus contract-specific Canon anchors. Do not rely on recent conversation imagery.

Add board-specific visual references only when:
- they are CANON or explicitly approved support;
- they answer a requirement in the exact contract;
- they do not displace the Style Lock.

Maximum default reference load:
- 2–3 execution-style anchors;
- 2–4 principle/semantic Canon anchors;
- never the quarantined recent outputs.

Do not inject the entire archive into a generation request.

## 5. Anti-Canon policy

Anti-Canon is primarily a **textual exclusion layer** during generation.

Do not feed Anti-Canon images into positive generation context unless running a dedicated isolated QA/comparison task.

Reason: image generators may imitate pixels even when an image is labeled "wrong."

### Hard visual warnings
Reject before human review if a board uses any of these as an unrequired aesthetic shortcut:
- generic skull;
- decorative skeleton;
- classical bust / Greco-Roman statue;
- generic premium statue;
- decorative halo;
- generic angelic sculpture;
- Gothic cathedral/arch used only as atmosphere;
- moon/eclipse used only as dark ambience;
- generic cloaked figure;
- tarot imagery;
- pseudo-occult sigils;
- dark-fantasy/game concept art;
- parchment-everywhere;
- grunge-as-history;
- cyan/neon;
- pseudo-luxury black/gold;
- decorative anatomical cutaway or human body with no semantic need;
- white/ivory editorial takeover caused only by a technical topic.

An element is allowed only when its semantic role is required by canon/contract.

## 6. Mandatory human-facing checkpoints

Each 5-board round uses exactly these checkpoints:

### Checkpoint 1 — IDs and objectives
Show the exact five next contract IDs and their purposes, recovered from the machine-readable plan.

### Checkpoint 2 — Technical construction
For each ID show:
- required content;
- visual families;
- canonical anchors;
- composition;
- A/B/H;
- material/color roles;
- explicit exclusions;
- acceptance criteria.

No generation before this checkpoint is visible to the human.

### Checkpoint 3 — Generate
Only after the human manually triggers generation:
- generate exactly five **independent** 16:9 boards;
- one output per contract ID;
- never a five-in-one composite.

There is no invented recurring scheduler. Manual trigger remains authoritative.

## 7. Preflight — mandatory before Checkpoint 1
Read `CURRENT_GENERATION_STATE.yaml` and verify:
- current accepted cursor;
- next allowed IDs;
- no skipped ID;
- no off-plan substitution;
- exact contracts exist;
- current round has not already passed;
- latest unapproved outputs are excluded from positive context.

If state and conversation conflict, state + human decision must be reconciled before generation.

## 8. Pre-display QA — mandatory after generation

Do not present a generated board as a valid round result until it passes:

### Gate A — Contract fidelity
- correct ID;
- correct objective;
- required elements present;
- one independent board;
- 16:9;
- declared new coverage is visible;
- output is useful downstream.

### Gate B — Visual Canon fidelity
- Style Lock preserved;
- Surface Lock passes: first-glance canvas remains dark-dominant unless the exact contract explicitly authorizes a light study;
- tonal/rendering character remains compatible with approved A11–A15 execution anchors without copying their content;
- board topic did not become a new art direction;
- Living Darkness/ivory/crimson/gold/ultramar roles remain semantic;
- anatomy/entity/environment use is justified;
- information hierarchy remains DIVINIVID.

### Gate C — Anti-Canon scan
Check every hard warning in section 5.

### Gate D — Self-reference scan
Confirm no unapproved recent generation influenced the board.

### Gate E — Surface fidelity
Run `SURFACE_LOCK_V1.md`:
- dark-dominant thumbnail test;
- ivory takeover test;
- human/statue shortcut test;
- architecture/celestial shortcut test;
- semantic color test.

### Gate F — Cardinality
Five contracts = five distinct files. A composite fails automatically.

### Gate G — Tool isolation
For a five-board round, use five independent generation calls inside the same execution turn when the generator cannot bind different contracts reliably inside one multi-output call. Each call must carry its own exact ID/contract and the same approved style anchor set.

Possible internal result:
- `PASS_TO_HUMAN`
- `MUTATE_BEFORE_HUMAN`
- `REJECT_BEFORE_HUMAN`

Only `PASS_TO_HUMAN` is presented as a candidate for approval.

## 9. Human approval semantics
Human approval is per board unless the human explicitly approves the complete round.

After approval:
- mark board `ACCEPTED`;
- update cursor;
- record lineage;
- only then may it become approved-support evidence.

A visually good board that changes the aesthetic is not a PASS.

## 10. Saturation checkpoints
At accepted boards 20, 40, 60 and 80:
- stop generation;
- audit redundancy and coverage;
- do not alter remaining contract IDs merely because recent generations suggest a new aesthetic;
- reallocation requires coverage evidence + human approval.

## 11. Recovery rule
A future agent must be able to resume generation by reading:
1. this file;
2. `CURRENT_GENERATION_STATE.yaml`;
3. exact contracts;
4. Execution Style Anchor Set;
5. Surface Lock;
6. Canon Anchor Set;
7. Visual Canon + Anti-Canon.

The originating chat must not be required.
