---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - 07_BUYER_INTERVIEW_GUIDE.md
  - 10_PROBLEM_RESONANCE_LOG.md
  - ../FIELD_VALIDATION_PLAN.md
---
# 08 — Interview Record Template

> **Instrument type:** per-interview evidence record. **Complete within 24 hours.**
> **Save to:** `docs/06-validation/interviews/I-0NN-[segment]-[role].md`
> **Index in:** `data/interview_index.csv`
>
> **Fill §4 (verbatim) completely before writing a single word of §5–§8.** Interpretation written
> alongside quotes contaminates the quotes — you start selecting for what fits.

## Privacy rule

Identify people by **role + initials** and business by name only if public. No personal email
addresses or phone numbers in the repository (`DR-2`, `DR-6`). If the interviewee asked for
anonymity, use `[anonymised]` for the business too, and say so in §1.

---

## Template

```markdown
---
interview_id: I-0NN
date: YYYY-MM-DD
account_id: A-0NN
account: [business name, or "anonymised"]
role: [job title]
committee_position: signer | champion | blocker | user | unknown
segment: S2 | S7 | S6 | S4 | other
tier: primary | hedge
geography: [metro]
source: warm | list | referral | partner | inbound
duration_minutes: NN
consent_recording: granted | refused
consent_quote: granted | refused | not asked
calibration: Y | N          # Y = operator's first interview; excluded from gate counts
hypotheses_touched: [H-10, H-06, H-11, ...]
---

# Interview I-0NN — [role], [segment]

## 1. Integrity header  (fill FIRST, before anything else)

| Field | Value |
|---|---|
| Minute the problem was first named **by me** | ___ (or "never") |
| Minute the offer was first described **by me** | ___ (or "never") |
| Open-narrative phase actually lasted | ___ minutes |
| **resonance_contaminated** | Y / N — **Y if I named the problem before Phase 4** |
| Did I send anything in advance that named the problem? | Y / N |
| Teardown previously sent to this account? | Y / N — if Y, did it name the problem? Y / N |
| Recording available for reclassification? | Y / N |

> If `resonance_contaminated = Y`, this interview is **excluded from the H-10 denominator**.
> It still counts for D3 access, H-06, H-11 and H-03b. Record it honestly — a contaminated
> interview that is counted destroys the only gate that tests the thesis.

## 2. Context

- Locations / size:
- Role and tenure:
- Who else is involved in decisions:

## 3. What they NEVER mentioned  (fill from the expected list)

Expected pains that did **not** come up unprompted:
- [ ] Missed / slow follow-up
- [ ] Enquiry handling across channels
- [ ] Booking friction
- [ ] No-shows
- [ ] Handoffs between staff or locations
- [ ] Attribution / not knowing what works
- [ ] Owner being the bottleneck

*Absence is evidence. A pain the plan predicts and the buyer never raises is a mark against the
thesis, not a gap in the interview.*

## 4. VERBATIM  — their words only

> Rules: their words, not a paraphrase. No tidying of grammar. Mark unclear audio `[unclear]`.
> Nothing of mine in this section. If I cannot recall the exact words, write `[paraphrase]` and
> flag it — a paraphrase is not verbatim and must never enter the messaging corpus.

**Phase 2 — open narrative (sealed):**
> "…"

> "…"

**Phase 4 — consequence / what bothers them most:**
> "…"

**Phase 5 — category language (H-11):**
> Q: "What would you even search for?"
> A: "…"
> Q: "Where would that come from, budget-wise?"
> A: "…"

**Phase 6 — reaction to the offer, if reached:**
> "…"

**Anything else worth preserving word-for-word:**
> "…"

## 5. OBSERVATION  — what happened, factually

*Behaviour and facts. No meaning yet.*

- Tone / engagement:
- Where they became animated:
- Where they became vague or changed the subject:
- Interruptions, distractions, time pressure:
- Whether they had answers to the measurement questions readily:

## 6. Structured findings

### Current workflow (Phase 2–3)
- Channels and mix:
- First responder:
- Out of hours:
- Cross-location:
- Unanswered enquiries:
- No-shows:
- Systems in use:

### Measurement / baseline availability  (H-06)
| Question | Answer |
|---|---|
| Could they retrieve last month's enquiry count? | yes / no / unsure |
| Could they link enquiries to bookings? | yes / no / unsure |
| How far back does the data go? | ___ weeks |
| Which system holds it? | |
| Does anyone review it? | |
| **≥ 4 weeks reconstructable?** | **yes / no** |

### Consequence and prior attempts
- What bothers them most (their nomination, not mine):
- Stated consequence:
- Prior attempts and outcome:

### Authority  (H-03b / Q3)
| Question | Answer |
|---|---|
| Who signs? (role) | |
| Additional approvers / threshold? | |
| Decision cadence (e.g. monthly partners' meeting)? | |
| Was the signer on this call? | yes / no |

### Competitive  (H-07)
- Anyone else looked at this? Who, and what did they do?
- Do they position on operations or on marketing?

## 7. INTERPRETATION  — my reading, may be wrong

*Everything in this section is mine. Nothing here is evidence about the buyer; it is evidence about
what I currently think.*

- 

## 8. INFERENCE for the plan

- Assumption touched (`A-##` / `U-##`):
- Direction: supports / weakens / neutral / **contradicts**
- Evidence grade produced: `SIGNAL` (default) — `FACT` **only** if money was received
- Does this change a number anywhere? Which, and to what?

## 9. WHAT SURPRISED ME?   ← MANDATORY, may not be blank

> If nothing surprised you, either the interview was too short, you talked too much, or you are not
> listening. Write the closest thing to a surprise, and note that it was weak.

- 

## 10. WHAT THIS CHALLENGED

| Field | Value |
|---|---|
| Assumption challenged | |
| What I expected to hear | |
| What I actually heard | |
| Am I tempted to explain this away? How? | |

## 10b. Brand-register reaction  (H-08 / X-05 — only if both variants were shown)

*Leave blank unless X-05 was run in this conversation.*

| Field | Value |
|---|---|
| Both variants shown? | Y / N |
| Order shown (which first) | plain / distinctive |
| **Question asked** | "Which of these would you forward to your business partner?" *(a trust question — never "which do you prefer?", which is an aesthetic one)* |
| Which they would forward | plain / distinctive / no preference |
| Unprompted reaction, verbatim | "…" |
| Did either change their stated willingness to proceed? | Y / N — how |
| Did I reveal which was "mine"? | Y / N — **Y contaminates this data point** |

Feeds `13_EXPERIMENT_RUNBOOK.md` X-05 and `BRAND_BUSINESS_INTERFACE.md` §7 test T-B7.

## 11. Follow-up and next experiment

| Field | Value |
|---|---|
| Follow-up agreed? | |
| Referral offered? | |
| Quote consent? | granted / refused / not asked |
| Next action + date | |
| Next experiment this suggests | |
| Ledger updated? | ☐ |
| Resonance log updated **from transcript**? | ☐ |
| Price log updated (if quoted)? | ☐ |
| Sales attempt log updated (if offered)? | ☐ |
| Qualification scorecard run? | ☐ |
| Hypothesis register updated? | ☐ |
```

---

## Emergency minimum record *(human-error mitigation `HE-1`)*

A rushed operator facing a 12-section template will skip it entirely and rely on memory. Memory is
the thing this whole instrument exists to distrust.

**So: if you have five minutes and not forty, capture these six fields within the hour.** Complete
the rest within 24 hours.

```markdown
I-0NN | date | account | role | duration
1. Minute I first named the problem: ___ (or "never")   → contaminated? Y/N
2. Did they volunteer a problem before I named one? Y/N  → which category (PC-_)
3. Their exact words for it: "…"
4. Can they retrieve last month's enquiry count? Y/N/unsure   (H-06)
5. Who signs? (role)                                          (H-03b)
6. WHAT SURPRISED ME:
```

Those six fields preserve every gate-critical input: D4 needs 1–3, D5 needs 5, D6 needs 4, and the
weekly review needs 6. Everything else in the full template is valuable but recoverable.

**A six-field record filed within the hour beats a perfect record written from memory on Friday.**

## Why the sections are separated this way

| Section | Contains | Never contains |
|---|---|---|
| §4 VERBATIM | Their exact words | Any word of mine |
| §5 OBSERVATION | What factually happened | What it means |
| §6 FINDINGS | Structured answers to asked questions | Conclusions |
| §7 INTERPRETATION | My reading, explicitly fallible | Anything presented as theirs |
| §8 INFERENCE | What it means for the plan | Upgraded evidence grades |

Only **§4** may feed the messaging corpus (`POSITIONING_ARCHITECTURE.md` §3). Buyer-facing copy
written from §7 is the agency talking to itself in the buyer's voice — which is precisely the
failure mode that `E-05` (synthetic VoC) exists to prevent.
