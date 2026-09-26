---
status: active_snapshot
owner: meta
created: 2026-09-25
authority: current_evidence_snapshot
scope: agency_ecosystem
derived_from:
  - docs/00-meta/source-of-truth.md
  - docs/00-meta/operating-model.md
  - docs/08-plans/master/META_PLAN.md
  - PROJECT_STATE.md
  - docs/07-decisions/index.md
  - noema.project.yaml
  - docs/09-handoffs/AGENCY_SCOPE_SPLIT_CHECKPOINT_PRE_NOEMA_VNEXT_2026-09-25.md
  - docs/09-handoffs/AGENCY_ECOSYSTEM_CONTEXT_HANDOFF_2026-09-25.md
---

# Agency Ecosystem State Map — 2026-09-25

## State legend

- **CANON / APPROVED** — accepted authority.
- **PROPOSED / REVIEW** — useful workbench; not a decision.
- **ACTIVE EXECUTION** — currently advancing under an authorized cursor.
- **BLOCKED** — cannot legitimately progress past a named dependency.
- **DEFERRED** — intentionally postponed.
- **EXTERNAL-EVIDENCE DEPENDENT** — unresolved by desk work.

## Workstream map

| Workstream | State | Authority | Blocking condition / evidence | Next decision |
|---|---|---|---|---|
| Repo governance / operating model | CANON / APPROVED | ADR-0001, ADR-0004, source-of-truth, operating-model | none | keep enforcing authority metadata + PR review |
| Capability-first workstream model | CANON / APPROVED | ADR-0005 | none | substitute executors only on demonstrated capability/cost grounds |
| Agency strategic thesis | PROPOSED / REVIEW | AGENCY_MASTER_PLAN + ADR-0006 | human approval + buyer evidence | approve/reject/mutate working thesis |
| ICP / segment portfolio | PROPOSED / REVIEW | ICP framework + ADR-0007 | founder inputs + access evidence | select validation allocation, not final ICP |
| Entry offer | PROPOSED / REVIEW | offer architecture + ADR-0008 | human approval + payment evidence | decide whether paid diagnostic is validation entry offer |
| Pricing | PROPOSED / REVIEW + EXTERNAL-EVIDENCE DEPENDENT | pricing model + ADR-0009 | WTP evidence | keep ranges provisional until price signal/payment |
| Positioning / AI category rule | PROPOSED / REVIEW | positioning + ADR-0010 | human approval + buyer language | decide working communication constraint |
| Field validation | EXTERNAL-EVIDENCE DEPENDENT | field-kit workbench | no qualified interviews logged; no payment evidence | complete D0 then start buyer contact |
| Proof system | PROPOSED / REVIEW | proof strategy | first delivery/baseline | use method/process proof pre-client; no fabricated social proof |
| Acquisition / sales | PROPOSED / REVIEW, ready for minimum execution | sales/acquisition modules | D0 + chosen validation thesis/segment | launch bounded outreach |
| Delivery OS / client lifecycle | PROPOSED / REVIEW | operations modules | first paid engagement | calibrate against actual hours/rework/runtime |
| Operations / scorecard | PROPOSED / REVIEW | Agency scorecard | live pipeline/delivery data | activate only fields with real observations |
| Brand / DIVINIVID | ACTIVE EXECUTION | approved visual canon + current Brand handoff | human P6 review | Brand workspace owns P6 → final lock → one vertical slice |
| Asset Factory | BLOCKED / REVIEW | approved workstream + ADR-0013/0014/0015; spec draft | mature identity spec + executable matrix + golden pilot | no mass production yet |
| Neutral Technical Foundation | CANON / APPROVED baseline; parallel | ADR-0011 + Issue #4 handoff | Brand values/runtime for production promotion | preserve labs; defer framework and production sanitizer |
| Tooling / automation | PROPOSED / REVIEW | TOOLING_AUTOMATION_REQUIREMENTS | concrete operational need + vendor evaluation | requirements first; no vendor freeze yet |
| CRM / analytics / Workspace | DEFERRED / UNVERIFIED | requirements only | validation workflow/runtime need | choose minimum stack when it directly supports outreach/measurement |
| MVS | PROPOSED validation artifact; NOT EVIDENCED LIVE | WEB_BUSINESS_REQUIREMENTS workbench | provisional copy + minimum credibility need | build only enough to support outreach; do not wait for Brand V1 |
| Brand Vertical Slice | ACTIVE/PLANNED IN BRAND WORKSPACE | Brand scope contract | Final Expression Lock | remains Brand proof, not MVS or production site |
| Production website | DEFERRED / BLOCKED | web requirements workbench | Brand + validated message/offers + runtime/system gates | do not start production build |
| Noema RC0 | CURRENT BASELINE | noema.project.yaml | none | use for recovery/conformance |
| Noema vNext migration | BLOCKED / NOT EXECUTED | pre-vNext checkpoints | migration execution not present in agency repo | migrate later without changing agency domain authority |
| Skill Foundry relationship | CANON relationship / capability reuse | noema.project.yaml + approved reusable skills | only when a genuine reusable capability gap exists | reuse published Skills; do not create agency-specific top-level Skills by default |

## Approved ADR set

`ADR-0001`–`ADR-0005`, `ADR-0011`–`ADR-0015`.

## Proposed ADR set

`ADR-0006`–`ADR-0010`.

## Current buyer / market evidence

Authoritative repository check on 2026-09-25:

- `docs/06-validation/interviews/` contains only `README.md`;
- qualified conversations logged: **0**;
- cleared payments logged: **0**;
- no evidence supports promotion of ICP, offer or pricing hypotheses.

## Actual critical path

`U-01…U-05 → strategy working gate → target list → minimum credibility instruments → outreach → qualified conversations → D4 resonance → D5 cleared payment → delivery → D6 delivery economics`.

The binding uncertainty is **external evidence**, not plan quality.

## Parallel tracks

- Brand completion in dedicated scope;
- Neutral Technical Foundation preservation;
- legal/accounting setup where it unblocks SOW/invoicing;
- minimum MVS/credibility artifact;
- Asset Factory architecture maintenance only, not production.

## Human / external gates

### Human
- U-01…U-05 and D0 recalibration;
- ADR-0006…0010;
- Brand P6 and final Brand promotion.

### External
- buyer contact;
- payment;
- delivery;
- accountant/counsel;
- runtime telemetry.

## Maximum 3 next actions

1. Complete U-01…U-05 + D0 recalibration.
2. Adjudicate ADR-0006…0010, with priority on 0006/0007/0008.
3. Launch the minimum validation loop to first qualified conversations.

Any additional strategy planning before those actions must demonstrate a concrete decision delta; otherwise STOP and execute.
