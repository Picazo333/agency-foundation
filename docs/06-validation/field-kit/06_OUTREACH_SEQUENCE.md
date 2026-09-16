---
status: review
owner: strategy
updated: 2026-09-16
authority: workbench
depends_on:
  - ../../02-strategy/sales/ACQUISITION_MARKETING_SYSTEM.md
  - ../../02-strategy/positioning/POSITIONING_ARCHITECTURE.md
  - ../../04-operations/GOVERNANCE_RISK_SECURITY_CHECKLIST.md
  - 04_TEARDOWN_SOP.md
---
# 06 — Outreach Sequence

> **Instrument type:** exact operational message sequences. **Hypotheses:** H-03, H-03b, X-01.
> **Gate:** D3. **Volume:** 15–20 new targets/week, 4 touches each (`ACQUISITION_MARKETING_SYSTEM.md` CH-1).
>
> **The ask is always a research conversation, never a meeting about your services.** That is not
> a softening tactic — it is what keeps H-10 testable and what makes the D4 gate meaningful.

## 0. Binding compliance rules

From `GOVERNANCE_RISK_SECURITY_CHECKLIST.md` §6, binding now, independent of jurisdiction answers:

- Identify yourself and your purpose in the first message.
- Honour opt-outs immediately and permanently, repository-wide.
- No scraped personal contact data. B2B channels only.
- No misleading subject lines.
- Jurisdiction-specific rules (`M-01`, `M-02`, `M-03`) are ⚖️ open and must be checked before
  contacting healthcare providers at volume.

## 1. Sequence at a glance

| Touch | Day | Channel | Purpose | Hypothesis |
|---|---|---|---|---|
| **1** Observation opener | 0 | Email | Earn a reply with one specific, verifiable observation | H-03 |
| **2** Teardown | +4 | Email | Deliver the artifact; demonstrate restraint | H-03, X-01 |
| **3** Pattern note | +11 | Email | One useful thing from another teardown; no ask | H-03 |
| **4** Close the loop | +25 | Email | Extract a reason for the silence | H-03, **loss codes** |
| — | — | — | **Stop. No touch 5.** | — |

Warm contacts (`warm_cold = warm`) use §2 instead and skip touches 1–2.

## 2. Warm introduction

**Purpose:** convert an existing relationship into a research conversation at the lowest possible
social cost.
**Hypothesis:** H-03 (warm arm). **Log:** `source=warm`, `touch_count=1`.

```
Subject: A favour — 25 minutes of questions?

Hi [name],

I'm doing something new and I need to be talked out of it or into it by people who actually
run [segment] businesses.

I'm mapping how [segment] groups handle enquiries — what happens between someone getting in
touch and actually being booked in. Not selling anything; I genuinely don't know enough yet
to sell anything.

Could I ask you 25 minutes of questions? I'd rather hear how it actually works than keep
guessing.

[name]
```

**What NOT to infer from a yes:** nothing commercial. A warm yes measures the relationship, not the
market. Warm conversations still count toward D3 *only if* they meet all four criteria in
`02_TARGET_ACCOUNT_LEDGER.md` §4 — and at D3 you must report the warm/cold split, because eight
warm conversations have tested your network rather than the segment's reachability.

## 3. Touch 1 — cold observation opener

**Purpose:** earn a reply by proving you looked, in under 90 words.
**Hypothesis:** H-03; the treatment arm of X-01.
**Log:** `touch_count=1`, `last_touch_date`, later `reply`.

```
Subject: One thing I noticed about your booking path

Hi [name] — I'm [name], I work on enquiry-to-booking systems for [segment] groups.

I was looking at how [business] handles enquiries. I sent a general question through your
web form on [day] at [time] to see how it was handled; the reply came [elapsed]. Through
WhatsApp the same question came back in [elapsed].

I don't know whether that's typical or whether it matters to you — that's genuinely not
something I can tell from outside.

I'm mapping how groups your size handle this. Worth 25 minutes?

[name]
```

| | |
|---|---|
| **Purpose** | A reply. Not a meeting, not interest |
| **Data to log** | `reply`, reply sentiment, elapsed time to reply |
| **What NOT to infer from a positive reply** | Nothing about demand, budget, or the problem's existence. A reply means the message worked. That is all it means |
| **Prohibited** | Any pitch · any price · any claim about their revenue or performance · the plan's framing language ("revenue leak") · manufactured urgency |
| **Why "I don't know whether that matters"** | It is true, it disarms defensiveness, and it leaves the buyer room to volunteer the problem — which is exactly what H-10 measures |

## 4. Touch 2 — teardown delivery

**Purpose:** transfer something of value with nothing attached.
**Log:** `teardown_status=sent`.

```
Subject: The full version — [business]

Hi [name],

I finished the short version — three things I could see from outside, plus a list of the
things I couldn't. Five-minute video and a one-page summary: [link]

No obligation and nothing to buy. If it's useful, the two questions at the end are the ones
I'd genuinely like to ask you.

[name]
```

**Prohibited:** "as you'll see, this is costing you…" · any next-step framing beyond the questions
· any offer. Per `04_TEARDOWN_SOP.md` §6, a pitch here contaminates H-10 for this account
permanently.

## 5. Touch 3 — pattern note

**Purpose:** demonstrate accumulating domain knowledge; stay present without asking.

```
Subject: Something I keep seeing

Hi [name],

I've now looked at [n] [segment] groups. The thing I did not expect: [one specific,
non-obvious, non-judgemental observation about the pattern — not about them].

Sharing it because it might be useful. No ask.

[name]
```

**Rules:** the observation must be real and drawn from your own teardowns. **Never invent a
pattern.** If you have not yet seen one, skip touch 3 — an invented pattern is fabricated evidence
that you will later start believing yourself. Never cite a statistic (`PP-1`).

## 6. Touch 4 — close the loop *(the highest-value message in the sequence)*

**Purpose:** extract a **reason**. Reasons are the output the validation plan needs.

```
Subject: Closing the loop

Hi [name],

I'll assume the timing isn't right and stop emailing — no hard feelings.

One thing that would genuinely help: was it the timing, the topic, or just not a priority?
One word is plenty. I'm trying to work out whether I'm solving a problem [segment] groups
actually have.

Thanks either way.

[name]
```

| | |
|---|---|
| **Data to log** | Reply → map to a loss code (`SALES_SYSTEM.md` §8). **`L-07` "no perceived problem" is the most strategically important code in the system** |
| **Why it works** | It removes the obligation to buy, which is what the silence was usually about |
| **Hard rule** | This is the **last** touch. There is no touch 5. Opt-out is permanent |
| **Escalation** | Three consecutive `L-07` responses → escalate to D4 immediately (`SALES_SYSTEM.md` §8). That is a thesis signal, not a sales problem |

## 7. Referral / intermediary outreach *(CH-3, X-06)*

**Targets:** PMS/EMR vendors, accountants and fractional CFOs serving the segment,
practice-management consultants, sector associations, non-competing agencies.

```
Subject: Your clients' implementation gap

Hi [name],

You work with [segment] groups; so do I, from a different angle — I measure and fix what
happens between an enquiry arriving and a booking existing.

The overlap I think exists: your clients stall at implementation, and that shows up in your
world as [churn / unadopted software / "we never got round to it"].

I'm not asking for referrals. I'd like 25 minutes to understand whether you see that too,
and whether it's worth either of us doing anything about.

[name]
```

**Log:** `source=partner`. **What NOT to infer:** an intermediary confirming a problem exists is
`SIGNAL` about the intermediary's perception, **not** buyer evidence. It never counts toward H-10,
which requires an actual buyer. Intermediary conversations are logged separately and excluded from
the H-10 denominator.

## 8. Reply handling

For each: what it means, what to do, what to log, and **what not to conclude**.

### 8.1 Interested — wants to talk
- **Do:** book 25–30 min within 5 business days. Send `07_BUYER_INTERVIEW_GUIDE.md` nothing in
  advance — no agenda that names the problem (H-10 protection).
- **Log:** `reply=positive`, book, set `next_action_date`.
- **Do NOT conclude:** that they have the problem, that they will buy, or that the thesis is
  working. Interest in a conversation is evidence about your *message*, not your *market*.

### 8.2 Curious but not obviously qualified
- **Do:** take the conversation anyway during the access phase. Run the interview guide normally.
- **Log:** conversation yes; `qualified_conversation` per the strict four-part test; qualification
  status from the scorecard only.
- **Do NOT conclude:** that a pleasant conversation is a pipeline entry. Set `NOT_YET` and mean it.

### 8.3 "No budget"
- **Do:** ask one question — *"Understood. Out of interest, if it were free to find out, would it
  be worth knowing? Or is it just not a priority?"* This separates `L-01` (no budget) from `L-07`
  (no perceived problem), which are completely different findings.
- **Log:** `L-01` or `L-07` accordingly. Record in `11_PRICE_SIGNAL_LOG.md` **only if a price was
  actually quoted** — otherwise it is not a price signal, it is a budget statement.
- **Do NOT conclude:** that the price is too high. No price was discussed.

### 8.4 Wrong person
- **Do:** ask for the right person by role, not by name: *"Who'd be the right person to ask about
  how enquiries get handled across your sites?"*
- **Log:** update `committee_position`; this is **H-03b** evidence about signer reachability.
- **Do NOT conclude:** a fail. Being routed is normal and the routing itself is data.

### 8.5 "We already have someone for this"
- **Do:** *"Makes sense — most groups your size do. Mine sits after the leads arrive rather than
  before, so it usually doesn't overlap. Worth 25 minutes to check?"*
- **Log:** the incumbent's name and category if offered — this is **H-07**, the only competitive
  intelligence available (`U-12`).
- **Do NOT:** criticise the incumbent (`PP-6`). **Do NOT conclude** the position is occupied unless
  the incumbent actually does operational measurement — most do marketing.

### 8.6 Not interested
- **Do:** one line of thanks. Nothing else.
- **Log:** `reply=negative`, loss code, stop the sequence.
- **Do NOT:** send the remaining touches. **Do NOT conclude** anything from a single no.

### 8.7 Opt-out / "remove me"
- **Do:** confirm once, briefly, then never contact again through any channel.
- **Log:** `reply=optout`. **Permanent, repository-wide.**

### 8.8 "How much does it cost?" — asked before any conversation
The most dangerous reply to handle, because answering it destroys the price test.

- **Do:**
  > "Honest answer: I can't price a fix before measuring what's actually happening — I'd just be
  > guessing, and you'd be paying for a guess. The first step is small and paid, and you keep the
  > measurement whether or not you do anything else with me. Can I ask you a few questions first so
  > I know whether it's even relevant?"
- **Log:** the fact that price was asked *unprompted* — a useful H-04 secondary signal.
- **Do NOT:** quote a number outside the structured probe in `11_PRICE_SIGNAL_LOG.md` §3. Quoting
  early contaminates the price sequence, anchors the relationship, and wastes the single most
  valuable data point you will get from that buyer.
- **Do NOT:** quote a *range*. Ranges anchor to the bottom (H-04 confound). One price, then silence.

### 8.9 An enthusiastic champion asks for a proposal to circulate internally

The hardest reply in the set, because refusing feels like refusing help. But a proposal written for
someone who cannot buy is the exact mechanism by which unbilled sales hours go from 20 to 80 per
close (`PRICING_AND_ECONOMICS_MODEL.md` §8.3), and a document circulated without you in the room
gets read by whoever is most sceptical, in the least favourable order.

- **Do:**
  > "I'd rather not send something you have to defend on my behalf — it never survives the
  > journey. What works better: I'll write you a half-page you can forward, and I ask for 20
  > minutes with whoever signs so they hear the trade-offs from me. If that's not realistic right
  > now, that's a genuinely useful thing for me to know."
- **What you may send:** a **half-page summary** — what you observed, what the diagnostic measures,
  duration, and that pricing follows a conversation. **Not** a proposal, **not** a price.
- **Log:** `committee_position=champion`; Q3 `FAIL` until a signer is named and spoken to; H-03b
  evidence that the signer is not directly reachable.
- **Do NOT conclude:** that an enthusiastic champion is a pipeline entry. `09_QUALIFICATION_SCORECARD.md`
  returns `NOT YET QUALIFIED`, and that is the correct, healthy outcome.
- **Do NOT:** write the full proposal anyway "because they seem serious." That is the rationalisation
  the gate exists to catch.

## 9. Volume, tiering and stop rules

| | |
|---|---|
| New targets/week | 15–20 |
| Deep research (test enquiry + teardown) | 6–8/week |
| Light research | 8–12/week |
| Outreach hours/week | 8–10, protected block (`OPERATING_MODEL.md` §6.1) |
| **Reply rate < 8% after 60 contacts** | The **message** is wrong, not the segment. Rewrite touch 1 before adding volume or rotating segment |
| **< 4 qualified conversations at day 30** | D3 fail → `DECISION_TREE.md` D3b. Diagnose channel vs message vs segment *before* rotating |

## 10. X-01 — the message test, run inside normal outreach

`FIELD_VALIDATION_PLAN.md` §5 X-01: 20 observation-first vs 20 generic-value openers; success is a
reply rate ≥ 2× for observation-first.

| Arm | Message | Assign by |
|---|---|---|
| **A — treatment** | §3 touch 1 as written | Alternate strictly down the target list |
| **B — control** | Same subject discipline, no specific observation: introduces who you are and asks for 25 minutes to understand how they handle enquiries | Alternate |

**Confound control:** assign by strict alternation, not by preference. Assigning your best-fit
accounts to arm A guarantees a false positive — and it is the mistake you will be tempted to make.
Log the arm in ledger `notes` at the moment of sending, never afterwards.

**Interpretation:** at n=40 this is a directional `SIGNAL` and an existence proof, not a
statistically significant result. Do not use the phrase "statistically significant"
(`13_EXPERIMENT_RUNBOOK.md` §2).
