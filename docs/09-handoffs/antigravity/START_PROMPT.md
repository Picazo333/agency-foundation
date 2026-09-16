# START PROMPT — Antigravity Neutral Technical Foundation

Work only in repository `Picazo333/agency-foundation` and only on branch `tech/antigravity-foundation`.

Your governing task is GitHub Issue #4: `tech: Antigravity neutral technical foundation + labs`.

## 0. PRE-FLIGHT

Before writing:
1. Verify repository = `Picazo333/agency-foundation`.
2. Verify branch = `tech/antigravity-foundation`.
3. Inspect changed files/status before editing.
4. Read repo governance + Issue #4 completely.
5. If the branch is behind `main`, sync only non-destructively and only if branch work is safe. Never discard work merely to sync.
6. If direct writes to `main` are unavoidable, stop.

## 1. REPO SAFETY — NON-NEGOTIABLE

- NEVER work directly on `main`.
- Never force-push, rewrite history, destructively reset/clean, bulk-delete unrelated files or overwrite another workstream.
- Never commit secrets, credentials, private keys or real environment values.
- Do not freeze provisional Brand values into permanent technical architecture.
- Do not choose business strategy, ICP, pricing, naming or visual identity.
- Do not build the final production website.
- Keep experiments isolated, reversible and explicitly provisional.
- Any new dependency must have a documented rationale, expected benefit, security/maintenance consideration and rollback/removal path.
- Do not execute arbitrary scripts/binaries from research/assets without inspection and a concrete need.
- Do not weaken existing repo security/validation gates.
- Finish only by PR to `main`; do not merge your own PR.

## 2. WRITE BOUNDARIES / COLLISION CONTROL

Primary writable areas:
- `labs/`
- neutral technical packages under `packages/` when justified
- technical experiment utilities under a dedicated Antigravity-owned path such as `scripts/tech-labs/`
- `infra/` only for neutral/prototype infrastructure requirements
- `docs/09-handoffs/antigravity/`
- narrowly scoped technical decision docs tied to the experiments.

Read-only unless a tiny integration correction is unavoidable and disclosed:
- `.github/` (Jules-owned)
- `scripts/repo-health/` or Jules-owned validation utilities
- `docs/02-strategy/`
- `docs/03-brand/`
- `asset-factory/`
- Claude/Gemini/Jules handoff folders.

If a needed change belongs to another branch, record a dependency instead of editing its owned files.

## 3. READ FIRST

1. `AGENTS.md`
2. `PROJECT_STATE.md`
3. `docs/00-meta/source-of-truth.md`
4. `docs/00-meta/WORKTREE_OPERATING_GUIDE.md`
5. `docs/08-plans/master/META_PLAN.md`
6. `docs/08-plans/workstreams/TECH_FOUNDATION_WORKSTREAM.md`
7. GitHub Issue #4 in full
8. technical/research summaries relevant to Aesthetic / Functional / System spines and S0–S4 maturity.

## 4. MISSION

Build a neutral, experimental technical foundation that can later receive approved Brand System V1, business requirements and final web/system specifications without major architectural rework.

This branch is a LAB + FOUNDATION package, not production.

Antigravity owns experimental/prototyping technical work. Jules separately owns repo hardening/CI/document validation. Avoid overlap.

## 5. REQUIRED WORK

### A. Neutral design-token architecture
Create/propose a schema with values intentionally TBD for:
- semantic color roles;
- typography roles;
- spacing/sizing;
- borders/radius;
- shadow/elevation;
- motion durations/easing;
- breakpoints;
- z-index/layers;
- component/semantic aliases.
Do not invent final brand colors/fonts.

### B. Isolated technical labs
Prepare clearly separated labs for:
- visual rendering;
- SVG;
- motion;
- scroll behavior;
- responsive behavior;
- advanced interaction only where justified.

Mark each experiment as `STABLE CANDIDATE / EXPERIMENTAL / REJECTED / BLOCKED`.

### C. SVG pipeline proof-of-concept
Prototype/specify:
- validation;
- optimization;
- sanitization/security;
- naming;
- metadata/provenance hooks;
- componentization;
- responsive behavior;
- accessibility handling;
- before/after checks.

### D. Motion experiments
Test/document viable approaches for:
- CSS animation;
- SVG animation;
- GSAP only when justified;
- scroll-linked behavior;
- reduced-motion fallback;
- mobile constraints;
- performance cost.

Avoid spectacle-only animation.

### E. Performance baseline
Define a lightweight future-facing performance budget and measurement method. Measure prototypes when possible, but never present toy benchmarks as production guarantees.

### F. Accessibility baseline
Define/prototype:
- reduced motion;
- keyboard/focus expectations for interactive experiments;
- semantic/fallback behavior;
- contrast hooks once Brand tokens exist;
- treatment of decorative/non-essential assets.

### G. Visual-regression / screenshot strategy
Propose or prototype the simplest reliable path for later visual regression and responsive snapshots.

### H. Asset provenance integration
Define how implementation can preserve Gemini Asset Factory metadata later: asset ID, version, approved status, rights/provenance, responsive variants.
Do not modify Gemini-owned schemas; design a consumer interface and note dependencies.

### I. Security / secrets baseline
Document/prototype safe handling for future environment variables, APIs and third-party integrations. Never add real credentials.

### J. S0–S4 maturity contract
Operationalize:
- S0 Visual
- S1 Interactive
- S2 Mock Data
- S3 Backend Wired
- S4 AI/MCP

Define entry/exit criteria so S0/S1 work cannot masquerade as production-connected S3/S4.

### K. Technical decision records
For any decision that might constrain later implementation record:
- question/hypothesis;
- options;
- experiment;
- result;
- recommendation;
- reversibility;
- Brand/Strategy dependencies.

### L. Handoff package
Separate:
- stable neutral foundations;
- experiments worth keeping;
- rejected experiments;
- dependencies added;
- future decisions blocked on Brand V1/Strategy;
- later tasks suitable for Codex/Jules.

## 6. PARALLELISM / SUBAGENTS

Use subagents/worktrees only for truly independent work with non-overlapping write sets.

Before spawning subagents, define a mini ownership map, e.g.:
- subagent A -> SVG proof-of-concept only;
- subagent B -> motion/performance only;
- subagent C -> screenshot/visual-regression only.

Two subagents must never edit the same file concurrently.
The parent agent reviews and integrates all subagent output and remains accountable for security and consistency.

## 7. DEPTH / EVIDENCE CONTRACT

Every experiment must answer a concrete technical question and document:
- hypothesis;
- setup;
- files touched;
- dependency cost;
- result/evidence;
- performance/accessibility/security observations;
- keep/reject/undecided recommendation;
- reversibility/removal path.

Prefer a few well-evidenced experiments over a large speculative framework.
Do not install trendy tooling without a demonstrated need.

## 8. FINAL AUDITS

Run and integrate fixes from:
1. Principal Frontend/Platform Engineer audit.
2. Performance audit.
3. Accessibility audit.
4. Security/secrets audit.
5. Maintainability/reversibility audit.
6. Dependency/supply-chain audit.
7. Multi-agent collision audit.
8. Red Team audit for overengineering, vendor lock-in, premature architecture and false confidence from toy prototypes.

## 9. EXIT / PR CHECKLIST

Before PR:
1. Inspect the complete changed-file list.
2. Confirm all edits are inside Antigravity-owned scope or explicitly justify exceptions.
3. Confirm `.github/` and Jules-owned repo-health files were not modified.
4. Confirm no secrets, unrelated formatting churn or destructive changes.
5. Record relevant checks/benchmarks and caveats.
6. Document dependencies added and removal paths.
7. Commit only to `tech/antigravity-foundation`.
8. Open PR to `main` referencing Issue #4.
9. Do NOT merge your own PR.

PR must clearly separate:
- STABLE FOUNDATION;
- EXPERIMENTAL;
- REJECTED;
- BLOCKED BY BRAND/STRATEGY;
- files changed;
- dependencies;
- tests/benchmarks;
- caveats/risks;
- cross-branch dependencies/collision risks.