---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - ../findings/LEARNING_LOG.md
  - ../hypotheses/HYPOTHESIS_REGISTER.md
  - ../../04-operations/AGENCY_SCORECARD.md
---
# 14 — Weekly Validation Review

> **Instrument type:** timeboxed weekly procedure. **20–30 minutes. Same day, same time, every week.**
> **Outputs:** an entry in `../findings/LEARNING_LOG.md`, updates to
> `../hypotheses/HYPOTHESIS_REGISTER.md`, and one decision.
>
> A review that produces no decision and no changed assumption was a status report. Status reports
> are not what this is for.

## 1. Agenda — 25 minutes, in this order

| # | Block | Min | Output |
|---:|---|---:|---|
| 1 | Numbers, read aloud, no commentary | 4 | Counts only |
| 2 | Contradictions and surprises | 6 | What reality did not match |
| 3 | Hypothesis movement | 5 | Register updates |
| 4 | Rationalisation check | 4 | Named temptations |
| 5 | Information-value triage | 3 | Next week's highest-value unknown |
| 6 | Stop / continue / start | 3 | One decision, written |

**Order matters.** Numbers before narrative — reversing it means the narrative selects the numbers.

## 2. Block 1 — Numbers *(4 min, read from the logs, no interpretation)*

| Metric | This week | Cumulative | Target | Source |
|---|---|---|---|---|
| Contacts initiated (M-01) | | | 15–20/wk | Ledger |
| Reply rate (M-02) | | | ≥ 8% | Ledger |
| **Qualified conversations (M-03)** | | | **≥ 2/wk, 8 by D3** | Ledger, strict test |
| — of which warm / cold | | | — | Ledger |
| Teardowns delivered | | | 2/wk | Ledger |
| Teardown → conversation (M-04) | | | ≥ 15% | Ledger |
| **Resonance: volunteered / denominator** | | | **≥ 5/10 by D4** | Resonance log |
| Quotes given | | | — | Price log |
| **Paid diagnostics (undiscounted)** | | | **≥ 2 by D5** | Sales log |
| Verbal-yes-unpaid | | | *reported separately* | Sales log |
| Loss codes this week | | | — | Ledger |
| Outreach hours (M-41) | | | 8–10 | Time log |
| Median days first-contact → payment (H-05) | | | *observe; `A-10` says 30–60* | Sales log |
| **Baseline availability (H-06)** — buyers with ≥4wk reconstructable ÷ asked | | | **≥ 50% pass · < 25% fail** | Interview §6 |

**Reporting rules:**
- Verbal intent is **never** added to paid. Two separate lines, always.
- Warm and cold are **never** merged in the D3 count.
- Contaminated interviews are **excluded** from the resonance denominator.
- Read the numbers before saying anything about them.

## 3. Block 2 — Contradictions and surprises *(6 min — the substance)*

Answer all. Short answers are fine; blank answers are not.

1. **What did reality contradict this week?**
2. **What surprised me?**
3. **What did I expect to hear and never heard?** *(absence is evidence)*
4. **What did buyers say that I did not have a category for?**
   **`PC-8` cluster check:** count unanticipated problems volunteered this week and cumulatively.
   One is noise. **Three or more of the *same* unanticipated problem is a reframe signal** — take it
   to the D4 gate as a candidate for the `DECISION_TREE.md` D4b reframe, not as a curiosity.
   Cumulative `PC-8` tally by theme: ______
5. **WHAT I WAS WRONG ABOUT THIS WEEK:** ← mandatory, see §7

## 4. Block 3 — Hypothesis movement *(5 min)*

| Hypothesis | Evidence added | Direction | Status change | Grade |
|---|---|---|---|---|
| H-01 | | supports / weakens / none | | `FACT` only on payment |
| H-03 | | | | |
| H-10 | | | | |
| H-06 | | | | |
| H-04 | | | | |
| H-03b / H-07 / H-11 | | | | |

**Rules:** status advances only at the defined sample size, never on the first encouraging
conversation. Grade advances only by the grade of evidence actually obtained — interviews produce
`SIGNAL`, only money produces `FACT`. Update `../hypotheses/HYPOTHESIS_REGISTER.md` now, in this
sitting, not "later."

## 5. Block 4 — Rationalisation check *(4 min)*

Read these aloud. They exist because the person running this review is the most invested person in
the room and therefore the least reliable auditor.

1. **What am I tempted to rationalise this week?**
2. Have I counted any enthusiasm as demand?
3. Have I counted any verbal intent as a sale?
4. Have I upgraded a qualification without new evidence from a new interaction?
5. Have I classified anything as VOLUNTEERED that was actually PROMPTED?
6. Have I excluded every contaminated interview from the resonance denominator?
7. Did I quote a price to anyone who was not qualified?
8. Am I explaining away a failed week with circumstances that would also explain a successful one?
9. **Have I spent time planning this week that should have been spent contacting buyers?**
   *(`AGENCY_THESIS.md` §11 stop rule; `RED_TEAM_REVIEW.md` RT-01)*

Q9 is the one most likely to be answered dishonestly, because planning feels like progress and
outreach feels like exposure.

## 6. Block 5 — Information-value triage *(3 min)*

| Question | Answer |
|---|---|
| Which hypothesis now matters **less** than last week? | |
| Which uncertainty has the **highest information value** right now? | |
| What is the **cheapest** way to reduce it this week? | |
| Am I working on the highest-priority untested hypothesis? *(H-01 > H-03 > H-10 > H-06 > H-04)* | |

## 7. The mandatory field

> ## WHAT I WAS WRONG ABOUT THIS WEEK

**Rules:**
- May not be blank.
- "Nothing" is only acceptable in a week with **zero buyer contact** — and a week with zero buyer
  contact is itself the thing that was wrong.
- **Two consecutive blank or "nothing" entries trigger the §8 escalation.** No exceptions.

Being wrong weekly is the expected state of a program with twelve open hypotheses and zero prior
buyer contact. A run of weeks with nothing wrong means either nothing is being learned or nothing
is being admitted — and in this program, with this much planning invested, the second is likelier.

## 8. Escalation — two consecutive blanks

Triggered automatically. Not optional, not deferrable.

| Step | Action |
|---|---|
| 1 | Stop the review. Do not continue the agenda |
| 2 | Re-read the last 5 interview records **§4 verbatim sections only** — not your own summaries |
| 3 | Answer in writing: *what, in those words, does not fit the thesis?* |
| 4 | If nothing: ask whether Phase 2 is actually being run for 12 minutes, or being cut short |
| 5 | If interviews are being cut short → that is the finding. Fix it before the next conversation |
| 6 | If no interviews happened in either week → **the program has stalled.** Record it, name the reason, and treat the next week as a recovery week with outreach as the only activity |
| 7 | Log the escalation in the learning log. Repeated escalations go to the human owner |

## 9. Block 6 — Decision *(3 min)*

Exactly one written decision. "No change, because…" is a valid decision and must state the because.

```markdown
## Week N decision — [date]
Decision:
Because:
Evidence it rests on (IDs):
What would reverse it:
Owner / date:
```

## 10. Gate proximity check

| Gate | Due | Current | On track? |
|---|---|---|---|
| D3 access | day 30 | ___ / 8 qualified | |
| D4 resonance | day 45 | ___ / ___ volunteered | |
| D5 monetisation | day 60 | ___ / 2 paid | |
| D6 delivery | day 90 | — | |

**If a gate is within two weeks and the count is below half the threshold, say so out loud and
record it.** Gates arrive faster than they feel. The purpose of this line is to make a miss
visible three weeks early, while there is still time to change the approach rather than only the
explanation.

## 11. Write-up

Copy the completed review into `../findings/LEARNING_LOG.md` using its template. Append only —
never revise a previous week to look more prescient. The value of the log is that it records what
you believed at the time.
