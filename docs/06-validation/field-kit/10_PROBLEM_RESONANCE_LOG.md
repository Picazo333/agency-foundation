---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - ../FIELD_VALIDATION_PLAN.md
  - 07_BUYER_INTERVIEW_GUIDE.md
  - 08_INTERVIEW_RECORD_TEMPLATE.md
---
# 10 — Problem Resonance Log (H-10)

> **Instrument type:** classification log for the D4 gate. **CSV:** `data/resonance_log.csv`.
> **Hypothesis:** H-10 — buyers recognise the revenue-leak problem **unprompted**.
> **Gate:** D4 at day 45. **Pass ≥ 5/10 volunteered. Fail ≤ 1/10.**
>
> This is the instrument that tests whether the thesis describes a real problem or one the plan
> invented. It is the easiest instrument in the kit to corrupt and the most expensive to corrupt.

## 1. What is being measured

Not "does the buyer have this problem." Not "does the buyer agree this is a problem."

> **Did the buyer describe a version of this problem, in their own words, before anyone described
> it to them?**

Everything else — agreement, interest, recognition after framing — is a different and much weaker
observation, and is logged separately so it cannot be mistaken for the real thing.

## 2. The three classifications

| Class | Definition | Counts toward D4? |
|---|---|---|
| **VOLUNTEERED** | Raised by the buyer in Phase 2 or nominated by them in Phase 4, with **no prior naming by the operator in this conversation or any prior contact with this account** | **YES — the only class that counts** |
| **PROMPTED** | Emerged only after the operator asked about that specific area (even neutrally, e.g. "what happens when someone enquires and goes quiet?") | No |
| **AGREED AFTER FRAMING** | The operator described the problem and the buyer agreed | **No — and it is nearly worthless as evidence** |

Plus one more, which is often the most valuable row in the log:

| Class | Definition | Use |
|---|---|---|
| **OTHER PROBLEM (unanticipated)** | The buyer volunteered a significant problem the plan did not predict | Does not count toward H-10. **Escalate to the weekly review** — repeated unanticipated problems are a signal the thesis is aimed at the wrong pain (`DECISION_TREE.md` D4b reframe) |

### Worked distinctions

| Situation | Class |
|---|---|
| Phase 2: "honestly the WhatsApp ones just get lost when it's busy" — unprompted | **VOLUNTEERED** |
| Phase 3: operator asks "what happens when someone enquires and goes quiet?" → "nothing, usually" | **PROMPTED** |
| Phase 6: operator explains the offer → "yeah, that's definitely us" | **AGREED AFTER FRAMING** |
| Phase 4: "what bothers you most?" → "getting staff to actually call people back" | **VOLUNTEERED** (they nominated it) |
| Phase 4: "what bothers you most?" → "recruitment, honestly" | **OTHER PROBLEM (unanticipated)** |
| Teardown named the problem, buyer later repeats it in Phase 2 | **Contaminated — excluded from the denominator** |

## 2b. Single source of truth for contamination

Two files carry a contamination field: `data/interview_index.csv` (`resonance_contaminated`) and
`data/resonance_log.csv` (`contaminated`). They can drift, and a drifted denominator is an
unfalsifiable gate.

> **`resonance_log.csv` is authoritative.** It is set during classification, from the transcript,
> at least an hour after the interview — the moment when the judgement is actually being made.
> `interview_index.csv` is a convenience copy for finding records and is never counted.

If the two disagree, the resonance log wins and the index is corrected. The weekly review checks
the two for drift (finding `DEEP-5`).

## 3. Classification procedure *(binding)*

1. Classify **from the recording or transcript**, not from memory. Memory systematically upgrades.
2. Classify **at least one hour after** the interview.
3. For every `VOLUNTEERED`, record the **verbatim line**. No quote → not volunteered.
4. Check the integrity header of the interview record: if `resonance_contaminated = Y`, the
   interview is **excluded from the denominator entirely** — it is neither a pass nor a fail.
5. Check prior contact: if a teardown or any earlier message to that account named the problem,
   the account is contaminated even if this conversation was clean.
6. If genuinely uncertain between VOLUNTEERED and PROMPTED → record **PROMPTED**. The tie always
   goes against the thesis.

## 4. Fields

| Field | Values |
|---|---|
| `interview_id` | `I-0NN` |
| `date` | — |
| `segment` / `role` | — |
| `contaminated` | `Y`/`N` — Y excludes from denominator |
| `contamination_reason` | operator named it / teardown named it / agenda named it / prior contact |
| `counts_in_denominator` | `Y`/`N` (auto: N if contaminated or `calibration = Y`) |
| **Problem categories** (each: `VOLUNTEERED` / `PROMPTED` / `AGREED` / `ABSENT`) | see §5 |
| `other_problem_volunteered` | free text — the unanticipated pain |
| `verbatim` | the exact line, required for any VOLUNTEERED |
| `phase` | 2 / 4 / 6 |
| `classified_from` | `transcript` / `recording` / `memory` — **`memory` is flagged as low quality** |
| `classified_at` | timestamp, must be ≥ 1 h after the interview |
| `warm_cold` | from the ledger — **required**; see §6.1 |
| `selected_on_fit_only` | `Y`/`N` — was this account chosen on ICP fit rather than observed dysfunction (`RT-K1`)? |

## 5. Problem categories tracked

| Code | Category |
|---|---|
| `PC-1` | Missed or slow follow-up on enquiries |
| `PC-2` | Enquiry handling fragmented across channels |
| `PC-3` | Booking friction |
| `PC-4` | No-show leakage |
| `PC-5` | Handoff failures between staff or locations |
| `PC-6` | Unclear attribution — not knowing what produces patients |
| `PC-7` | Operational bottleneck, typically the owner |
| `PC-8` | **Other / unanticipated** — free text, always recorded |

**The D4 counter:** an interview counts as a resonance hit if **any of `PC-1`…`PC-7` is
`VOLUNTEERED`**. One is enough; the categories are facets of the same underlying claim.

## 6. The D4 calculation

```
denominator = interviews where counts_in_denominator = Y
numerator   = those with ≥1 of PC-1..PC-7 classified VOLUNTEERED
```

| Result | Reading | Action |
|---|---|---|
| ≥ 5/10 | **PASS** | → D5. Harvest the verbatim corpus (`POSITIONING_ARCHITECTURE.md` §3) |
| 2–4/10 | **PARTIAL** | → D4b reframe, once, around the problem they *did* volunteer |
| ≤ 1/10 | **FAIL** | Thesis' core claim is false in this segment → D3b or D7 |
| Clean denominator < 10 | **UNDER-SAMPLED** | Separate exclusions from volume first, then `15_DECISION_GATE_CHECKLIST.md` G-8: named cause + re-gate within 14 days + strike |

### 6.1 The warm/cold split — mandatory at D4 *(red-team finding `RT-K2`)*

Report the ratio **split by `warm_cold`**, always:

```
Cold:  volunteered ___ / denominator ___
Warm:  volunteered ___ / denominator ___
```

Warm contacts are friendlier, more forthcoming, and more likely to reach for a problem that pleases
the person asking. A resonance ratio carried by warm conversations is a measure of goodwill.

> **If ≥ 60% of the clean denominator is warm, record `PASS (warm-dependent)`.** H-10 is then
> supported for warm buyers only, and the cold arm remains untested. Keep interviewing cold until
> the cold denominator alone reaches 10.

### 6.2 The denominator-order rule

The denominator is **every clean interview, in chronological order**. It is never the "best ten,"
never the ten most relevant, never the ten you remember most clearly. Selecting which interviews
count is the cheapest available way to pass this gate dishonestly, and it leaves no trace.

**Denominator honesty is the whole game.** Excluding contaminated interviews shrinks the
denominator and makes the gate harder to reach. That is correct and intentional. Counting a
contaminated interview as a pass is the single cheapest way to fake this program's most important
result.

## 7. Signals to watch beyond the ratio

| Signal | Meaning |
|---|---|
| Same `PC-x` volunteered repeatedly | Thematic saturation — the wedge should be built on that facet specifically |
| High `PC-8` rate | The plan is aimed at the wrong pain. Strong D4b reframe candidate |
| High `AGREED AFTER FRAMING`, low `VOLUNTEERED` | **You are selling a problem, not finding one.** The most dangerous pattern in the log |
| High `ABSENT` across all categories | Either the segment does not have it, or Phase 2 is being cut short |
| Volunteered but with no consequence attached | Real but not urgent — it will not fund a diagnostic |

That third row deserves emphasis: a log dominated by `AGREED AFTER FRAMING` looks encouraging and
means nothing. If you find it, the correct response is to lengthen Phase 2, not to celebrate.

## 7b. Survivorship bias — a limit that cannot be removed

Only people who replied are interviewed, and repliers plausibly self-select for having the problem.
**This biases H-10 upward and cannot be eliminated** — you cannot interview someone who ignored you.

Partial counters:
- The touch-4 close-the-loop message (`06_OUTREACH_SEQUENCE.md` §6) extracts a *reason* from
  non-repliers. A cluster of `L-07` ("no perceived problem") among non-repliers is the closest
  available read on the silent majority, and it is **counted against** the thesis at the weekly review.
- Report the reply rate alongside the resonance ratio, always. 5/10 volunteered from a 40% reply
  rate is a substantially stronger result than 5/10 from an 8% reply rate, and the gate result
  should say which it was.

Stated here so that a D4 pass is read with the bias attached, rather than as a clean market fact.

## 8. CSV format

```csv
interview_id,date,segment,role,warm_cold,selected_on_fit_only,contaminated,contamination_reason,counts_in_denominator,PC1,PC2,PC3,PC4,PC5,PC6,PC7,PC8_other,verbatim,phase,classified_from,classified_at
```

### SYNTHETIC EXAMPLE — NOT EVIDENCE
*Format illustration only. No interview took place. Must never be counted or cited. Delete before use.*

```csv
I-000,2026-09-16,S2,[SYNTHETIC] Ops Dir,cold,Y,N,,Y,VOLUNTEERED,PROMPTED,ABSENT,ABSENT,VOLUNTEERED,ABSENT,ABSENT,,"[SYNTHETIC — NOT A REAL QUOTE]",2,transcript,2026-09-16T18:00
```
