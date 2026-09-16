---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - OFFER_ARCHITECTURE.md
  - CLIENT_LIFECYCLE.md
  - PRICING_AND_ECONOMICS_MODEL.md
---
# Delivery Operating System

> **Module 13 of the Agency Master Plan** (Issue #2 Phase 10, delivery half). How the work is
> actually produced: phases, QA gates, change control, AI leverage, proof capture and the
> documentation that makes delivery delegable.

## 1. Delivery principles

| # | Principle | Consequence |
|---|---|---|
| 1 | **Measure before building.** Every build follows a diagnostic that established the baseline | No unmeasurable engagements (`RF-8`) |
| 2 | **Scope is a contract, not an intention.** Exclusions are as binding as inclusions | Change control is mandatory (§6) |
| 3 | **Log hours as worked.** Rework logged separately | Reconstructed hours hide `A-13`, the largest margin variable |
| 4 | **AI does the volume; the founder does the judgement** | §7 |
| 5 | **Every engagement produces a reusable asset** | Templates compound; the third delivery must cost less than the first |
| 6 | **Documentation is a deliverable, not an afterthought** | Delegation depends on it (`OPERATING_MODEL.md` §7) |
| 7 | **Proof capture is a gate, not a task** | `PROOF_STRATEGY.md` §10 |
| 8 | **Nothing ships to a client without passing internal QA** | §9 |

## 2. Delivery modes

| Mode | Applies to | Character |
|---|---|---|
| **Measure** | L0, L1, O-0 | Analytical. Output is evidence |
| **Build** | L2, L4 | Productive. Output is a working system |
| **Operate** | L3 | Cyclical. Output is a report and small changes |

Mode matters because the failure modes differ: Measure fails on data access, Build fails on scope,
Operate fails on value communication.

## 3. L0 Teardown production

| Phase | Time | Activity |
|---|---|---|
| Target research | 40 min | Public surfaces; submit a test enquiry from a neutral address; note the timestamp. **Rules (`AUD-07-04`): enquiry only, never a booking; never occupy an appointment slot; never impersonate a patient with a medical complaint; disclose that the enquiry was a timing test in the teardown itself** |
| Measurement | 24–48 h elapsed, 10 min active | Record actual first-response latency and channel behaviour |
| Analysis | 40 min | Compare against the standard checklist; identify the 3 highest-value observations |
| Recording | 30 min | 5–8 minute screen walkthrough, single take, no editing beyond trimming |
| Packaging | 20 min | One-page summary, send |

**Hard cap 3 hours.** Exceeding the cap on a single target means the target is being treated as a
prospect rather than as an outreach unit — stop and move on.

Standard checklist: enquiry channels present and functional · first-response latency by channel ·
booking-path friction (steps, required fields, mobile behaviour) · cross-location consistency ·
tracking presence · follow-up on an unconverted enquiry · review-response behaviour.

## 4. L1 Diagnostic production

| Phase | Days | Hours | Activity | Gate |
|---|---|---|---|---|
| D1 Access + kickoff | 1–2 | 4 | Credentials, stakeholders, scope confirmation | Access verified or clock pauses |
| D2 Current-state mapping | 2–4 | 6 | Map every enquiry path across channels and locations; interview ops lead | Map reviewed with client |
| D3 Instrumentation | 3–5 | 6 | Install tracking where missing; verify data flowing | **Instrumentation verified functional** |
| D4 Measurement window | 6–15 | 2 | Passive collection; disclosed test enquiries; spot checks | Minimum data volume reached |
| D4b **Day-8 interim note** | 8 | 0.5 | One-paragraph "here is what we are seeing so far" | **Mandatory.** A three-week silence during the first paid engagement is where trust is lost (`AUD-01-02`) |
| D5 Analysis + quantification | 16–17 | 8 | Stage-by-stage loss quantification; each figure sourced or marked as an estimate | Every figure traceable |
| D6 Options + pricing | 17 | 2 | 2–3 bounded build options | Scope and exclusions written |
| D7 Report + walkthrough | 18 | 2 | Report; 45-min findings session | Delivered |
| **Total** | **18** | **30** | | |

### 4.1 Quantification discipline

Every number in a diagnostic report carries one of three labels:

| Label | Meaning |
|---|---|
| **Measured** | Directly observed in the client's data during the window |
| **Reconstructed** | Derived from the client's historical records; method stated |
| **Estimated** | Modelled from assumptions; the assumptions are listed inline |

> An unlabelled number in a diagnostic report is a defect. The report's entire value is that its
> numbers are honest; a single unsourced figure discovered by the client destroys the deliverable's
> credibility and, with it, the positioning (`POSITIONING_ARCHITECTURE.md` POS-1).

### 4.2 Minimum data volume

If the measurement window produces too little data for a defensible conclusion, **say so and extend
the window** rather than reporting a conclusion the data does not support. Extending costs days;
publishing a false finding costs the relationship. Stated in the SOW as a possibility.

## 5. L2 Core build production

Six phases. C-1 hours shown; C-2 adds ~20 hours concentrated in W2–W3.

| Phase | Week | Hours | Activity | Gate |
|---|---|---|---|---|
| B1 Discovery + design | 1 | 18 | Detailed requirements from diagnostic findings; system design; integration map; **rollback plan** | **G1 client sign-off** |
| B2 Build core | 2 | 30 | Primary system construction | Internal checkpoint |
| B3 Build integrations + automation | 3 | 28 | Connections, sequences, routing, measurement | Internal checkpoint |
| B4 Internal QA | 4 | 12 | §9 checklist; fix; re-test | **G3 internal QA pass** |
| B5 Client review + revision | 4 | 8 | Consolidated feedback, one round | **G4 client approval** |
| B6 Training + launch | 5 | 10 | Training (recorded), runbook, staged launch | **G5 go-live** |
| B7 Stabilisation | 6 | 4 | Monitoring, fixes, first measurement | Handoff complete |
| **Total** | | **110** | | |

**Rollback plan in B1, not B6.** Every change to a live client system must have a documented way
back before it is made. This is the difference between an incident and a catastrophe, and a solo
operator has no second pair of hands during one.

**Staged launch:** one location or one channel first, observe for 48 hours, then the rest. The cost
is two days; the benefit is that a systemic error affects one site rather than fifteen.

## 6. Change control

```text
Request (any channel) → Logged within 24h → Assessed (hours/schedule/dependency)
   → Written change order (scope, price, revised dates) → Client written approval → Execute
```

| Rule | Detail |
|---|---|
| No verbal change orders | Ever |
| No work before written approval | The single most important margin rule in this document |
| <1 hour | May be absorbed at discretion, **logged, and reported as absorbed** in the weekly update |
| Schedule impact always stated | A change that adds 6 hours adds days, not evenings |
| Change orders priced at standard yield | No "while we're in there" discounts — they teach the client that scope is free |
| Cumulative changes >25% of original value | Stop. Re-scope as a new engagement |

**Logged absorbed changes serve two purposes:** they make generosity visible to the client, and
they produce the data that shows whether the offer's scope definition is systematically too narrow.

## 7. AI and automation in delivery

The mechanism that makes the economics work (`AGENCY_THESIS.md` §6.1) — and a source of real risk.

| Task class | Approach | Human role |
|---|---|---|
| Research, data extraction, first-pass analysis | AI-generated | **Verify every figure against source** |
| Documentation, runbooks, training material | AI-drafted | Edit for accuracy and tone |
| Code and configuration scaffolding | AI-generated | Review, test, own |
| Report and proposal drafting | AI-drafted from structured inputs | Judgement, framing, every number |
| Client communication | **Human-written** | AI may draft; the founder sends nothing unread |
| Quantification and findings | **Human-owned** | AI may compute; the founder verifies and signs |
| Scope and pricing decisions | **Human-only** | Never delegated |
| Anything touching client personal data | Gated by §7.1 | — |

### 7.1 AI governance rules *(binding)*

| # | Rule |
|---|---|
| AI-1 | No client personal data is sent to a third-party AI service without a contractual basis and client disclosure (`GOVERNANCE_RISK_SECURITY_CHECKLIST.md` §5) |
| AI-2 | **No clinical or patient records through any AI system**, ever (`RF-7`) |
| AI-3 | Client data used for AI processing is minimised and pseudonymised where the task permits |
| AI-4 | Every AI-produced number is verified against its source before it reaches a client |
| AI-5 | AI-generated code touching a live system is reviewed and tested as if written by an unknown contractor |
| AI-6 | AI use is disclosed on request and never denied (`EC-9`) |
| AI-7 | No credentials, secrets or access tokens in any AI prompt |
| AI-8 | Where a deliverable's accuracy matters commercially, a human check is a named step in the QA checklist, not an intention |

**AI-4 is where this model is most likely to fail embarrassingly.** The speed advantage creates the
temptation to skip verification, and a confidently wrong number in a diagnostic report is worse
than no report. The QA checklist (§9) enforces it structurally.

## 8. Proof capture during delivery

Per `PROOF_STRATEGY.md` §10, enforced as gates rather than tasks:

| Point | Capture | Gate |
|---|---|---|
| Onboard day 1 | Baseline snapshot, dated, immutable | **Engagement cannot enter Build without it** |
| Onboard day 1 | Benchmark fields (P7) | Required field |
| During build | Before/after artifacts, decision log | Weekly |
| Acceptance | Outcome measurement vs baseline | **Engagement cannot be marked complete without it** |
| +30 days | Second measurement; testimonial request | Scheduled task |
| +90 days | Third measurement; reference request | Scheduled task |

## 9. Quality gates

### 9.0 The solo-QA problem

A solo operator reviews their own work, which is the weakest possible QA arrangement and cannot be
fully solved at this scale (`AUD-06-03`). Three partial mitigations, all mandatory:

1. **A minimum 12-hour gap between build completion and the QA pass.** Reviewing immediately after
   building reproduces the same blind spots that created the defect.
2. **The checklist is run literally, item by item, from the written list** — not from memory, and
   not by judgement. A checklist run from memory is not a checklist.
3. **Automated checks wherever the test is deterministic** (link checking, form submission, load
   measurement, contrast checking), because automation has no blind spots to reproduce.

When a contractor exists, QA of their work by the founder — and spot-checking of the founder's work
by the contractor — replaces this section.

### 9.1 Internal QA checklist (G3) — no client sees anything before this passes

**Functional:** every SOW deliverable present and demonstrable · every automation triggered and
verified end to end · error and edge cases tested (empty submission, duplicate, out-of-hours,
malformed input) · mobile and desktop verified · cross-browser on the two most common in the
client's analytics.

**Data:** measurement verified against a known-good source · attribution correct · no test data in
production · **no client personal data in logs, screenshots or documentation**.

**Security:** no credentials in code or configuration · least-privilege access confirmed · MFA where
available · no public exposure of internal endpoints · third-party scripts reviewed.

**Accessibility:** keyboard navigable · form labels present · contrast checked · screen-reader
sanity pass on client-facing surfaces. *Not optional* — public-facing surfaces have legal exposure
in several jurisdictions (`GOVERNANCE_RISK_SECURITY_CHECKLIST.md` §9).

**Performance:** page load measured on a representative connection · no obvious blocking resources.

**Documentation:** runbook complete · known limitations written · access register updated.

**AI verification:** every AI-produced figure traced to its source (AI-4) · every AI-generated
configuration reviewed line by line (AI-5).

**Licensing:** every font, image, icon and library licensed for the use, with the licence recorded.
Inherited from `IMPLEMENTATION_SUMMARY.md` principle 4 and enforced here because it is a real legal
exposure that is trivially avoidable at build time and expensive afterwards.

### 9.2 Acceptance criteria (G4/G5)

Recorded walkthrough demonstrating every SOW line · dashboard reporting against the baseline ·
training delivered and recorded · runbook handed over · known limitations acknowledged in writing ·
client sign-off or deemed approval per `CLIENT_LIFECYCLE.md` §5.

## 10. Templates and reusable assets

The mechanism by which the third delivery costs less than the first. **Rule: every engagement
contributes at least one reusable asset**, and the contribution is a completion criterion.

| Asset | Built during | Reused in |
|---|---|---|
| Diagnostic report template | L1 #1 | Every L1 |
| Measurement instrumentation kit | L1 #1 | Every L1, O-0 |
| Loss-quantification model | L1 #1–3 | Every L1 |
| Intake/routing pattern library | C-1 #1 | Every C-1 |
| Automation sequence library | C-1, C-2 | All builds |
| CRM configuration blueprint (per supported platform) | C-2 #1 | Every C-2 |
| QA checklist | Continuous | All |
| Runbook template | C-1 #1 | All |
| Training deck + recording | C-1 #1 | All |
| Monthly report template | L3 #1 | Every L3 |

**Platform discipline:** support at most **two** CRM platforms and **two** booking/PMS integration
patterns. Each additional platform multiplies the template library and destroys the repeatability
that `DECISION_TREE.md` D8 measures. Saying "we don't work with that platform" is a productization
decision, not a limitation.

## 11. Delivery metrics

| Metric | Definition | Target | Trigger |
|---|---|---|---|
| Hours vs budget | Actual ÷ budgeted delivery hours | ≤ 110% | T-1 at >130% twice |
| Rework ratio | Rework ÷ total delivery hours | ≤ 20% (`A-13`) | T-2 at >35% |
| On-time milestone rate | Milestones met ÷ total, excluding client-caused delay | ≥ 85% | Diagnose below |
| Change orders per engagement | Count and value | 1–2 | Zero suggests under-scoping *or* silent absorption |
| Defects found at client review | Count | ≤ 2 | >5 means internal QA failed |
| Time to first measured outcome | Launch → first outcome record | ≤ 30 days | — |
| Template reuse rate | Reused components ÷ total | Rising | Flat means productization is not happening |

**Zero change orders is a warning, not a success.** It usually means scope is being absorbed
silently, which appears as rework rather than revenue.

## 12. Delivery risks

| Risk | Impact | Mitigation |
|---|---|---|
| Client access delayed | Schedule slip | Clock-pause clause |
| Scope creep via informal channels | Margin (`A-13`) | §6; route every request |
| Platform surprise (undocumented API limits, no export) | Rework, sometimes fatal | Technical feasibility check in B1 **before** the design is committed |
| Staff non-adoption | Outcome failure despite technical success | Staff involved in B1; training recorded; adoption measured in stabilisation |
| Client data quality worse than assumed | Baseline unreliable | Verify in D3, not D5. Escalate to O-0 if needed |
| AI-produced error reaches client | Credibility | AI-4, AI-5, QA gate |
| Founder unavailable mid-build | Total stop | Documentation-first practice; contractor bench (`OPERATING_MODEL.md` §8) |
| Live-system change breaks client operations | Severe | Rollback plan in B1; staged launch; out-of-peak-hours deployment |

## 13. Incident handling

| Severity | Definition | Response | Communication |
|---|---|---|---|
| S1 | Client's live operations broken by our change | Immediate; roll back first, diagnose after | Call within 1 hour; written summary same day |
| S2 | Automation failing; data not flowing | Same business day | Written notice with ETA |
| S3 | Degraded but functioning | Within 2 business days | Weekly update |
| S4 | Cosmetic or minor | Next cycle | Weekly update |

**Post-incident, every S1 and S2 gets a written note**: what happened, why, what was done, what
prevents recurrence. This is uncomfortable and it is the practice that turns an incident into a
trust event. It also directly supports `EC-10`.
