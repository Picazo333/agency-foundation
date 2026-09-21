---
id: HARVEST-20260921-divinivid-generation-authority-drift
status: candidate
owner: meta
created: 2026-09-21
source_event_type: INCIDENT
confidentiality: INTERNAL
routes:
  - skill_candidate
  - sop_process
  - template_schema
  - eval_test
  - benchmark_lesson
provenance:
  issue: null
  pr:
    - https://github.com/Picazo333/agency-foundation/pull/30
    - https://github.com/Picazo333/agency-foundation/pull/31
  commit:
    - 89a6296b0b109e7ff1e9ff1dc73db9c7b91be938
    - a4b2cfcb7f0310e91b597567bfa69504748addcd
  adr: docs/07-decisions/ADR-0013-visual-universe-to-asset-factory-sequencing.md
  artifact: docs/03-brand/workbench/divinivid/generation/GENERATION_RUNTIME_LOCK_V1.md
---
# Harvest Record — Preventing reference-authority drift in generative visual systems

## What happened
During execution of the locked DIVINIVID 100-moodboard program, repeated image-generation rounds remained visually competent but drifted away from the latest approved execution style. The drift persisted even after the first Generation Runtime Lock because semantic Canon references and current execution-style references were still treated as one undifferentiated positive-reference pool.

A second incident also exposed contract-binding failure: a five-board round could produce plausible outputs whose visual content and titles did not reliably stay bound to the exact A16-A20 contracts.

## Previous state / problem
The project already had Visual Canon, Anti-Canon, exact 100-board contracts, a durable current cursor, quarantine rules for rejected outputs, and a rule against self-referential generation.

However, positive references still mixed two different authority types:
1. semantic/principle authority — what DIVINIVID means;
2. execution-style authority — how the currently approved surface is rendered.

This allowed older exploratory but canonical imagery to reintroduce ivory-dominant editorial surfaces. Technical topics such as accessibility, factory readiness or governance further amplified the failure because the generator interpreted the topic as a reason to change art direction.

## What changed
### PR #30 — Generation Runtime Lock V1
- exact-contract-first execution;
- current cursor persisted in repo;
- Anti-Canon hardened;
- self-referential generation prohibited;
- recent unapproved outputs quarantined;
- pre-display QA required.

### PR #31 — Execution Style Anchor Set + Surface Lock
- A11-A15 pinned as the latest human-approved execution-style anchors;
- semantic Canon separated from execution-style authority;
- Surface Lock makes dark dominance executable rather than interpretive;
- near-absolute black / Living Darkness becomes the default 75-90% canvas field unless an exact contract explicitly justifies a light study;
- ivory is constrained to bounded counterforms, specimen fields, typography and controlled inserts;
- five-board rounds must use five independently bound generation calls when one multi-output call cannot preserve contract identity;
- both failed A16-A20 attempts remain useful evidence but are quarantined from positive-reference context.

## Why it mattered
A project can have a correct Canon and still drift if all positive references are treated as equivalent.

For generative workflows, durable authority needs at least three distinct layers:
1. semantic Canon — meaning, principles, families and color roles;
2. execution-style anchors — latest approved surface/tonal state;
3. negative/quarantined evidence — material that must not become positive reference context.

Without this split, generative defaults can silently roll a project back to an earlier exploratory state even while appearing on-brand.

## Evidence
Primary evidence:
- PR #30: Generation Runtime Lock V1;
- PR #31: Execution Style Anchor Set V1 + Surface Lock V1;
- docs/03-brand/workbench/divinivid/generation/GENERATION_RUNTIME_LOCK_V1.md;
- docs/03-brand/workbench/divinivid/generation/EXECUTION_STYLE_ANCHOR_SET_V1.md;
- docs/03-brand/workbench/divinivid/generation/SURFACE_LOCK_V1.md;
- docs/03-brand/workbench/divinivid/generation/CURRENT_GENERATION_STATE.yaml;
- docs/03-brand/workbench/divinivid/ANTI_CANON.md.

Observed failure evidence:
- multiple visually competent A16-A20 attempts were rejected because they moved toward ivory editorial / sacred-premium surfaces;
- one attempt also mismatched exact board contracts;
- the human identified the tonal-background drift before the first runtime correction fully solved it.

## Key lessons
1. Semantic Canon and execution-style state are different authorities.
2. A qualitative rule such as dark-dominant may need an operational threshold and thumbnail gate to be executable.
3. Unapproved outputs must be quarantined even when visually attractive.
4. Technical subject matter must not be allowed to rewrite art direction.
5. Multi-output generation can be a contract-binding risk; independent calls inside one user-visible round are safer when outputs have distinct contracts.
6. Recency has no authority; explicit human-approved state does.

## Reuse conditions
High-value for mature brands with long visual exploration histories, generative design systems, multi-agent visual workflows, asset factories, and projects where approved direction evolves through multiple aesthetic phases.

Lower value for one-off image generation, projects without a stable approved visual state, and simple brands where one small reference pack is already unambiguous.

## Failure / constraint / caveat
- The 75-90% dark-field threshold is DIVINIVID-specific and must not become a universal brand rule.
- The reusable pattern is authority separation and executable surface constraints, not the specific colors or proportions.
- The new runtime still requires further evidence from successful A16-A20 regeneration.
- Generator APIs differ in how explicitly they accept image references; adapters must preserve the authority model without assuming one provider.

## Downstream routes
- [ ] Story / media seed
- [x] Skill candidate
- [x] SOP / process
- [x] Template / schema
- [x] Eval / test
- [ ] Reusable component / code
- [ ] Asset
- [ ] Case study / proof
- [x] Benchmark / lesson

## Candidate downstream artifact
### Skill Foundry
Feed this incident into the already-approved candidate sf-cand-20260920-divinivid-visual-production-system.

The G7 specifications should include reference-authority separation, execution-style anchor packs, quarantine semantics, self-reference prevention, contract-bound generation, pre-display surface/canon QA, and evals for visually competent but off-canon outputs.

### Noema
Evaluate whether a future protocol-level pattern is needed for typed context/reference authority so a project can distinguish semantic authority from execution-state authority without pushing domain-specific rules into Noema.

Noema should not absorb DIVINIVID aesthetics or Brand-domain state.

## Confidentiality / redaction notes
INTERNAL process lesson. No confidential client data is needed.

## Canon impact
- [ ] No canon impact
- [x] Consider ADR / policy update separately

The source project already implemented project-local runtime policy. Any universal Noema or Skill Foundry change requires its own governance path.

## Human review
- reviewer: pending
- decision: pending
- notes: High-signal incident. Route to Noema as protocol candidate and Skill Foundry as post-G6 implementation evidence.