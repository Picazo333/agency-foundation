---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - ../FIELD_VALIDATION_PLAN.md
  - ../hypotheses/HYPOTHESIS_REGISTER.md
---
# 13 — Experiment Runbook

> **Instrument type:** run instructions for X-01…X-06 (`FIELD_VALIDATION_PLAN.md` §5).
> Each experiment is specified so it can be executed without further design work, and interpreted
> without overclaiming.

## 1. Rules that apply to every experiment

| # | Rule |
|---|---|
| E-1 | Assignment to arms is **mechanical** (alternation or sequence), never by judgement. Assigning better prospects to your preferred arm guarantees a false positive |
| E-2 | The arm is recorded **at the moment of execution**, never afterwards |
| E-3 | Success, partial and failure conditions are written **before** the first data point |
| E-4 | A stop condition exists and is honoured |
| E-5 | No experiment runs while an earlier-priority hypothesis is untested (H-01 > H-03 > H-10 > H-06 > H-04) |
| E-6 | Results are interpreted with §2 vocabulary. **Never "statistically significant"** |

## 2. Interpretation vocabulary *(use these exact words)*

| Term | Means | Typical n |
|---|---|---|
| **EXISTENCE PROOF** | At least one instance occurred. Cannot be generalised, cannot be dismissed | n ≥ 1 |
| **SIGNAL** | A directional pattern consistent enough to act on provisionally | n ≈ 8–20 |
| **THEMATIC SATURATION** | New observations stop producing new categories | n ≈ 8–15 homogeneous |
| **FALSIFICATION** | A predicted result failed to appear where it should have. The strongest result available at this scale | varies |
| ~~statistically significant~~ | **Never used.** No experiment here has the sample for it | — |

> Falsification is the most valuable outcome this programme can buy. An experiment that cannot fail
> is not an experiment.

---

## X-01 — Teardown response test

| Field | Value |
|---|---|
| **Hypothesis** | H-03; message effectiveness |
| **Decision affected** | D3 — and specifically whether a D3 failure is a *message* or a *segment* problem |
| **Setup** | 40 cold accounts, alternating arms strictly down the ordered target list |
| **Arm A (treatment)** | `06_OUTREACH_SEQUENCE.md` §3 — observation-first opener naming one measured, verifiable thing |
| **Arm B (control)** | Same length, same subject discipline, **no specific observation** — introduces who you are and asks for 25 minutes |
| **Sample** | 20 per arm |
| **Inclusion** | Cold only. Warm contacts excluded — they confound the message effect entirely |
| **Variable** | Presence of a specific observation. Everything else held constant |
| **Data captured** | Ledger: arm, `reply`, reply sentiment, `conversation_held`, `qualified_conversation` |
| **Contamination risks** | Assigning better-fit accounts to arm A · writing arm B carelessly on purpose · running arms in different weeks (seasonality) · a teardown reaching an arm-B account |
| **Confounds** | Segment mix differing between arms; send-day and send-time effects |
| **Success** | Arm A reply rate ≥ 2× arm B → `SIGNAL` that observation-first works |
| **Partial** | A > B but < 2× → weak `SIGNAL`; keep arm A, do not conclude much |
| **Failure** | A ≤ B → the observation is not what earns the reply. **Investigate before adding volume** |
| **Stop** | After 40 sends, or if total reply rate < 8% at 60 contacts (then the problem is both arms) |
| **Interpretation** | n=40 → `SIGNAL` and `EXISTENCE PROOF`. Not a conversion rate |
| **Next action** | Arm A wins → standardise. Arm B wins or ties → rewrite touch 1 before rotating segment |

---

## X-02 — Price-point probe

| Field | Value |
|---|---|
| **Hypothesis** | H-04 |
| **Decision affected** | D5; `PRICING_AND_ECONOMICS_MODEL.md` §4 re-derivation; trigger T-11 |
| **Setup** | First 8 quotes at base; next 7 at base + 25% |
| **Precondition** | **Do not start before 8 conversations have happened** — the base must be observed first |
| **Sample** | 15 quotes |
| **Inclusion** | `QUALIFIED` or `QUALIFIED_WITH_RISK` only |
| **Variable** | The number said aloud. Scope, script and delivery held constant |
| **Data captured** | `11_PRICE_SIGNAL_LOG.md` — arm, seconds to reaction, reaction class, objection, counteroffer, decision |
| **Contamination risks** | **Quoting the higher price only to wealthier-looking buyers** (fatal) · softening delivery on the higher arm · offering a discount · quoting a range |
| **Confounds** | Qualification quality drifting upward over time as the operator improves; segment mix |
| **Success** | A detectable difference in resistance between arms → `SIGNAL` on price elasticity |
| **Partial** | No detectable difference → the range is not the binding constraint; look at trust and problem objections |
| **Failure** | > 70% dismiss immediately in **both** arms → the modelled range is wrong, not the increment |
| **Stop** | 15 quotes, or 5 consecutive immediate dismissals in the base arm (stop and re-derive) |
| **Interpretation** | n=15 → directional `SIGNAL`. A single acceptance is an `EXISTENCE PROOF` that someone pays this, not that the price is correct |
| **Cost** | **Real.** This experiment will lose deals. Accepted: mispricing for a year costs more |
| **Interaction with H-01 / D5** | X-02 arm 2 runs right across the D5 boundary, so the H-01 denominator at day 60 will contain **two different prices**. Rules: (a) a payment at **either** price counts toward H-01 — the hypothesis is "will they pay for diagnosis", not "will they pay exactly this"; (b) at D5, **report the paid count split by arm**; (c) if every base-arm quote converted and every +25% quote failed, that is an H-04 price finding, **not** an H-01 failure — do not route to path C on it; (d) if both arms failed, H-01 and H-04 cannot be separated at this sample — say so rather than picking the more comfortable of the two (finding `DEEP-7`) |
| **Next action** | Fire T-11 on any real price observation; re-derive §4 at the next weekly review |

---

## X-03 — Message-frame test

| Field | Value |
|---|---|
| **Hypothesis** | H-11 — is category language comprehensible and budgetable |
| **Decision affected** | Positioning language; Brand V1 input (`MR-1`) |
| **Setup** | Two one-page variants of the same content: **plain description** (CAT-5) vs **category label** (CAT-1/CAT-2) |
| **Sample** | 12 buyers, shown in-conversation; or two landing variants if traffic exists |
| **Inclusion** | Any interviewed buyer at Phase 5 |
| **Variable** | The self-description only. Body content identical |
| **Data captured** | Interview record Phase 5 verbatim: what would you search for, and **which budget line** |
| **Contamination risks** | Asking which they "prefer" (aesthetic answer, not a buying answer) · showing them after the offer has been explained |
| **Confounds** | Operator enthusiasm differing between variants |
| **Success** | One variant consistently produces a **named budget line** |
| **Partial** | Comprehension similar, budget line unclear in both → keep CAT-5 plain description for cold contexts |
| **Failure** | No buyer can name a budget line for either → the category has no budget owner; dual-frame anchoring becomes mandatory (`AUD-08-01`) |
| **Interpretation** | `THEMATIC SATURATION` at ~10–12 on what buyers call this |
| **Next action** | Adopt the winning language in outreach; log as a Brand V1 requirement, not a brand decision |

---

## X-04 — Concierge pilot

| Field | Value |
|---|---|
| **Hypotheses** | H-06 (baseline capturable), H-12 (delivery fits the hour budget) |
| **Decision affected** | D6 |
| **Setup** | Deliver **one** L1 diagnostic entirely manually. No templates, no automation, nothing reused |
| **Sample** | n=1 |
| **Inclusion** | First paid diagnostic |
| **Data captured** | Actual hours **by phase, logged as worked** · whether a ≥4-week baseline was obtainable and how long access took · rework hours separately · client's own words about the findings' value |
| **Contamination risks** | Reconstructing hours at the end (**systematically under-reports rework**, the single most important number) · over-delivering to protect the relationship and then recording it as standard scope |
| **Confounds** | First-time inefficiency — expect the first to run long; that is information, not failure |
| **Success** | Baseline captured within the window **and** the buyer describes the findings as valuable in their own words |
| **Partial** | Findings valuable but hours > 130% of budget → trigger T-1: re-scope or re-price before selling another |
| **Failure** | No usable baseline obtainable → H-06 fails → **O-0 instrumentation pre-phase becomes mandatory**, timeline extends to 5–6 weeks, and that must be priced and disclosed at the point of sale |
| **Stop** | Delivery complete |
| **Interpretation** | `EXISTENCE PROOF` only. One delivery tells you the thing is possible and roughly what it costs. It does not establish a repeatable cost — that needs D8 |
| **Next action** | Calibrate `A-13` (rework), `A-14` (unbilled sales hours) and the §2.1 hour table from real data |

---

## X-05 — Brand-register test

| Field | Value |
|---|---|
| **Hypothesis** | H-08 — does distinctive visual work reduce trust in this segment |
| **Decision affected** | Gate 1 Brand/Business Fit Review; `BRAND_BUSINESS_INTERFACE.md` §7 test T-B7 |
| **Setup** | Two versions of the **same** one-page method document: plain/professional vs the distinctive register |
| **Sample** | 8 buyers |
| **Inclusion** | Interviewed buyers, shown at the end of the conversation |
| **Variable** | Visual register only. **Identical words** |
| **Data captured** | Unprompted reaction verbatim; which they would forward to a colleague; whether either changes their stated willingness to proceed |
| **Contamination risks** | Asking "which do you prefer?" — an aesthetic question, not a trust question. **Ask which they would forward to their business partner.** That is a trust question · operator revealing which one is "theirs" |
| **Confounds** | Order effects — alternate which is shown first |
| **Success** | No consistent trust penalty for the distinctive register → `SIGNAL` that register separation is unnecessary |
| **Partial** | Mixed reactions → keep the register separation in `BRAND_BUSINESS_INTERFACE.md` §2 (plain at the door, distinctive at the table) |
| **Failure** | Consistent negative trust reaction → Gate 1 **MUTATE**, not KILL. Tighten the plain register; move figurative elements further back in the funnel |
| **Interpretation** | `SIGNAL` at n=8. Qualitative reaction, not preference share |
| **Note** | **This is the test most likely to produce an uncomfortable result** (`E-24`). Its purpose is to make Gate 1 evidence-based rather than taste-based. Run it even if — especially if — you would rather not |

---

## X-06 — Partner-channel probe

| Field | Value |
|---|---|
| **Hypothesis** | CH-3 viability; feeds `DECISION_TREE.md` pivot P-C |
| **Decision affected** | Whether partnership-led entry is a real fallback if D3 fails twice |
| **Setup** | Approach 5 intermediaries (PMS/EMR vendors, accountants, practice consultants, non-competing agencies) with `06_OUTREACH_SEQUENCE.md` §7 |
| **Sample** | 5 |
| **Inclusion** | Serves the primary segment; does not compete on operational measurement |
| **Data captured** | Do they recognise the implementation gap in their clients? Would they co-deliver a pilot? What economics would they expect? |
| **Contamination risks** | **Treating intermediary confirmation as buyer evidence.** It is not. An intermediary's view of their clients' problems never counts toward H-10 and is excluded from that denominator |
| **Confounds** | Intermediaries are professionally agreeable; they agree with plausible propositions at very low cost |
| **Success** | ≥ 1 agrees to a pilot referral → `EXISTENCE PROOF` that P-C is available |
| **Partial** | Interest but no commitment → partnerships are slower than CH-1; keep seeded at low effort |
| **Failure** | 0 of 5 → P-C is not a live fallback. **This materially raises the cost of a D3 failure** and should be reported at the weekly review |
| **Interpretation** | `EXISTENCE PROOF` at n=5, nothing more |

---

## 2b. Hypotheses outside this kit's window

Three hypotheses cannot be tested inside the 90-day validation window because they require
delivered work. They are listed here so their absence is deliberate rather than an oversight, and
so the capture location exists before it is needed.

| Hypothesis | Earliest testable | Captured where | Gate |
|---|---|---|---|
| **H-12** — delivery fits the hour budget within 130% | First paid diagnostic delivered (~week 10) | Time log, **by phase, logged as worked, rework separate** (`DELIVERY_OS.md` §11). Surfaced via X-04 | D6, day 90 |
| **H-09** — 40% of cores attach an operated layer | After **3 delivered cores** (~month 5–6) | Engagement records; offered at day 21 of each build, not post-launch (`OFFER_ARCHITECTURE.md` §6.1) | **D9, day 180 — outside this kit** |
| **H-05** — sales cycle 30–60 days | First payment | `12_DIAGNOSTIC_SALES_ATTEMPT_LOG.md` field `days_quote_to_payment`; median reported weekly | Informs D5 timing and cash planning |

**Do not attempt to bring H-09 forward.** `FIELD_VALIDATION_PLAN.md` §2 is explicit: do not test
H-09 before H-01. An operated layer offered before a core has been delivered tests nothing and
burns the relationship.

## 3. Sequencing

| Weeks | Running | Precondition |
|---|---|---|
| 2–6 | X-01 | Target list exists |
| 4–8 | X-06 | — |
| 6–9 | X-02 | ≥ 8 conversations held |
| 5–8 | X-03 | Interviews reaching Phase 5 |
| 7–9 | X-05 | Both document variants exist |
| 9–12 | X-04 | First paid diagnostic sold |

**Never run more than two experiments at once.** Three concurrent experiments on one operator's
outreach make every result uninterpretable, because the arms interact and nobody can say which
change produced which effect.

## 3b. The time log *(information-efficiency finding `IE-1`)*

`A-13` (rework), `A-14` (unbilled sales hours), H-12, M-10 and M-41 all depend on hours data, and
nothing in the plan defines how to capture it. Without this the operator invents a convention, or
more likely reconstructs hours at month end — which **systematically under-reports rework**, the
single most sensitive variable in the economic model.

**Template:** `data/time_log.csv`

| Field | Rule |
|---|---|
| `date` | — |
| `category` | `outreach` / `research` / `teardown` / `interview` / `admin` / `delivery` / `rework` / `planning` |
| `account_id` | where attributable |
| `hours` | decimal |
| `billable` | `Y`/`N` |
| `notes` | — |

**Three rules that make it worth keeping:**

1. **Log as worked, not at the end of the week.** Reconstruction under-reports rework because
   rework does not feel like a separate activity while you are doing it.
2. **`rework` is its own category**, never folded into `delivery`. The whole point is the split.
3. **`planning` is a category** — and its weekly total is read out at the review. It is the direct
   measure of the `RED_TEAM_REVIEW.md` RT-01 failure mode, and the only one that cannot be argued
   with.

**Weekly rollups:** outreach hours (M-41) · hours per qualified conversation · unbilled sales hours
per opportunity (M-10, `A-14`) · rework ÷ delivery (`A-13`) · **planning hours** (RT-01 watch).

## 4. Per-experiment result block

```markdown
## [X-0N] result — [date]
n: ___ (planned ___)
Arms / conditions:
Raw result:
Classification: EXISTENCE PROOF | SIGNAL | THEMATIC SATURATION | FALSIFICATION | INCONCLUSIVE
Contamination observed: none | [what]
Confounds I cannot rule out:
What this does NOT show:
Decision this changes:
Assumption updated (A-##):
Next action:
```

The **"what this does NOT show"** field is mandatory. It is the field that prevents an experiment
from quietly becoming a belief.
