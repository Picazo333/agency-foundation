---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - 00_README.md
  - 01_FOUNDER_INPUTS_U01_U05.md
  - ../../08-plans/master/30_60_90_180_365_ROADMAP.md
---
# 16 — Day-0 Validation Launch Checklist

> **Open this file tomorrow morning and work down it in order.**
>
> **Not prerequisites:** Brand V1 · a name · the production website · any further strategy.
> Anything presenting itself as a prerequisite that is not on this list is procrastination with a
> justification (`RED_TEAM_REVIEW.md` RT-01, `AGENCY_THESIS.md` §11).

## Day 0 — before anything else *(2 hours)*

### 1. Answer U-01 to U-05 *(15 min)*
- [ ] Copy `01_FOUNDER_INPUTS_U01_U05.md` → `../findings/FOUNDER_INPUTS_ANSWERED.md`
- [ ] Answer all five. One sitting. No research
- [ ] **Do not skip:** if runway < 3 months or hours < 15/week, stop and read §8 of that file first

### 2. Recalculate *(10 min)*
- [ ] Work through the §7 worksheet, R-1 to R-12
- [ ] Apply the **1.35–1.45× tax multiplier** to break-even (`AUD-04-03`)
- [ ] Update the changed `A-##` rows in `../../02-strategy/thesis/EVIDENCE_AND_ASSUMPTIONS_REGISTER.md`
- [ ] Record your D0 exit

### 3. Clear the blockers that actually block outreach *(20 min)*
Only these. Everything else on the governance checklist blocks *selling*, not *talking*.

- [ ] **Can I contact businesses in my jurisdiction?** — `GOVERNANCE_RISK_SECURITY_CHECKLIST.md`
      `M-01`, `M-02`. If unresolved, start with **warm contacts only** while you check ⚖️
- [ ] **Healthcare marketing restrictions?** — `M-03`. Affects what you may *build*, rarely what
      you may *ask*. Note it; do not let it stop interviews
- [ ] Binding now regardless: identify yourself and your purpose in the first message · honour
      opt-outs permanently · no scraped personal data · B2B channels only
- [ ] MFA on all business accounts; password manager in use (`S-01`, `S-02`)
- [ ] **Not blockers for this phase:** contract templates (needed before the first SOW), invoicing
      setup (needed before the first invoice), insurance (needed before some engagements). Start
      them in parallel — none of them stops a conversation

### 4. Confirm segments *(10 min)*
- [ ] Primary + hedge per `ADR-0007` (proposed) and `ICP_FRAMEWORK.md` §5
- [ ] **Apply the override:** if U-04 shows ≥15 reachable businesses in one segment, that segment
      is primary regardless of the desk ranking
- [ ] Write both down. 75% / 25% effort

## Days 1–3 — build the minimum instruments *(6 hours)*

### 5. First target list *(2 h)*
- [ ] 40–60 accounts into `data/target_account_ledger.csv`
- [ ] Every row has a `reason_selected`. No reason → not on the list
- [ ] Mark `warm_cold` honestly — this split decides whether D3 tests anything
- [ ] **Delete the synthetic example row**

### 6. Research the first accounts *(2 h)*
- [ ] `03_ACCOUNT_RESEARCH_TEMPLATE.md` light tier on 10
- [ ] Deep tier on the 3 best-fit
- [ ] Classify every line **OBSERVABLE / INFERENCE / QUESTION TO VALIDATE**
- [ ] Send test enquiries on the deep three — **enquiry only, never a booking, never a medical
      complaint, disclosed later in the teardown** (`AUD-07-04`)

### 7. Method document *(2 h, in parallel)*
- [ ] One page: what you measure, how, what the output looks like, what its limits are
      (`PROOF_STRATEGY.md` §3, rung P0)
- [ ] Plain type. **No brand system required.** A competent default beats waiting

## Days 3–5 — first contact

### 8. First teardown *(3 h)*
- [ ] Wait for the test-enquiry responses (24–48 h elapsed)
- [ ] `04_TEARDOWN_SOP.md`, then `05_TEARDOWN_TEMPLATE.md`
- [ ] Run the step-8 self-check: **no revenue claims, no benchmarks, no pitch**
- [ ] If you cannot find three observations worth sending — **send nothing.** That is a correct outcome

### 9. First outreach *(1 h)*
- [ ] `06_OUTREACH_SEQUENCE.md` §3 (cold) or §2 (warm)
- [ ] Assign X-01 arms by **strict alternation** down the list, recorded at send time
- [ ] Warm contacts first — they are the cheapest conversations available
- [ ] Log every send immediately

### 10. Prepare to interview *(30 min)*
- [ ] `07_BUYER_INTERVIEW_GUIDE.md` open and read once through
- [ ] `08_INTERVIEW_RECORD_TEMPLATE.md` ready to type into
- [ ] Recording set up
- [ ] **Timer**, for the 12-minute sealed phase
- [ ] Re-read §10 prohibited leading questions. This is the part that decides whether D4 means anything

## Week 1 onward — the loop

### 11. Run the loop
- [ ] 15–20 new targets/week · 6–8 deep, the rest light
- [ ] 2 teardowns/week
- [ ] Every conversation → interview record within 24 h
- [ ] Every interview → resonance classification **from transcript**, ≥1 h later
- [ ] Every quote → price log · every offer → sales attempt log
- [ ] Qualification scorecard after every interview, from the record

### 12. Start the evidence log
- [ ] First `../findings/LEARNING_LOG.md` entry at the end of week 1
- [ ] `../hypotheses/HYPOTHESIS_REGISTER.md` updated as evidence arrives

### 13. Fix the review date
- [ ] Weekly review in the calendar — **same day, same time, recurring**
- [ ] Gate dates in the calendar now: **D3 day 30 · D4 day 45 · D5 day 60 · D6 day 90**
- [ ] Set them from your actual Day 0

## The only things that can stop you

| Real blocker | Not a blocker |
|---|---|
| U-01–U-05 unanswered | No brand |
| Runway < 3 months (changes the *shape*, not the *start*) | No website beyond a plain page |
| A legal restriction on contacting your segment ⚖️ | No case studies |
| No target list | No logo, no name |
| | Not feeling ready |
| | Wanting to refine the plan first |

> The last two are the ones that will actually stop you. The plan is finished. The stop rule is
> active: **no further strategic planning artifact until 10 qualified buyer conversations are
> logged** (`AGENCY_THESIS.md` §11).

## Day-0 completion

```markdown
Day 0 completed: [date]
U-01..U-05 answered: ☐    Recalibration done: ☐
Primary segment: ______   Hedge: ______
Target list: ___ accounts (warm ___ / cold ___)
First outreach sent: [date]
D3 due: ____  D4 due: ____  D5 due: ____  D6 due: ____
Weekly review: [day, time]
```
