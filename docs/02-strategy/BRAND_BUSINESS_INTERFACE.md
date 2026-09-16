---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - POSITIONING_ARCHITECTURE.md
  - ICP_FRAMEWORK.md
  - PROOF_STRATEGY.md
---
# Brand / Business Interface

> **Module 19 of the Agency Master Plan** (Issue #2 Phase 16).
>
> ## Scope boundary — read first
>
> This document **does not** select a name, a visual direction, a palette, a typeface or a voice.
> Those belong to the Brand workstream (`OWNERSHIP_MATRIX.md`, `AGENTS.md`, `STOP_RULE.md`), and
> nothing in `docs/03-brand/` is modified by this plan.
>
> What this document does is state, from the commercial side, **what the brand must be able to do**
> — the constraints it must satisfy and the tests it must pass at the Brand/Business Fit Review
> (`BRAND_BUSINESS_FIT_REVIEW.md`). It is an input to Gate 1, not a verdict.

## 1. The tension, stated honestly

This is the most consequential finding in the master plan, and it is uncomfortable.

| Side | What the evidence says |
|---|---|
| **Founder's calibrated aesthetic** (`E-07`, `FACT`) | Sacred beauty and horror; illuminated manuscripts; anatomical engraving; angelic grotesque; chiaroscuro; ivory/charcoal/ultramarine/crimson/aged gold; editorial, annotation-dense, information-rich. Anti-profile explicitly rejects AI gradients, neon tech, glassmorphism, SaaS bento and pseudo-luxury |
| **Most reachable buyer** (`ICP_FRAMEWORK.md` §5) | Owner-operators of private specialty clinic groups — conservative, risk-averse, trust-gated, buying an operational repair from a supplier with no track record |
| **The inference** (`E-24`) | A visual system organised around sacred grotesque imagery may actively **reduce trust** with a clinical buyer evaluating an unknown supplier |

**This is not a reason to change the brand.** It is a reason to be precise about *where* the brand
operates, and to test the assumption rather than assume it (H-08). Two errors are possible here and
both are expensive: forcing the business to fit the aesthetic (which `E-08` exists to prevent), and
discarding a genuine differentiator out of caution.

## 2. The proposed resolution

> **The category is bought. The craft is experienced.**
> (`POSITIONING_ARCHITECTURE.md` §5)

| Surface | Register | Why |
|---|---|---|
| Cold outreach, first contact | **Plain.** No brand expression beyond typographic competence | The buyer is deciding whether to reply, not whether they like you |
| Website above the fold | **Plain, confident, legible.** Brand present in typography and restraint, not in imagery | 8-second credibility judgement by a sceptical stranger |
| Method document, diagnostic report, proposal | **Full register.** Editorial density, annotation systems, precise information design | This is where distinctiveness converts into perceived rigor — the strongest possible fit between `E-07` and a commercial artifact |
| Monthly L3 report | **Full register** | A report that is a pleasure to read is the retention mechanism (`CLIENT_LIFECYCLE.md` §8) |
| Deep website pages, case studies, published teardowns | **Full register** | Reached by people already interested |
| Social, peer-facing, talent-facing | **Full register, unrestrained** | Different audience, different job: memorability and attraction |

**What this exploits:** the founder's aesthetic is strongest at exactly the thing this business
sells — dense, annotated, rigorous information design. A diagnostic report in the illuminated-
editorial register is not a compromise with the business model; it is the single best expression of
it. The grotesque and sacred-figurative elements, which are the parts most likely to unsettle a
clinical buyer, live in peer-facing and campaign surfaces rather than in the buyer's first
impression.

## 3. What the brand must communicate — by commercial requirement

| # | Requirement | Because | Failure mode if unmet |
|---|---|---|---|
| BR-1 | **Rigor before creativity** in buyer-facing surfaces | Positioning is measurement (POS-1); the buyer is buying accuracy | Read as a creative agency → wrong category, wrong budget, wrong expectations |
| BR-2 | **Trust at a mid-premium price point** | L2 at USD 9k–20k from an unproven supplier | Too cheap-looking → price resistance; too luxurious → "we can't afford them" |
| BR-3 | **Category flexibility** | The vertical and category label are both unvalidated (`DECISION_TREE.md` D3, H-11) | A name or system welded to "clinics" or to "AI" becomes a liability at the first pivot |
| BR-4 | **Buyer appropriateness for conservative operators** | `ICP_FRAMEWORK.md` §6.2 | Buyer cannot picture this supplier in their waiting room |
| BR-5 | **Extensibility across surfaces** | One-page cold pitch to 30-page evidence document | A system that only works on a poster is unusable |
| BR-6 | **Data and evidence presentation as a first-class citizen** | The flagship artifact is a report full of tables and numbers | Beautiful brand, unreadable deliverable — the most likely failure here |
| BR-7 | **ES/EN parity** | `E-16` | Name or wordmark that breaks in one language |
| BR-8 | **No AI signalling** | `RF-1`; also already in the `E-07` anti-profile | Contradicts the entire positioning |
| BR-9 | **Works at low production cost** | Solo operator; no photography budget; no illustration budget per client | A system requiring commissioned artwork per deliverable will not be maintained |
| BR-10 | **Distinctiveness that does not require explanation** | A brand that needs a story to be tolerated has failed with a busy buyer | — |

## 4. Named constraints for Brand V1

| ID | Constraint |
|---|---|
| **BC-01** | The system must have a **plain register and a full register**, both native to it — not a "corporate version" grafted on. §2 |
| **BC-02** | The **method document and diagnostic report are the flagship artifacts**, not the logo. Designing the identity without designing the report is designing the wrong thing (`PROOF_STRATEGY.md` §3) |
| **BC-03** | The **monthly report template** is a retention mechanism and must be designed as a product surface, not as collateral (`OFFER_ARCHITECTURE.md` §6.1) |
| **BC-04** | The name and system must carry **either a category label or a plain description** without breaking (`AGENCY_THESIS.md` §2.2) |
| **BC-05** | Must accommodate **dense tabular and annotated data** legibly at print and screen sizes |
| **BC-06** | Must not require **licensed imagery per deliverable** (`BR-9`, and the licensing gates in `IMPLEMENTATION_SUMMARY.md`) |
| **BC-07** | Must be **implementable by the founder alone** in the tools already in use |
| **BC-08** | Must not encode the vertical or the category in a way that a pivot would invalidate (`BR-3`) |
| **BC-09** | Accessibility is a brand constraint, not only an implementation one: contrast and type sizing must hold in the full register (`DELIVERY_OS.md` §9.1) |
| **BC-10** | Must survive being seen next to a client's own conservative branding without making the client look reckless for choosing it |

## 5. What the business does *not* constrain

Stated explicitly so the Brand workstream is not over-constrained by a strategy document:

- The name itself. All ten `NAMING_WORKBENCH.md` candidates remain viable against these constraints.
- Palette specifics. The `E-07` palette (ivory/charcoal/ultramarine/crimson/aged gold) is entirely
  compatible with BR-1 and BR-2 — arguably better suited to them than a conventional agency palette.
- Typography, beyond BC-05 and BC-09.
- The peer-facing and campaign register, which may be as unrestrained as the Brand workstream wishes.
- Which of the five visual territories is selected. Business criteria do not favour any one of them;
  the differences that matter are in *application discipline*, not in territory choice.

## 6. Dependencies between the workstreams

| Brand needs from strategy | Status | Where |
|---|---|---|
| Category language candidates | Provided, unvalidated | `AGENCY_THESIS.md` §2.2 |
| Target buyer profile | Provided, unvalidated | `ICP_FRAMEWORK.md` §6 |
| Price/trust positioning | Provided | BR-2; `PRICING_AND_ECONOMICS_MODEL.md` §4 |
| Surface inventory | Provided | §2 |
| Message hierarchy | Provisional until D4 | `POSITIONING_ARCHITECTURE.md` §4 |
| Real buyer language | **Blocked on D4** | `FIELD_VALIDATION_PLAN.md` |

| Strategy needs from brand | Status | Blocking? |
|---|---|---|
| A usable typographic system for the method document | Needed week 3 | **No** — an interim system is used; waiting would breach `RT-01` |
| Minimum viable site identity | Needed week 3 | No — plain and fast beats beautiful and late |
| Brand V0 for Gate 1 | Needed after D5 | No |
| Full Brand V1 | Needed for the production site | Yes, for the site only |

> **Explicit non-blocker:** market validation does not require Brand V1, or Brand V0, or a name.
> The first 90 days run on a plain, competent, typographically decent presentation. Any decision to
> delay market contact for brand readiness should be recognised as the over-planning failure mode
> (`R-14`, `RT-01`), not as professionalism.

## 7. Gate 1 test criteria

Proposed additions to `BRAND_BUSINESS_FIT_REVIEW.md`, to be evaluated with H-08 evidence in hand:

| # | Test | Evidence |
|---|---|---|
| T-B1 | Does it read as rigorous before creative in the plain register? | Buyer reaction, H-08 |
| T-B2 | Does it support a USD 9k–20k price without reading as cheap or as unaffordable? | Buyer reaction |
| T-B3 | Does it survive a pivot to a different vertical or category label? | Structural review |
| T-B4 | Can a 30-page evidence document be produced in it, legibly, by the founder alone? | Produce one |
| T-B5 | Does it work in ES and EN? | Review |
| T-B6 | Does it avoid AI signalling? | Review against `E-07` anti-profile |
| T-B7 | **Does the target buyer trust it?** | **H-08 — the only test with external evidence** |
| T-B8 | Can the founder maintain it without external production? | Practical test |

**Outcome per `BRAND_BUSINESS_FIT_REVIEW.md`:** PASS / MUTATE / KILL, with an ADR if canonical
direction changes.

**Recommendation on how to read a failure:** if T-B7 fails, the likely correct response is
**MUTATE the application discipline, not KILL the direction** — i.e. tighten the plain register and
move figurative elements further back in the funnel. A KILL would only be warranted if the
territory cannot produce a plain register at all.

## 8. The honest risk

> There is a real possibility that the aesthetic the founder is most motivated by is not the
> aesthetic that sells to the buyer the founder can most easily reach.

If H-08 confirms that, the options are, in order of preference:

1. **Register separation** (§2) — most likely sufficient, and costs nothing.
2. **Move the aesthetic later in the funnel** — plain until the relationship exists.
3. **Change the ICP** to buyers who reward distinctiveness (which points back at M5 in
   `STRATEGY_RECONCILIATION.md`, with its 18–36 month proof-building cost stated plainly).
4. **Mutate the aesthetic toward the editorial/anatomical-precision end** of `E-07` and away from
   the figurative-grotesque end, keeping typography, annotation density, palette and chiaroscuro.

**What is not an option:** choosing the ICP to suit the aesthetic without acknowledging the trade.
`E-08` exists precisely to prevent that, and it is a rule the founder wrote before the temptation
existed — which is the best kind of rule.
