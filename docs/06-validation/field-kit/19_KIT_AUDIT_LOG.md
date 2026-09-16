---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - 17_TRACEABILITY_MATRIX.md
  - tests/SYNTHETIC_FIXTURES.md
---
# 19 — Kit Audit Log

> The eight quality passes run against this kit after the instruments were drafted. Findings are
> listed only where they were real; each names the fix and where it was applied.

## Summary

| Pass | Focus | Findings | Fixed | Accepted as a stated limit |
|---|---|---:|---:|---:|
| 1 | Traceability | 4 | 4 | 0 |
| 2 | Contamination | 3 | 3 | 0 |
| 3 | Operator simulation | 3 | 3 | 0 |
| 4 | Adversarial buyers | 2 | 2 | 0 |
| 5 | Information efficiency | 3 | 3 | 0 |
| 6 | Human error | 1 | 1 | 0 |
| 7 | Red team | 3 | 2 | 1 |
| 8 | Integration | 2 | 2 | 0 |
| **Total** | | **21** | **20** | **1** |

---

## Pass 1 — Traceability audit

Mapped all 12 hypotheses to instrument, evidence field and gate. Output:
`17_TRACEABILITY_MATRIX.md`.

| ID | Finding | Fix |
|---|---|---|
| TR-1 | **H-09 had zero instrumentation** anywhere in the kit | It cannot be tested in 90 days (needs 3 delivered cores). Added `13_EXPERIMENT_RUNBOOK.md` §2b stating capture location, earliest test date and D9 gate, so the absence is deliberate rather than an oversight |
| TR-2 | **H-08 had no capture field** — the experiment was specified with nowhere to record it | Added `08_INTERVIEW_RECORD_TEMPLATE.md` §10b, including the trust-framed question ("which would you forward to your partner?") rather than the aesthetic one |
| TR-3 | **H-05 appeared in one file** with no gate or review presence | Added to `14_WEEKLY_VALIDATION_REVIEW.md` §2 and to the D5 gate as a mandatory observation |
| TR-4 | **H-12 had no logging location** | `13_EXPERIMENT_RUNBOOK.md` §2b + §3b time log |

**Result:** 12/12 hypotheses now have an instrument, a named field and a gate or interpretation rule.

---

## Pass 2 — Contamination audit

Scanned for leading questions, framing contamination, vanity metrics, subjective scoring, synthetic
leakage, enthusiasm-as-demand, verbal-intent-as-payment, and operator interpretation mixed with
buyer language.

| ID | Finding | Fix |
|---|---|---|
| CONT-1 | Two **closed questions in the live interview script** (not in the prohibited list): "Would you be able to tell which ones turned into appointments?" and "Is there a threshold where someone else has to agree?" — the second presupposes a threshold | Rewritten open: "How would you tell which of those turned into appointments?" and "Who else would need to agree, and does that change above a certain spend?" |
| CONT-2 | The synthetic teardown's **NOT-EVIDENCE warning sat outside the code fence** — copy-pasting the block would strip it | Warning comment moved inside the fence so it travels with the copy |
| CONT-3 | Verbatim and interpretation were separated in the record but nothing **enforced the writing order** | `08_INTERVIEW_RECORD_TEMPLATE.md` now requires §4 to be completed before any word of §5–§8 |

**Clean on scan:** no vanity metrics · no misuse of "statistically significant" (all six occurrences
are prohibitions) · no `FACT` grade detached from payment · no scoring or weighting in the
qualification instrument.

---

## Pass 3 — Operator simulation

Walked the full loop asking at each step: *would the operator need to invent a process that is not
documented?*

| ID | Step | Finding | Fix |
|---|---|---|---|
| OPSIM-1 | Target selection | The plan says "build a list of 40–60" and **never says where they come from** | `02_TARGET_ACCOUNT_LEDGER.md` §4b — six sourcing methods with expected yield, and the site-count verification rule |
| OPSIM-2 | Outreach | **No documented way to find a contact route** while honouring the no-scraping rule. The operator would have invented one, and the obvious invention is prohibited | `02_TARGET_ACCOUNT_LEDGER.md` §4c — permitted vs prohibited routes |
| OPSIM-3 | After a sale | **The kit ended at "paid" with no exit** | `00_README.md` — handoff table to the delivery instruments, plus the warning that validation does not stop at the first sale |

---

## Pass 4 — Adversarial buyer tests

Three synthetic fixtures run through the full instrumentation:
`tests/SYNTHETIC_FIXTURES.md`. **None produced a false positive.**

| ID | Finding | Fix |
|---|---|---|
| P4-1 | Fixture 2 exposed **no phrasing for refusing a proposal request from an enthusiastic champion**. Under pressure the operator invents one, and the easiest invention is to send the proposal | `06_OUTREACH_SEQUENCE.md` §8.9 — the half-page alternative, plus the explicit note that this is the rationalisation the gate exists to catch |
| P4-2 | Fixture 3 exposed that **`PC-8` unanticipated problems were recorded but never aggregated**. One is noise; a cluster is a reframe signal, and nothing counted them | `PC-8` cluster check added to `14_WEEKLY_VALIDATION_REVIEW.md` §3 and to the D4 gate inputs |

**Confirmed by all three fixtures:** a conversation can be *qualified for access* (D3) while the
buyer is *not qualified to buy* (D5). Collapsing those two meanings is the most likely route to a
manufactured pipeline, and the instruments keep them in separate columns feeding separate gates.

---

## Pass 5 — Information efficiency

For every field: *what decision can this change?* For every gate: *what evidence does it require,
and does a field capture it?*

| ID | Finding | Fix |
|---|---|---|
| IE-1 | **`A-13`, `A-14`, H-12, M-10 and M-41 all depend on hours data, and no time-logging convention existed.** The operator would reconstruct hours at month end, which systematically under-reports rework — the most sensitive variable in the economic model | `13_EXPERIMENT_RUNBOOK.md` §3b + `data/time_log.csv`. Includes a `planning` category whose weekly total is the only unarguable measure of the RT-01 failure mode |
| IE-2 | `evidence_level` and `evidence_grade` are deterministically related — double entry | Retained deliberately as a consistency check, with the mapping stated (`11_PRICE_SIGNAL_LOG.md` §5.1). `VERBAL_INTENT → NONE` is the mapping an optimistic operator most wants to break; writing both forces the contradiction into view |
| IE-3 | The **D6 baseline check had no capture artifact** — only a yes/no in the gate | Gate now requires a *dated, immutable* baseline record. "We know roughly what it was" fails the check |

No fields were found that change no decision. Fields the task specification requires
(`hypotheses_touched`, `website`) are retained as operational lookups.

---

## Pass 6 — Human-error audit

Assumed a founder who is rushed, optimistic, attached to the thesis, tempted to count weak signals,
skip logging, rationalise a failed gate, and keep planning instead of contacting buyers.

| ID | Finding | Fix |
|---|---|---|
| HE-1 | **A rushed operator facing a 12-section record will skip it entirely** and rely on memory — the exact thing the instrument distrusts | `08_INTERVIEW_RECORD_TEMPLATE.md` — six-field emergency minimum record capturing every gate-critical input, filed within the hour |

**Already present and verified as adequate:** mandatory `WHAT SURPRISED ME` · mandatory
`WHAT I WAS WRONG ABOUT` with two-week escalation · the override register with read-aloud rule ·
the tie-goes-against-the-thesis rule in resonance classification · count-before-you-discuss at every
gate · classification from transcript ≥1 h later · scorecard run from the record, not from memory ·
the §5 self-deception checklist · the weekly `planning hours` read-out.

---

## Pass 7 — Red team: *make this kit produce misleading positive evidence*

| ID | Attack | Outcome |
|---|---|---|
| **RT-K1** | **Select targets on observed dysfunction.** Search for clinics with visibly broken booking paths, and the finding that clinics have broken booking paths is manufactured. D4 passes on a sample built to pass it | **Fixed.** `02_TARGET_ACCOUNT_LEDGER.md` §4b selection-bias prohibition: accounts are selected on ICP fit, then researched — never the reverse. Permitted vs prohibited `reason_selected` values given. ~1 in 5 deep-tier passes should find nothing worth sending; if none do, the list was selected on dysfunction |
| **RT-K2** | **Pass D4 on warm contacts.** Friends are forthcoming and reach for a problem that pleases the asker. The resonance gate had no warm/cold split | **Fixed.** `10_PROBLEM_RESONANCE_LOG.md` §6.1 — mandatory split; ≥60% warm forces `PASS (warm-dependent)` and the cold arm stays open. §6.2 denominator-order rule prevents selecting the "best ten" |
| **RT-K3** | **Survivorship.** Only repliers are interviewed, and repliers self-select for having the problem. This biases H-10 upward | **Accepted as a stated limit** — it cannot be removed; you cannot interview someone who ignored you. Partially countered: touch-4 extracts reasons from non-repliers, `L-07` clusters among them count *against* the thesis, and the reply rate is now reported alongside the resonance ratio so a pass is read with the bias attached (`10_PROBLEM_RESONANCE_LOG.md` §7b) |

**Attacks that failed** — the kit already blocked them: enthusiasm→demand (no field accepts it) ·
verbal intent→payment (four-level ladder, cleared funds only) · teardown-then-"volunteered"
(contamination check on prior contact) · discounted sale→H-01 (`discount_offered` excludes the row)
· unqualified buyer→D5 denominator (attempt requires prior qualification) · late gate→quiet pass
(gates run on the due date, counted before discussed).

---

## Pass 8 — Final integration

| ID | Finding | Fix |
|---|---|---|
| INT-1 | The Field Kit was not reachable from the documents an operator would open first | Cross-links added to `FIELD_VALIDATION_PLAN.md`, `HYPOTHESIS_REGISTER.md`, `LEARNING_LOG.md`, `AGENCY_MASTER_PLAN.md`, `EXECUTIVE_SYNTHESIS.md`, `CLAUDE_HANDOFF.md` — pointers only, no rewriting |
| INT-2 | ADR numbering in the kit had to match post-merge `main` (`ADR-0006`–`ADR-0010`) | Verified: the kit references `ADR-0007` (segments), `ADR-0008` (paid diagnostic), `ADR-0009` (pricing freeze), all still **PROPOSED**. No ADR status altered |

---

## Non-regression verification

| Check | Result |
|---|---|
| Brand files modified | **None** — `docs/03-brand/` untouched |
| APPROVED/FROZEN canon altered | **None** |
| ADR-0006…0010 status | **All still PROPOSED** |
| Fabricated evidence | **None** — three fixtures, all in `tests/`, all labelled NOT EVIDENCE |
| Synthetic fixtures in evidence logs | **None** — `data/*.csv` are headers only |
| Invented buyer quotes | **None** — all marked `[SYNTHETIC — NOT A REAL QUOTE]` |
| Inferred pricing published | **No** — `ADR-0009` honoured; the only figure repeated is the existing `INFERRED RANGE` base |
| Legal conclusions invented | **None** — ⚖️ items routed to counsel |
| Secrets introduced | **None** |
| Numeric thresholds changed | **None** — D3 ≥8, D4 ≥5/10, D5 ≥2 paid, D6 ≤130% all verbatim from source |
| Code or dependencies changed | **None** — documentation only |
