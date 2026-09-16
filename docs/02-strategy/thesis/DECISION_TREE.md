---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - STRATEGY_RECONCILIATION.md
  - AGENCY_THESIS.md
  - FIELD_VALIDATION_PLAN.md
---
# Decision Tree

> **Module 4 of the Agency Master Plan.** The executable control flow of the next 180 days.
> Where other modules describe *what* could be true, this one specifies *what happens next*
> for each way the evidence lands. Every node has an owner, a decision rule and a date.

## 0. How to read this

- **Node** = a decision point with a defined input and a defined set of exits.
- **Gate** = a node that may not be passed without the stated evidence.
- No node permits "continue while we figure it out." Each exit is explicit, including the exits
  that end the program.
- Dates are relative to **Day 0 = the day `ADR-0005` is approved**, not the merge date of this PR.

## 1. Master flow

```text
                          D0  Founder context (U-01..U-05)
                                     │
                          D1  Thesis approval (ADR-0005)
                                     │
                          D2  ICP shortlist confirmation
                                     │
                    ┌────────────────┴────────────────┐
                 D3 ACCESS GATE (Day 30) ──── fail ──→ D3b Segment rotation
                    │ pass                                   │ (max 2 rotations)
                    │                                        └──→ D7 if exhausted
                 D4 PROBLEM-RESONANCE GATE (Day 45)
                    │ pass / fail → D4b reframe
                 D5 MONETISATION GATE (Day 60)
                    │
        ┌───────────┼──────────────┬───────────────┐
   paid diagnostic  │         free teardown     no sale
     sells (A)      │          → paid core (B)   at all (C)
        │           │                │               │
        └───────────┴────────────────┘               ↓
                 D6 DELIVERY GATE (Day 90)        D7 KILL / PIVOT
                    │
                 D8 REPEATABILITY GATE (Day 120)
                    │
                 D9 RECURRING GATE (Day 180)
                    │
                 D10 SCALE vs DEEPEN
```

Running in parallel, not blocking the commercial path:

```text
   Brand V0 (ChatGPT) ──┐
                        ├──→ GATE 1: Brand/Business Fit Review  (earliest: after D5)
   Agency Master Plan ──┘
```

---

## 2. Node specifications

### D0 — Founder context resolution
**When:** Day 0–3. **Owner:** founder. **Input:** `U-01`–`U-05`.

| Question | Why it gates |
|---|---|
| Geography, jurisdiction, operating language, entity status | Currency, legal checklist, channel mix, ICP density |
| Weekly hours available | Every capacity and break-even number (`A-03`) |
| Runway in months; minimum monthly draw | Whether a diagnostic-led ramp is survivable at all (`U-03`) |
| Who can you contact this month without cold outreach — by name, with count | May dominate ICP selection entirely (`U-04`) |
| Verifiable prior delivery work and references | Proof ladder entry rung; price ceiling (`U-05`) |

**Exits:**
- **Runway < 3 months** → the diagnostic-led ramp is not survivable. Take the bounded M7 runway
  exception (`STRATEGY_RECONCILIATION.md` §3 M7) *in parallel*, capped at 20% of hours, and
  compress the validation window to 45 days. **Do not abandon validation to do billable work** —
  that is how the program becomes M7 permanently.
- **Warm network ≥ 15 reachable businesses in one segment** → that segment enters the shortlist
  automatically at D2, overriding the desk-research ranking in `ICP_FRAMEWORK.md`. Access beats
  attractiveness (`E-23`).
- **Available hours < 15/week** → the plan does not fit. Re-scope to a single-offer, single-segment
  micro-version or defer. Say so explicitly rather than silently under-delivering
  (`NO_SILENT_DOWNGRADE.md`).
- Otherwise → D1.

---

### D1 — Thesis approval
**When:** Day 0–7. **Owner:** human project owner. **Input:** this master plan.

**Exits:**
- **Approve `ADR-0005`** → M8 becomes the working thesis under validation. The §11 stop rule in
  `AGENCY_THESIS.md` activates. → D2.
- **Approve with modified thesis** → amend `AGENCY_THESIS.md` §1, re-derive `FIELD_VALIDATION_PLAN.md`
  hypotheses, then → D2.
- **Reject** → return to `STRATEGY_RECONCILIATION.md` §4 and select a different survivor. The only
  other undisqualified survivors are M3 and M6 standalone; M5 requires accepting a 18–36 month
  proof-building period with no near-term revenue path (state this explicitly if chosen).

---

### D2 — ICP shortlist confirmation
**When:** Day 7. **Owner:** founder + strategy. **Input:** `ICP_FRAMEWORK.md` §6, D0 network answer.

**Rule:** confirm exactly **one primary** segment (≈75% of outreach effort) and **one hedge**
segment (≈25%). Not three. Not one.

- *Why not one:* a single segment that fails the access gate costs 30 days with no comparative
  information.
- *Why not three:* founder attention divides, per-segment learning rate collapses, and no segment
  reaches conversational saturation (audit finding `AUD-02-01`).

**Exit:** → D3.

---

### D3 — ACCESS GATE *(the first real gate)*
**When:** Day 30. **Owner:** founder. **Input:** outreach log in `docs/06-validation/interviews/`.
**Hypothesis:** H-03.

**Threshold:** **≥ 8 qualified conversations** with the primary segment within 30 days, where
*qualified* means: a decision-maker or direct influencer, a real business in the segment, a
conversation of ≥ 20 minutes about their operations.

| Result | Exit |
|---|---|
| ≥ 8 qualified in primary | Pass → D4. Reduce hedge segment to 10% effort |
| 4–7 qualified in primary | Partial. Diagnose channel vs segment: if one channel produced nearly all of them, double down and re-test in 15 days. If spread thin, treat as fail |
| < 4 qualified in primary, ≥ 8 in hedge | **Swap.** Hedge becomes primary. → D4. This is a success of the two-segment design, not a failure |
| < 4 in both | Fail → D3b |

**Why access is the first gate and not the last:** an attractive segment you cannot reach is worth
strictly less than an average segment you can. This inverts the conventional ICP-scoring order, and
it is deliberate (`E-23`).

---

### D3b — Segment rotation
**When:** Day 30–60. **Rule:** rotate to the next-ranked candidate from `ICP_FRAMEWORK.md` §5,
**maximum two rotations**.

Before rotating, answer honestly: *was the failure the segment, the channel, or the message?*
Rotating the segment when the channel was the problem burns 30 days and learns nothing.

- Rotation 1 exhausted and failed → rotation 2.
- Rotation 2 exhausted and failed → **D7**. Two failed rotations is strong evidence that the
  constraint is the founder's distribution, not the segment choice — and that is a different
  problem requiring a different plan (partnership-led or employment-funded entry).

---

### D4 — PROBLEM-RESONANCE GATE
**When:** Day 45. **Owner:** founder. **Input:** interview notes. **Hypothesis:** H-10.

**Threshold:** in **≥ 5 of the last 10** qualified conversations, the buyer describes a version of
the revenue-leak problem **before being pitched it**, in their own language.

This is the gate that separates a real market from a market the plan invented. Buyers agreeing
with a well-framed pitch is worthless evidence; buyers volunteering the problem is not.

| Result | Exit |
|---|---|
| ≥ 5/10 unprompted | Pass → D5. **Capture their exact wording** — it becomes the messaging corpus (`POSITIONING_ARCHITECTURE.md` §3) and replaces all synthetic research VoC (`E-05`) |
| 2–4/10 | Partial → D4b reframe |
| ≤ 1/10 | The thesis' core problem claim is likely false in this segment → D3b (different segment) or D7 if rotations exhausted |

---

### D4b — Problem reframe
**When:** Day 45–60. The buyers have a problem; it is not the one the thesis named.

Rewrite `AGENCY_THESIS.md` §1 around the problem they *did* volunteer, keep the M8 structure
(diagnostic → build → operated), and re-enter at D4 with a 15-day window. **Maximum one reframe.**
A second reframe means the model is being fitted to noise.

---

### D5 — MONETISATION GATE *(the decisive gate)*
**When:** Day 60. **Owner:** founder. **Input:** sales attempts. **Hypotheses:** H-01, H-04.

**Threshold:** **≥ 2 paid diagnostics sold** (money received, not verbally agreed) from ≤ 20
qualified conversations.

| Path | Condition | Consequence |
|---|---|---|
| **A — Thesis holds** | ≥ 2 paid diagnostics sold | M8 confirmed as designed. → D6 |
| **B — Free-teardown fallback** | 0–1 diagnostics sold, but ≥ 1 core build sold after a *free* teardown | `A-07` is false; `P-2` in `STRATEGY_RECONCILIATION.md` §5 is falsified. The paid wedge becomes a free wedge. **Consequences, stated plainly:** acquisition cost rises (teardowns are unpaid labour), qualification weakens (free attracts tire-kickers), and the teardown must be time-capped at 3 hours and templated hard or it will consume all capacity. Model mutates to M3+M6. → D6 |
| **C — No monetisation** | 0 diagnostics and 0 cores sold from ≥ 20 qualified conversations | → D7 |

**Diagnosing path C before acting on it** — required, because the four causes have opposite
remedies:
1. *Price* → buyers engage then stall at the number → re-test at a lower price point before killing.
2. *Trust* → buyers like the idea, will not buy from an unproven supplier → the proof ladder is the
   problem; go get one pilot at near-zero price with an explicit case-study agreement.
3. *Problem* → buyers do not think it is worth money → the thesis is wrong; D4b already failed; go to D7.
4. *Wrong buyer* → the person in the room cannot authorise spend → qualification failure, not
   model failure; fix `SALES_SYSTEM.md` §3 gates and re-run 15 days.

---

### D6 — DELIVERY GATE
**When:** Day 90. **Owner:** founder. **Input:** first delivered engagement.
**Hypotheses:** H-06, H-12.

| Check | Threshold | If failed |
|---|---|---|
| Baseline captured at kickoff | Yes/no | If no baseline was obtainable, `P-1` is falsified: the proof engine does not work. Add a paid instrumentation pre-phase (`OFFER_ARCHITECTURE.md` §4 O-0) and re-test |
| Actual delivery hours vs budget | ≤ 130% | Re-price or narrow scope before selling another (`PRICING_AND_ECONOMICS_MODEL.md` §9 trigger T-1) |
| Rework hours vs `A-13` (20%) | ≤ 30% | Change-control process failed — fix `DELIVERY_OS.md` §6 before the next sale |
| Client would provide a reference | Yes/no | If no, diagnose before scaling; an unreferenceable delivery is a broken product |

**Exit:** all pass → D8. Any fail → fix the specific mechanism, deliver one more, re-gate. **Do not
sell a third engagement with a known-broken delivery model.**

---

### D8 — REPEATABILITY GATE
**When:** Day 120. **Threshold:** **3 delivered core engagements**, with delivery-hour variance
between them ≤ ±25% and at least 2 captured outcomes.

| Result | Exit |
|---|---|
| Pass | The offer is genuinely productized → D9, and the second-vertical prohibition (`AGENCY_THESIS.md` §3.1) lifts |
| Variance > ±25% | Not a product, a bespoke service wearing a product's clothes. Narrow the scope until it repeats, or re-price as custom. **Do not scale a non-repeating offer** |

---

### D9 — RECURRING GATE
**When:** Day 180. **Hypothesis:** H-09. **Threshold:** ≥ 1 operated account retained past 90 days
with a documented monthly value artifact the client actually reads.

| Result | Exit |
|---|---|
| Pass | The operated layer is real → D10 |
| Attaches but churns < 90 days | The layer is priced but not valued. Redesign around the one output clients engage with; do not discount |
| Does not attach at all | `A-11` false. The business is project-only. This is survivable but structurally weaker: revenue resets monthly, and the valuation argument disappears. Re-plan capacity and cash-flow accordingly; do not pretend otherwise |

---

### D10 — SCALE vs DEEPEN
**When:** Day 180+. Input: everything above.

| Signal | Direction |
|---|---|
| Demand > capacity, delivery repeats, outcomes captured | **Scale:** first contractor (`OPERATING_MODEL.md` §7 hiring triggers) |
| Demand ≈ capacity, margins thin | **Deepen:** raise price against captured outcomes before adding cost |
| Demand < capacity, delivery excellent | **Distribute:** the constraint is acquisition — partnerships and referral engineering, not hiring |
| Expansion revenue > new-logo revenue | **Farm:** the account base is the asset; invest in expansion offers first |

---

### D7 — KILL / PIVOT
Reached from D3b (rotations exhausted), D4 (problem absent), or D5 path C.

**This node exists so that failure is a decision rather than a slow fade.** A solo operator without
a kill node does not stop; they drift into M7 (`STRATEGY_RECONCILIATION.md` §3) and call it a
business.

| Pivot option | When it is the right answer | What it costs |
|---|---|---|
| **P-A: Change the vertical, keep the model** | Access failed but the diagnostic resonated where it was heard | 30–45 days |
| **P-B: Change the wedge, keep the vertical** | Segment is reachable and has budget, but will not buy diagnosis | Re-design entry offer as a concrete build; forfeits the funded-qualification advantage |
| **P-C: Partnership-led entry** | Direct access failed twice, but an intermediary (vertical SaaS vendor, accountant, consultant) has the relationship | Margin share; slower; but it is the standard answer to a pure distribution problem |
| **P-D: Employment or contract work to fund a slower build** | Runway exhausted (`U-03`) | Honest, common, and far better than a failing business consuming savings. Not a defeat |
| **P-E: Pursue M5 deliberately** | Validation shows inbound interest in distinctive work exceeds outbound interest in operational repair (falsifies `E-24`) | Accept 18–36 months of portfolio-building with thin revenue, and say so explicitly |

**Rule:** exactly one pivot option may be selected, it must be written into an ADR superseding
`ADR-0005`, and the new path re-enters the tree at D2.

---

## 3. Gate summary

| Gate | Day | Tests | Threshold | Failure consequence |
|---|---|---|---|---|
| D3 Access | 30 | Can we reach them? | 8 qualified conversations | Rotate segment (max 2) |
| D4 Resonance | 45 | Is the problem real to them? | 5/10 unprompted | Reframe (max 1) |
| D5 Monetisation | 60 | Will they pay? | 2 paid diagnostics | Kill/pivot |
| D6 Delivery | 90 | Can we deliver it profitably? | Baseline + ≤130% hours | Fix before selling more |
| D8 Repeatability | 120 | Is it a product? | 3 cores, ≤±25% variance | Narrow until it repeats |
| D9 Recurring | 180 | Does it stick? | 1 operated account >90 days | Accept project-only economics |
| Gate 1 Brand fit | after D5 | Does the brand fit the buyer? | See `BRAND_BUSINESS_INTERFACE.md` §7 | PASS / MUTATE / KILL per `BRAND_BUSINESS_FIT_REVIEW.md` |

## 4. Decisions deliberately *not* in this tree

Per `STOP_RULE.md`, these belong to other owners and appear here only as dependencies:

- Final agency name and visual identity — Brand workstream, Gate 1.
- Asset factory activation — blocked on Brand V1, `META_PLAN.md` Wave 4.
- Production website build — blocked on D5 minimum (message validated) plus Brand V1;
  see `WEB_BUSINESS_REQUIREMENTS.md` §9.
- Legal entity, contracts and jurisdiction-specific obligations — qualified local professionals;
  see `GOVERNANCE_RISK_SECURITY_CHECKLIST.md`.
