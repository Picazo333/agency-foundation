# START PROMPT — Jules Repo Hardening + CI/Documentation Foundation

Work only in repository `Picazo333/agency-foundation` and only on branch `tech/jules-repo-hardening`.

Your governing task is GitHub Issue #6: `tech: Jules repo hardening + CI/documentation foundation`.

## 0. PRE-FLIGHT

Before writing:
1. Verify repository = `Picazo333/agency-foundation`.
2. Verify branch = `tech/jules-repo-hardening`.
3. Inspect current changed files/status.
4. Read repo governance + Issue #6 completely.
5. If behind `main`, sync only non-destructively and only if branch work is safe. Never discard work merely to sync.
6. If direct writes to `main` are unavoidable, stop.

## 1. REPO SAFETY — NON-NEGOTIABLE

- NEVER work directly on `main`.
- Never force-push, rewrite history, destructively reset/clean, bulk-delete unrelated files or overwrite another workstream.
- Do not modify Brand, naming, ICP, offer, pricing, strategy or research conclusions.
- Do not build the production website.
- Never commit secrets, tokens, credentials, private keys or real `.env` values.
- Do not mass-upgrade dependencies.
- Do not enable destructive automation or auto-fix workflows that can rewrite large parts of the repo without review.
- Do not weaken checks to make CI pass; fix root causes or document an intentional exception.
- Keep changes small, deterministic, reviewable and reversible.
- Finish only through a PR to `main`; do not merge your own PR.

## 2. WRITE BOUNDARIES / COLLISION CONTROL

Primary writable areas:
- `.github/`
- dedicated repo-health utilities such as `scripts/repo-health/`
- minimal root-level config files when directly required for repository hygiene
- repo-governance docs under `docs/00-meta/` when directly within scope
- `docs/09-handoffs/jules/`

Read-only unless fixing a provably broken repo-level reference and explicitly disclosing it:
- `labs/` (Antigravity-owned)
- experimental/neutral `packages/` (Antigravity-owned unless shared later)
- `asset-factory/` (Gemini-owned)
- `docs/02-strategy/` and `docs/04-operations/` (Claude-owned)
- `docs/03-brand/` (Brand workstream)
- other agents' handoff folders.

Never edit another active workstream's owned file merely to improve style or consistency. Log the issue instead.

## 3. READ FIRST

1. `AGENTS.md`
2. `PROJECT_STATE.md`
3. `README.md`
4. `docs/00-meta/source-of-truth.md`
5. `docs/00-meta/WORKTREE_OPERATING_GUIDE.md`
6. current `.github/` files/workflows/templates
7. GitHub Issue #6 in full
8. repo governance / Definition-of-Done documentation relevant to scope.

## 4. MISSION

Harden the repository so multiple human/AI workers can operate concurrently with less collision risk, safer defaults, clearer validation and lower manual-review overhead.

Jules owns REPO HYGIENE + CI + DOCUMENT VALIDATION + AGENTIC-WORK TEMPLATES + SECRET HYGIENE.
Antigravity owns experimental visual/motion/SVG/interaction labs and broader neutral technical experimentation.

Do not duplicate Antigravity's architecture.

## 5. REQUIRED WORK

### A. Repository health audit
Inspect for:
- broken/missing doc references;
- inconsistent paths/naming;
- duplicated/stale governance docs;
- source-of-truth ambiguity;
- missing ignore/config safeguards;
- fragile automation;
- places where agents can accidentally write to the wrong area;
- stale/accidental branches or governance debt that should be reported for human cleanup.

Do not reorganize the whole repo for aesthetics.

### B. CI / deterministic validation
Strengthen lightweight checks where justified for:
- Markdown/document health;
- broken internal links where practical;
- required metadata/frontmatter where already expected;
- structural invariants;
- duplicate identifiers where risky;
- obvious invalid references;
- basic secret-leak prevention if feasible without exposing secrets.

Prefer low-maintenance, deterministic checks.

### C. Secret / environment hygiene
Review/improve where needed:
- `.gitignore`;
- `.env.example` strategy;
- guidance preventing real secrets entering Git;
- CI behavior that must not print sensitive values;
- recommendations for GitHub secret scanning/settings if these require human action.

Never add actual credentials.

### D. Agentic-work templates
Audit/improve:
- PR template;
- Issue templates;
- Definition of Done;
- changed-files reporting;
- validation evidence;
- risks/non-goals;
- explicit branch-only work;
- PR-before-merge discipline;
- cross-workstream dependency/collision reporting.

### E. AGENTS guidance
Review `AGENTS.md` for correctness/usability. Keep it concise and link to deeper docs rather than bloating it.

### F. Local/CI helper scripts
Where useful, create small deterministic helpers that humans/agents can run before PR. Document exact usage and exit behavior.

Use a Jules-owned script namespace such as `scripts/repo-health/` to avoid collisions with Antigravity technical-lab scripts.

### G. GitHub settings recommendations
Inspect visible state and produce exact human-side recommendations for:
- branch protection/rulesets;
- required checks;
- review requirements;
- deletion protection where useful;
- secret scanning/security features if applicable;
- auto-merge policy if any.

Do not claim settings were enabled if your environment cannot enable them.

### H. Hardening report
Create `JULES_REPO_HARDENING_REPORT.md` in the appropriate Jules handoff/technical documentation location containing:
- baseline findings;
- changes made;
- before/after checks;
- remaining risks;
- recommended human GitHub settings;
- deferred items;
- stale/accidental branches or cleanup recommendations;
- collision risks with active branches.

## 6. CHANGE-DISCIPLINE CONTRACT

Before changing any existing file ask:
1. Is this file owned by Jules's scope?
2. Is the change necessary for repo safety/reliability?
3. Can it be solved with a narrower change?
4. Could another active branch be editing this file?
5. Is there a deterministic way to validate the change?

Avoid repo-wide formatting churn.
Avoid lockfile changes unless directly required.
Avoid package upgrades unless a specific security/reliability issue justifies them.

For any CI change, record:
- trigger;
- expected runtime/cost;
- failure conditions;
- false-positive risk;
- how to reproduce locally if possible;
- rollback/removal path.

## 7. QUALITY STANDARD

Do not create enterprise bureaucracy for its own sake.
Every check/automation must be:
- deterministic;
- understandable;
- documented;
- cheap to maintain;
- proportionate to risk;
- easy to remove if it stops adding value.

Measure before/after where possible rather than claiming improvement abstractly.

## 8. FINAL AUDITS

Run and integrate fixes from:
1. Repository maintainer audit.
2. CI reliability audit.
3. Secret-safety audit.
4. Multi-agent collision audit.
5. Developer/agent ergonomics audit.
6. Red Team audit for false failures, over-constraint, hidden destructive behavior or maintenance burden.

## 9. EXIT / PR CHECKLIST

Before PR:
1. Run all checks you added/changed and record results.
2. Inspect complete changed-file list.
3. Confirm all edits are inside Jules-owned scope or explicitly justify an exception.
4. Confirm no `labs/`, Gemini Asset Factory, Brand or Claude-owned content was modified unintentionally.
5. Confirm no secrets or credentials.
6. Confirm no mass formatting/dependency churn.
7. Commit only to `tech/jules-repo-hardening`.
8. Open PR to `main` referencing Issue #6.
9. Do NOT merge your own PR.

PR must include:
- files changed;
- checks run/results;
- remaining risks;
- human GitHub settings recommended;
- before/after repository-health observations;
- any stale/accidental branch cleanup recommendations;
- coordination needed with Antigravity or future implementation agents;
- cross-branch collision risks.