# START PROMPT — Gemini Asset Factory Architecture

Work only in repository `Picazo333/agency-foundation` and only on branch `asset/gemini-foundry-architecture`.

Your governing task is GitHub Issue #3: `asset: Gemini Asset Factory architecture`.

## 0. PRE-FLIGHT

Before writing:
1. Verify repository = `Picazo333/agency-foundation`.
2. Verify branch = `asset/gemini-foundry-architecture`.
3. Inspect current changed files/status.
4. Read repo governance + Issue #3 before editing.
5. If behind `main`, update only non-destructively and only if branch work is safe. Never discard existing changes just to sync.
6. If direct writes to `main` are the only available mode, stop.

## 1. REPO SAFETY — NON-NEGOTIABLE

- NEVER work directly on `main`.
- Never force-push, rewrite history, destructively reset/clean, bulk-delete unrelated files or overwrite another workstream.
- Do not alter/freeze Brand naming or visual canon.
- Do not commit secrets, credentials, private keys or real environment values.
- Do not mass-produce final assets in this task.
- Do not ingest or redistribute third-party reference files as production assets merely because they are present in research.
- Do not silently copy protected/reference-only material into approved outputs.
- If Brand V1 does not define a value, create a schema/interface/placeholder rather than inventing the final value.
- Finish only through PR to `main`; do not merge your own PR.

## 2. WRITE BOUNDARIES / COLLISION CONTROL

Primary writable areas:
- `asset-factory/`
- `docs/09-handoffs/gemini/`
- tightly related Asset Factory documentation under existing planning/spec locations.

Read-only unless a tiny direct correction is unavoidable and disclosed:
- `docs/03-brand/`
- `docs/02-strategy/`
- `docs/04-operations/`
- `labs/`
- `packages/`
- `.github/`
- Antigravity/Jules handoff folders.

Do not edit files owned by active Claude, Antigravity or Jules branches. If you need a change from another workstream, log a dependency instead.

## 3. READ FIRST

1. `AGENTS.md`
2. `PROJECT_STATE.md`
3. `docs/00-meta/source-of-truth.md`
4. `docs/08-plans/master/META_PLAN.md`
5. `docs/08-plans/workstreams/GEMINI_ASSET_FACTORY_WORKSTREAM.md`
6. `asset-factory/spec/README.md`
7. GitHub Issue #3 in full
8. Brand workbench and visual research only as PROVISIONAL context.

Always remember: `brand workbench != brand canon`.

## 4. MISSION

Design the complete reusable architecture of a future Gemini Gem / Asset Factory that can receive an approved Brand System V1 and reliably produce coherent, traceable, reusable production assets at scale.

This task builds the FACTORY, not the final asset inventory.

The architecture must accept Brand V1 later without fundamental redesign.

## 5. REQUIRED SYSTEM DESIGN

### A. Brand Pack input contract
Specify exact required/optional fields for:
- brand thesis/personality;
- approved name/wordmark rules;
- typography;
- palette/tokens;
- illustration/image language;
- composition/grid;
- ornament/graphic devices;
- iconography;
- motion rules;
- accessibility constraints;
- responsive behavior;
- anti-patterns;
- provenance/licensing rules.

### B. Asset taxonomy
Cover at minimum:
- SVG ornaments;
- borders/frames/dividers;
- patterns/textures;
- illustration families;
- anatomical plates;
- bestiary/figurative assets if Brand V1 permits;
- celestial/diagrammatic systems;
- icons;
- backgrounds;
- web-section art;
- UI decoration;
- case-study assets;
- social formats;
- deck/presentation assets;
- motion frames/sequences;
- responsive variants.

### C. Prompt architecture
Create reusable prompt templates and parameter contracts, not one-off prompts.
Define:
- global Brand context;
- asset-specific fields;
- format/dimensions;
- variant controls;
- negative constraints;
- reference/source handling;
- originality requirements;
- safe fallback behavior;
- naming/version conventions.

### D. Metadata / provenance schema
Every asset must be representable with:
- asset ID;
- category/purpose;
- status/version;
- format/dimensions;
- palette/tokens;
- source/reference lineage;
- original/generated/licensed/reference-only state;
- license/usage notes;
- responsive variants;
- accessibility notes where relevant;
- QA state;
- approval/rejection history.

### E. Lifecycle / state machine
Define explicit promotion flow:
`requested -> generated -> staging -> reviewed -> approved` or `rejected/deprecated`.

No generated output is canonical merely because it exists.

### F. QA gates
Design checks for:
- Brand consistency;
- line-weight/style consistency;
- palette/token conformity;
- SVG validity/optimization;
- legibility/accessibility relevance;
- responsive suitability;
- performance implications;
- originality/reference-distance concerns;
- license/provenance completeness;
- duplicate detection;
- naming/version discipline;
- visual-family cohesion.

### G. Invent-vs-ask authority rules
Specify exactly what may be varied autonomously and what requires Brand authority.

### H. Failure / rejection handling
Cover:
- visually attractive but off-brand outputs;
- invalid/bloated SVG;
- missing provenance;
- inaccessible output;
- inconsistent variants;
- licensing uncertainty;
- duplicate/uncontrolled sprawl;
- prompt drift;
- missing Brand Pack fields.

### I. Handoff contract
Define how approved assets move into implementation without reverse-engineering.

### J. Operating guide
Define request, generation, batch review, approval/rejection, regeneration, deprecation and version upgrade workflows.

## 6. DEPTH / EXECUTABILITY CONTRACT

Do not stop at prose. Produce concrete machine/human-usable artifacts where appropriate:
- field definitions;
- JSON/YAML schema examples or equivalent structured examples;
- status/state definitions;
- folder/layout proposal;
- naming conventions;
- QA matrix;
- approval checklist;
- batch request template;
- rejection/regeneration template;
- handoff manifest example.

Create at least 3 illustrative asset-request examples using placeholder Brand values only. Do NOT generate final brand assets.

## 7. PROVENANCE / RIGHTS SAFETY

The factory must distinguish:
- original;
- generated;
- open-license;
- commercial-license;
- reference-only;
- unknown/blocked.

No asset with unknown or reference-only rights may silently enter `approved`.
Define what information a human must supply when rights cannot be determined automatically.

## 8. AUTONOMY

Continue without routine checkpoints.
If Brand data is missing, model the interface/placeholder and continue.
Only stop on a true fatal blocker.

## 9. FINAL AUDITS

Run and integrate fixes from:
1. Creative Director audit.
2. Design Systems audit.
3. Production-scale audit.
4. Web/Performance audit.
5. Licensing/Provenance audit.
6. Accessibility audit.
7. Red Team audit for brand drift, unusable outputs, rights failures and asset sprawl.
8. Multi-agent collision audit confirming no files from other active workstreams were modified.

## 10. EXIT / PR CHECKLIST

Before PR:
1. Inspect complete changed-file list.
2. Confirm every change is inside allowed scope or explicitly justified.
3. Confirm no final Brand values were invented.
4. Confirm no reference-only/licensing-uncertain material was promoted as production-ready.
5. Confirm no secrets or unrelated changes.
6. Validate docs/schemas/examples.
7. Commit only to `asset/gemini-foundry-architecture`.
8. Open PR to `main` referencing Issue #3.
9. Do NOT merge your own PR.

PR must explain:
- architecture;
- schemas/state machine;
- QA/provenance gates;
- Brand V1 dependencies;
- files changed;
- validation performed;
- cross-branch dependencies/collision risks;
- exactly what becomes executable after Brand V1 freezes.