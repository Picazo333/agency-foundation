---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - AGENCY_MASTER_PLAN.md
  - EXECUTIVE_SYNTHESIS.md
---
# Claude / CoWork Handoff — Agency Master Plan

Workstream: `docs/08-plans/workstreams/CLAUDE_MASTER_PLAN_WORKSTREAM.md`
Governing task: **GitHub Issue #2 — plan: Claude / CoWork — complete Agency Master Plan**
Branch: `claude/sharp-gauss-9cso51` (see §9)
Format: `docs/09-handoffs/claude/HANDOFF_TEMPLATE.md`

## Objective completed

Produced the complete decision and execution architecture required to turn the existing research
corpus and founder capabilities into a testable agency model: 21 planning modules, 9 audit passes,
a red-team review, a cross-document integration pass, and 5 ADR proposals — without deciding brand
identity, freezing any commercial claim, or importing unsupported precision from research.

**Entry point:** [`docs/08-plans/master/AGENCY_MASTER_PLAN.md`](../../08-plans/master/AGENCY_MASTER_PLAN.md)
**Read first if deciding:** [`EXECUTIVE_SYNTHESIS.md`](../../08-plans/master/EXECUTIVE_SYNTHESIS.md)
then [`RED_TEAM_REVIEW.md`](../../08-plans/master/RED_TEAM_REVIEW.md)

## Inputs used

`AGENTS.md` · `PROJECT_STATE.md` · `README.md` · `ROADMAP.md` · `RISK_REGISTER.md` ·
`OPEN_QUESTIONS.md` · `PENDING.md` · `docs/00-meta/*` (all) · `docs/01-research/**` (all summaries)
· `docs/07-decisions/*` (ADR-0001…0004) · `docs/08-plans/master/META_PLAN.md` ·
`docs/08-plans/workstreams/*` (all 30) · `docs/09-handoffs/claude/CLAUDE_KICKSTART.md` ·
`docs/03-brand/**` (read only) · GitHub Issue #2.

## Most consequential findings

### 1. Four archetypes are eliminable without any new evidence
Classic agency (portfolio-gated), horizontal AI/automation agency (names the supplier's tools, not
the buyer's problem), standalone consultancy (credential-gated), and white-label (structurally
commoditised). These conclusions do not depend on a single unvalidated number, which makes them the
most reliable content in the plan.

### 2. The craft-led studio is the founder's likely preference and is not viable today
M5 (creative-technology studio) is the best fit for the documented visual direction (`E-07`) and
fails two disqualifiers today: portfolio-gated, and craft quality is not countable inside an
engagement. It is treated as a destination reachable in 18–36 months, with an explicit reopen
condition. **This is the finding most likely to be resisted, and `E-08` — the repository's own rule
that visual taste may not score a market — is what decides it.**

### 3. Access, not strategy quality, is the binding constraint
`E-09` plus `A-06` mean an attractive segment that cannot be reached is worth less than an average
one that can. The plan therefore puts the **access gate at Day 30, before resonance and
monetisation** — an inversion of conventional ICP scoring, made deliberately.

### 4. Proof is the deciding property of the model
The diagnostic captures a baseline in week one, making every engagement a case study by
construction. No other candidate model produces proof this fast, and for a supplier with no
references nothing else is worth as much.

### 5. The founder's aesthetic and the reachable buyer may be in conflict
`E-24`. A sacred/grotesque visual register may suppress trust with conservative clinical buyers.
Proposed resolution is register separation — plain at the door, distinctive at the table — which is
a *hypothesis about buyer reaction*, not a resolution. Routed to H-08 and Gate 1.

### 6. The largest risk in this program is this program
`RT-01`. Twenty-one strategy modules, a full governance system, and zero buyer conversations.
Planning of this quality is a competence trap. A binding stop rule is proposed.

### 7. Discounting is quantitatively equivalent to catastrophic scope failure
A 20% discount destroys as much effective yield as tripling the rework rate
(`PRICING_AND_ECONOMICS_MODEL.md` §8.2). One happens over months; the other in one sentence on a
call.

### 8. High diagnostic conversion is a capacity crisis, not a windfall
At 50% conversion, ten diagnostics generate 1,200 hours against a 780-hour solo ceiling. Success
arrives as a contractor decision.

## Outputs produced

**21 modules** (paths in [`DELIVERABLE_MAP.md`](../../08-plans/master/DELIVERABLE_MAP.md)):
evidence register · strategy reconciliation · agency thesis · decision tree · ICP framework ·
positioning architecture · offer architecture · pricing and economics · proof strategy ·
acquisition system · sales system · client lifecycle · delivery OS · operating model · tooling
requirements · governance/risk/security checklist · agency scorecard · field validation plan ·
brand/business interface · web business requirements · 30/60/90/180/365 roadmap.

**Supporting:** master plan index · executive synthesis · audits (passes 1–8) · red team (pass 9) ·
integration pass · deliverable map · hypothesis register · learning log · this handoff.

**Proposed ADRs:** `ADR-0005` working thesis · `ADR-0006` two-segment portfolio ·
`ADR-0007` paid diagnostic entry offer · `ADR-0008` defer pricing freeze ·
`ADR-0009` AI as mechanism not category.

**Updated:** `RISK_REGISTER.md` (+6 rows) · `OPEN_QUESTIONS.md` · `PROJECT_STATE.md` ·
`CHANGELOG.md` · `docs/07-decisions/index.md`.

## Proposed decisions vs observed facts

| Proposed decision (requires approval) | Observed fact it rests on |
|---|---|
| Adopt M8 as working thesis | `E-17`, `E-18` (`SIGNAL`); the rest is `INFERENCE` |
| Multi-site clinic groups as primary candidate | `E-19` (`SIGNAL`) only; all bands are `INFERENCE` |
| Paid diagnostic as entry offer | **No supporting evidence.** `A-07`, low confidence, tested by H-01 |
| The price ranges | **No supporting evidence.** All `INFERRED RANGE` (`E-22`) |
| 40% recurring attachment | **No supporting evidence.** `A-11` |
| AI as mechanism not category | `E-17` (`SIGNAL`) + `E-07` (`FACT`, anti-profile) |

**Observed facts used throughout:** `E-01`–`E-15`, principally `E-02` (no primary sources),
`E-09` (zero buyer contact), `E-12` (working governance system), `E-07` (documented visual
direction).

## Assumptions requiring validation

18 assumptions (`A-01`–`A-18`) and 12 unknowns (`U-01`–`U-12`) are registered with confidence bands,
breakage consequences and calibration routes. The five that gate the most:

| ID | Assumption | Resolved by |
|---|---|---|
| `A-07` | Buyer pays for diagnosis | H-01, day 60 |
| `A-11` | 40% recurring attachment | H-09, day 180 |
| `A-13` | 20% rework | Measured from engagement 1 |
| `U-03` | Runway and minimum draw | **Founder, this week** |
| `U-04` | Warm network | **Founder, this week** |

## Unresolved conflicts

| ID | Conflict | Status |
|---|---|---|
| C-01 | Founder aesthetic vs conservative buyer trust | **Unresolved.** → H-08, Gate 1 |
| C-02 | Vertical focus vs option value | **Unresolved by design.** Review at D8 |
| C-03 | Diagnostic bootstrap circle | **Partially resolved** by the free teardown rung; residual → H-01 |
| C-04 | BOLD anti-AI vs AI as the founder's fastest lever | **Resolved** by `ADR-0009` |
| C-05 | Two deliverable-name contracts | **Resolved** via `DELIVERABLE_MAP.md`; see §8 |
| C-06 | Kickstart cites non-existent research files | **Not resolvable in scope**; see §8 |

## Dependencies on Brand V0

| Need | Blocking? |
|---|---|
| Brand V0 for Gate 1 | No — Gate 1 slips, the business does not |
| Brand V1 for the production website | Yes, for the site only |
| Interim typographic system for the method document | **No** — a competent default is used |
| A name | **No** — validation runs without one |

> **Explicit:** market validation requires no brand asset at all. Delaying outreach for brand
> readiness would be the over-planning failure mode (`RT-01`), not professionalism.

## Dependencies created

| For | What |
|---|---|
| Brand workstream | 10 commercial requirements (`BR-1`–`BR-10`) and 10 constraints (`BC-01`–`BC-10`); 8 proposed Gate 1 test criteria; H-08 evidence requirement |
| Technical workstream | `WEB_BUSINESS_REQUIREMENTS.md` — MVS spec (week 3), production gates G-W0–G-W5, spine and `S0→S4` mapping |
| Human owner | 5 ADR decisions; 5 founder questions; 2 professional engagements ⚖️ |
| Gemini / asset factory | None. Unchanged, still blocked on Brand V1 |

## Files changed

**Created (35):** 21 modules · 6 master-level supporting documents (index, executive synthesis,
audits, red team, integration pass, deliverable map) · 2 validation registers · 5 ADR proposals ·
this handoff.
**Modified (5):** `RISK_REGISTER.md` · `OPEN_QUESTIONS.md` · `PROJECT_STATE.md` · `CHANGELOG.md` ·
`docs/07-decisions/index.md`.

Full inventory: `DELIVERABLE_MAP.md`.

## Intentionally NOT changed

| Area | Why |
|---|---|
| `docs/03-brand/**` | Brand workstream owns it. Task brief: do not modify Brand canon. **Zero files touched** |
| `docs/01-research/**` | Research workstream; read-only input |
| `docs/00-meta/**` | Canon owned by meta; includes `operating-model.md`, whose name the new `docs/04-operations/OPERATING_MODEL.md` resembles |
| `docs/05-product-web/**` | Technical workstream; and its READMEs state it is populated after convergence |
| `docs/08-plans/workstreams/**` | Canon. The deliverable-name conflict (C-05) is recorded in `DELIVERABLE_MAP.md` rather than by editing a canonical spec |
| `apps/`, `packages/`, `labs/`, `infra/`, `scripts/`, `asset-factory/`, `assets/` | Other workstreams |
| `PENDING.md`, `FOUNDATION_BASELINE_REPORT.md` | Not in scope |
| `.github/**`, `.env.example`, `.gitignore` | Not in scope |
| ADR-0001…0004 | No FROZEN or APPROVED decision altered |

**No code, no dependencies, no configuration, no secrets.** This change is documentation only.

## Risks / gaps

| Gap | Severity |
|---|---|
| **No primary research available** (`E-02`) — every conclusion rests on synthesis summaries plus structural reasoning | High |
| **Every price is an `INFERRED RANGE`** — no market pricing data exists | High |
| **Segment analysis is desk reasoning**, not field research | High |
| **No legal or tax conclusions** — only questions, routed to professionals ⚖️ | Medium, by design |
| **Buying-committee model is inferred** (`U-09`) | Medium |
| **Delivery hour estimates are constructed**, not measured | Medium |
| **Founder context unknown** (`U-01`–`U-05`) | High, and cheap to fix |

Per `NO_SILENT_DOWNGRADE.md`, these are stated rather than concealed:
`INTEGRATION_PASS.md` §8 carries the full list.

## Validation performed

| Check | Result |
|---|---|
| All Issue #2 deliverables exist | ✅ 23/23 |
| Relative markdown links resolve | ✅ 0 broken |
| Backtick file references resolve | ✅ 0 unresolved |
| Front-matter present on every new file | ✅ |
| Secret scan | ✅ 0 (3 matches reviewed: security-policy text) |
| Numeric consistency across modules | ✅ after 5 corrections (`INTEGRATION_PASS.md` §3) |
| Ownership boundaries | ✅ `DELIVERABLE_MAP.md` §5 |
| Brand canon untouched | ✅ `git status` on `docs/03-brand/` |
| 9 audit passes completed | ✅ 35 findings: 23 applied, 8 accepted, 4 open |

## Items for the human owner beyond the ADRs

1. **`CLAUDE_MASTER_PLAN_WORKSTREAM.md` names deliverables that Issue #2 superseded** (C-05). The
   canonical spec may want updating; that is a canon change and was not made here.
2. **`CLAUDE_KICKSTART.md` "Read first" items 10–12 reference research files that do not exist**
   (C-06): `BOLD_STRATEGIC_INPUT.md`, `SPARK_RESEARCH_GUARDRAILS.md`,
   `WEB_IMPLEMENTATION_RESEARCH_SYNTHESIS.md`. The curated summaries were used instead. Either the
   files should be imported or the kickstart corrected.
3. **The task brief for this run referenced `docs/09-handoffs/claude/START_PROMPT.md`, which does
   not exist.** `CLAUDE_KICKSTART.md` was treated as the equivalent contract.
4. **`docs/04-operations/OPERATING_MODEL.md` resembles `docs/00-meta/operating-model.md` in name.**
   The filename is fixed by the Issue #2 contract and disambiguated in the document header;
   renaming is a human decision.
5. **`E-02` — the raw research archives are still not in the repository.** This caps the evidence
   grade of everything downstream and is already tracked in `PENDING.md`.

## Recommended next action

1. Read `EXECUTIVE_SYNTHESIS.md`, then `RED_TEAM_REVIEW.md`.
2. Answer `U-01`–`U-05` (one sitting).
3. Approve, amend or reject `ADR-0005`–`ADR-0009`.
4. Engage an accountant and a commercial lawyer ⚖️.
5. **Begin outreach within seven days.** Not after Brand V1, not after the website, not after more
   planning.
6. Activate the stop rule: no further strategic planning artifact until 10 qualified buyer
   conversations are logged.

## Definition-of-Done evidence

Against `docs/00-meta/definitions-of-done.md`, "Strategic plan":

| Criterion | Evidence |
|---|---|
| Assumptions explicit | 18 assumptions with confidence bands and calibration routes |
| Evidence dependencies explicit | 26 graded evidence items; 12 unknowns routed |
| Kill criteria and validation plan included | 12 hypotheses; 7 gates; explicit kill path with a 7-day ADR deadline |
| Does not silently freeze unvalidated claims | Every file `status: review`; 5 ADRs `PROPOSED`; `ADR-0008` prohibits publishing any price |

Against `CLAUDE_KICKSTART.md` "Definition of Done" and Issue #2 §"Required Master Outputs":
see `AGENCY_MASTER_PLAN.md` §8.
