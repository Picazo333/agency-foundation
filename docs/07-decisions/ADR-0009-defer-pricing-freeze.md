# ADR-0009 — Defer any pricing freeze until willingness-to-pay evidence exists

Status: **PROPOSED**
Date: 2026-09-16
Proposed by: Claude/CoWork Agency Master Plan workstream (Issue #2)
Decided by: human project owner

## Context

`docs/02-strategy/pricing/README.md` requires that public prices, price signals, inferred ranges and
internal models remain clearly separated, and that inferred economics never become market facts.

The program currently holds **zero `PUBLIC PRICE` records and zero `PRICE SIGNAL` records** (`E-22`),
because the raw research archives are not in the repository (`E-02`) and the Spark corpus's numeric
outputs are declared non-factual unless individually sourced (`E-04`).

`docs/02-strategy/pricing/PRICING_AND_ECONOMICS_MODEL.md` therefore derives every figure bottom-up
from capacity and cost logic. Not one is an observation.

## Decision

1. **Every price in the master plan is labelled `INFERRED RANGE`** and is a modelling instrument,
   not a price.
2. **No price is published** — not on the website, not in a rate card, not in a public proposal
   template — before H-04 returns real price signals.
3. **Quote a single price, never a range**, in live conversations. Ranges anchor to the bottom and
   contaminate the WTP test.
4. **No price is frozen as canon** until at least 8 real quotes have been issued and their reactions
   recorded.
5. **Trigger T-11:** the first observed competitor price or buyer counter-offer converts
   `INFERRED RANGE` → `PRICE SIGNAL` and requires re-derivation of §4 of the pricing model.
6. **Discounting is prohibited.** Scope reduction is the only permitted response to price
   resistance. The pilot exception (max 2, ≥60% of base, written case-study agreement) is
   consideration for a case study, not a discount.

## Alternatives considered

| Option | Rejected because |
|---|---|
| Publish a rate card now | Would present `INFERRED RANGE` as market fact — the exact failure `ADR-0004` and the pricing README prohibit |
| Import price benchmarks from the Spark corpus | `E-02`, `E-04`: unavailable and declared non-factual |
| Value-based pricing with no floor | A floor derived from capacity is what prevents pricing below survival; the model needs both |
| Hourly billing | Transfers estimation risk to the client, caps upside, forfeits the AI-leverage advantage |

## Why

Publishing a price derived from no observation would be the single clearest violation of the
research/canon firewall, in the area where a mistake is most expensive and hardest to reverse: a
published price anchors the market, the referral network and the buyer's expectations
simultaneously, and it cannot be quietly withdrawn.

## Consequences

- The website carries no prices until after H-04. Some buyers will disqualify themselves for that
  reason; that cost is accepted.
- Pricing conversations happen live, which is slower and requires the founder to hold a number
  without flinching.
- The economic model must be **re-derived** once real signals exist. It is built so quantities can
  be replaced without rebuilding the structure.
- The scorecard tracks the inputs that calibrate it from engagement one: actual hours, rework
  (`A-13`), unbilled sales hours (`A-14`), conversion (`A-08`), attachment (`A-11`).

## Evidence / assumptions

`E-22`, `E-02`, `E-04`. Assumptions `A-02`, `A-13`, `A-14`, `A-15`–`A-18`. `U-07` unresolved.
`RED_TEAM_REVIEW.md` RT-07 notes that if local price anchors sit far below the model, the geography
choice itself may be wrong — which is a pricing-evidence question before it is a strategy question.

## Reopen if

- H-04 returns price signals materially outside the modelled ranges → re-derive §4 entirely.
- T-3 fires (core win rate >70%) → the price is too low; raise 15–25%.
- T-4 fires (win rate <20% after 8 proposals) → diagnose price vs positioning vs qualification
  before cutting price.
- A primary pricing corpus is imported and graded → `INFERRED RANGE` may be upgraded.
