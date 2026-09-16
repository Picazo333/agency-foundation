---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - POSITIONING_ARCHITECTURE.md
  - OFFER_ARCHITECTURE.md
---
# Proof, Portfolio and Trust Strategy

> **Module 9 of the Agency Master Plan** (Issue #2 Phase 7). How an agency with no clients
> (`A-06`, `E-09`) becomes credible without exaggerating — and how proof is manufactured as a
> *byproduct of delivery* rather than as a marketing project.

## 1. The problem, precisely stated

The agency needs proof to sell, and needs to sell to get proof. Most new agencies resolve this by
lying a little: implied rosters, borrowed credentials, unsourced statistics, outcome claims with no
denominator. That path is unavailable here, for two reasons — one ethical (`RF-5`), one strictly
commercial:

> The only durable asset a supplier without a reputation has is that **its numbers are real**.
> Once a buyer catches one inflated claim, every subsequent number is discounted to zero. For a
> business whose entire positioning is measurement (`POSITIONING_ARCHITECTURE.md` POS-1), a
> credibility failure is not a setback; it is the end of the thesis.

So the strategy is not to simulate proof. It is to **restructure the offer so that proof is
generated in week two of the first engagement** — which is exactly what the L1 diagnostic does.

## 2. The proof ladder

Each rung is available at a different stage and carries different persuasive weight. **Rungs L0–L2
require no clients and are available today.**

| Rung | Proof type | Available | Effort | Persuasive weight | Risk |
|---|---|---|---|---|---|
| **P0** | Method transparency — the published diagnostic method | Now | Low | Medium-high | None |
| **P1** | Governance artifact — the versioned decision system itself (`E-12`) | Now | Zero (it exists) | Medium | None |
| **P2** | Self-applied evidence — the agency's own instrumented operation | Week 2–4 | Medium | Medium | None |
| **P3** | Anonymised teardowns of comparable businesses | Week 2+ | Low each | Medium | Reputational if identifiable |
| **P4** | Pilot engagement with captured outcome | Month 2–4 | High | **High** | Requires consent |
| **P5** | Named case study with baseline + outcome | Month 4–6 | Low marginal | **Highest** | Requires consent |
| **P6** | Reference calls | Month 5+ | Low | **Highest** | Client goodwill |
| **P7** | Benchmark dataset ("in 14 clinics like yours…") | Month 12+ | Accumulates | **Decisive** | Consent + anonymisation |
| **P8** | Testimonials | Month 4+ | Low | Low — everyone has them | None |

**Order of investment:** P0, P1, P2 in weeks 1–3 (they are cheap and available); P3 continuously as
outreach; P4/P5 as soon as the first engagement permits; P7 from engagement one, silently
accumulating.

## 3. P0 — Method transparency *(the most underrated rung)*

**What:** publish the diagnostic method in full — what is measured, how, with what instruments,
what the outputs look like, what the known limitations are. Include a redacted sample report.

**Why it works without any client history:** it is *verifiable rigor*. A buyer cannot verify a
claimed result from a stranger, but they can read a method and judge whether the person who wrote
it knows what they are doing. For a technically credible founder (`E-21`) this converts an
unfalsifiable claim into a falsifiable artifact.

**Why almost nobody does it:** agencies treat method as proprietary. It is not — the method is
copyable in form and not in execution (`AGENCY_THESIS.md` §8), and the trust gained from publishing
it exceeds the value of hiding it by a wide margin at this stage.

**Deliverables:** a public method document; a redacted sample diagnostic report; a short
"what we measure and why" page. **Owned by:** founder. **By:** week 3.

**This is also where `E-07` earns its commercial keep.** An editorially rigorous, annotation-dense,
information-rich method document is exactly what the founder's aesthetic produces naturally, and
exactly what signals seriousness to a sceptical buyer. See `BRAND_BUSINESS_INTERFACE.md` `BC-02`.

## 4. P1 — The governance artifact

`E-12` is a `FACT`: this repository is a working, versioned, ADR-governed decision system with
explicit evidence grading and a research/canon firewall. That is unusual to the point of being
remarkable among SMB service suppliers.

**Legitimate use:** "Here is how I run projects — every decision recorded, every assumption
labelled, every change traceable. This is my own program's decision record." It answers the
sceptical buyer's real question — *will this person be organised and honest with me?* — with
evidence rather than assertion.

**Constraints:** share a curated view, not the whole repository (it contains strategic reasoning
about the buyer's own segment, which would be uncomfortable reading). Never present internal
planning as client work. Never imply the governance system is a product unless it becomes one.

## 5. P2 — Self-applied evidence

**Principle:** the agency must run on the system it sells. A supplier who sells measured
enquiry-to-booking pipelines and cannot show their own is not credible, and knows it.

| Artifact | What it proves | By |
|---|---|---|
| Own enquiry pipeline, instrumented end to end | The method is real and we live in it | Week 4 |
| Own response-time SLA, measured and published | We hold ourselves to what we sell | Week 4 |
| Own CRM with stages, attribution, follow-up automation | The C-2 product works | Week 6 |
| Own monthly metrics report, in the same format clients receive | The L3 deliverable is real | Month 2 |

**Honesty limit:** "we did it for ourselves" is weak proof of *client* outcomes and must never be
presented as a case study. It is proof of *practice*, not of *results*. State it that way.

## 6. P3 — Teardowns

Mechanically the L0 offer (`OFFER_ARCHITECTURE.md` §2), commercially a proof asset.

**Publication rules — strict, because the downside is asymmetric:**
1. A named teardown requires **written consent** from the business. No exceptions.
2. An anonymised teardown must be genuinely unidentifiable: no location count, no specialty and
   city combination, no screenshots with recognisable branding.
3. Never publish a teardown of a business that declined to engage. It reads as retaliation and it
   will be recognised as such within the segment.
4. Never frame a teardown as criticism of an incumbent supplier (`PP-6`) — it creates the
   `ICP_FRAMEWORK.md` §6.2 blocker directly.

**Format:** the observation (what happened), the mechanism (why it happens), the cost (what it
plausibly costs, with the estimate clearly labelled as an estimate), the fix (described, not sold).

**Volume target:** 2 per week during weeks 2–8. This is the primary content engine, the primary
outbound opener, and the primary skill-building exercise, simultaneously.

## 7. P4/P5 — Pilots and case studies

### 7.1 Pilot terms

Per `PRICING_AND_ECONOMICS_MODEL.md` §7.1: maximum two pilots, minimum 60% of base price, written
case-study agreement. The agreement must specify, before work begins:

- Named attribution and logo use, or anonymised-with-sector attribution as the fallback.
- Publication rights, with a review window (not a veto — a review window; an unconditional veto
  means there is no agreement).
- Baseline capture and before/after publication of agreed metrics.
- One reference call per quarter for 12 months.
- Consent for anonymised inclusion in benchmark data (P7).

**Why this is negotiated before work starts:** asking for a case study after delivery converts a
commercial right into a favour, and favours are refused by exactly the clients whose names are most
valuable.

### 7.2 Case-study structure

Fixed template, because consistency is itself a credibility signal:

1. **Context** — sector, scale, no name if anonymised.
2. **The situation before** — with the measured baseline, dated.
3. **What was found** — the diagnostic findings, quantified.
4. **What was built** — scope, duration, who did what.
5. **What changed** — the measurement, with `POSITIONING_ARCHITECTURE.md` §8.2 discipline applied:
   denominator, time window, attribution caveat.
6. **What we would do differently** — included deliberately; it is the single strongest credibility
   signal in the document and costs nothing.
7. **Client statement** — optional.

**Prohibited in case studies:** projected results, annualised extrapolations from short windows,
percentages without denominators, "up to" figures, and any metric that was not baselined before
work started.

### 7.3 The no-baseline rule

> **No baseline, no outcome claim. Ever.** If the baseline was not captured at kickoff, the
> engagement produces a *process* case study — what was built, how, in what time — and no outcome
> claim whatsoever.

This rule is why baseline capture is a **contractual client input** in L1 and L2
(`OFFER_ARCHITECTURE.md` §3, §4) rather than a best effort, and why `RF-8` disqualifies buyers who
will not grant measurement access.

## 8. P7 — The benchmark dataset

The highest-value long-term asset (`AGENCY_THESIS.md` §4.2), and the cheapest to start.

**Start capturing at engagement one**, even with nothing to compare against. The fields are defined
once and captured identically every time:

| Field group | Examples |
|---|---|
| Firmographic | Location count, specialty, staff size band, market tier |
| Channel | Enquiry sources and mix |
| Performance | First-response latency, enquiry→booking rate, no-show rate, cost per booked unit, per-location spread |
| Systems | PMS/CRM platform, integration depth, tracking maturity |
| Outcome | Change on each measured metric, window, intervention applied |

**Requirements:**
- Consent for anonymised aggregate use, granted in the MSA (`GOVERNANCE_RISK_SECURITY_CHECKLIST.md` §4).
- Stored separately from identifiable client data, with the join key held separately.
- **Never published below n=5 per cohort** — small-n medians are both re-identifiable and
  statistically meaningless.
- Claims from it are T3 tier (`POSITIONING_ARCHITECTURE.md` §8.1) and carry n and period.

## 9. Ethical claim rules

Binding. Violating any one is treated as a serious defect, not a marketing choice.

| # | Rule |
|---|---|
| EC-1 | No outcome claim without a captured pre-intervention baseline |
| EC-2 | Every percentage carries denominator, time window and attribution caveat |
| EC-3 | No implied client roster before named clients exist (`PP-4`) |
| EC-4 | No borrowed credibility — no partner logos, certifications or affiliations not actually held |
| EC-5 | No unsourced industry statistics (`PP-1`) |
| EC-6 | No guarantees of outcome (`PP-5`) |
| EC-7 | Self-applied results labelled as self-applied |
| EC-8 | Anonymised means unidentifiable, tested by asking whether a competitor in the segment could name them |
| EC-9 | Where AI produced a substantial part of a deliverable, that is disclosed on request and never denied |
| EC-10 | A result that got worse is reported to the client with the same prominence as one that improved |

**EC-10 is the one that will hurt**, and it is the one that produces P6 references. A supplier who
reports a bad month unprompted is the supplier a client recommends.

## 10. Proof capture SOP *(embedded in delivery, not bolted on)*

| Stage | Action | Owner | Artifact |
|---|---|---|---|
| Contract | Case-study and benchmark consent clauses signed | Founder | MSA/SOW |
| Kickoff day 1 | **Baseline snapshot captured and stored, dated and immutable** | Founder | Baseline record |
| Kickoff day 1 | Benchmark fields captured | Founder | Benchmark row |
| During delivery | Screenshots, before/after artifacts, decision log | Founder | Engagement folder |
| Acceptance | Outcome measurement vs baseline | Founder | Outcome record |
| Day 30 post-launch | Second measurement; testimonial request | Founder | Outcome record v2 |
| Day 90 | Third measurement (if L3 attached); reference-call request | Founder | Case study draft |
| Quarterly | Case study published if consent permits | Founder | Published asset |

**Gate:** an engagement cannot be marked complete in the delivery system without a baseline record
and an outcome record attached. This makes proof capture structurally unskippable rather than a
matter of discipline — which matters, because it is always the first thing skipped when a project
runs late.

## 11. Trust signals available before any proof exists

Cheap, immediate, and disproportionately effective with the sceptical SMB buyer:

| Signal | Mechanism |
|---|---|
| Response speed | Reply within 2 hours in business hours. A supplier selling response-time improvement who responds slowly has lost the deal before the pitch |
| Written scope with explicit exclusions | Signals experience; most competitors' proposals are vague |
| Fixed price with a payment schedule | Transfers risk visibly |
| A method document that predates the relationship | P0 |
| Naming what you will not do | `DO NOT SELL` register, stated in the sales conversation. Counter-intuitively increases trust more than any capability claim |
| Admitting the absence of sector references | `A-06` stated plainly, then redirected to the small first step. Buyers discover it anyway; volunteering it converts a weakness into a credibility signal |
| Handing over the instrumentation regardless of outcome | Demonstrable non-lock-in |

## 12. What this strategy refuses

| Refused | Why |
|---|---|
| Buying reviews or testimonials | Detectable; terminal |
| "As seen in" from paid placements | Borrowed credibility (`EC-4`) |
| Fabricated or composite case studies | Fraud |
| Vanity metrics as outcomes (impressions, "engagement") | Not revenue; invites comparison with cheaper suppliers |
| Free full diagnostics to build a portfolio | Destroys the entry offer's price anchor permanently (`DNS-13`) |
| Publishing client data without consent | Legal and ethical exposure (`GOVERNANCE_RISK_SECURITY_CHECKLIST.md` §4) |
| Claiming sector expertise before delivering in the sector | `EC-3`; and the buyer's first detailed question will expose it |
