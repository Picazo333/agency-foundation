# START PROMPT — Gemini Asset Factory Architecture

Work from repository `Picazo333/agency-foundation` on branch `asset/gemini-foundry-architecture` and execute GitHub Issue #3 end-to-end.

Read first:
1. `AGENTS.md`
2. `PROJECT_STATE.md`
3. `docs/00-meta/source-of-truth.md`
4. `docs/08-plans/master/META_PLAN.md`
5. `docs/08-plans/workstreams/GEMINI_ASSET_FACTORY_WORKSTREAM.md`
6. `asset-factory/spec/README.md`
7. relevant Brand workbench and research summaries only as provisional context.

Mission:
Design the reusable Asset Factory architecture that will later turn an approved Brand System V1 into production-ready assets. Do NOT mass-produce final assets now and do NOT reinterpret or freeze the brand.

Define, at minimum:
- Brand Pack input contract;
- asset taxonomy: SVG ornament, borders, frames, patterns, illustration, bestiary, anatomical plates, celestial diagrams, icons, dividers, backgrounds, social, deck, case-study, web-section assets, motion frames and UI decoration;
- prompt templates and prompting rules;
- output metadata schema;
- provenance/licensing schema;
- invent-vs-ask rules;
- responsive/variant rules;
- generated -> staging -> approved promotion workflow;
- naming/versioning conventions;
- QA gates for visual consistency, SVG validity, accessibility/performance relevance, line-weight consistency, palette conformity, originality and license status;
- failure handling and rejection rules;
- handoff contract to web/implementation agents.

Key constraint:
`brand workbench != brand canon`. Treat all current visual directions as exploratory. The factory must remain flexible enough to accept the final Brand System V1 later without architectural rework.

Autonomy:
Continue without human checkpoints unless a true fatal blocker exists. If information is not yet frozen, define a placeholder/interface rather than guessing a final value.

Before finishing, run three audits:
1. Creative Director audit: can this factory produce a coherent visual family rather than isolated pretty assets?
2. Production/Design Systems audit: are outputs structured, versionable and reusable?
3. Red Team audit: where could the factory create brand drift, licensing risk, unusable SVGs, inconsistent variants, or uncontrolled asset sprawl?

Finish by committing work to `asset/gemini-foundry-architecture` and opening a PR to `main` that references/closes Issue #3. The PR must explain the architecture, schemas, unresolved dependencies on Brand V1, and exactly what will be ready to activate after the brand freeze.
