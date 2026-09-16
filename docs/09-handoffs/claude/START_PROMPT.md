# START PROMPT — Claude / CoWork Complete Agency Master Plan

Work only in repository `Picazo333/agency-foundation` and only on branch `plan/claude-master-agency`.

Your governing task is GitHub Issue #2: `plan: Claude / CoWork — complete Agency Master Plan`.

## 0. PRE-FLIGHT — DO THIS BEFORE ANY WRITE

1. Verify the repository is exactly `Picazo333/agency-foundation`.
2. Verify the current branch is exactly `plan/claude-master-agency`.
3. Inspect branch status and changed files before editing.
4. Read `AGENTS.md`, `PROJECT_STATE.md`, source-of-truth rules and Issue #2 before planning.
5. If the branch is behind `main`, update only through a safe, non-destructive fast-forward/rebase/merge supported by the environment and only if there is no risk of losing branch work. If not safe, continue on the branch and record the divergence in the PR.
6. Do not start if the environment would require direct writes to `main`.

## 1. NON-NEGOTIABLE REPO SAFETY

- NEVER work directly on `main`.
- NEVER force-push, rewrite Git history, use destructive resets/clean commands, bulk-delete unrelated files, or run repo-wide search/replace without an explicit scoped reason.
- Do not overwrite work owned by another branch/workstream.
- Do not modify or freeze Brand naming/visual canon. Brand is owned by the Brand workstream.
- Do not commit secrets, credentials, tokens, private keys or real `.env` values.
- Do not mass-upgrade dependencies or make unrelated code changes.
- Do not execute or trust arbitrary scripts/binaries from research or asset folders merely because they exist.
- Do not upload repository content to external services unless the task explicitly requires it and the material is appropriate to share.
- Treat research as evidence/input, workbench as exploratory and canon/approved ADRs as higher authority.
- If sources conflict, preserve and explain the conflict; never manufacture reconciliation.
- Finish only through a PR to `main`; do not merge your own PR.

## 2. WRITE BOUNDARIES / COLLISION CONTROL

Primary writable areas:
- `docs/02-strategy/`
- `docs/04-operations/`
- `docs/06-validation/`
- `docs/08-plans/`
- `docs/09-handoffs/claude/`
- risk/open-question files only where the existing governance explicitly permits updates.

Treat as read-only unless a tiny, directly necessary correction is unavoidable and explicitly disclosed in the PR:
- `docs/03-brand/`
- `asset-factory/`
- `labs/`
- `packages/`
- `.github/`
- Antigravity/Jules handoff folders.

If another active branch owns a file, do not edit it. Instead create a dependency note or proposed change in the Claude handoff.

## 3. READ FIRST

Read in this order before creating the plan:

1. `AGENTS.md`
2. `PROJECT_STATE.md`
3. `README.md`
4. `docs/00-meta/source-of-truth.md`
5. `docs/00-meta/operating-model.md`
6. `docs/00-meta/dependency-map.md`
7. `docs/08-plans/master/META_PLAN.md`
8. `docs/08-plans/workstreams/CLAUDE_MASTER_PLAN_WORKSTREAM.md`
9. GitHub Issue #2 in full
10. relevant research under `docs/01-research/`
11. relevant decisions/ADRs under `docs/07-decisions/`
12. Brand workbench only as provisional context, never as commercial truth.

## 4. MISSION

Build the most complete planning architecture possible for turning this project from its current research/brand-exploration state into a serious, launchable, operable and scalable agency/business.

This is NOT a short business plan, executive summary, generic consulting memo or brainstorm.

It must become the master planning layer from which later agents and humans can execute the agency without repeatedly reopening foundational reasoning.

Do not optimize for brevity. Optimize for:
- decision completeness;
- actionability;
- traceability;
- explicit dependencies;
- falsifiability;
- risk visibility;
- operational realism;
- sequencing;
- parallelization;
- non-regression;
- clear ownership;
- concrete definitions of done.

Every major section must do at least one of the following:
- support/reject a decision;
- define a future execution contract;
- expose a material risk;
- define evidence still required;
- specify a measurable gate;
- identify a dependency, blocker or critical path.

No filler or generic agency advice.

## 5. STRATEGY RECONCILIATION BEFORE COMMITMENT

Do NOT assume the correct company is a generic AI/automation agency because that was the starting idea.

Compare at minimum:
- classic multidisciplinary agency;
- AI/automation agency;
- productized boutique;
- consultancy-led model;
- creative-technology / systems studio;
- vertical specialist;
- plausible hybrid models supported by evidence.

Treat BOLD as contrarian/falsification input, not predetermined truth.
Treat Spark according to actual evidence quality and downgrade unsupported precision.

Classify material claims as:
`VERIFIED FACT / OBSERVED SIGNAL / INFERENCE / HYPOTHESIS / UNKNOWN`.

Modeled economics are never observed facts.

## 6. COMPLETE REQUIRED SCOPE

Execute the full Issue #2 scope end-to-end, covering at minimum:

1. Evidence and research reconciliation.
2. Agency thesis and category architecture.
3. ICP/buyer architecture and selection logic.
4. Positioning and strategic messaging requirements.
5. Full offer ladder: entry/core/expansion/recurring/optional + DO-NOT-SELL.
6. Pricing, unit economics, capacity, cash-flow and scenario modeling.
7. Proof/portfolio/trust system for a new agency.
8. Acquisition/marketing channel portfolio and sequencing.
9. Sales operating system from lead to close/lost learning.
10. Complete client lifecycle and delivery operating system.
11. Operations/organization design and founder-to-team transition.
12. Tooling, automation and internal-systems requirements.
13. Governance, contracts/IP/privacy/security/legal/accounting review checklist.
14. Agency KPI/scorecard and management cadence.
15. Field validation system with hypotheses, tests, thresholds and kill criteria.
16. Brand/Business interface requirements without choosing final Brand identity.
17. Website/digital-presence business requirements using Aesthetic / Functional / System spines and S0–S4 maturity.
18. Dependency-aware 30/60/90/180/365 roadmap from current state to launch and scale.

Also identify anything an experienced agency founder, COO, CFO, sales leader, delivery lead, legal/risk reviewer or skeptical buyer would insist on that is materially missing from the current corpus.

## 7. DEPTH CONTRACT FOR EVERY MAJOR MODULE

Where applicable, every major module must explicitly contain:
- current-state summary;
- decision question;
- viable options;
- evidence and evidence quality;
- recommendation or working hypothesis;
- what would falsify it;
- dependencies;
- risks/downside;
- validation plan;
- owner/workstream;
- inputs;
- outputs;
- Definition of Done;
- what can run in parallel;
- what blocks downstream work;
- human decisions still required.

Avoid arbitrary numeric scoring when evidence does not support precision. Use qualitative or range-based reasoning when more honest.

## 8. REQUIRED OUTPUT FILES

Create the complete set specified in Issue #2. At minimum:

- `AGENCY_MASTER_PLAN.md`
- `STRATEGY_RECONCILIATION.md`
- `EVIDENCE_AND_ASSUMPTIONS_REGISTER.md`
- `DECISION_TREE.md`
- `ICP_FRAMEWORK.md`
- `POSITIONING_ARCHITECTURE.md`
- `OFFER_ARCHITECTURE.md`
- `PRICING_AND_ECONOMICS_MODEL.md`
- `PROOF_STRATEGY.md`
- `ACQUISITION_MARKETING_SYSTEM.md`
- `SALES_SYSTEM.md`
- `CLIENT_LIFECYCLE.md`
- `DELIVERY_OS.md`
- `OPERATING_MODEL.md`
- `TOOLING_AUTOMATION_REQUIREMENTS.md`
- `GOVERNANCE_RISK_SECURITY_CHECKLIST.md`
- `AGENCY_SCORECARD.md`
- `FIELD_VALIDATION_PLAN.md`
- `BRAND_BUSINESS_INTERFACE.md`
- `WEB_BUSINESS_REQUIREMENTS.md`
- `30_60_90_180_365_ROADMAP.md`
- updated risks/open questions where justified
- one executive synthesis separating `DECIDED / PROVISIONAL / BLOCKED / NEEDS VALIDATION / NEXT`.

Use the existing strategy/operations/validation/planning structure; do not create a disconnected parallel documentation tree.

## 9. CONSISTENCY / TRACEABILITY REQUIREMENTS

- Cross-reference dependent documents.
- Maintain one shared assumptions vocabulary.
- Keep ICP, offer, pricing, sales, delivery and economics internally consistent.
- Every strategic recommendation must be traceable to evidence or explicitly labeled as a hypothesis.
- Make contradictions visible rather than smoothing them away.
- Identify the critical path and parallelizable workstreams.
- Identify which outputs become inputs for Brand V1, Gemini Asset Factory and technical implementation.

## 10. AUTONOMY

Do not stop for routine checkpoints.
Continue until Issue #2 Definition of Done is met.
Uncertainty is not a blocker: record it as assumption/unknown/validation requirement and continue.
Only stop on a true fatal blocker that prevents meaningful progress.

## 11. MANDATORY FINAL AUDITS

Independently challenge the complete plan as:
1. experienced agency founder;
2. B2B GTM strategist;
3. COO/operator;
4. CFO/unit-economics reviewer;
5. sales leader;
6. delivery/quality lead;
7. security/privacy/risk reviewer;
8. skeptical buyer/procurement reviewer;
9. Red Team trying to prove the proposed business should not exist.

Then perform one integration pass checking:
- lifecycle completeness;
- internal consistency;
- explicit dependencies/critical path;
- realistic parallelization;
- unsupported numerical precision;
- downstream handoff readiness;
- no unauthorized Brand decisions;
- no repo-safety violations.

## 12. EXIT / PR CHECKLIST

Before opening the PR:
1. Inspect the complete changed-file list.
2. Confirm every changed file is inside the allowed scope or explicitly justify any exception.
3. Confirm no secrets/credentials/private material were added.
4. Validate internal links/references where practical.
5. Confirm no unrelated formatting churn or mass rewrites.
6. Confirm no files owned by other active workstreams were overwritten.
7. Commit only to `plan/claude-master-agency`.
8. Open a PR to `main` referencing Issue #2.
9. Do NOT merge your own PR.

PR summary must include:
- strategic model(s) proposed for validation;
- decisions proposed;
- hypotheses requiring field evidence;
- unresolved contradictions;
- critical risks;
- files changed;
- validation performed;
- human decisions required before merge;
- immediate next workstreams after approval;
- any cross-branch dependencies/collision risks.

Completion means a human can review one PR and understand the proposed architecture of the entire agency from strategy through launch and operating system.