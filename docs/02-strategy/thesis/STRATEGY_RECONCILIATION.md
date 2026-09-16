---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - ADR-0004
  - EVIDENCE_AND_ASSUMPTIONS_REGISTER.md
---
# Strategy Reconciliation

> **Module 2 of the Agency Master Plan.** Determines which business archetypes survive contact
> with the evidence, which are killed, and what the surviving construct is.
> Every claim cites `E-##` / `A-##` / `U-##` from `EVIDENCE_AND_ASSUMPTIONS_REGISTER.md`.

## 1. Method, and why it is not a scoring matrix

Issue #2 requires "a selection framework, not arbitrary scoring precision." Numeric scoring of
business archetypes would manufacture exactly the false precision that `E-04` forbids: a weighted
model with invented weights produces a decisive-looking total from undecidable inputs.

This reconciliation therefore uses **ordinal bands** and **elimination logic**:

- Bands: `STRONG` / `MODERATE` / `WEAK` / `UNKNOWN`.
- A model is eliminated when it fails a **disqualifier**, not when it accumulates a low score.
- Disqualifiers are properties that cannot be fixed by effort within the program's constraints.
- Surviving models are then compared on the criteria that actually differ between them.

### 1.1 The four disqualifiers

A model is killed if any of these hold:

| # | Disqualifier | Justification |
|---|---|---|
| D-1 | **Requires capital or headcount the program does not have and cannot acquire in 90 days** | `A-03`, `A-04`, `U-03` |
| D-2 | **Requires reputation or references that do not exist and cannot be manufactured ethically** | `A-06`, `E-09`, `PROOF_STRATEGY.md` claim rules |
| D-3 | **Cannot produce countable evidence of value inside one engagement** | Without this, no case study exists, no price holds, and no referral engine starts (`E-23`) |
| D-4 | **Competes primarily on a commoditised axis** (price, speed-to-deliver, tool access) | `E-17`; a solo operator loses every price war |

### 1.2 The criteria used to compare survivors

From `CLAUDE_KICKSTART.md` §1, retained in full. **Brand fit is deliberately evaluated last and
treated as a tiebreaker only**, per `E-08`.

`buyer clarity` · `willingness/ability to pay` · `differentiation` · `delivery complexity` ·
`repeatability` · `recurring potential` · `proof requirements` · `acquisition difficulty` ·
`founder dependence` · `margin sensitivity` · `scalability` · `commoditization risk` ·
*(brand fit — tiebreaker only)*

## 2. The candidate set

Issue #2 requires at minimum seven archetypes. Two more are added because the evidence suggests
them: white-label subcontracting (the default trap for capable solo operators) and the
diagnostic-led hybrid that the BOLD signal points toward (`E-18`).

| ID | Archetype | One-line definition |
|---|---|---|
| M1 | Classic multidisciplinary agency | Sells brand + web + marketing as bespoke retained relationships |
| M2 | Horizontal AI/automation agency | Sells AI and automation implementation across any industry |
| M3 | Productized boutique | Sells a small number of fixed-scope, fixed-price, repeatable products |
| M4 | Consultancy-led model | Sells diagnosis, strategy and roadmaps; implementation optional or referred |
| M5 | Creative-technology / systems studio | Sells distinctive, technically ambitious digital work as craft |
| M6 | Vertical specialist | Sells a full stack of services to exactly one industry |
| M7 | White-label / subcontract shop | Sells production capacity to other agencies |
| M8 | Hybrid — diagnostic-led vertical productized studio | Paid diagnostic wedge → productized core builds → operated recurring layer, inside one vertical |
| M9 | Hybrid — productized horizontal with vertical marketing | Same products sold to many industries, marketed as if vertical |

## 3. Archetype analysis

### M1 — Classic multidisciplinary agency

| Criterion | Band | Reasoning |
|---|---|---|
| Buyer clarity | `MODERATE` | Buyers understand "agency", but not what makes one worth choosing |
| Willingness to pay | `MODERATE` | Budgets exist; they route to incumbents with portfolios |
| Differentiation | `WEAK` | The category's defining feature is that everyone claims the same things |
| Delivery complexity | `STRONG` (bad) | Multidisciplinary scope with one person is unmanageable |
| Repeatability | `WEAK` | Every engagement is bespoke by definition |
| Recurring potential | `MODERATE` | Retainers exist, but are the first line cut in a downturn |
| Proof requirements | `STRONG` (bad) | Portfolio-gated: you cannot sell without the portfolio you cannot build without selling |
| Acquisition difficulty | `WEAK` | Highest-noise category in professional services |
| Founder dependence | Total | — |
| Margin sensitivity | `WEAK` | Bespoke scope + revision exposure (`A-13`) |
| Scalability | `WEAK` | Scales by headcount only |
| Commoditization risk | `STRONG` (bad) | — |

**Verdict: KILLED.** Fails `D-2` (portfolio-gated with no portfolio, `A-06`) and `D-4`.

**Kill criterion, stated positively:** M1 becomes viable only if the founder acquires a
referenceable portfolio of three or more comparable engagements. That is an outcome of another
model, not a starting point.

---

### M2 — Horizontal AI/automation agency

| Criterion | Band | Reasoning |
|---|---|---|
| Buyer clarity | `WEAK` | "AI agency" describes a supplier's toolkit, not a buyer's problem. Buyers do not hold an "AI" budget line; they hold marketing, ops and IT budget lines |
| Willingness to pay | `UNKNOWN` | Bimodal: some buyers pay a novelty premium, others discount because "AI makes it cheap". No evidence either way (`U-07`) |
| Differentiation | `WEAK` | The tooling is the same tooling everyone has; the category's entry cost approaches zero |
| Delivery complexity | `MODERATE` | Manageable, but every client is a new system landscape |
| Repeatability | `WEAK` | Horizontal scope means no two integrations repeat |
| Recurring potential | `STRONG` | Automations genuinely need maintenance — the one real strength |
| Proof requirements | `MODERATE` | Outcomes are countable when a baseline exists (`U-08`) |
| Acquisition difficulty | `WEAK` | Saturated inbound, saturated outbound, saturated content |
| Founder dependence | Total | — |
| Margin sensitivity | `MODERATE` | Good on repeat patterns, poor on novel integrations |
| Scalability | `MODERATE` | — |
| Commoditization risk | `STRONG` (bad) | `E-17` |

**Verdict: KILLED as a category identity.** Fails `D-4` and, more importantly, fails buyer clarity:
the model names the supplier's means rather than the buyer's end.

**But the capability is retained.** This is the most consequential distinction in the whole
reconciliation, and the plan's answer to the BOLD signal (`E-06`, `E-17`):

> **Kill AI as a category. Keep AI as a mechanism.**
> AI and automation are how the work gets done cheaply, fast and at unusual quality for a solo
> operator. They belong in the delivery model (`DELIVERY_OS.md`) and the margin model
> (`PRICING_AND_ECONOMICS_MODEL.md`), and in the "how" section of a proposal. They do not belong
> in the category name, the tagline, or the first sentence a buyer reads.
> Enforced in `POSITIONING_ARCHITECTURE.md` §7.

---

### M3 — Productized boutique

| Criterion | Band | Reasoning |
|---|---|---|
| Buyer clarity | `STRONG` | Fixed scope, fixed price, fixed timeline is the most legible thing a new supplier can offer |
| Willingness to pay | `MODERATE` | Productization caps price; the ceiling is the product, not the client |
| Differentiation | `MODERATE` | The product design itself differentiates, if the product is well chosen |
| Delivery complexity | `STRONG` (good) | Same shape every time |
| Repeatability | `STRONG` | Definitional |
| Recurring potential | `MODERATE` | Requires a deliberately designed recurring layer; not automatic |
| Proof requirements | `MODERATE` | One good case study serves all future sales of the same product |
| Acquisition difficulty | `MODERATE` | Easier to explain, still needs distribution |
| Founder dependence | High initially, reducible | Productization is the precondition for delegation |
| Margin sensitivity | `STRONG` (good) | Scope control is built in |
| Scalability | `MODERATE` | Scales by throughput and templating before headcount |
| Commoditization risk | `MODERATE` | A well-defined product is copyable; the wedge and the data are less so |

**Verdict: SURVIVES.** No disqualifier fires. Strongest structural fit for a solo operator with
no reputation: it converts the founder's scarcest resource (attention) into a repeatable shape.

**Weakness to carry forward:** productization without a vertical produces a product nobody can be
told about efficiently. Productization answers *what to sell*; it does not answer *who to tell*.

---

### M4 — Consultancy-led model

| Criterion | Band | Reasoning |
|---|---|---|
| Buyer clarity | `MODERATE` | Buyers understand advice; SMB buyers often refuse to pay for it separately |
| Willingness to pay | `WEAK` at SMB scale, `STRONG` at enterprise scale | Enterprise is unreachable without reputation (`A-06`) |
| Differentiation | `MODERATE` | Differentiation is the consultant, which is the problem |
| Delivery complexity | `STRONG` (good) | Low |
| Repeatability | `STRONG` | Diagnostic instruments repeat well |
| Recurring potential | `WEAK` | Advice ends |
| Proof requirements | `STRONG` (bad) | Pure advice is bought on credentials, which do not exist yet |
| Acquisition difficulty | `WEAK` as a standalone | — |
| Founder dependence | Total and permanent | Consulting does not delegate; it replaces |
| Margin sensitivity | `STRONG` (good) | Near-zero COGS |
| Scalability | `WEAK` | Sells hours of one brain |
| Commoditization risk | `MODERATE` | — |

**Verdict: KILLED as a standalone model.** Fails `D-2` (credential-gated) and `D-3`
(advice alone produces no countable outcome inside the engagement).

**But the instrument is retained.** A diagnostic that ends in a *quoted implementation* is not
consulting — it is a qualified, paid, de-risked sales process that the buyer funds. It survives as
the **entry offer** of M8, not as the business.

---

### M5 — Creative-technology / systems studio

| Criterion | Band | Reasoning |
|---|---|---|
| Buyer clarity | `WEAK` | The buyer who wants this is rare and already has suppliers |
| Willingness to pay | `STRONG` where the buyer exists | Ambitious work commands real budgets |
| Differentiation | `STRONG` | Highest of any model here, and the best fit for `E-07` and `E-21` |
| Delivery complexity | `STRONG` (bad) | Ambitious work is ambitious to deliver, solo |
| Repeatability | `WEAK` | Craft resists templating |
| Recurring potential | `WEAK` | Project-shaped |
| Proof requirements | `STRONG` (bad) | Bought almost entirely on portfolio |
| Acquisition difficulty | `WEAK` | Demand is thin and concentrated in a few cities/networks |
| Founder dependence | Total | — |
| Margin sensitivity | `WEAK` | Craft overruns |
| Scalability | `WEAK` | — |
| Commoditization risk | `STRONG` (good — low) | The one model with a real moat |
| *Brand fit* | `STRONG` | Perfect fit for `E-07` |

**Verdict: DEMOTED, not killed.** Fails `D-2` today (portfolio-gated with no portfolio) and
`D-3` (craft quality is not countable inside one engagement).

This is the most emotionally dangerous model in the set, and it deserves to be named as such:
**M5 is the model the founder's taste will lobby for** (`E-07`, `E-24`). `E-08` exists precisely
to prevent that lobbying from deciding. M5 is therefore treated as a **destination, not a
starting point** — reachable in 18–36 months on the back of proof, network and cash produced by a
model that can actually be sold cold today. Its capability is retained as a *delivery-quality
differentiator* inside M8 (see `POSITIONING_ARCHITECTURE.md` §5: "the category is bought, the
craft is experienced").

**Reopen condition:** M5 becomes the primary model if, during validation, inbound demand for
distinctive work materially exceeds outbound-generated demand for operational repair — a
result that would falsify `E-24` and invert the plan. This is a real possible outcome and is
tested by H-08.

---

### M6 — Vertical specialist

| Criterion | Band | Reasoning |
|---|---|---|
| Buyer clarity | `STRONG` | "We only work with X" is instantly legible |
| Willingness to pay | `MODERATE`→`STRONG` | Specialists out-earn generalists at equal skill |
| Differentiation | `STRONG` | Domain knowledge compounds and is genuinely hard to copy quickly |
| Delivery complexity | `STRONG` (good) | Same problems recur; solutions harden into assets |
| Repeatability | `STRONG` | — |
| Recurring potential | `STRONG` | Domain familiarity lowers the cost of ongoing support |
| Proof requirements | `STRONG` (good) | A case study inside the vertical is worth several outside it |
| Acquisition difficulty | `STRONG` (good) | Target lists are enumerable; associations, events and referral loops are dense |
| Founder dependence | High initially | Domain knowledge is documentable and therefore delegable |
| Margin sensitivity | `STRONG` (good) | Estimation accuracy improves with repetition |
| Scalability | `MODERATE` | Ultimately capped by vertical size |
| Commoditization risk | `MODERATE` | Attracts imitators once visible |

**Verdict: SURVIVES.** No disqualifier fires. The strongest single answer to acquisition
difficulty, which `E-23` identifies as the binding constraint.

**Weakness to carry forward:** picking the wrong vertical is expensive and slow to detect, and
`U-04` (who the founder can actually reach) is unanswered. Vertical choice must therefore be
treated as a **validated hypothesis with an exit**, not a founding commitment — see
`ICP_FRAMEWORK.md` §7 and `DECISION_TREE.md` node D3.

---

### M7 — White-label / subcontract shop

| Criterion | Band | Reasoning |
|---|---|---|
| Buyer clarity | `STRONG` | Agency buyers know exactly what they want |
| Willingness to pay | `WEAK` | Structurally priced at cost-plus-thin-margin |
| Differentiation | `WEAK` | The buyer's entire purpose is fungibility |
| Delivery complexity | `MODERATE` | Specified work, but zero control over scope hygiene |
| Repeatability | `STRONG` | — |
| Recurring potential | `MODERATE` | Real, and dangerously comfortable |
| Proof requirements | `STRONG` (good) | Near zero — the fastest possible revenue |
| Acquisition difficulty | `MODERATE` | Small, reachable buyer set |
| Founder dependence | Total | — |
| Margin sensitivity | `WEAK` | Someone else owns the client and the margin |
| Scalability | `WEAK` | — |
| Commoditization risk | `STRONG` (bad) | Definitionally commoditised |

**Verdict: KILLED as a strategy.** Fails `D-4` outright.

**Named as a trap.** M7 is the single most likely failure mode for a capable solo operator with
runway pressure (`U-03`): it pays this month and forecloses every other model, because it produces
no brand, no case studies, no buyer relationships and no pricing power. It is listed on the
`DO NOT SELL` register in `OFFER_ARCHITECTURE.md` §9.

**Narrow exception, deliberately bounded:** white-label work may be accepted **only** as
explicit runway financing, capped at 20% of founder hours, for a maximum of two consecutive
months, and only if `U-03` reveals a genuine cash constraint. It must never be marketed, never
appear on the website, and never be allowed to displace validation activity. If it exceeds the
cap, that is the signal that the business has become M7 by drift.

---

### M8 — Hybrid: diagnostic-led vertical productized studio

The construct assembled from the survivors: **M3 (productized) + M6 (vertical) + M4's instrument
(paid diagnostic) + M2's capability (AI/automation as mechanism) + M5's craft (as delivery
quality, not as category).**

Shape:

```text
PAID DIAGNOSTIC (entry wedge, weeks)
        ↓ buyer-funded qualification, baseline instrumentation, quoted options
PRODUCTIZED CORE BUILD (fixed scope/price, 4–8 weeks)
        ↓ measurable change against the baseline captured in the diagnostic
OPERATED RECURRING LAYER (monthly)
        ↓ retained measurement, optimisation, expansion
EXPANSION / ADDITIONAL UNITS
```

| Criterion | Band | Reasoning |
|---|---|---|
| Buyer clarity | `STRONG` | Buyer sees a small, priced, bounded first step against a named problem |
| Willingness to pay | `MODERATE` | Diagnostic price is low-friction; core price is anchored by the diagnostic's findings rather than by a rate card |
| Differentiation | `MODERATE`→`STRONG` | The diagnostic *instrument* plus vertical depth, not the deliverables |
| Delivery complexity | `MODERATE` | Bounded by productization |
| Repeatability | `STRONG` | — |
| Recurring potential | `STRONG` | Designed in from the start rather than retrofitted |
| Proof requirements | `STRONG` (good) | Baseline captured in the diagnostic makes every engagement a case study by construction — this is the model's defining advantage |
| Acquisition difficulty | `MODERATE` | Vertical makes lists enumerable; the diagnostic is a low-commitment ask |
| Founder dependence | High, with a designed reduction path | — |
| Margin sensitivity | `MODERATE` | Exposed to `A-13` rework, controlled by change orders |
| Scalability | `MODERATE` | — |
| Commoditization risk | `MODERATE` | Copyable in form; the accumulated vertical benchmark data is not |
| *Brand fit* | `MODERATE` | Tension with `E-07` — routed to Module 16 |

**Verdict: SURVIVES — recommended working thesis.**

**The bootstrap objection, stated honestly:** a paid diagnostic requires enough credibility to be
bought, and its purpose is to create credibility. This is circular and is *not fully resolved* by
this plan (logged as contradiction `C-03`). It is partially resolved by the proof ladder in
`PROOF_STRATEGY.md`: a free asynchronous teardown precedes the paid diagnostic in the ladder, so
credibility is demonstrated before it is charged for. Whether that is sufficient is `H-01`, the
highest-priority validation hypothesis in the program.

---

### M9 — Hybrid: productized horizontal, marketed vertically

Same products, sold to any industry, with vertical-looking landing pages and case studies.

| Criterion | Band | Reasoning |
|---|---|---|
| Buyer clarity | `MODERATE` | Works at first contact, degrades on contact with a real specialist |
| Differentiation | `WEAK` | Presentation-layer only; no accumulating domain asset |
| Proof requirements | `MODERATE` | Case studies are thin in every vertical simultaneously |
| Acquisition difficulty | `MODERATE` | — |
| Repeatability | `STRONG` | — |
| Commoditization risk | `STRONG` (bad) | — |

**Verdict: KILLED as a strategy, RETAINED as a tactic.** Fails `D-4` over any horizon: it never
accumulates the domain asset that makes M6/M8 defensible.

**But it is the correct hedging tactic during validation only.** Running the same productized
core against a second segment at low effort is how the program tests vertical choice cheaply
without committing (see `ICP_FRAMEWORK.md` §7, ICP-B). The rule: M9 is allowed as a
**90-day experiment**, never as the shape of the business at day 180.

## 4. Reconciliation result

| Model | Outcome | Reason |
|---|---|---|
| M1 Classic agency | **KILLED** | `D-2`, `D-4` |
| M2 Horizontal AI/automation | **KILLED as category; capability retained** | `D-4`; fails buyer clarity |
| M3 Productized boutique | **SURVIVES → absorbed into M8** | — |
| M4 Consultancy-led | **KILLED as model; instrument retained as entry offer** | `D-2`, `D-3` |
| M5 Creative-technology studio | **DEMOTED to future destination; craft retained** | `D-2`, `D-3` today |
| M6 Vertical specialist | **SURVIVES → absorbed into M8** | — |
| M7 White-label | **KILLED; named as trap; bounded runway exception only** | `D-4` |
| M8 Diagnostic-led vertical productized studio | **RECOMMENDED WORKING THESIS** | No disqualifier |
| M9 Productized horizontal | **KILLED as strategy; retained as 90-day hedging tactic** | `D-4` |

## 5. What the result depends on

The recommendation of M8 rests on four load-bearing propositions. If any is false, the
reconciliation changes:

| # | Proposition | If false | Falsified by |
|---|---|---|---|
| P-1 | The selected buyer has a countable commercial problem that can be baselined in days | M8's proof advantage evaporates; fall back to M3 sold on deliverables | H-06 |
| P-2 | The buyer will pay something, however small, for diagnosis before implementation | Entry wedge collapses; free teardown → paid core becomes the only path (still M3+M6, without the funded qualification) | H-01 |
| P-3 | A vertical exists that the founder can actually reach without a warm network | M6 component collapses; the program is reduced to M3 with paid-acquisition dependence, which `A-03`/`U-03` may not survive | H-03, `U-04` |
| P-4 | Distinctive craft does not actively repel the selected buyer | M8 and the founder's brand can coexist; otherwise Gate 1 must resolve a real conflict | H-08 |

`P-1`–`P-4` are the four propositions the field-validation plan is designed around. Nothing else
in this program is worth testing before them.

## 6. What this reconciliation explicitly does not decide

Per `STOP_RULE.md` and `HUMAN_AUTHORITY.md`:

- **Not decided:** the final agency name, visual identity, or brand voice — Brand workstream.
- **Not decided:** the actual vertical. M8 requires *a* vertical; `ICP_FRAMEWORK.md` proposes
  candidates and a selection procedure, and the selection is made by evidence, not by this document.
- **Not decided:** any price. `PRICING_AND_ECONOMICS_MODEL.md` builds models with labelled
  assumptions; none is a commitment.
- **Not frozen:** M8 itself. It is a *working thesis under validation*, proposed for human approval
  as `ADR-0006`. Approving `ADR-0006` authorises 90 days of validation spend and effort; it does
  not freeze the business model.

## 7. The one-sentence result

> Stop trying to be an AI agency. Become the supplier who, for a modest fee, tells one specific
> kind of business exactly where it is losing revenue — with numbers the business can verify —
> and then sells a bounded, priced, repeatable build to fix it, with a measured, operated layer
> on top. Use AI to make that economically possible for one person. Use craft to make it
> memorable. Never lead with either.
