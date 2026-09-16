# Jules Repo Hardening Report

## Baseline Findings
- No systematic local or CI check for broken Markdown links or required document frontmatter.
- No automated secret leak detection tailored to common issues.
- `.gitignore` and `.env.example` lacked robust agent-specific exclusion (like local worktree formats).
- PR and Issue templates lacked explicit checklists for multi-agent safety and boundary constraints.
- `AGENTS.md` missing explicit command to run pre-PR checks.

## Changes Made
- **Created `scripts/repo-health/validate_repo.py`**: A deterministic python script with zero dependencies that scans for secrets, broken relative links, and verifies canonical document frontmatter.
- **Implemented GitHub Actions CI**: Added `.github/workflows/repo-health.yml` that runs the validation script on `push` to `main` and all `pull_request` events.
- **Updated Secret Hygiene**: Expanded `.gitignore` with more key/cert extensions and ignored worktrees matching `../agency-*`. Explicit warnings added to `.env.example`.
- **Improved Templates**: Added specific "Agent Safety Checks" sections to `.github/ISSUE_TEMPLATE/task.md` and `research.md`. Appended similar verifications and the local validation command to `.github/PULL_REQUEST_TEMPLATE.md`.
- **Updated `AGENTS.md`**: Added a rule mandating running the repo validation script locally before PR submission.

## Before/After Checks
- **Before**: Run validation script manually (failed if arbitrary bad links were present).
- **After**: All tests pass cleanly (`✅ All Repository Health Checks Passed.`). PRs will be automatically guarded by the CI workflow running the same script.

## Remaining Risks
- The secret checking in `validate_repo.py` is heuristic and lightweight (regex-based) to maintain zero dependencies and determinism. It might miss complex or obfuscated secrets, and it has a small false-positive risk.
- Autonomous AI agents may skip reading PR templates or `AGENTS.md` unless explicitly instructed in their handoff prompts.

## Human GitHub Settings Recommendations
- **Branch Protection**: Go to GitHub Repo Settings -> Branches -> Add branch protection rule for `main`.
  - Check "Require a pull request before merging".
  - Check "Require status checks to pass before merging" and select the `validate` job from the Repository Health workflow.
  - Disable "Allow force pushes".
- **Secret Scanning**: Enable GitHub Secret Scanning in the repo security settings if available on your plan (this provides a much deeper layer of security than the basic python script).

## Deferred Items
- We deferred adding dependency auto-upgrades or third-party auto-formatting to avoid mass dependency churn (per safety rules).
- We avoided complex AST or deep code analysis since this repository acts heavily as a markdown-based configuration and planning space right now.

## Collision Risks & Stale Branches
- **Collision Risk**: Active branches (like `tech/agent-foundation` or `plan/claude-master-agency`) might conflict with template or `.gitignore` changes here. When merging this PR, recommend that active agents run `git pull origin main` into their local branches, but do so carefully.
- **Stale Branches**: It is recommended that a human operator periodically inspects remote branches using `git branch -r` and deletes any abandoned branches to prevent agent confusion.
