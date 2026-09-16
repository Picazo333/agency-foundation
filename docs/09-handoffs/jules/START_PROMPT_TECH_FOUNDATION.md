# JULES START PROMPT — NEUTRAL TECHNICAL FOUNDATION

Repository: `Picazo333/agency-foundation`

Preferred execution branch: `tech/jules-technical-foundation`

Governing task: GitHub Issue #4 — Neutral technical foundation + labs — Jules execution.

## Preflight

Before making changes:

1. Confirm the repository is exactly `Picazo333/agency-foundation`.
2. Confirm you are NOT on `main`.
3. Prefer the prepared branch `tech/jules-technical-foundation`. If Jules provisions an isolated task branch, it must start from this branch or an equivalent up-to-date base.
4. Confirm the governance change from PR #10 (`meta: simplify executors and consolidate foundation work on Jules`) is present in the base you are using. If PR #10 has not been merged to `main`, do not start substantive work; report that dependency instead.
5. Sync from the latest `main` using a normal non-destructive merge/update path before substantive edits. If synchronization causes conflicts, stop and report them rather than force-resolving or rewriting history.
6. Confirm the working tree is clean before substantive edits.
7. Read `AGENTS.md`, `PROJECT_STATE.md`, `docs/00-meta/source-of-truth.md`, `docs/08-plans/master/META_PLAN.md`, `docs/08-plans/workstreams/TECH_FOUNDATION_WORKSTREAM.md`, relevant Aesthetic/Functional/System spine rules, the S0–S4 maturity model, relevant security/provenance docs, and Issue #4 in full.
8. Treat older references to Antigravity as historical executor metadata. The current executor is Jules and the capability goal is unchanged.

## Safety and scope

- Never write directly to `main`.
- Never force-push or rewrite history.
- Never merge your own PR.
- Do not modify Brand, naming, ICP, pricing, offer or Strategy decisions.
- Do not build the final production agency website.
- Do not freeze provisional Brand V0 values into permanent components.
- Do not duplicate Issue #6 repo-hardening/CI work except where a narrow technical integration requires it; document overlap explicitly.
- Do not add secrets, real credentials or private environment values.
- Do not mass-upgrade dependencies.
- Every new dependency must include rationale, maintenance/security implications and a removal path.
- Prefer reversible, isolated proofs over premature production architecture.

## Mission

Build a neutral technical foundation that can later receive:

- Brand System V1;
- approved Agency Strategy;
- Web Business Requirements;
- final functional/system specifications;

without requiring avoidable architectural rework.

Work primarily in:

- `labs/`;
- neutral portions of `packages/`;
- `scripts/tech-labs/`;
- experimental/neutral `infra/`;
- relevant technical documentation.

## Required work

1. Neutral design-token schema with all Brand values explicitly TBD.
2. Visual lab isolated from production.
3. SVG lab and validation/optimization/sanitization/componentization proof-of-concept.
4. Motion lab with CSS/SVG/GSAP/scroll experiments only where justified.
5. Interaction lab with clear boundaries from production components.
6. Reduced-motion behavior and accessibility baseline.
7. Performance budget and measurement approach/harness.
8. Visual-regression/screenshot strategy or lightweight prototype.
9. Asset provenance/licensing consumer interface.
10. Security/secrets baseline relevant to future implementation.
11. S0–S4 maturity contract:
   - S0 Visual
   - S1 Interactive
   - S2 Mock Data
   - S3 Backend Wired
   - S4 AI/MCP
12. Entry/exit criteria for every maturity stage.
13. Technical decision notes for experiments with downstream architectural impact.
14. Handoff classification for each significant result: `STABLE_FOUNDATION`, `EXPERIMENTAL`, `REJECTED`, or `BLOCKED_BY_BRAND_STRATEGY`.

## Experiment contract

Every non-trivial experiment must document:

- hypothesis;
- purpose;
- setup;
- files touched;
- dependencies;
- result/evidence;
- performance implications;
- accessibility implications;
- security implications;
- keep/reject/undecided decision;
- rollback/removal path.

Do not install tooling simply because it is popular. Prefer the lightest mechanism that materially controls a real implementation risk.

## Audit before delivery

Review from these perspectives:

1. Principal Frontend / Platform Engineer
2. Performance Engineer
3. Accessibility reviewer
4. Security / dependency-supply-chain reviewer
5. Maintainability / reversibility reviewer
6. Multi-agent collision reviewer
7. Red Team against overengineering, premature architecture and hidden Brand assumptions

Correct material findings before delivery.

## Delivery

1. Review the full changed-file list.
2. Confirm every change belongs to Issue #4.
3. Confirm no Brand/Strategy decisions were silently introduced.
4. Confirm no secrets or destructive automation exist.
5. Record dependencies, tests/benchmarks and removal paths.
6. Commit only on the isolated Jules task branch for this workstream.
7. Open a Pull Request to `main` referencing Issue #4.
8. In the PR separate: `STABLE_FOUNDATION`, `EXPERIMENTAL`, `REJECTED`, `BLOCKED_BY_BRAND_STRATEGY`.
9. Do NOT merge the PR.
