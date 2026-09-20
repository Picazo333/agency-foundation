---
status: review
owner: meta
updated: 2026-09-20
authority: process
depends_on:
  - ../../noema.project.yaml
  - source-of-truth.md
  - operating-model.md
  - ../08-plans/master/DIVINIVID_VISUAL_UNIVERSE_META_PLAN_V2.md
---
# DIVINIVID — Noema RC0 Selective Adoption

## Purpose
Apply Noema RC0 to DIVINIVID without transferring domain authority away from the project and without turning conformance into a substitute for creative or commercial quality.

This migration follows the prior Noema reference audit of `Picazo333/agency-foundation`.

## Findings carried forward from the reference audit
- AF-01: `PROJECT_STATE.md` had drifted behind actual work.
- AF-02: default agent bootstrap loaded too much context.
- AF-03: some universal governance and project-specific governance are co-located.
- AF-04: executor assignment was more concrete than the capability-first architecture.
- AF-05: cross-project relations were human-readable but not machine-declared.
- AF-06: Noema conformance must never replace Brand/market gates.
- AF-07: large-media/Asset Factory storage migration should not be forced prematurely.

## Changes in this migration
1. add `noema.project.yaml` pinned to Noema `0.1.0-rc.0`;
2. declare project authority, quality claims and relations to Noema/Skill Foundry;
3. replace heavy unconditional bootstrap with progressive context routing;
4. refresh `PROJECT_STATE.md` to the current visual-universe checkpoint;
5. add Noema conformance workflow pinned to an immutable Noema commit;
6. document the DIVINIVID visual-universe meta-plan as a durable artifact;
7. capture reusable visual-production lessons through Project Harvest;
8. keep visual canon, business strategy, human gates and Asset Factory semantics domain-owned.

## Authority boundary
Noema owns:
- protocol;
- schemas;
- conformance;
- interoperable coordination semantics.

DIVINIVID owns:
- brand/visual canon;
- strategy/delivery canon;
- visual evaluation;
- Asset Factory contracts;
- project-specific quality gates;
- final human approvals.

Skill Foundry owns:
- reusable Skill taxonomy/ontology/registry;
- Skill lifecycle and eval semantics.

## Progressive context
`AGENTS.md` is reduced to an entry map and invariant set. The manifest owns exact mode routing.

Agents should start from:
1. `AGENTS.md`;
2. `noema.project.yaml`;
3. the current task.

Deeper context is loaded only when the selected mode/task requires it.

## Quality claims
The project declares:
- contract-conformance;
- delivery-integrity;
- research-groundedness;
- visual-coherence;
- provenance;
- context-efficiency;
- security-boundaries;
- recoverability.

A Noema PASS only establishes structural conformance. Visual coherence and delivery quality still require DIVINIVID evidence and human/model/deterministic checks as appropriate.

## Repository identity
The human-facing name is now **DIVINIVID**.

The Noema project ID remains `agency-foundation` as a stable ecosystem identifier. The intended repository slug is `divinivid`; changing the GitHub slug is operationally separate and must preserve redirects/provenance.

## Deferred intentionally
- no bulk media migration;
- no new state service;
- no Noema-owned Brand taxonomy;
- no automatic Skill publication;
- no automatic canon promotion;
- no global executor routing rewrite unless actual operational pressure justifies it.

## Re-evaluate when
- the repo slug has been renamed;
- Archive V1 and Visual Canon Registry exist;
- Skill Foundry returns the G5 architecture proposal;
- the Asset Factory pilot begins;
- context maintenance exceeds the Noema complexity budget.
