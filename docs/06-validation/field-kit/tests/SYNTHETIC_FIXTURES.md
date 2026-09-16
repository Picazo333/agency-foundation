---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - ../09_QUALIFICATION_SCORECARD.md
  - ../10_PROBLEM_RESONANCE_LOG.md
  - ../12_DIAGNOSTIC_SALES_ATTEMPT_LOG.md
---
# Synthetic Test Fixtures

> # ⚠️ SYNTHETIC TEST FIXTURE — NOT EVIDENCE
>
> **Every buyer, quote, reaction and number below is invented for the purpose of testing this
> kit's instruments.** No interview took place. No person said any of these words. No business is
> described.
>
> These fixtures must **never** be entered into `../data/*.csv`, counted toward any gate, cited in
> the learning log, quoted in any buyer-facing material, or referenced as market evidence. They
> live in `tests/` precisely so they cannot be mistaken for the contents of the evidence
> directories.
>
> `E-09` remains true: **zero real buyer conversations have occurred.**

## Purpose — Pass 4

Each fixture is a buyer who would produce a **false positive** in a loosely designed kit. Running
them through the instruments tests one thing: *does the kit refuse to count them?*

---

## Fixture 1 — Interested buyer with no budget

**SYNTHETIC.** A 4-site dermatology group. The operations director is engaged and delighted by the
teardown, volunteers unprompted in Phase 2 that "the WhatsApp ones just disappear when we're busy,"
asks detailed questions about the diagnostic, and says *"this is exactly what we need."* When the
price is quoted she says *"honestly, there's no money for anything like this until the new site
opens next year."* No counteroffer. No signer conversation.

### Run through the instruments

| Instrument | Result | Correct? |
|---|---|---|
| Ledger `qualified_conversation` | **Y** — 30 min, ops director (direct influencer), in-segment, about operations | ✅ Counts for D3 access. Access *was* achieved |
| Resonance log | **VOLUNTEERED** (`PC-1`, `PC-2`), verbatim captured, uncontaminated | ✅ Counts for D4. The problem *is* real here |
| Qualification Q1 fit | PASS | ✅ |
| Qualification Q2 problem | PASS — volunteered, verbatim, contaminated = N | ✅ |
| Qualification **Q3 authority** | **FAIL** — signer never named or spoken to | ✅ |
| Qualification Q4 access | RISK — not discussed | ✅ |
| **Outcome** | **NOT YET QUALIFIED** | ✅ |
| Quote permitted? | **NO** — only QUALIFIED / QUALIFIED_WITH_RISK may be quoted | ✅ |
| Price log | If quoted anyway: `dismissed`/budget statement, `evidence_level = PRICE_SIGNAL`, **not** payment | ✅ |
| Sales attempt log | **Not an attempt** — the buyer was not qualified. Excluded from the H-01 denominator | ✅ |
| Loss code | `L-01` no budget — **separated from `L-07`** by the §8.3 probe | ✅ |

**Does the kit produce a false positive?** No. The enthusiasm reaches no counter that matters.
She contributes correctly to D3 (access works) and D4 (the problem is real) and correctly
contributes **nothing** to D5.

**What a loose kit would have done:** counted her as a "warm lead," logged her enthusiasm as
demand, and arrived at D5 with an inflated sense of a pipeline.

**Weakness this exposed:** none new. §8.3 of the outreach sequence already forces the
`L-01` vs `L-07` distinction, which is what makes this buyer legible rather than just "a no."

---

## Fixture 2 — Real problem, no decision authority

**SYNTHETIC.** A 7-site dental group. The marketing coordinator takes the call, is well-informed,
volunteers in Phase 2 that leads from three channels are tracked in three different places and
"nobody really owns the ones that come in overnight." He is enthusiastic, says he will "definitely
push for this internally," asks for a proposal to circulate, and cannot say who signs — *"probably
the partners, they meet monthly-ish."* He does not offer to arrange an introduction.

### Run through the instruments

| Instrument | Result | Correct? |
|---|---|---|
| Ledger `qualified_conversation` | **Y** — direct influencer, in-segment, 25 min, operations | ✅ |
| Ledger `committee_position` | `champion` — and potentially also the §6.2 blocker, being the marketing owner | ✅ |
| Resonance log | **VOLUNTEERED** (`PC-2`, `PC-5`) | ✅ |
| Qualification Q3 | **FAIL** — "probably the partners, monthly-ish" is precisely the `AUD-05-02` answer the gate rejects | ✅ |
| **Outcome** | **NOT YET QUALIFIED** — specific next action: one conversation with a named signer | ✅ |
| Proposal on request? | **Refused** — `SALES_SYSTEM.md` §5.1 prohibits a written proposal before Q1–Q4 pass | ✅ |
| H-03b evidence | Signer **not** directly reachable — logged | ✅ |

**Does the kit produce a false positive?** No. Q3 is explicitly written so that "the managing
partner is keen" fails, and this is the softer version of that.

**Weakness this exposed — and fixed:** the kit had no phrasing for *refusing* a proposal request
from an enthusiastic champion without damaging the relationship. An operator under pressure would
have invented one, and the easiest invention is to send the proposal. **Fixed:** added §8.9 to
`06_OUTREACH_SEQUENCE.md`.

---

## Fixture 3 — Rejects the core problem

**SYNTHETIC.** A 5-site aesthetics group. The owner is direct and unhurried. In Phase 2 he
describes the enquiry path fluently and without complaint. Asked in Phase 4 what bothers him most,
he says: *"Getting people through the door isn't the issue. I can't hire injectors fast enough —
that's the whole problem."* He is polite about the teardown, accurate about his own numbers, and
entirely uninterested in measuring intake.

### Run through the instruments

| Instrument | Result | Correct? |
|---|---|---|
| Ledger `qualified_conversation` | **Y** — signer, in-segment, 30 min, operations. **A rejection from a qualified buyer is a successful conversation** | ✅ |
| Resonance log `PC-1`…`PC-7` | **ABSENT** across all seven | ✅ |
| Resonance log `PC-8` | **OTHER PROBLEM (unanticipated)**: recruitment/capacity | ✅ Recorded, not discarded |
| Counts in D4 denominator? | **Yes — as a non-hit.** This is the point of the denominator | ✅ |
| Qualification Q2 | **FAIL** — no relevant problem described | ✅ |
| **Outcome** | **DISQUALIFIED** (Q2 fail, no realistic path) | ✅ |
| Loss code | **`L-07` no perceived problem** — the most strategically important code | ✅ |
| Escalation | 3 consecutive `L-07` → escalate to D4 (`SALES_SYSTEM.md` §8) | ✅ |

**Does the kit produce a false positive?** No — and more importantly, it **extracts the finding**.
This buyer is the most valuable of the three: he is a clean falsification data point *and* he
volunteered an unanticipated problem that the D4b reframe path exists to catch.

**Weakness this exposed:** the `PC-8` column existed but nothing aggregated it. A single
unanticipated problem is noise; five of the same one is a reframe signal, and nothing was counting
them. **Fixed:** added a `PC-8` cluster check to `14_WEEKLY_VALIDATION_REVIEW.md` §4 and to the D4
gate inputs.

---

## Pass 4 summary

| Fixture | False positive produced? | Correctly counted where it should be |
|---|---|---|
| 1 — Interested, no budget | **No** | D3 ✅ · D4 ✅ · D5 ✅ excluded |
| 2 — Problem, no authority | **No** | D3 ✅ · D4 ✅ · D5 ✅ excluded · H-03b ✅ |
| 3 — Rejects the problem | **No** | D3 ✅ · D4 ✅ counted as a non-hit · `PC-8` ✅ |

**The load-bearing separation confirmed by all three:** a conversation can be *qualified for access*
(D3) while the buyer is *not qualified to buy* (D5). Collapsing those two meanings is the single
most likely way this kit would have manufactured a false pipeline — and the instruments keep them
in different columns, with different definitions, feeding different gates.

**Two fixes were produced by this pass** and are recorded in `../19_KIT_AUDIT_LOG.md`.

> ⚠️ Repeat: **SYNTHETIC — NOT EVIDENCE.** Nothing above happened.
