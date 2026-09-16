# START PROMPT — Jules Repo Hardening + CI/Documentation Foundation

Work only in repository `Picazo333/agency-foundation` and only on branch `tech/jules-repo-hardening`.

Your governing task is GitHub Issue #6: `tech: Jules repo hardening + CI/documentation foundation`.

## REPO SAFETY — NON-NEGOTIABLE

1. NEVER work directly on `main`.
2. Do not force-push, rewrite Git history, delete unrelated files or overwrite another workstream.
3. Do not modify Brand, naming, ICP, offer, pricing, strategy or research conclusions.
4. Do not build the final production website.
5. Do not commit secrets, tokens, credentials, private keys or real `.env` values.
6. Do not mass-upgrade dependencies.
7. Keep changes narrowly scoped, deterministic and easy to review/revert.
8. All work must stay on `tech/jules-repo-hardening` and finish as a PR to `main`.
9. Do not merge your own PR.
10. If a repository setting cannot be changed from your environment, document the exact human action required rather than claiming it was changed.

## READ FIRST

1. `AGENTS.md`
2. `PROJECT_STATE.md`
3. `README.md`
4. `docs/00-meta/source-of-truth.md`
5. `docs/00-meta/WORKTREE_OPERATING_GUIDE.md`
6. current `.github/` files and workflows
7. GitHub Issue #6 in full
8. repo governance/definition-of-done documentation relevant to your scope.

## MISSION

Harden the repository so multiple human/AI workers can operate safely, consistently and with less manual review overhead.

Jules owns repo hygiene, CI/document validation and narrowly scoped maintenance. Antigravity separately owns experimental visual/motion/SVG/interaction technical labs. Avoid overlapping with Antigravity's architecture unless an objectively broken repo-level integration must be fixed.

## REQUIRED WORK

### 1. Repository health audit
Inspect the current tree for:
- broken/missing documentation references;
- inconsistent paths/naming;
- duplicated or stale governance files;
- obvious source-of-truth violations;
- missing ignore/config files;
- fragile automation;
- areas where an agent could accidentally write to the wrong place.

Do not reorganize the whole repo merely for aesthetics. Make only justified changes.

### 2. CI / deterministic validation
Strengthen lightweight checks where appropriate for:
- Markdown/document health;
- broken internal links if practical;
- required metadata/frontmatter where the repo already expects it;
- basic structural invariants;
- duplicate IDs/names where they are genuinely risky;
- obvious invalid references.

Prefer simple scripts/actions with low maintenance cost.

### 3. Secret/environment hygiene
Review and improve, where needed:
- `.gitignore`;
- `.env.example` strategy;
- instructions preventing real secrets from entering Git;
- CI behavior that must not expose sensitive values.
Never add actual credentials.

### 4. Agentic-work templates
Audit/improve:
- PR template;
- Issue templates;
- Definition of Done fields;
- required reporting of files changed, validation performed, risks and non-goals;
- instructions that reinforce branch-only work and PR review.

### 5. AGENTS guidance
Review `AGENTS.md` for correctness and usability. Keep it concise. Link to deeper documentation rather than bloating it.

### 6. Local/CI helper scripts
Where valuable, create small deterministic scripts that a human or agent can run to validate repo health before opening a PR. Document how to use them.

### 7. GitHub settings recommendations
Inspect what is currently visible and produce a precise list of human-side settings worth enabling later, such as branch protection/required checks/review rules. Do not claim to have enabled anything you could not actually change.

### 8. Hardening report
Create `JULES_REPO_HARDENING_REPORT.md` in the appropriate handoff/technical documentation area containing:
- audit findings;
- changes made;
- checks added;
- remaining risks;
- recommended manual GitHub settings;
- deferred items;
- any collision risks with other active branches.

## QUALITY STANDARD

Do not create complexity for its own sake. The goal is a safer repo for parallel AI/human work, not an enterprise bureaucracy.

Every automation/check must be:
- deterministic;
- understandable;
- documented;
- cheap to maintain;
- easy to remove if it stops providing value.

## FINAL AUDITS

Before delivery run:
1. Repository maintainer audit.
2. CI reliability audit.
3. Secret-safety audit.
4. Multi-agent collision audit.
5. Red Team pass: identify ways your own changes could block legitimate work, create false failures or over-constrain the repo.

Then fix material issues.

## DELIVERY

1. Commit only to `tech/jules-repo-hardening`.
2. Run all new/existing checks you touched and record results.
3. Inspect the complete diff for unrelated modifications or secrets.
4. Open a PR to `main` referencing Issue #6.
5. Do NOT merge your own PR.
6. PR must list files changed, checks run, remaining risks, manual GitHub settings recommended and any coordination needed with Antigravity or future implementation agents.