# ADR-0008 — Paid diagnostic as the mandatory entry offer

Status: **PROPOSED**
Date: 2026-09-16
Proposed by: Claude/CoWork Agency Master Plan workstream (Issue #2)
Decided by: human project owner

## Context

A supplier with no references (`A-06`) selling fixed-price builds must either quote against an
unmeasured problem — accepting scope risk and producing unprovable outcomes — or measure first.
`docs/02-strategy/offers/OFFER_ARCHITECTURE.md` specifies the measure-first ladder.

## Decision

1. **Every core build is preceded by a paid diagnostic (L1)**, except under a written skip-upward
   exception which records that no outcome claim may be made from that engagement.
2. **No written proposal is produced before qualification gates Q1–Q4 pass**
   (`SALES_SYSTEM.md` §5.1). Speculative proposals are prohibited.
3. **A free teardown (L0) precedes the paid diagnostic** in the ladder, capped at 3 hours, to
   demonstrate competence before charging for it.
4. **50% of the diagnostic fee credits against a core build contracted within 30 days.** Not 100%.
5. **No engagement without measurement access** (`RF-8`), and **no outcome claim without a captured
   baseline** (`RF-5`, `EC-1`).

## Alternatives considered

| Option | Rejected because |
|---|---|
| Free audit as the entry offer | Unpaid labour scaling linearly with outreach; attracts unqualified buyers; teaches the market that diagnosis is worthless. Retained only as the D5 path B fallback if `H-01` fails |
| Straight to a fixed-price build | Quoting an unmeasured problem produces scope overrun (`A-13`) and unprovable outcomes |
| Hourly/time-and-materials | Transfers estimation risk to the client, caps upside at the clock, and forfeits the AI-leverage advantage |
| 100% diagnostic credit | Makes the diagnostic free whenever conversion is good — penalises the desired outcome and contradicts the standalone-value claim (`AUD-04-01`) |
| No free teardown | Leaves the bootstrap problem unaddressed (`AUD-01-01`) |

## Why

- **Buyer-funded qualification.** After L1 is sold, discovery, scoping and proposal work are paid
  for. Unbilled sales hours are worth 28% of effective yield (`PRICING_AND_ECONOMICS_MODEL.md`
  §8.3), so moving them inside a paid engagement is the third-largest economic lever in the model.
- **Price anchoring.** The core is priced against the quantified loss, not against a rate card.
- **Proof by construction.** The baseline captured in week one makes every engagement a case study.
- **Risk reversal.** A small, bounded first step from an unproven supplier is a far easier yes than
  a five-figure build.

## Consequences

- **The first sale is harder.** The diagnostic must be sold cold to a buyer who does not know the
  supplier. This is `H-01`, the highest-priority validation hypothesis, and the model's principal
  risk.
- Buyers who refuse measurement access are disqualified (`RF-8`). This will lose real, willing
  buyers, and losing them is correct: an unmeasurable engagement produces no proof, no defensible
  renewal and no case study.
- Buyers who want a number immediately will be told that a fix cannot be priced before the problem
  is measured. Some will leave (`AUD-05-04`).
- The diagnostic is roughly cost-neutral by design; it is an acquisition instrument, not revenue.
- Where no baseline is reconstructable, a paid instrumentation pre-phase (O-0) is sold first, and
  time-to-findings extends to 5–6 weeks (`OFFER_ARCHITECTURE.md` §3.2).

## Evidence / assumptions

`A-07` (buyer pays for diagnosis) — **low confidence, unvalidated**. `A-08` (30% conversion) —
`INFERRED RANGE`. `U-08` (baseline availability) — unresolved, tested by H-06.
`RED_TEAM_REVIEW.md` RT-03 argues SMB owners buy things, not analysis; the counter-framing (an
instrumented asset you keep, not a report) is itself a hypothesis.

## Reopen if

- D5 path B: 0–1 diagnostics sold but a core sells after a free teardown → `A-07` is false; the
  wedge becomes free, with the stated costs (higher acquisition cost, weaker qualification, hard
  3-hour cap required).
- Three consecutive diagnostics fail to convert (T-10) → audit findings quality and qualification
  before changing the structure.
- H-06 shows <25% of buyers have reconstructable data → O-0 becomes mandatory and the offer is
  re-timed and re-priced.
