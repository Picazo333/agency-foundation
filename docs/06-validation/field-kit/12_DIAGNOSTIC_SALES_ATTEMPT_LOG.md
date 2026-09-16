---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - ../FIELD_VALIDATION_PLAN.md
  - ../../02-strategy/thesis/DECISION_TREE.md
  - 09_QUALIFICATION_SCORECARD.md
  - 11_PRICE_SIGNAL_LOG.md
---
# 12 — Diagnostic Sales Attempt Log (H-01)

> **Instrument type:** the decisive evidence log. **CSV:** `data/sales_attempt_log.csv`.
> **Hypothesis:** H-01 — the buyer will pay for a diagnostic before implementation. **Priority 1.**
> **Gate:** D5, day 60. **Pass: ≥ 2 paid diagnostics from ≤ 20 qualified conversations.**
>
> Every other instrument in this kit produces `SIGNAL`. This one can produce `FACT`, and it is the
> only one that can.

## 1. What counts as an attempt

An attempt is logged when the L1 diagnostic was **described with a specific price to a buyer who
passed qualification**. All three required.

**Not an attempt:** mentioning that you do diagnostics · an unqualified buyer hearing the offer ·
describing it without a number · a conversation that never reached Phase 6.

Logging non-attempts inflates the denominator and makes a real failure look like a near miss.

## 2. What counts as a sale

> **Money received and cleared. Nothing else.**

| Not a sale | Why |
|---|---|
| "Yes, let's do it" | Verbal intent (`11_PRICE_SIGNAL_LOG.md` §2) |
| Signed proposal, unpaid | Signature is not cash |
| "Invoice me" | — |
| Verbal agreement pending a partners' meeting | Especially not this one |
| A discounted sale | Excluded from H-01 — it tested your willingness to discount |
| A free diagnostic delivered to build goodwill | Tests nothing; also violates `DNS-13` |

## 3. Fields

| Field | Values |
|---|---|
| `attempt_id` | `S-0NN` |
| `date`, `account_id`, `interview_id`, `quote_id` | — |
| `qualification_status` | must be `QUALIFIED` / `QUALIFIED_WITH_RISK` — else not an attempt |
| `offer_made` | `L1 diagnostic` / `L1 + O-0` |
| `price_quoted` | single number |
| `scope_stated` | `Y`/`N` — was scope and exclusions actually stated? |
| `signer_present` | `Y`/`N` (H-03b) |
| `reaction_verbatim` | their exact words |
| **`objection_primary`** | `price` / `trust` / `problem` / `authority` / `timing` / `none` |
| `objection_price` | `Y`/`N` — "too expensive", counteroffer, budget absent |
| `objection_trust` | `Y`/`N` — "no references in our sector", unproven supplier |
| `objection_problem` | `Y`/`N` — does not accept the problem is worth money |
| `objection_authority` | `Y`/`N` — cannot authorise, needs others |
| `objection_timing` | `Y`/`N` — not now |
| `result` | `paid` / `verbal_yes_unpaid` / `pending` / `declined` / `ghosted` |
| `loss_code` | `L-01`…`L-13` |
| **`payment_received`** | `Y`/`N` — **cleared funds only** |
| `payment_date`, `payment_amount` | — |
| `days_quote_to_payment` | H-05 evidence |
| `discount_offered` | `Y`/`N` — **`Y` invalidates the row for H-01** |
| `free_alternative_offered` | `Y`/`N` — see §5 |
| `evidence_grade` | `FACT` only when `payment_received = Y` |
| `follow_up_action`, `follow_up_date` | — |

## 4. D5 interpretation rules *(binding — `DECISION_TREE.md` D5)*

```
qualified_conversations = count(qualification_status ∈ {QUALIFIED, QUALIFIED_WITH_RISK})
paid                    = count(payment_received = Y AND discount_offered = N)
```

| Condition | Path | Action |
|---|---|---|
| `paid ≥ 2` by day 60 | **A — thesis holds** | → D6. H-01 supported (`SIGNAL`, with `FACT`-grade payment events) |
| `paid = 1` | **Partial** | Extend 15 days. If still 1 → treat as fail and run the §4.1 diagnosis |
| `paid = 0` but ≥ 1 core sold after a **free** teardown | **B — free-wedge fallback** | `A-07` false. Wedge becomes free, with stated costs. Model mutates to M3+M6. → D6 |
| `paid = 0` and no core sold, from ≥ 20 qualified | **C — no monetisation** | → §4.1 diagnosis, then D7 |
| 0 paid **and** < 20 qualified at day 60 | **UNDER-SAMPLED** | `15_DECISION_GATE_CHECKLIST.md` §D5-U. Named cause + re-gate within 14 days + strike. **Never a neutral hold.** A **pass at ≥2 paid is called at any denominator** |

### 4.1 Path C diagnosis — required before any action

Four causes, opposite remedies. Read from the objection columns, not from impression.

| Dominant objection | Cause | Remedy |
|---|---|---|
| `objection_price` | **Price** | Re-test at a lower point **before** killing. The offer may be right and the number wrong |
| `objection_trust` | **Trust** | Proof-ladder gap. Get one pilot at ≥60% of base with a written case-study agreement (`PRICING_AND_ECONOMICS_MODEL.md` §7.1) |
| `objection_problem` | **Problem** | Thesis is wrong. D4b already failed → D7 |
| `objection_authority` | **Wrong buyer** | Qualification failure, not model failure. Tighten Q3, re-run 15 days |

**Pre-commitment:** at path C, a pivot option is selected and **written into an ADR within 7 days**
(`FIELD_VALIDATION_PLAN.md` §6). This exists because "let's give it another month," repeated three
times, is how a 90-day validation becomes an 18-month drift.

## 5. The free-alternative rule

> **Disambiguation first — these are two different things and conflating them corrupts H-01.**
>
> | | What it is | Status |
> |---|---|---|
> | **L0 teardown** | The free, 3-hour, asynchronous observation piece that opens the conversation | **Always free, by design.** Sending one is never a "free alternative". `free_alternative_offered` stays `N` |
> | **Free alternative** | Giving away the **L1 diagnostic** — the paid measurement — at no charge | **Prohibited** until 15 qualified attempts have failed |
>
> D5 path B ("core sold after a free teardown") refers to the L0 teardown doing the wedge's job
> without a paid diagnostic in between. It does **not** mean a diagnostic was given away.
>
> Marking `free_alternative_offered = Y` because you sent a teardown would invalidate every row in
> this log as H-01 evidence. Marking it `N` after giving away a diagnostic hides the one violation
> the column exists to catch.

`FIELD_VALIDATION_PLAN.md` §3 H-01: *no free alternative is offered unless and until 15 qualified
attempts have failed.*

Offering free early destroys the test — you never learn whether they would have paid, and you
cannot un-learn it. The `free_alternative_offered` column exists so that any violation is visible
in the data rather than remembered charitably.

| Attempts so far | Free alternative permitted? |
|---|---|
| < 15 failed attempts | **No** |
| ≥ 15 failed attempts | Yes — and this is D5 path B by definition |

## 6. What NOT to conclude

| Observation | Tempting reading | Correct reading |
|---|---|---|
| Buyer enthusiastic, no payment | "Nearly sold" | Zero evidence. Enthusiasm is free |
| Verbal yes, awaiting a partners' meeting | "One sale" | Not a sale. `verbal_yes_unpaid` |
| Sold after discounting | "H-01 supported" | Excluded. You proved you will discount |
| 1 sale from 5 attempts | "20% conversion" | n=5 cannot produce a rate. Existence proof only |
| Several "let me think about it" | "Warm pipeline" | Usually a soft no. Run probe 3 to get the reason |
| Sale to a warm contact | "The model works" | A relationship bought it. Note `source=warm`; the cold arm is still untested |

That last row matters at D5: **if both paid diagnostics came from warm contacts, H-01 is supported
only for warm buyers.** Record it explicitly at the gate rather than passing on a misread.

## 7. CSV format

```csv
attempt_id,date,account_id,interview_id,quote_id,qualification_status,offer_made,price_quoted,scope_stated,signer_present,reaction_verbatim,objection_primary,objection_price,objection_trust,objection_problem,objection_authority,objection_timing,result,loss_code,payment_received,payment_date,payment_amount,days_quote_to_payment,discount_offered,free_alternative_offered,evidence_grade,follow_up_action,follow_up_date
```

### SYNTHETIC EXAMPLE — NOT EVIDENCE
*Format illustration only. No offer was made to anyone. Never count or cite. Delete before use.*

```csv
S-000,2026-09-16,A-000,I-000,Q-000,QUALIFIED,L1 diagnostic,2400,Y,Y,"[SYNTHETIC — NOT A REAL QUOTE]",authority,N,N,N,Y,N,pending,,N,,,,N,N,NONE,Ask for 20 min with signer,2026-09-23
```

## 8. Running tally for the weekly review

| Measure | Formula |
|---|---|
| Qualified conversations to date | count of qualified |
| Attempts | count of rows |
| **Paid (undiscounted)** | `payment_received=Y ∧ discount_offered=N` |
| Verbal-yes-unpaid | `result=verbal_yes_unpaid` — **report separately, never combined with paid** |
| Objection distribution | count by `objection_primary` |
| Warm vs cold among paid | split by ledger `warm_cold` |
| Median days quote → payment | H-05 |
