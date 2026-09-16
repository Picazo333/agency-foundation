---
name: project-impeccable-adapter
description: Safe project adapter for the pinned upstream Impeccable skill. Use for bounded design critique, refinement, accessibility, responsive, hierarchy and frontend quality review.
license: Apache-2.0 (upstream)
---
# Impeccable — Project Adapter

## Upstream source
- Repository: `pbakaus/impeccable`
- Commit: `0a4e72a254f3b175c95b36b82e5f2e60fa63f116`
- Path: `skill/SKILL.src.md`
- License: Apache-2.0

Read the exact pinned upstream Skill and only the command/reference files necessary for the current task when GitHub access is available. Do not silently substitute upstream `main`/`latest`.

## Local authority
Impeccable is a **validation and refinement capability** for an already defined surface or visual world.

It may review/refine:
- typography hierarchy;
- spacing/rhythm/alignment;
- layout;
- color/contrast;
- accessibility;
- responsive behavior;
- motion/micro-interactions;
- visual polish;
- production-readiness of frontend surfaces.

It may NOT:
- redefine Brand strategy, naming, or frozen visual thesis;
- replace an approved visual world unless the task explicitly requests redesign;
- broaden workstream scope;
- change factual copy or business claims without task authority;
- run hooks, installers, binaries, package commands, or external network actions without explicit approval.

## Safe execution mode
`REFERENCE_ONLY` by default.

Upstream Impeccable can use a launcher/binary and hooks. Those executable behaviors are intentionally disabled by this adapter until explicitly approved as Tier 3 under `docs/00-meta/capability-governance.md`.

## Preferred invocation pattern
Use bounded passes rather than endless polishing.

For each target provide:
- current visual canon;
- current surface/mode;
- exact refinement objective;
- allowed edits;
- forbidden changes;
- acceptance criteria.

Return:
1. highest-impact defects;
2. concrete corrections;
3. accessibility/responsive risks where relevant;
4. changes intentionally not made;
5. one bounded confirmation pass after fixes.

## Current Brand-route use
For KIROGRAF, Impeccable is best used after concept selection to refine foundations, composition, digital specimens and stress-test outputs. It is not the source of the visual thesis.
