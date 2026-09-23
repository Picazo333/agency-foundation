# ADR-0014 — Targeted visual synthesis and expression-base locks

Status: APPROVED
Date: 2026-09-22

## Context
ADR-0013 introduced the 100-board program to move DIVINIVID from open-ended discovery into controlled coverage before production.

Subsequent work established a coherent Core, identified diminishing returns from continued quota-driven moodboard generation, and produced two human-approved expression bases:
- Route 3+4 as the preferred principal expression/production base;
- Route 3+5 as a specialized bestiary/apparition base.

The remaining need is no longer broad aesthetic discovery. It is targeted synthesis, translation and production readiness.

## Decision
1. Keep the 100-contract corpus as historical specification, coverage inventory and reference checklist.
2. Stop treating all 100 contracts as mandatory rendered moodboards.
3. Continue with the targeted synthesis plan in `docs/08-plans/master/DIVINIVID_TARGETED_VISUAL_SYNTHESIS_PLAN_V1.md`.
4. Freeze:
   - `DIVINIVID_CORE_LOCK_V1`;
   - `BASE_LOCK_B1` — Route 3+4;
   - `BESTIARY_BASE_B0` — Route 3+5.
5. Use minimum-necessary mutation and explicit human gates for the M1/M2 sequence.
6. Keep the bestiary branch separate from the primary production base during this sequence.

## Immediate sequence
`M1-A Anatomía Celeste -> M1-B Topografía Orgánica -> human comparison -> optional bounded synthesis -> M2-Soft -> M2-Hard -> human comparison -> MAIN_SYSTEM_B2`.

## Scope of supersession
This ADR supersedes only the requirement to render the full 100-board program before synthesis.

It preserves:
- Archive V1;
- Visual Canon V1;
- Anti-Canon;
- lineage and provenance work;
- the 100-contract corpus as coverage/reference evidence;
- runtime anti-drift lessons;
- human-gated promotion;
- the requirement for a mature production specification before mass asset production.

## Why
This path preserves the strongest discoveries while reducing drift, token waste and redundant exploration. It creates a smaller number of diagnostic visual experiments and a faster path toward identity synthesis, Figma and web prototyping.

## Trade-offs
- the project will not necessarily have 100 rendered boards;
- some coverage remains specified rather than visualized;
- later stress testing may still justify targeted gap pieces.

## Reopen if
- M1/M2 shows that B1 cannot cover the required range;
- application stress tests reveal a foundational identity failure;
- the bestiary/base separation creates an unresolvable split;
- explicit human evidence materially contradicts the current locks.
