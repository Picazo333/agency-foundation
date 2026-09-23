---
id: HARVEST-20260922-prelock-behavior-exploration
status: candidate
owner: meta
created: 2026-09-22
source_event_type: ADR
confidentiality: INTERNAL
routes:
  - sop_process
  - eval_test
  - skill_candidate
  - benchmark_lesson
provenance:
  artifact:
    - docs/07-decisions/ADR-0015-pre-lock-exploration-before-final-expression-lock.md
    - docs/08-plans/master/DIVINIVID_PRE_LOCK_EXPLORATION_V1.md
---
# Harvest Record — Explore identity behavior before final expression lock

## What changed
After a visual breakthrough, the project chose not to immediately freeze the expression or industrialize it into a full design system.

Instead, it inserted a bounded pre-lock program to test how the visual language behaves across:
- typography;
- sign/icon grammar;
- hero composition;
- density/intensity;
- motion;
- digital interface;
- commercial/application stress.

## Reusable lesson
A strong aesthetic breakthrough is not yet a production identity.

Before final lock, test the system dimensions most likely to reveal accidental dependencies or hidden incompatibilities.

A portable sequence is:

`visual breakthrough -> behavior labs -> application stress -> synthesis -> red team -> final expression lock -> production design system`.

## Why it matters
This can prevent:
- accidentally canonizing typography or icons that appeared only as generation artifacts;
- building a design system around an untested hero composition;
- discovering too late that the identity cannot survive low-intensity or functional contexts;
- premature component/token industrialization;
- aesthetic drift caused by testing too many variables at once.

## Portable controls
- one major variable under test per lab;
- shared fixed working anchor;
- strict candidate budgets;
- human promotion only;
- rejected lab outputs excluded from later positive context;
- at least one stress context that removes a common aesthetic crutch;
- final lock only after commercial and production viability checks.

## Candidate evals
1. A visual breakthrough is promoted directly into a design system without behavior testing.
   - Expected: flag premature lock risk.
2. Typography and iconography from one generated artifact are silently treated as canonical.
   - Expected: fail authority.
3. A brand works only at maximum visual intensity.
   - Expected: fail elasticity test.
4. A system passes visual review but cannot produce usable digital primitives.
   - Expected: fail production-viability gate.

## Reuse boundary
Portable:
- behavior-first pre-lock exploration;
- bounded lab structure;
- final synthesis gate.

Project-local:
- DIVINIVID visual language;
- M1-B;
- exact route names and palette.
