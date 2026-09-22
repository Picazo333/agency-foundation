---
status: review
owner: brand
created: 2026-09-22
authority: evidence
confidentiality: INTERNAL
related:
  - docs/03-brand/workbench/divinivid/generation/GENERATION_RUNTIME_LOCK_V1.md
  - docs/03-brand/workbench/divinivid/generation/EXECUTION_STYLE_ANCHOR_SET_V1.md
  - docs/03-brand/workbench/divinivid/generation/SURFACE_LOCK_V1.md
  - docs/03-brand/workbench/divinivid/generation/CURRENT_GENERATION_STATE.yaml
  - docs/10-knowledge-harvest/records/HARVEST-20260921-divinivid-generation-authority-drift.md
---
# DIVINIVID Postmortem — Active visual conditioning failure and monolithic-board drift

## Executive summary
The R03 recovery attempt on 2026-09-22 did not produce an acceptable contractual A11 and was stopped before A12-A15 could be promoted.

The failure was not evidence that the approved DIVINIVID direction is incoherent. Earlier conversations had already produced visually congruent boards, including the five human-approved artifacts now retained as `STYLE-S01-S05`.

The incident exposed a narrower runtime problem: **having approved image references available in repository/Library context is not equivalent to proving that those pixels are actively conditioning the image-generation call**.

Repeated A11 attempts preserved some superficial palette and editorial cues while collapsing into generic gothic priors: statues, religious figures, skulls, gothic arches, eclipses, black/gold luxury framing and table-like infographic layouts. These are either explicitly Anti-Canon or evidence of topic/style substitution.

A separate tool-routing error generated A12-A15 through Runway even though that executor was not the intended recovery path. Those outputs are evidence only and are quarantined.

No output from this incident is accepted as contractual A11-A15 or as a positive style reference.

## What happened

### 1. Correct logical state was recovered
The session successfully recovered:
- contiguous valid cursor through A10;
- exact contractual A11-A15;
- `STYLE-S01-S05`;
- Surface Lock;
- Canon / Anti-Canon;
- five-independent-job requirement;
- human-gated promotion.

### 2. The first execution did not preserve visual authority
The initial recovery generation path translated approved anchors into text and then sent large monolithic prompts to an image executor.

This lost the strongest part of the original successful condition: the approved visual state itself.

### 3. Tool routing increased the failure
A12-A15 were dispatched to Runway during the failed round. This was not a justified provider substitution and broke continuity with the previously successful image-generation workflow.

Those four outputs must remain quarantined as:
`R03_RECOVERY_RUNWAY_A12_A15_2026-09-22`.

### 4. Repeated A11 attempts revealed stable fallback priors
Several A11 retries produced similar substitutions:
- gothic/religious figures;
- skulls / literal anatomical-heart shorthand;
- cathedral or arch ambience;
- eclipse/moon shorthand;
- generic premium black/gold;
- spreadsheet-like matrix dominance;
- decorative codex framing.

The stability of these motifs across retries indicates a model prior, not random noise.

### 5. Reference availability was mistaken for reference binding
The approved anchors were successfully found in Library and inspected. However, the runtime did not establish an auditable guarantee that the intended images were actually supplied to the generation model as effective visual-conditioning inputs.

This distinction must now be explicit:

`REFERENCE_AVAILABLE != REFERENCE_BOUND != REFERENCE_EFFECTIVE`

A future executor adapter must attest which positive visual references were actually attached/consumed for each generation job.

## Root causes

### RC1 — Active multimodal state was not reconstructed
The earlier successful conversation had approved imagery inside the live multimodal context. The recovery session reconstructed repository state, but not necessarily the same perceptual conditioning state.

### RC2 — Semantic rules were over-translated into prompt text
A long prompt attempted to restate palette, Anti-Canon, layout, semantics and exact contract simultaneously.

This increased concept surface area and allowed the generator to satisfy words such as gothic, anatomy, sacred, manuscript or dark through generic visual shortcuts.

### RC3 — Negative prompting was used as if it were a constraint engine
Listing prohibited motifs does not guarantee exclusion and can increase their salience. Anti-Canon should primarily operate as a QA/rejection layer unless a compact negative instruction is proven useful for the specific executor.

### RC4 — Monolithic technical-board generation overloaded one model call
A11-A15 combine information architecture, exact text, diagrams, semantic correctness, art direction and imagery. One image model was asked to solve all layers at once.

Technical subject matter then pulled the output toward infographic/dashboard conventions.

### RC5 — Generated descendants were allowed too close to active context
Even rejected outputs can become perceptually salient inside a conversation. This creates self-reference risk despite repository policy declaring them non-authoritative.

### RC6 — Executor substitution was not gated
Switching to a different image executor occurred without proving equivalence in reference conditioning or style fidelity.

## Durable findings

1. **Repository authority and perceptual conditioning are separate runtime concerns.**
2. A reference needs at least three states: `available`, `bound`, `effective/verified`.
3. Approved root anchors should be used in a **star topology**. Every contractual board starts again from approved roots; a generated sibling does not become style input merely because it is recent.
4. Unapproved descendants must remain quarantined both logically and, where possible, from active generation context.
5. Anti-Canon is primarily a QA/eval surface, not a giant negative prompt.
6. Executor changes require an explicit adapter/gate.
7. A polished output that hits contract content but misses surface authority remains a hard failure.
8. For high-precision boards, layout/typography/graphs may need deterministic design-system assembly while generative models create only imagery or specimens.
9. The deterministic fallback is not automatically the default. First preserve the previously proven monolithic path when effective image-reference conditioning can be verified.
10. Human visual approval remains the authority for style-anchor promotion.

## Immediate runtime correction

### New precondition: REFERENCE_BINDING_ATTESTATION
Before any A11-A15 generation, the execution record must state:
- executor;
- exact reference IDs;
- whether each reference was actually attached to the generation request;
- reference role: execution-style / semantic / negative;
- whether the executor supports image-reference conditioning;
- whether current-round generated outputs are excluded.

If this cannot be established, generation stops.

### New topology rule
For every board:

`CURRENT_STATE + EXACT_CONTRACT + APPROVED_ROOT_STYLE_ANCHORS + CONTRACT_CANON -> EXECUTION`

Never:

`A11 -> A12 -> A13 -> ...`

unless a human explicitly promotes a generated board to an approved anchor.

### New fallback gate
If two correctly bound root-anchor attempts on the same contract fail surface fidelity, do not continue prompt iteration.

Route the contract to:
`STRUCTURED_ASSEMBLY_CANDIDATE`

where Figma/SVG/HTML owns exact typography/layout/diagram logic and image generation is reduced to bounded asset slots.

## Evidence disposition

### Accepted
- STYLE-S01-S05 remain the current approved execution-style anchors.

### Quarantined
- all R03 A11 retries produced during the 2026-09-22 incident;
- Runway A12-A15 outputs from the same incident;
- any screenshot or derivative made from those outputs.

### Contract status
No change:
- A11-A15 remain missing;
- A16/A18/A19 remain targeted completion;
- A17 remains traceability confirmation;
- A20 remains dependency-blocked;
- B01-B05 remain unauthorized.

## Figma/v0 consequence
Figma is now a strong candidate for the composition and design-system control layer, especially for technical boards and eventual product/UI implementation. v0 is a strong downstream implementation/prototyping layer.

Neither tool becomes Canon by adoption alone.

The proposed workflow is documented separately in:
`docs/03-brand/workbench/divinivid/generation/FIGMA_V0_PROFESSIONAL_WORKFLOW_PROPOSAL_V1.md`.

## Reusable abstraction
This incident should be routed to:
- Noema: active reference-binding semantics and context-attestation candidate;
- Skill Foundry: evals for reference presence vs effective binding, star-topology anchor reuse, executor substitution, and structured-assembly fallback.

Project-specific aesthetics remain owned by DIVINIVID.
