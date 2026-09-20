---
id: HARVEST-20260920-divinivid-visual-production-system
status: candidate
owner: meta
created: 2026-09-20
source_event_type: MILESTONE
confidentiality: INTERNAL
routes:
  - skill_candidate
  - sop_process
  - template_schema
  - eval_test
  - benchmark_lesson
provenance:
  issue: null
  pr: null
  commit: null
  adr: docs/07-decisions/ADR-0013-visual-universe-to-asset-factory-sequencing.md
  artifact: docs/08-plans/master/DIVINIVID_VISUAL_UNIVERSE_META_PLAN_V2.md
---
# Harvest Record — From visual exploration to an auditable asset factory

## What happened
DIVINIVID progressed from open visual exploration into a coherent visual universe spanning moodboards, applications, motion, entities, specimens, environments and physical communication. Repeated generation failures also produced a meaningful negative-evidence corpus.

The project then redesigned the pipeline so that production does not begin directly from moodboards. It now inserts archive/canon classification, coverage audit, executable visual specifications and a golden-set factory pilot before mass asset production.

## Previous state / problem
The workflow had several recurring risks:
- visual approvals existed partly in conversation rather than durable artifacts;
- failed/rejected boards could accidentally re-enter generation context;
- generators sometimes condensed five requested boards into one, recycled previous rounds or drifted aesthetically;
- fixed generation volume could create redundancy without increasing coverage;
- Asset Factory architecture existed, but the Brand Pack was not yet sufficiently executable;
- asking one model to both interpret aesthetics and manufacture final assets caused quality drift.

## What changed
The new pipeline separates:
1. evidence inventory;
2. canon/negative-evidence classification;
3. explicit moodboard contracts;
4. controlled high-signal expansion;
5. multidimensional coverage audit;
6. Visual Spec + Visual Matrix + Asset Ontology;
7. golden-set production pilot;
8. deterministic-ish factory production with QA/repair loops;
9. Brandbook assembly and release governance.

Each substantial round also gains a lightweight preflight/work-order/QA/harvest/checkpoint envelope.

## Why it mattered
This changes the bottleneck from “generate more visual ideas” to “preserve authority, prove coverage and make production contracts executable.” It reduces aesthetic rediscovery, context drift, redundant generation and the probability of mass-producing assets that later require redesign.

## Evidence
Primary project evidence:
- `docs/08-plans/master/DIVINIVID_VISUAL_UNIVERSE_META_PLAN_V2.md`;
- `docs/03-brand/workbench/divinivid/VISUAL_UNIVERSE_CHECKPOINT_2026-09-20.md`;
- `docs/03-brand/workbench/divinivid/ANTI_CANON.md`;
- `asset-factory/spec/01-brand-pack-contract.md`;
- `asset-factory/spec/04-metadata-provenance-schema.md`;
- `docs/07-decisions/ADR-0013-visual-universe-to-asset-factory-sequencing.md`.

Observed evidence from the working process includes repeated human rejection/correction of condensed, recycled and aesthetically drifting moodboard generations, followed by improved results when scope, board identity and canon constraints were explicit.

## Key lesson
For complex visual systems, **exploration and production should be separate capabilities**. A moodboard corpus becomes industrially useful only after authority, lineage, coverage and negative evidence are explicit; mass production should begin only after a representative pilot proves that the visual specification is executable.

## Reuse conditions
Likely useful for:
- brand systems with large asset libraries;
- multi-agent creative pipelines;
- generative design systems;
- visual worldbuilding;
- brandbook production;
- SVG/vector factories;
- projects where visual identity must survive multiple executors.

Do not apply the full pipeline to small brands that need only a logo, palette and a few simple templates; the governance cost would exceed the value.

## Failure / constraint / caveat
The current lesson comes from one high-complexity project. The exact number of moodboards, audit dimensions and pilot assets should remain proportional to project complexity.

The intended Gemini factory has not yet passed the golden-set pilot, so executor-specific conclusions remain hypotheses.

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
Skill Foundry should evaluate whether the workflow is best covered by:
- extension/mode of `brand-visual-direction`;
- extension/mode of `brand-identity-system`;
- extension of `brand-book-builder`;
- a reusable visual-coverage auditor;
- a production-spec/asset-factory handoff capability;
- or no new Skill if existing Brand Skills can absorb the workflow cleanly.

The correct Foundry outcome is not assumed.

## Confidentiality / redaction notes
INTERNAL process evidence. No client-confidential data is required.

## Canon impact
- [ ] No canon impact
- [x] Consider ADR / policy update separately

ADR-0013 records the project-specific sequencing decision. Skill Foundry must not auto-promote this project pipeline into global capability canon.

## Human review
- reviewer: pending
- decision: pending
- notes: Route to Skill Foundry G0-G5 for overlap analysis before any Skill build.
