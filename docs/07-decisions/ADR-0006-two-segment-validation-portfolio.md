# ADR-0006 — Two-segment validation portfolio, not a single ICP commitment

Status: **PROPOSED**
Date: 2026-09-16
Proposed by: Claude/CoWork Agency Master Plan workstream (Issue #2)
Decided by: human project owner

## Context

`docs/02-strategy/icp/README.md` states that healthcare, dental, clinics and labs are candidates,
not predetermined winners. `E-09` records zero buyer contact, and `U-04` (which businesses the
founder can actually reach) is unanswered. Committing to a single ICP before the access gate would
convert an untested assumption into a sunk cost.

## Decision

Run validation against **exactly two segments**: one **primary** at ~75% of outreach effort and one
**hedge** at ~25%, with a defined swap rule at the Day 30 access gate.

Recommended, pending `DECISION_TREE.md` D0:
- **Primary:** multi-site specialty clinic groups, 3–15 locations (S2).
- **Hedge:** established D2C/e-commerce brands with operational drag (S7).
- **Rotation 1:** boutique real-estate developers/brokerages (S6). **Rotation 2:** mid-market
  professional services (S4). Maximum two rotations.

**Override clause:** if the founder's warm network contains ≥15 reachable businesses in any single
segment, that segment becomes primary regardless of the desk ranking. Fifteen warm doors beat a
better-scoring segment behind a cold one.

**Selection principle:** reachability dominates attractiveness until three engagements are
delivered. This inverts conventional ICP scoring deliberately and is the reason the access gate
precedes the resonance and monetisation gates.

## Alternatives considered

| Option | Rejected because |
|---|---|
| Single ICP from day 0 | A segment that fails the access gate costs 30 days with no comparative information |
| Three or more segments | Founder attention divides; per-segment learning rate collapses; no segment reaches conversational saturation (`AUD-02-01`) |
| No segment focus (horizontal) | M9, killed — never accumulates a domain asset |
| Rank by attractiveness first | Produces a segment that cannot be reached (`E-23`) |

## Why

Two segments produce comparative information at an acceptable attention cost, and the hedge is
cheap insurance against a primary-segment access failure. S2 is recommended because its problem is
operational rather than promotional, which escapes the saturated "more patients" channel; its
outcomes are countable in the buyer's own terms; and each additional location is an expansion unit
with zero acquisition cost.

## Consequences

- Outreach instruments must be built for two segments, at roughly 1.3× the cost of one.
- The hedge is a permitted 90-day M9 tactic only; it must not become the shape of the business.
- The second-vertical prohibition holds until three cores are delivered with captured outcomes
  (`AGENCY_THESIS.md` §3.1).
- The ICP framework is expected to be **re-ranked with real data at Day 120** (`ICP_FRAMEWORK.md`
  §7). A framework that survives contact unchanged was probably not testing anything.

## Evidence / assumptions

`E-19` (`SIGNAL`) seeds the longlist. Every band in `ICP_FRAMEWORK.md` §4 is `INFERENCE`; none is
`FACT`. `U-07` (WTP) and `U-12` (competitive density) are unresolved for every candidate.
`U-09` (buying committee) is unresolved for S2 and is the segment's main qualification risk.

## Reopen if

- D3 access fails for both segments after two rotations → distribution problem, not segment
  problem → pivot P-C or P-D.
- D0 reveals a warm network that overrides the ranking.
- D8 re-ranking with real data favours a different segment.
