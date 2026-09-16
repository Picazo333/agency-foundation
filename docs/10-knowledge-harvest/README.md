---
status: review
owner: meta
updated: 2026-09-16
authority: process
---
# Project Harvest / Knowledge Harvest

This directory defines a low-overhead sidecar process for extracting reusable organizational knowledge from real project work.

## Purpose

A project should not produce only its primary deliverable. Meaningful work may also produce reusable:

- lessons;
- story/media seeds;
- Skill candidates;
- SOP/process candidates;
- templates/schemas;
- eval/test cases;
- reusable code/components;
- assets;
- case-study/proof material;
- benchmarks/failure patterns.

The harvest layer captures those outputs once, with provenance, so downstream systems can reuse them without reconstructing the original conversation or implementation history.

## Core principle

**Real work -> evidence -> reusable knowledge -> optional downstream production.**

Do not invert this into content generation for its own sake.

## What this is NOT

- not a requirement to document every commit;
- not an automatic media/content generator;
- not a new source of strategic canon;
- not a dependency on Noema, Skill Foundry, or any single external tool;
- not a blocking CI gate;
- not permission to expose client/confidential information.

## Trigger level

Prefer meaningful project events such as:

- merged/high-value PR;
- ADR or important decision;
- milestone;
- validated experiment;
- failure/postmortem;
- meaningful before/after;
- client/project outcome cleared for capture;
- discovery of a reusable workflow or capability.

Routine formatting, typo fixes, dependency noise, and trivial housekeeping normally produce no harvest record.

## Directory model

```text
docs/10-knowledge-harvest/
├── README.md
├── PROJECT_HARVEST_PROTOCOL.md
├── records/
│   └── README.md
└── templates/
    ├── HARVEST_RECORD_TEMPLATE.md
    └── STORY_SEED_TEMPLATE.md
```

## Lifecycle

`CANDIDATE -> REVIEWED -> APPROVED_FOR_REUSE -> ROUTED`

A story/media route has an additional explicit human gate before anything is considered public-ready.

`APPROVED_FOR_REUSE` does **not** mean strategic canon. Canon remains governed by the existing source-of-truth and ADR system.

## Downstream consumers

A neutral harvest record may later be consumed by:

- Noema / Media Factory;
- Skill Foundry;
- Agency operations;
- case-study/proof systems;
- technical knowledge bases;
- design/asset systems;
- future tools not yet selected.

The producer records the reusable knowledge. The downstream consumer decides how to transform it.

See `PROJECT_HARVEST_PROTOCOL.md` for the governing rules.