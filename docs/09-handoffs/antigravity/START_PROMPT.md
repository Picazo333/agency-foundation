# START PROMPT — Antigravity Neutral Technical Foundation

Work only in repository `Picazo333/agency-foundation` and only on branch `tech/antigravity-foundation`.

Your governing task is GitHub Issue #4: `tech: Antigravity neutral technical foundation + labs`.

## REPO SAFETY — NON-NEGOTIABLE

1. NEVER work directly on `main`.
2. Do not force-push, rewrite history, delete unrelated files or overwrite another workstream.
3. Do not commit secrets, credentials, private keys or real environment values.
4. Do not freeze provisional Brand values into permanent technical architecture.
5. Do not select business strategy, ICP, pricing, naming or visual identity.
6. Do not build the final production website in this task.
7. Keep experiments isolated and reversible.
8. Any new dependency must have a documented reason, expected benefit and rollback/removal path.
9. Use worktrees/subagents only in isolated scopes; do not let parallel agents edit the same files concurrently.
10. All work stays on `tech/antigravity-foundation` and ends in a PR to `main`; do not merge your own PR.

## READ FIRST

1. `AGENTS.md`
2. `PROJECT_STATE.md`
3. `docs/00-meta/source-of-truth.md`
4. `docs/00-meta/WORKTREE_OPERATING_GUIDE.md`
5. `docs/08-plans/master/META_PLAN.md`
6. `docs/08-plans/workstreams/TECH_FOUNDATION_WORKSTREAM.md`
7. GitHub Issue #4 in full
8. technical/research summaries relevant to Aesthetic / Functional / System spines and S0–S4 maturity.

## MISSION

Build a neutral, experimental technical foundation that can later receive an approved Brand System V1, business requirements and final website/system specifications without major architectural rework.

This is not the production site. Treat this branch as a technical lab and foundation package.

Antigravity is the experimental/prototyping lead. Jules has a separate repo-hardening/CI scope. Avoid duplicating Jules's work unless a technical experiment requires a minimal repo-level integration.

## REQUIRED WORK

### 1. Neutral design-token architecture
Create/propose a token schema with brand values intentionally TBD:
- color roles;
- typography roles;
- spacing;
- sizing;
- borders;
- radius;
- shadow/elevation;
- motion durations/easing;
- breakpoints;
- z-index/layers;
- component/semantic aliases.
Do not invent final colors/fonts.

### 2. Isolated technical labs
Prepare clearly separated labs for:
- visual rendering experiments;
- SVG;
- motion;
- scroll interaction;
- responsive behavior;
- advanced interaction only when justified.
Everything experimental must be clearly marked disposable/provisional.

### 3. SVG pipeline proof-of-concept
Prototype or specify:
- validation;
- optimization;
- sanitization/security concerns;
- naming;
- metadata/provenance;
- componentization;
- responsive behavior;
- accessibility handling;
- before/after checks.

### 4. Motion experiments
Test or document viable approaches for:
- CSS transitions/animations;
- SVG animation;
- GSAP where justified;
- scroll-linked behavior;
- reduced-motion fallback;
- mobile constraints;
- performance cost.
Avoid animation for spectacle alone.

### 5. Performance baseline
Define a lightweight performance budget and measurement approach for later Brand/Web implementation. Measure prototypes where possible. Do not claim production benchmarks from toy examples.

### 6. Accessibility baseline
Define/prototype:
- reduced motion;
- keyboard/focus expectations for interactive experiments;
- semantic/fallback expectations;
- contrast evaluation hooks once Brand tokens exist;
- non-essential decorative asset handling.

### 7. Visual-regression / screenshot strategy
Propose or prototype the simplest reliable system for later visual regression and responsive snapshots.

### 8. Asset provenance integration
Define how technical consumption of assets will preserve metadata from the Gemini Asset Factory: asset ID, version, license/provenance state, approved status and responsive variants.

### 9. Security/secrets baseline
Document/prototype safe handling for future environment variables, API keys and third-party integrations. Never add real secrets.

### 10. S0–S4 maturity contract
Operationalize the stages:
- S0 Visual
- S1 Interactive
- S2 Mock Data
- S3 Backend Wired
- S4 AI/MCP
Define explicit entry/exit criteria so a visually complete prototype cannot masquerade as a connected production system.

### 11. Technical decision records
For decisions that may constrain later implementation, record:
- hypothesis;
- options;
- experiment;
- result;
- recommendation;
- reversibility;
- what still requires Brand/Strategy input.

### 12. Handoff package
Clearly distinguish:
- stable neutral foundations;
- experiments worth keeping;
- experiments rejected;
- dependencies added;
- future decisions blocked on Brand V1/Strategy;
- tasks suitable for Jules/Codex later.

## PARALLELISM / SUBAGENTS

Antigravity may use isolated worktrees/subagents for genuinely independent experiments, for example one agent on SVG validation and another on motion performance. Do not parallelize work that edits the same files or shares mutable state.

Before integrating subagent output, review it in the parent task. The parent agent remains responsible for consistency and repo safety.

## QUALITY STANDARD

Prefer small, demonstrable, reversible foundations over speculative large frameworks.

Any prototype should answer a concrete question and include enough evidence to justify keep/discard/undecided.

Do not install fashionable tooling merely because it exists.

## FINAL AUDITS

Before delivery run:
1. Principal Frontend/Platform Engineer audit.
2. Performance audit.
3. Accessibility audit.
4. Security/secrets audit.
5. Maintainability/reversibility audit.
6. Red Team audit for unnecessary complexity, vendor lock-in and premature architecture.

Then integrate fixes.

## DELIVERY

1. Commit only to `tech/antigravity-foundation`.
2. Run and record relevant checks/benchmarks.
3. Inspect all changed files for accidental cross-workstream edits or secrets.
4. Open a PR to `main` referencing Issue #4.
5. Do NOT merge your own PR.
6. PR must separate stable foundations from disposable experiments and include files changed, dependencies, checks run, benchmark caveats, unresolved risks and future decisions required.