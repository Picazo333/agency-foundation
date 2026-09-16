# Jules Repo Hardening Report

## Baseline Findings
- No systematic local or CI check for broken Markdown links or required document frontmatter.
- No automated secret leak detection tailored to common issues.
- `.gitignore` and `.env.example` lacked stronger secret/agent hygiene guidance.
- PR and Issue templates lacked explicit checklists for multi-agent safety and boundary constraints.
- `AGENTS.md` lacked an explicit command to run pre-PR checks.

## Changes Made
- **Created `scripts/repo-health/validate_repo.py`**: a deterministic, zero-dependency Python baseline that scans text files for several common secret formats, checks local Markdown links (including repository-escape paths), and validates required metadata on approved/frozen docs that use YAML frontmatter.
- **Implemented GitHub Actions CI**: added `.github/workflows/repo-health.yml` to run the same validator on pull requests and pushes to `main`.
- **Updated Secret Hygiene**: expanded `.gitignore` for common credential/key files and local IDE/agent artifacts; `.env.example` now uses placeholders that are intentionally not shaped like real credentials.
- **Improved Templates**: added explicit Agent Safety Checks to Issue/PR templates and the local validation command to the PR checklist.
- **Updated `AGENTS.md`**: added a pre-PR repository-health validation rule.

## Before/After Checks
- **Before**: repository safety depended primarily on manual review.
- **After**: a single deterministic local command and matching CI job provide a repeatable baseline for obvious secrets, broken local links, repository-escaping links, malformed canonical frontmatter, and required canonical metadata.

Local reproduction:

```bash
python3 scripts/repo-health/validate_repo.py
```

## Remaining Risks
- The secret checker is intentionally heuristic and lightweight. It is not a substitute for GitHub Secret Scanning / push protection and may miss novel, encoded, or provider-specific credentials.
- Markdown parsing is intentionally simple; unusually complex Markdown/HTML link syntax may require future refinement.
- Generated/binary-heavy `assets/` is excluded from this lightweight walk. Asset provenance/licensing and binary validation are handled by their own workstreams/contracts.
- Autonomous agents can still ignore repository guidance unless their task contract requires reading `AGENTS.md` and passing CI.
- Repository `.gitignore` cannot ignore worktrees created outside the repository; external worktree cleanup is an operational Git task, not an ignore-file feature.

## Human GitHub Settings Recommendations
- **Branch Protection / Ruleset for `main`**:
  - require a pull request before merging;
  - require the Repository Health `validate` status check once it has run successfully at least once;
  - disable force pushes and branch deletion where appropriate;
  - consider requiring conversation resolution before merge.
- **Secret Scanning / Push Protection**: enable GitHub secret scanning and push protection when available. These provide substantially deeper detection than the local regex baseline.

## Deferred Items
- Dependency auto-upgrades and third-party auto-formatting were intentionally deferred to avoid broad, low-signal churn.
- Complex AST/deep-code analysis was deferred because the repository is currently documentation/planning-heavy.
- Helper/superseded branch retirement remains explicitly tracked in `PENDING.md`; no branch is deleted until unique work is ruled out.

## Collision Risks & Stale Branches
- **Collision risk**: active branches may also modify `AGENTS.md`, templates, or root hygiene files. Integrate those changes deliberately rather than resolving by overwrite.
- **Stale/helper branches**: periodically inspect remote branches and retire only those confirmed to contain no unique work. Do not assign new work to superseded/helper branches.
