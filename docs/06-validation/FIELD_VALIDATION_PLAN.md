---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - DECISION_TREE.md
  - AGENCY_THESIS.md
  - EVIDENCE_AND_ASSUMPTIONS_REGISTER.md
---
# Field Validation Plan

> **Module 18 of the Agency Master Plan** (Issue #2 Phase 15). The mandatory module. Everything
> else in this plan is reasoning; this is the part that produces evidence.
>
> `E-09` is a `FACT`: **zero buyer contact has occurred.** This plan exists to change that fact as
> quickly and as informatively as possible.
>
> ## ▶ To execute this plan, open [`field-kit/00_README.md`](field-kit/00_README.md)
>
> The **Field Validation Execution Kit** turns everything below into ready-to-run instruments:
> target ledger, research and teardown SOPs, outreach sequences, an interviewer-ready script,
> evidence logs for H-01/H-04/H-10, an experiment runbook, a weekly review and operator checklists
> for every gate. Start at [`field-kit/16_VALIDATION_LAUNCH_CHECKLIST.md`](field-kit/16_VALIDATION_LAUNCH_CHECKLIST.md).
>
> The kit **implements** this plan and changes no threshold, hypothesis or decision rule in it.
> Coverage map: [`field-kit/17_TRACEABILITY_MATRIX.md`](field-kit/17_TRACEABILITY_MATRIX.md).

## 1. Method note — what this plan can and cannot establish

Qualitative validation at n=12–20 does **not** produce statistically significant results, and any
document claiming otherwise is misusing the word. What it produces is:

| Achievable | Not achievable |
|---|---|
| **Thematic saturation** — the point at which new conversations stop producing new problem framings (typically 8–15 in a homogeneous segment) | Statistically significant conversion or pricing estimates |
| **Existence proof** — at least some buyers have this problem and will pay | Market sizing |
| **Falsification** — nobody in 20 conversations recognises the problem, which is decisive | Confidence intervals |
| **Real buyer language** — replacing synthetic VoC (`E-05`) | Reliable segment-wide generalisation |
| **Access measurement** — how hard these people are to reach, which is directly observed, not inferred | — |

Evidence obtained here is graded `SIGNAL`, never `FACT` (`EVIDENCE_AND_ASSUMPTIONS_REGISTER.md` §5
rule 2). **The only `FACT`-grade evidence in commercial validation is money received.** That is why
the D5 monetisation gate outranks every interview.

## 2. Hypotheses, ranked by risk

Ranking = (probability of being wrong) × (cost if wrong). Test in this order; do not test H-09
before H-01.

| ID | Hypothesis | Grade | If false | Gate | Priority |
|---|---|---|---|---|---|
| **H-01** | The target buyer will pay for a diagnostic before implementation | `HYPOTHESIS` (`A-07`) | Entry wedge collapses → D5 path B | D5 | **1** |
| **H-03** | 8+ qualified conversations are reachable in 30 days in the primary segment | `HYPOTHESIS` | Segment rotation; possibly a distribution problem, not a segment problem | D3 | **2** |
| **H-10** | Buyers recognise the revenue-leak problem unprompted | `HYPOTHESIS` | Thesis' core claim fails → reframe or kill | D4 | **3** |
| **H-06** | A usable baseline can be captured in ≤ 2 weeks | `HYPOTHESIS` (`U-08`) | Proof engine breaks; O-0 pre-phase required | D6 | **4** |
| **H-04** | Price tolerance for L1/L2 falls within the modelled ranges | `UNKNOWN` (`U-07`) | Re-derive the entire pricing model | D5 | **5** |
| **H-09** | 40% of delivered cores attach an operated layer | `HYPOTHESIS` (`A-11`) | Project-only economics; weaker but survivable | D9 | 6 |
| **H-03b** | The signer is reachable directly | `HYPOTHESIS` (`U-09`) | Sales cycle lengthens; Q3 gate tightens | D5 | 7 |
| **H-07** | No local competitor already occupies this position | `UNKNOWN` (`U-12`) | Differentiation collapses to execution | D4 | 8 |
| **H-08** | Distinctive visual work does not reduce trust in this segment | `HYPOTHESIS` (`E-24`) | Brand/business conflict → Gate 1 MUTATE | Gate 1 | 9 |
| **H-11** | Category language is comprehensible and budgetable | `HYPOTHESIS` | Revert to CAT-5 plain description | D4 | 10 |
| **H-12** | Delivery fits the hour budget within 130% | `HYPOTHESIS` | Re-price or narrow scope (T-1) | D6 | 11 |
| **H-05** | Sales cycle is 30–60 days | `HYPOTHESIS` (`A-10`) | Cash-flow timeline extends; runway pressure | D5 | 12 |

## 3. Hypothesis test designs

### H-01 — Paid diagnostic *(the decisive test)*

| Field | Specification |
|---|---|
| **Test** | Offer the L1 diagnostic at the base price to every qualified buyer. No free alternative offered unless and until 15 qualified attempts have failed |
| **Evidence threshold** | **Money received.** Verbal agreement, "send me a proposal", and enthusiasm are all worth zero |
| **Sample** | 20 qualified conversations |
| **Pass** | ≥ 2 paid diagnostics by day 60 |
| **Partial** | 1 sold → extend 15 days; if still 1, treat as fail and diagnose |
| **Fail** | 0 from 20 → D5 path C, with the four-cause diagnosis in `DECISION_TREE.md` D5 |
| **Confound to avoid** | Discounting to force a sale. A discounted yes tests nothing and destroys the anchor (`DNS-13`) |
| **Secondary data** | At what point in the conversation does resistance appear? Price, trust, problem, or authority? |

### H-03 — Access

| Field | Specification |
|---|---|
| **Test** | Run CH-1 outbound at 15–20 new targets/week with 4 touches, plus CH-2 warm |
| **Evidence** | Count of qualified conversations (M-03) |
| **Sample** | 60 targets over 30 days |
| **Pass** | ≥ 8 qualified |
| **Fail** | < 4 → diagnose *channel vs message vs segment* before rotating (`DECISION_TREE.md` D3b) |
| **Confound** | A bad message looks exactly like a bad segment. Fix the message first — it is cheaper and faster |

### H-10 — Problem resonance

| Field | Specification |
|---|---|
| **Test** | In the first 12 minutes of discovery, ask open questions only. Record whether the buyer volunteers a version of the revenue-leak problem **before** it is described to them |
| **Evidence** | Verbatim transcript excerpts, logged per conversation |
| **Sample** | 10 conversations |
| **Pass** | ≥ 5/10 unprompted |
| **Fail** | ≤ 1/10 → thesis' core claim is false in this segment |
| **Confound** | **Leading questions.** "Do you lose enquiries?" invalidates the test. The permitted form is "walk me through what happens when someone enquires" |
| **Bonus output** | The messaging corpus (`POSITIONING_ARCHITECTURE.md` §3) |

### H-04 — Willingness to pay

| Field | Specification |
|---|---|
| **Test** | Three probes, in this order: (1) "What have you spent on this kind of thing before?" (2) Quote the diagnostic and observe the reaction before speaking again. (3) On loss, the close-out message asking why |
| **Evidence** | `PRICE SIGNAL` — the first real price data the program will ever hold (`E-22`) |
| **Sample** | 15 quotes |
| **Pass** | ≥ 40% engage with the price rather than dismissing it |
| **Fail** | >70% dismiss immediately → the range is wrong, not the offer |
| **Confound** | Anchoring. Never state a range "from X to Y"; state one price |
| **Outcome** | Converts `INFERRED RANGE` → `PRICE SIGNAL` and fires T-11 |

### H-06 — Baseline availability

| Field | Specification |
|---|---|
| **Test** | In discovery, ask exactly what is recorded today: enquiry timestamps, source, booking outcome, no-shows |
| **Evidence** | Count of buyers with reconstructable history |
| **Sample** | 12 conversations |
| **Pass** | ≥ 50% have ≥ 4 weeks of reconstructable data |
| **Fail** | < 25% → O-0 instrumentation pre-phase becomes mandatory (`OFFER_ARCHITECTURE.md` §3.2) and the time-to-findings extends to 5–6 weeks, which must then be priced and sold as such |

### H-09 — Recurring attachment

Tested only after 3 delivered cores. Offered at day 21 of the build, not post-launch
(`OFFER_ARCHITECTURE.md` §6.1). Pass: ≥ 1 of 3. Fail: 0 of 3 → redesign L3 value delivery; do not
discount.

### H-07 — Competitive position

| Field | Specification |
|---|---|
| **Test** | (a) Ask every buyer "who else have you looked at for this?"; (b) structured search for suppliers positioning on operations rather than marketing in the local market |
| **Evidence** | Named competitors and their positioning — the first real data against `U-12` |
| **Fail condition** | A local supplier is already established in this exact position with references |
| **Response if failed** | Differentiate on vertical depth or method rigor, or move segment. **Do not compete on price** |

### H-08 — Brand/trust interaction

| Field | Specification |
|---|---|
| **Test** | Two variants of the same one-page method document — one plain/professional, one in the distinctive register — shown to buyers for reaction. Not A/B traffic testing; direct qualitative reaction |
| **Evidence** | Reactions, and whether either affects willingness to proceed |
| **Sample** | 8 buyers |
| **Interpretation** | This is the most likely test to produce an *uncomfortable* result (`E-24`). Its purpose is to make Gate 1 evidence-based rather than taste-based |
| **Feeds** | `BRAND_BUSINESS_INTERFACE.md` §7; `BRAND_BUSINESS_FIT_REVIEW.md` |

### H-11 — Category language

Ask buyers to describe, in their own words, what they would call a supplier who does this, and
which budget it would come from. The budget answer matters more than the label: a category that
maps to no budget line cannot be bought (`POSITIONING_ARCHITECTURE.md` §2.1). Sample 12.

## 4. Interview programme

### 4.1 Targets

| Type | Count | Purpose |
|---|---|---|
| Primary-segment decision makers (S2 owners/directors) | 12–15 | H-01, H-03, H-04, H-06, H-10, H-11 |
| Primary-segment operators (administrators, coordinators) | 5–8 | Operational reality; champion identification |
| Hedge-segment buyers (S7) | 5–8 | Comparative signal |
| Intermediaries (PMS vendors, accountants, consultants) | 3–5 | CH-3 partnerships; indirect market view |
| Adjacent suppliers (non-competing agencies) | 2–3 | Competitive landscape (H-07), pricing signal |

### 4.2 Interview guide requirements

**Structure:** context (5 min) → **open narrative, no leading (12 min)** → mechanics (10 min) →
measurement (5 min) → consequence and prior attempts (5 min) → process and authority (3 min).

**Rules:**
1. **Never describe the offer before the open-narrative segment ends.** It contaminates H-10, which
   is the most valuable output of the conversation.
2. Record with permission; if refused, take verbatim notes.
3. Log the buyer's own words, not a paraphrase.
4. Log the date, role, segment, source and how contact was made.
5. Log what was *not* said — an expected pain that never comes up is data.
6. Log the interview within 24 hours or the verbatim quality is lost.

**Prohibited:** "Would you buy…?" (answers are unreliable), "Do you have problem X?" (leading),
pitching during discovery, and any question whose answer you would be disappointed by.

### 4.3 Where interviews are recorded

`docs/06-validation/interviews/`, one file per interview, with a standard front-matter block:
date · role · segment · location · source · duration · consent status · hypotheses touched ·
verbatim excerpts · observations · what surprised me.

**The "what surprised me" field is mandatory and is the most valuable line in the file.** Surprise
is the only reliable signal that a real assumption just moved.

## 5. Non-interview experiments

| ID | Experiment | Tests | Design | Success | Cost |
|---|---|---|---|---|---|
| X-01 | **Teardown response test** | H-03, message | 20 observation-first vs 20 generic-value outreach | Observation-first reply rate ≥ 2× generic | Hours only |
| X-02 | **Price-point probe** | H-04 | Quote base to the first 8, base+25% to the next 7. Observe reaction, not just outcome | A detectable difference in resistance | Hours; real deal risk |
| X-03 | **Message-frame test** | H-11 | Two landing variants: plain description vs category label | Meeting-booking rate | Hours |
| X-04 | **Concierge pilot** | H-06, H-12 | Deliver one diagnostic fully manually, no templates | Findings that a buyer calls valuable | 30–40 hours |
| X-05 | **Brand-register test** | H-08 | §3 H-08 design | Qualitative reactions | Hours |
| X-06 | **Partner-channel probe** | CH-3 | Approach 5 intermediaries with the co-delivery pitch | ≥ 1 agrees to a pilot referral | Hours |

**X-02 carries real cost:** it risks losing deals to learn about price. It is worth running anyway,
because pricing an unvalidated offer for a year is more expensive than losing one deal. Run it only
after 8 conversations, so the base price has been observed first.

## 6. Kill, pivot and continue criteria

| Result | Meaning | Action |
|---|---|---|
| H-03 fail twice after rotation | Distribution problem, not segment problem | `DECISION_TREE.md` D7 → pivot P-C (partnership-led) or P-D |
| H-10 fail (≤1/10) | The thesis' problem claim is false here | D4b reframe once, then D7 |
| H-01 fail (0/20) | Buyers will not fund diagnosis | D5 path B (free wedge) or path C |
| H-01 fail **and** H-10 fail **and** H-03 fail | The model does not work | **Kill.** `AGENCY_THESIS.md` §1.3 |
| H-04 shows tolerance far below model | Economics do not work at achievable prices | Re-derive; if break-even is unreachable at market prices, the model is not viable at this scale |
| H-06 fail | No baselines available | O-0 becomes mandatory; re-price and re-time |
| H-07 fail | Position already occupied | Differentiate or move; never compete on price |
| H-08 fail | Brand suppresses trust | Gate 1 MUTATE — not a business kill |
| H-09 fail | No recurring layer | Continue as project business with weaker economics; say so explicitly |

**Kill criteria are honoured or they are decoration.** The specific failure mode to guard against:
reaching day 60 with zero sales and deciding to "give it another month" three times. That is how a
90-day validation becomes an 18-month drift. The pre-commitment is: **at D5 path C, a pivot option
is selected and written into an ADR within 7 days.**

## 7. Learning log

A running log at `docs/06-validation/findings/LEARNING_LOG.md`, one entry per week:

| Field | Content |
|---|---|
| Week | — |
| Conversations held | Count and segments |
| Hypotheses touched | IDs |
| What I learned | Specific, not "people seem interested" |
| **What surprised me** | The most valuable field |
| What I was wrong about | Explicit; assumption IDs |
| Assumption updates | `A-##` with the new grade |
| Next week's focus | One thing |

**The "what I was wrong about" field is compulsory and may not be left empty for two consecutive
weeks.** An empty entry means either no learning is happening or it is not being admitted — and in
a program with this much planning invested (`E-21`, `R-14`), the second is the likelier failure.

## 8. Schedule

| Week | Activity | Hypotheses | Gate |
|---|---|---|---|
| 1 | `U-01`–`U-05`; target list; instruments | — | D0 |
| 2 | Teardown template; first 10 contacts; X-01 begins | H-03 | — |
| 3–4 | Outreach at volume; first conversations | H-03, H-10, H-06 | — |
| 4 | **Access gate** | H-03 | **D3** |
| 5–6 | Conversations at volume; first quotes | H-10, H-04, H-11 | — |
| 6–7 | **Resonance gate**; X-02 begins | H-10 | **D4** |
| 7–8 | Diagnostic sales attempts; X-05 | H-01, H-04, H-08 | — |
| 9 | **Monetisation gate** | H-01 | **D5** |
| 9–12 | First diagnostic delivery; X-04 | H-06, H-12 | — |
| 13 | **Delivery gate** | H-06, H-12 | **D6** |
| 13–17 | First core build | H-12 | — |
| 18 | Core delivered; first outcome | — | — |
| 18+ | L3 offer | H-09 | D9 at day 180 |

## 9. Resource cost

| Activity | Hours/week (weeks 1–12) |
|---|---|
| Outreach and teardowns | 8–10 |
| Interviews and follow-up | 4–6 |
| Logging and synthesis | 2–3 |
| Instrument building | 2 (front-loaded) |
| **Total** | **16–21** |

Against `A-03` (30 h/week), validation consumes **55–70% of founder capacity for 12 weeks**. This
is not a side activity, and it is the reason `U-03` (runway) is a go/no-go input rather than a
detail. Cash cost is near zero; the cost is entirely time and forgone billable work.
