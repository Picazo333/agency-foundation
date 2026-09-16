# START PROMPT — Claude / CoWork Complete Agency Master Plan

Work only in repository `Picazo333/agency-foundation` and only on branch `plan/claude-master-agency`.

Your governing task is GitHub Issue #2: `plan: Claude / CoWork — complete Agency Master Plan`.

## NON-NEGOTIABLE REPO SAFETY

1. NEVER work directly on `main`.
2. NEVER force-push, rewrite Git history, delete unrelated files, or overwrite work owned by another branch/workstream.
3. Do not modify or freeze Brand naming/visual canon. Brand is owned by the separate Brand workstream.
4. Do not commit secrets, credentials, tokens, private keys or real `.env` values.
5. Do not mass-upgrade dependencies or make unrelated code changes.
6. Before writing, confirm you are on `plan/claude-master-agency` and inspect the repository state.
7. If the branch is behind `main`, sync non-destructively if your environment supports it. Never discard existing branch work to do so.
8. All substantive work must stay on this branch and finish as a PR to `main`.
9. Treat existing files according to authority: research is evidence/input, workbench is exploratory, canon/approved decisions have higher authority. Do not silently promote hypotheses to facts.
10. If two sources conflict, preserve the conflict and explain it; do not manufacture reconciliation.

## READ FIRST

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

## MISSION

Build the most complete planning architecture possible for turning this project from its current research/brand-exploration state into a serious, launchable, operable and scalable agency/business.

This is NOT a short business plan, executive summary, generic consulting memo or brainstorm.

It must become the master planning layer from which later agents and humans can execute the agency.

Do not optimize for brevity. Optimize for:
- decision completeness;
- actionability;
- traceability;
- explicit dependencies;
- falsifiability;
- risk visibility;
- operational realism;
- sequencing;
- non-regression;
- clear ownership;
- concrete definitions of done.

Every section should do at least one of the following:
- support or reject a decision;
- define a future execution contract;
- expose an important risk;
- define evidence still required;
- specify a measurable gate;
- identify a dependency or critical path.

Do not pad with generic agency advice.

## STRATEGIC REQUIREMENT: RECONCILE BEFORE COMMITTING

Do NOT assume the correct company is a generic AI/automation agency because that was the starting idea.

Perform Strategy Reconciliation first. Compare at minimum:
- classic multidisciplinary agency;
- AI/automation agency;
- productized boutique;
- consultancy-led model;
- creative-technology / systems studio;
- vertical specialist;
- plausible hybrid models discovered in the evidence.

Treat the BOLD research as a contrarian/falsification input, not predetermined truth.
Treat Spark research according to actual evidence quality; downgrade unsupported precision.

For material claims use a discipline such as:
`VERIFIED FACT / OBSERVED SIGNAL / INFERENCE / HYPOTHESIS / UNKNOWN`.

Do not convert modeled economics into observed facts.

## REQUIRED SCOPE

Execute the complete scope in Issue #2, including at minimum:

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

Also identify anything an experienced agency founder, COO, CFO, sales leader, delivery lead or procurement buyer would insist on that is missing from the current corpus. Add it if it materially improves execution readiness.

## REQUIRED OUTPUT QUALITY

The output must be deep enough that later workers can execute modules without reopening foundational reasoning from scratch.

For every major recommendation include where appropriate:
- rationale;
- evidence level;
- assumptions;
- alternatives considered;
- dependencies;
- downside/risk;
- validation method;
- decision or kill gate;
- owner/workstream;
- what can run in parallel;
- what blocks downstream work.

Use structured tables, decision trees, matrices, process maps and checklists when they improve execution clarity.

Where exact values are unknown, build a model or a range and label it as a hypothesis. Never manufacture certainty.

## OUTPUT FILES

Create the full set specified in Issue #2. At minimum it must include:

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
- one final executive synthesis explaining what is DECIDED, PROVISIONAL, BLOCKED, NEEDS VALIDATION and NEXT.

Organize files under the existing strategy/operations/validation/planning structure rather than creating a disconnected parallel documentation tree.

## AUTONOMY

Do not stop for routine human checkpoints.

Continue through all phases until the Issue #2 Definition of Done is met.

Only stop if a true fatal blocker prevents meaningful progress. Uncertainty is not a fatal blocker: record it as an assumption or validation requirement and continue.

## MANDATORY FINAL AUDITS

Before delivery, independently re-read and challenge the whole plan from these roles:

1. Experienced agency founder.
2. B2B GTM strategist.
3. COO/operator.
4. CFO/unit-economics reviewer.
5. Sales leader.
6. Delivery/quality lead.
7. Security/privacy/risk reviewer.
8. Skeptical enterprise/professional-services buyer or procurement reviewer.
9. Red Team whose job is to prove the proposed business should not exist.

Resolve contradictions where the evidence allows it. Otherwise record the contradiction and its required test.

Then perform one final integration pass checking:
- no major lifecycle stage is missing;
- documents do not contradict each other silently;
- dependencies and critical path are explicit;
- downstream Brand/Asset/Technical workstreams know what they need from this plan;
- unsupported numerical precision is removed or labeled;
- no final naming or visual-brand decision has been taken on behalf of the Brand workstream.

## DELIVERY

1. Commit all work only to `plan/claude-master-agency`.
2. Validate files, internal links and document references.
3. Review `git diff`/changed files before delivery and verify there are no unrelated changes or secrets.
4. Open a Pull Request from `plan/claude-master-agency` to `main` referencing Issue #2.
5. Do NOT merge your own PR.
6. In the PR summarize:
   - strategic model(s) recommended for validation;
   - decisions proposed;
   - assumptions/hypotheses still requiring field evidence;
   - unresolved contradictions;
   - critical risks;
   - files changed;
   - tests/validation performed;
   - human decisions required before merge;
   - immediate next workstreams after approval.

Completion means a human can review one PR and understand the proposed architecture of the entire agency from strategy through launch and operating system.