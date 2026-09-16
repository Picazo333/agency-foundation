---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - ../../02-strategy/pricing/PRICING_AND_ECONOMICS_MODEL.md
  - ../../07-decisions/ADR-0009-defer-pricing-freeze.md
  - ../FIELD_VALIDATION_PLAN.md
---
# 11 — Price Signal Log (H-04)

> **Instrument type:** price-evidence log. **CSV:** `data/price_signal_log.csv`.
> **Hypothesis:** H-04 — price tolerance falls within the modelled ranges.
> **Sample:** 15 quotes. **Pass:** ≥ 40% engage with the price. **Fail:** > 70% dismiss immediately.
> **Outcome:** converts `INFERRED RANGE` → `PRICE SIGNAL`, fires trigger **T-11**.

## 1. The evidence ladder — the point of this instrument

The program currently holds **zero** price observations (`E-22`, `ADR-0009`). Everything in
`PRICING_AND_ECONOMICS_MODEL.md` §4 is constructed from capacity logic. This log exists to change
that — and to stop the change happening prematurely, in the direction the founder would prefer.

| Level | What it is | Evidence grade | Counts as |
|---|---|---|---|
| **INTEREST** | "That sounds useful" / "interesting" / positive body language | **NONE** | Nothing. Record it, never count it |
| **VERBAL INTENT** | "Yes, let's do it" / "send me the paperwork" / "I'm in" | **NONE** | Nothing. See §2 |
| **PRICE SIGNAL** | A substantive reaction to a **specific number**: a counteroffer, a budget statement, a comparison to prior spend, a considered decline citing price | `SIGNAL` | H-04 evidence |
| **PAYMENT** | Money received and cleared | **`FACT`** | H-01 evidence; the only `FACT` in the system |

> **Only the bottom row is money evidence.** `EVIDENCE_AND_ASSUMPTIONS_REGISTER.md` §5: the only
> `FACT`-grade evidence in commercial validation is money received.

## 2. Why verbal intent scores zero

"Yes, let's do it" from an enthusiastic buyer converts at a rate this program has no data on, and
the gap between verbal yes and cleared payment is where new suppliers lose months. Counting verbal
intent as validation is how a business reaches day 90 believing it has three customers and holding
no money.

**Operational rule:** a deal does not exist until the payment clears. Not on signature. Not on
"invoice me." `12_DIAGNOSTIC_SALES_ATTEMPT_LOG.md` enforces the same boundary.

## 3. The quote procedure *(H-04 test protocol — follow exactly)*

Run only when the qualification scorecard returned `QUALIFIED` or `QUALIFIED WITH RISK`.

**Probe 1 — prior spend, before any number of yours:**
> "Before I give you a number — have you spent money on anything in this area before? Roughly what
> sort of level?"

Record verbatim. This is the cleanest anchor-free budget data available, and it is lost forever
once you name a price.

**Probe 2 — quote once, then stop talking:**
> "The diagnostic is [single number]. That covers [scope]; you keep the instrumentation either way."

Then **silence.** Do not justify, do not soften, do not add "but we can be flexible." The first
reaction is the measurement. Count the seconds before they speak and record it.

| Binding rules | |
|---|---|
| **One number, never a range** | Ranges anchor to the bottom (H-04 confound, `FIELD_VALIDATION_PLAN.md` §3) |
| **Never explain the price by naming your tools** | `POSITIONING_ARCHITECTURE.md` §7 |
| **Never discount** | `DNS-13`; a discounted yes tests nothing and destroys the anchor |
| **Never quote to an unqualified buyer** | Wastes the single most valuable data point you get from them |
| Reduce scope if pressed, never price | `PRICING_AND_ECONOMICS_MODEL.md` §7 |

**Probe 3 — on loss, the close-out:**
> "That's fine. Was it the number, or the thing itself?"

This separates `L-02` (price too high, value understood) from `L-03` (value not understood) from
`L-07` (no perceived problem) — three findings with three completely different remedies.

## 4. X-02 price-point probe

`FIELD_VALIDATION_PLAN.md` §5: base to the first 8 quotes, base + 25% to the next 7.

| Rule | |
|---|---|
| Do not start until **8 conversations** have happened, so the base has been observed first | — |
| Assign by **sequence**, not by how wealthy the buyer looks | Assigning the higher price to better prospects guarantees a false positive |
| Record the arm **at the moment of quoting** | Retrospective assignment is fabrication |
| n=15 is a directional `SIGNAL`, never a statistically significant result | §7 |

**This experiment costs real deals.** That is accepted: pricing an unvalidated offer for a year is
more expensive than losing one engagement.

## 5. Fields

| Field | Values / rule |
|---|---|
| `quote_id` | `Q-0NN` |
| `date`, `account_id`, `interview_id` | — |
| `qualification_status` | must be `QUALIFIED` or `QUALIFIED_WITH_RISK` |
| `offer` | `L1 diagnostic` / `O-0` / `L2 C-1` / `L2 C-2` |
| `price_quoted` | the single number actually said aloud |
| `x02_arm` | `base` / `base+25` / `n/a` — recorded at quote time |
| `prior_spend_stated` | verbatim from probe 1 |
| `seconds_to_first_reaction` | integer |
| `reaction_verbatim` | **their exact words** |
| `reaction_class` | `engaged` / `neutral` / `dismissed_immediately` / `counteroffer` / `deferred` |
| `objection_primary` | `price` / `trust` / `problem` / `authority` / `timing` / `none` |
| `budget_context` | verbatim; budget line named, if any (H-11) |
| `counteroffer_amount` | if any |
| `decision` | `accepted` / `declined` / `pending` |
| `loss_code` | `L-01`…`L-13` if declined |
| **`payment_received`** | `Y` / `N` — **Y only when funds have cleared** |
| `payment_date`, `payment_amount` | — |
| `evidence_level` | `INTEREST` / `VERBAL_INTENT` / `PRICE_SIGNAL` / `PAYMENT` |
| `evidence_grade` | `NONE` / `SIGNAL` / `FACT` — **`FACT` requires `payment_received = Y`** |
| `discount_offered` | `Y`/`N` — **any `Y` invalidates this row as H-01 evidence** |

### 5.1 Why `evidence_level` and `evidence_grade` are both recorded

They are deterministically related, so recording both is double entry — kept deliberately as a
consistency check, not as extra data (information-efficiency finding `IE-2`). Any row where the two
disagree is a logging error and is corrected at the weekly review.

| `evidence_level` | must imply `evidence_grade` |
|---|---|
| `INTEREST` | `NONE` |
| `VERBAL_INTENT` | `NONE` |
| `PRICE_SIGNAL` | `SIGNAL` |
| `PAYMENT` | `FACT` |

The pairing exists because `VERBAL_INTENT → NONE` is the mapping an optimistic operator most wants
to break, and writing both columns forces the contradiction into view.

## 6. Classifying the reaction

| Class | Looks like | Counts as |
|---|---|---|
| `engaged` | Asks what it covers, how long, when you could start; compares to prior spend; counteroffers | **PRICE SIGNAL** — the H-04 pass condition |
| `neutral` | "OK." / "Let me think." / no substantive engagement | Weak signal |
| `dismissed_immediately` | Visible rejection within seconds, no engagement with scope | **PRICE SIGNAL** — the H-04 fail condition |
| `counteroffer` | Proposes a different number | **Strongest possible PRICE SIGNAL.** Record the number exactly |
| `deferred` | "Not now, maybe later" | Usually `L-06`, sometimes a soft no |

**H-04 calculation:** `engaged + counteroffer` ÷ total quotes.
Pass ≥ 40%. Fail if `dismissed_immediately` > 70%.

## 7. Interpretation rules

1. At n=15 this is a **directional `SIGNAL` and an existence proof**. Never "statistically
   significant."
2. A single acceptance proves **existence** — that at least one buyer will pay this — not that the
   price is right.
3. Zero dismissals is a warning, not a triumph: **the price is probably too low** (trigger T-3
   logic). Record it as such.
4. A discounted acceptance is **excluded** from H-04 and H-01. It measures your willingness to
   discount.
5. On any real price observation, fire **T-11**: `INFERRED RANGE` → `PRICE SIGNAL`, and re-derive
   `PRICING_AND_ECONOMICS_MODEL.md` §4 at the next weekly review.
6. **No observed price may be published anywhere** until `ADR-0009` is revisited by the human owner.

## 8. CSV format

```csv
quote_id,date,account_id,interview_id,qualification_status,offer,price_quoted,x02_arm,prior_spend_stated,seconds_to_first_reaction,reaction_verbatim,reaction_class,objection_primary,budget_context,counteroffer_amount,decision,loss_code,payment_received,payment_date,payment_amount,evidence_level,evidence_grade,discount_offered
```

### SYNTHETIC EXAMPLE — NOT EVIDENCE
*Format illustration only. No quote was given to anyone. Never count or cite. Delete before use.*

```csv
Q-000,2026-09-16,A-000,I-000,QUALIFIED,L1 diagnostic,2400,base,"[SYNTHETIC]",6,"[SYNTHETIC — NOT A REAL QUOTE]",engaged,none,"[SYNTHETIC]",,pending,,N,,,PRICE_SIGNAL,SIGNAL,N
```
