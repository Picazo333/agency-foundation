---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - AGENCY_THESIS.md
  - ICP_FRAMEWORK.md
  - POSITIONING_ARCHITECTURE.md
---
# Offer Architecture

> **Module 7 of the Agency Master Plan** (Issue #2 Phase 5). Specifies the ladder, every offer as an
> execution contract, and the explicit `DO NOT SELL` register.
> Prices live in `PRICING_AND_ECONOMICS_MODEL.md`; every figure there is an `INFERRED RANGE` (`E-22`).

## 1. Ladder

```text
  L0  TEARDOWN            free, async, ≤3h    →  demonstrates competence, creates the reason to talk
  L1  DIAGNOSTIC          paid, 2–3 weeks     →  ENTRY. Buys access, funds qualification, captures baseline
  L2  CORE BUILD          fixed, 4–8 weeks    →  PRIMARY REVENUE. Produces the countable outcome
  L3  OPERATED            monthly, 6-mo term  →  RECURRING. Retains measurement, creates expansion surface
  L4  EXPANSION           fixed, 1–3 weeks    →  HIGHEST EFFECTIVE MARGIN. Zero acquisition cost
  L5  CUSTOM              time-boxed          →  CAPPED EXCEPTION. Not a growth path
```

Design rules, each of which costs something:

1. **Every rung must stand alone.** A buyer who stops after L1 must have received full value. If
   L1 is only useful as a lead-in to L2, it is a sales pitch with an invoice, and buyers detect
   that immediately.
2. **Each rung lowers the perceived risk of the next.** Risk descends as price ascends, which is the
   inverse of how most agencies sell.
3. **No rung may be skipped upward without a written exception.** Selling L2 without L1 means
   quoting a fix for an unmeasured problem — the failure mode that produces scope overrun (`A-13`)
   and unprovable outcomes (`RF-5`). Permitted only under §7.
4. **Every rung captures proof** (`DELIVERY_OS.md` §8).
5. **The ladder must survive the buyer stopping at any rung.** Revenue concentration in L2 is
   accepted at month 3 and is a structural problem by month 18 — see `AGENCY_THESIS.md` §5.

## 2. L0 — Teardown *(free, bounded)*

Added in response to audit finding `AUD-01-01` and the bootstrap objection `C-03`: a paid
diagnostic requires credibility that the diagnostic is meant to create. L0 breaks the circle by
demonstrating competence before asking for money.

| Field | Specification |
|---|---|
| Target problem | Buyer has no reason to believe an unknown supplier is competent |
| ICP | S2 primary, S7 hedge |
| Scope | Asynchronous review of publicly observable surfaces: enquiry paths, response latency measured by actually contacting them as a prospect, booking friction, cross-location consistency, tracking presence |
| **Exclusions** | No access to their systems. No custom analysis. No live meeting. No written recommendations beyond observations |
| Inputs required | None — deliberately zero-friction |
| Deliverables | 5–8 minute recorded walkthrough + one-page observation summary |
| Milestones | Single delivery |
| Duration | **Hard cap 3 hours** including recording |
| Dependencies | Templated checklist and recording setup (built once, Week 2) |
| Acceptance | Delivered; no client acceptance concept |
| Revisions | None |
| Proof captured | The teardown library itself (anonymised) becomes a marketing asset |
| Support burden | Zero |
| Upsell path | → L1. Explicit close: *"This is what's visible from outside. The diagnostic measures what's actually happening inside."* |
| Productization | High — 80% templated after ~5 iterations |

**The danger, stated:** L0 is unpaid labour that scales linearly with outreach. If conversion from
L0 to L1 is below ~15% after 10 teardowns, L0 is consuming the capacity that should be producing
revenue. **Stop-rule: reassess at 10 teardowns** (`AGENCY_SCORECARD.md` metric M-04).

## 3. L1 — Revenue Operations Diagnostic *(entry offer)*

The load-bearing offer of the entire model.

| Field | Specification |
|---|---|
| **Target problem** | The buyer knows revenue is being lost but cannot say where, how much, or what to fix first |
| **ICP** | S2 (3–15 locations); S7 variant |
| **Scope** | (a) Map the full enquiry→booking→attendance path across channels and locations; (b) instrument it where measurement is missing; (c) measure 2–4 weeks of real activity or reconstruct from existing records; (d) quantify loss at each stage in currency; (e) rank remediation by value/effort; (f) price 2–3 bounded build options |
| **Exclusions** | No implementation. No changes to live systems beyond read-only tracking. No clinical/patient-record access (`RF-7`). No creative work. No ad account management (`RF-2`). No staff interviews beyond 3 |
| **Client inputs required** | Read access to booking system, CRM/spreadsheet, web analytics, ad accounts (read-only), enquiry channels; 60 min with the operations lead; 30 min with the signer; permission to contact the business as a mystery prospect |
| **Deliverables** | 1. Measured current-state map. 2. Quantified loss table by stage, with method and confidence stated per line. 3. Prioritised remediation list. 4. 2–3 priced build options with scope and exclusions. 5. **The instrumentation itself, in the client's own accounts, retained whether or not they proceed.** 6. 45-minute findings walkthrough |
| **Milestones** | M1 kickoff + access (day 1–2) · M2 instrumentation live (day 3–5) · M3 measurement window (day 6–15) · M4 findings review (day 16–18) |
| **Duration** | 2–3 weeks, bounded by the measurement window |
| **Dependencies** | Client access within 5 business days — **if not met, the engagement pauses and the clock stops**; this is written into the SOW |
| **Acceptance criteria** | Findings delivered with method disclosed; instrumentation verified functional in client accounts; every quantified figure traceable to a named data source or explicitly marked as an estimate |
| **Revisions** | One round of clarification within 10 days. Additional analysis is a change order |
| **Proof captured** | The baseline — the single most valuable artifact in the model. Anonymised benchmark fields (`AGENCY_THESIS.md` §4.2), consented in the MSA |
| **Support burden** | Near zero after delivery |
| **Cross-sell** | → L2, with **50% of the diagnostic fee credited against a build contracted within 30 days** |
| **Productization** | Very high. Target: 70% templated by the third delivery |

### 3.1 Why the credit is 50% and not 100%

Audit finding `AUD-04-01`. A 100% credit makes the diagnostic free-with-extra-steps: it destroys
margin exactly when conversion is *good*, and it teaches the buyer that the diagnosis had no
independent value — which contradicts design rule 1. A 50% credit, time-boxed to 30 days, preserves
the standalone value claim, creates genuine urgency, and keeps the diagnostic roughly cost-neutral
in both conversion outcomes.

### 3.2 The no-baseline path

`U-08`/`P-1` may fail: many SMBs have no usable historical data. Audit finding `AUD-06-01`. If
discovery reveals no baseline is reconstructable:

- **O-0 Instrumentation Sprint** is sold first: 1 week, priced at roughly one third of L1, purely
  to install measurement. The measurement window then runs 3–4 weeks before L1 findings.
- Total time to findings extends to 5–6 weeks. This must be said at the point of sale.
- **`RF-8` still applies:** if the client will not instrument, there is no engagement. This
  disqualification will lose deals, and losing them is correct — an unmeasurable engagement
  produces no proof, no renewal argument and no case study.

## 4. L2 — Core builds

Three defined products. **Only C-1 and C-2 may be sold before three engagements are delivered**
(`DECISION_TREE.md` D8); C-3 is a post-repeatability offer.

### C-1 — Conversion Path Rebuild

| Field | Specification |
|---|---|
| Target problem | Enquiries arrive and are lost before booking: slow response, fragmented channels, friction at the booking step |
| ICP | S2, S7 |
| Scope | Unified enquiry intake across channels; routing and ownership rules; response-time SLA automation; booking-path rebuild (landing/booking surface); confirmation and reminder sequences; measurement dashboard; staff training |
| Exclusions | Full website redesign; brand identity work; ad creative; PMS/EMR data migration; clinical-record integration (`RF-7`); anything not named in the SOW |
| Client inputs | Named project owner with ≥2h/week; content and credentials within 10 days; staff availability for 2 training sessions; sign-off within 3 business days per gate |
| Deliverables | Working intake and routing system; rebuilt booking path; automated sequences; live dashboard; runbook documentation; 2 training sessions; 30-day post-launch monitoring |
| Milestones | W1 discovery+design · W2–3 build · W4 internal QA + client review · W5 staff training + launch · W6 stabilisation and measurement |
| Duration | 4–6 weeks |
| Dependencies | L1 completed (baseline exists); client inputs on schedule — slippage moves the date, not the price |
| Acceptance | Every SOW line demonstrated in a recorded walkthrough; dashboard reporting against the L1 baseline; runbook delivered; training completed |
| Revisions | 2 rounds inside defined gates. Outside the gates or outside scope → change order (`DELIVERY_OS.md` §6) |
| Proof captured | Before/after on named metrics from the L1 baseline; testimonial request at day 30; case-study consent in the MSA |
| Support burden | 30 days included, then L3 or lapse. **An unsupported automated system degrades silently** — this is the main argument for L3, and it is honest, not a sales tactic |
| Cross-sell | → L3 (offered at day 21, not day 30 — see §6.1); → L4 per location |
| Productization | High after 3 deliveries |

### C-2 — Revenue Operations Build

| Field | Specification |
|---|---|
| Target problem | Demand is captured but not managed: no pipeline visibility, no follow-up discipline, no attribution |
| ICP | S2 multi-location, S7 |
| Scope | CRM configuration or rebuild; pipeline stages and required fields; lead-source attribution; follow-up and reactivation automation; no-show recovery; per-location reporting; management scorecard; documentation and training |
| Exclusions | CRM licence costs; historical data cleansing beyond 1 import pass; custom software; finance-system integration; clinical records (`RF-7`) |
| Client inputs | CRM admin access; data export; named owner; stage definitions agreed in W1 |
| Deliverables | Configured CRM; automation suite; attribution reporting; management scorecard; data dictionary; runbook; 2 training sessions; 30-day monitoring |
| Milestones | W1 process mapping + stage design · W2–3 configuration + automation · W4 data migration + QA · W5 training + go-live · W6 stabilisation |
| Duration | 5–7 weeks |
| Dependencies | L1; a decision on the CRM platform in W1 — **delay here is the top schedule risk** |
| Acceptance | Pipeline reporting reconciles against the client's own booking records within an agreed tolerance; automations verified; training completed |
| Revisions | 2 rounds; data re-imports beyond the first are change orders |
| Proof captured | Pipeline visibility before/after; follow-up compliance rate; reactivation revenue |
| Support burden | Higher than C-1 — CRM systems drift with staff turnover. Strengthens the L3 case |
| Cross-sell | → L3; → C-1 if not already delivered; → L4 |
| Productization | Medium-high; platform variance is the limiting factor. **Mitigation: support at most two CRM platforms.** Supporting five destroys repeatability |

### C-3 — Full Commercial System *(locked until D8)*

C-1 + C-2 delivered together with a unified measurement layer. 8–10 weeks.

**Locked because:** selling a 10-week engagement before either component has been delivered three
times converts estimation error into a margin catastrophe and a reference risk simultaneously.
Unlocked by `DECISION_TREE.md` D8 (≤±25% delivery variance across 3 engagements).

## 5. L4 — Expansion offers

Sold only to delivered clients. **Structurally the most profitable revenue in the model**: no
acquisition cost, no trust cost, no discovery cost, known systems.

| ID | Offer | Duration | Notes |
|---|---|---|---|
| X-1 | Additional location rollout | 1–2 weeks | Near-pure margin; the strongest argument for the S2 multi-site ICP |
| X-2 | Second service line / specialty path | 1–2 weeks | — |
| X-3 | Reactivation campaign system | 2 weeks | Fast, countable, excellent case-study material |
| X-4 | Internal ops tool (rota, inventory, referral tracking) | 2–4 weeks | **Scope-creep risk**: this is custom software wearing a product's name. Must have a hard change-order boundary |
| X-5 | Proof/content engine (review capture, testimonial pipeline, case-study production) | 2–3 weeks | Also generates the agency's own proof supply |

**Operating rule:** expansion is *offered on a schedule*, not when convenient. One expansion
conversation per operated account per quarter, tied to the quarterly business review
(`CLIENT_LIFECYCLE.md` §9). Ad-hoc upselling erodes trust; scheduled review does not.

## 6. L3 — Operated *(the recurring layer)*

| Field | Specification |
|---|---|
| Target problem | The system was built; without ownership it degrades — staff change, channels change, nobody watches the numbers |
| ICP | Any delivered L2 client |
| Tiers | **Monitored** (reporting + alerting + minor fixes) · **Operated** (monitored + monthly optimisation cycle + a defined change allowance) · **Partnered** (operated + quarterly strategic review + priority capacity) |
| Scope | Uptime and data-integrity monitoring; monthly measured report against baseline; a defined allowance of change requests; optimisation experiments; quarterly business review at the top tier |
| Exclusions | New builds (→ L4); emergency out-of-hours response (**no 24/7 SLA — `RF` operational limit; a solo operator cannot honour one, and promising it is a lie with a delay**); third-party platform outages; work outside the named systems |
| Client inputs | Continued access; a named counterpart; 30 min/month |
| Deliverables | Monthly report; change requests within the allowance; quarterly review at top tier |
| Milestones | Monthly cycle |
| Duration | 6-month initial term, then monthly |
| Acceptance | Report delivered by the 5th business day; change allowance honoured; response-time commitment met |
| Proof captured | **Longitudinal outcome data — the most credible proof type available**, and the input to T3 benchmark claims |
| Support burden | Must be capped by the change allowance or it becomes an unpriced retainer |
| Cross-sell | → L4 at quarterly review |
| Productization | Very high; the most delegable part of the business and therefore the first to be staffed |

### 6.1 Attachment mechanics

`A-11` (40% attachment) is unvalidated and is the plan's most consequential unvalidated assumption.
Three mechanisms improve the odds, all of them structural rather than persuasive:

1. **Offer at day 21 of the L2 build, not at day 30 post-launch.** At day 21 the client is engaged
   and the system feels valuable; at day 30 post-launch it feels finished. Timing is the largest
   controllable variable here.
2. **Price L3 against the measured loss the L1 diagnostic quantified**, never as a percentage of
   the build. The question is "what does it cost you when this drifts back?", not "what's a fair retainer?"
3. **Make the monthly report genuinely readable and genuinely about their business.** `E-07`'s
   editorial and information-design strengths have their highest commercial value here: a report a
   client actually reads is the entire retention mechanism (`BRAND_BUSINESS_INTERFACE.md` `BC-03`).

**Churn diagnosis rule:** if L3 attaches and then churns inside 90 days, the failure is value
communication, not price. Do not discount (`DECISION_TREE.md` D9).

## 7. L5 — Custom work *(capped exception)*

Permitted only when: (a) an existing client asks; (b) it is time-boxed with a written cap;
(c) it does not exceed **15% of monthly delivery hours**; (d) it does not require a new
capability the agency does not already have.

**Why capped:** custom work is how productized businesses quietly become classic agencies (M1,
killed). It always pays well this month and always costs repeatability. The cap is the mechanism
that makes the refusal survivable.

## 8. Skip-upward exception

Selling L2 without L1 requires a written exception recording: why the baseline is unnecessary or
already exists, who approved it, and an acknowledgement that **no outcome claim may be made from
that engagement** (`RF-5`). Expected legitimate case: a client with mature analytics who has
already diagnosed the problem themselves.

## 9. DO NOT SELL register

Each entry has a real cost. That is what makes it a strategy rather than a preference.

| # | Do not sell | Why | What it costs us |
|---|---|---|---|
| DNS-1 | Ad-spend management on a percentage of spend | `RF-2`; misaligned incentives, most commoditised service in the market | An easy recurring line |
| DNS-2 | SEO retainers with ranking commitments | Uncontrollable; the outcome depends on a third party's algorithm | A common SMB budget line |
| DNS-3 | Staff augmentation / hourly placement | `RF-3`, `D-4`; destroys pricing power permanently | The fastest cash in month 1 |
| DNS-4 | White-label production for other agencies | M7 trap; zero proof value. Bounded runway exception only | Immediate low-sales-effort revenue |
| DNS-5 | Standalone "AI strategy" decks or workshops | `RF-1`; advice without implementation fails `D-3` | A trendy, high-margin product |
| DNS-6 | Generic chatbot deployments | Commoditised to near-zero; high failure rate; reputational drag | A frequently requested item |
| DNS-7 | Logo/brand identity as a standalone service | Outside the thesis; competes with the founder's own Brand workstream for attention | Work the founder would enjoy — which is precisely why it is listed |
| DNS-8 | Anything requiring 24/7 or sub-4-hour SLA | A solo operator cannot honour it | Enterprise-adjacent deals |
| DNS-9 | Custom software touching clinical/patient records | `RF-7`, `U-10`; unreviewed regulatory exposure | The largest deals in the S2 segment |
| DNS-10 | Engagements without measurement access | `RF-8`; no proof, no renewal, no case study | Real, willing buyers |
| DNS-11 | Results-based / revenue-share pricing | Uncontrollable variables; uncapped exposure; unbounded dispute surface | Deals from buyers who want to share risk |
| DNS-12 | Work for a client whose incumbent agency's scope this duplicates, with no intention to change | Political cost exceeds deal value | Occasional deals |
| DNS-13 | Discounted first engagements "to build the portfolio" | Anchors the relationship and the market at the discounted price; the discount never reverses | Speed to first client |

**DNS-13 deserves a note.** The pressure to discount the first engagement will be intense and the
reasoning will feel sound. The alternative that preserves the price anchor is a **narrower scope at
full rate**, or an explicit, written, one-time *pilot* with a case-study agreement as the stated
consideration — which is a different thing from a discount and is priced as such
(`PRICING_AND_ECONOMICS_MODEL.md` §7).

## 10. Offer-to-module map

| Offer | Price model | Delivery spec | Proof captured | Metrics |
|---|---|---|---|---|
| L0 Teardown | §3 (cost only) | `DELIVERY_OS.md` §3 | Teardown library | M-04 |
| L1 Diagnostic | §4 | `DELIVERY_OS.md` §4 | Baseline | M-05, M-06 |
| L2 C-1/C-2/C-3 | §5 | `DELIVERY_OS.md` §5 | Before/after | M-07…M-10 |
| L3 Operated | §6 | `DELIVERY_OS.md` §7 | Longitudinal | M-11, M-12 |
| L4 Expansion | §6 | `DELIVERY_OS.md` §5 | Incremental | M-13 |
| L5 Custom | §7 | ad hoc | Usually none | M-14 (cap monitor) |
