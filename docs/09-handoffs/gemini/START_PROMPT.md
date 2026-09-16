# START PROMPT — Gemini Asset Factory Architecture

Work only in repository `Picazo333/agency-foundation` and only on branch `asset/gemini-foundry-architecture`.

Your governing task is GitHub Issue #3: `asset: Gemini Asset Factory architecture`.

## REPO SAFETY — NON-NEGOTIABLE

1. NEVER work directly on `main`.
2. Do not force-push, rewrite history, delete unrelated files or overwrite another workstream.
3. Do not alter/freeze Brand naming or visual canon.
4. Do not commit secrets, credentials or real environment values.
5. Do not mass-produce final brand assets in this task.
6. If Brand V1 does not yet define a value, create a schema/interface/placeholder; do not invent the final value.
7. Keep all work on `asset/gemini-foundry-architecture` and deliver through a PR to `main`.
8. Before finishing, inspect changed files and confirm nothing outside the allowed scope was modified unintentionally.

## READ FIRST

1. `AGENTS.md`
2. `PROJECT_STATE.md`
3. `docs/00-meta/source-of-truth.md`
4. `docs/08-plans/master/META_PLAN.md`
5. `docs/08-plans/workstreams/GEMINI_ASSET_FACTORY_WORKSTREAM.md`
6. `asset-factory/spec/README.md`
7. GitHub Issue #3 in full
8. Brand workbench and visual research only as PROVISIONAL context.

Remember at all times:
`brand workbench != brand canon`.

## MISSION

Design the complete reusable architecture of a future Gemini Gem / Asset Factory that can receive an approved Brand System V1 and reliably produce coherent, reusable, traceable production assets at scale.

This task is about building the FACTORY, not producing the final inventory.

The system must be designed so that Brand V1 can later be inserted without architectural rework.

## REQUIRED DESIGN

Define at minimum:

### 1. Brand Pack input contract
Specify exactly what the factory requires from Brand V1:
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
- licensing/provenance rules.

### 2. Asset taxonomy
Design a scalable taxonomy covering at least:
- SVG ornaments;
- borders/frames/dividers;
- patterns/textures;
- illustration families;
- anatomical plates;
- bestiary/figurative assets if Brand V1 allows them;
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

### 3. Prompt architecture
Create reusable prompt templates and parameter contracts rather than one-off prompts.
Define:
- global brand context;
- asset-specific fields;
- format/dimensions;
- variants;
- negative constraints;
- source/reference handling;
- originality requirements;
- safe fallback behavior;
- deterministic naming/versioning conventions.

### 4. Metadata/provenance schema
Every asset should be able to record:
- asset ID;
- category;
- purpose;
- status;
- version;
- format/dimensions;
- palette/tokens used;
- source/reference lineage;
- original/generated/licensed/reference-only state;
- license/usage notes;
- responsive variants;
- accessibility notes where relevant;
- QA state;
- approval/rejection history.

### 5. Lifecycle
Design the promotion flow:
`generated -> staging -> reviewed -> approved` or `rejected/deprecated`.
No generated file becomes canonical merely because it exists.

### 6. QA gates
Design checks for:
- brand consistency;
- line weights/style consistency;
- palette/token conformity;
- SVG validity and optimization;
- legibility/accessibility relevance;
- responsive suitability;
- performance implications;
- originality/reference-distance concerns;
- license/provenance completeness;
- duplicate asset detection;
- naming/version discipline;
- visual-family cohesion.

### 7. Invent-vs-ask rules
Specify when the factory may generate a variation autonomously and when it must stop because the Brand Pack lacks authority.

### 8. Failure/rejection handling
Define how to handle:
- visually attractive but off-brand outputs;
- invalid/bloated SVG;
- missing provenance;
- inaccessible output;
- inconsistent variants;
- copyright/licensing uncertainty;
- duplicate or uncontrolled asset sprawl;
- prompt drift.

### 9. Handoff contract
Specify how approved assets move into web/design/implementation workstreams without requiring another agent to reverse-engineer them.

### 10. Factory operating guide
Define how a human or future agent requests an asset batch, reviews it, promotes/rejects it, and regenerates only the necessary variants.

## OUTPUT STANDARD

Create a modular specification under the existing `asset-factory/` and Gemini handoff structure. Prefer schemas, templates, checklists and examples over vague prose.

Do not hard-code the current Chirograph-adjacent exploration as final Brand truth. Use examples only when explicitly labeled as examples.

## AUTONOMY

Continue without routine checkpoints. If a final Brand decision is missing, represent it as an interface/placeholder and continue.

## FINAL AUDITS

Before delivery run:

1. Creative Director audit — would the system generate a coherent family rather than isolated pretty assets?
2. Design Systems audit — are schemas, naming, versioning and reuse robust?
3. Production audit — could hundreds of assets be managed without chaos?
4. Web/Performance audit — could outputs actually be integrated responsibly?
5. Licensing/Provenance audit — can every approved asset be traced and legally evaluated?
6. Red Team audit — how could this factory cause brand drift, unusable outputs or uncontrolled asset sprawl?

Then consolidate fixes.

## DELIVERY

1. Commit only to `asset/gemini-foundry-architecture`.
2. Validate docs/schemas/examples.
3. Inspect changed files for unrelated edits or secrets.
4. Open a PR to `main` referencing Issue #3.
5. Do NOT merge your own PR.
6. PR summary must explain architecture, schemas, QA gates, unresolved Brand V1 dependencies, files changed and exactly what becomes executable after Brand V1 freezes.