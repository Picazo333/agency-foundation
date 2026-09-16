---
status: approved
owner: meta
updated: 2026-09-16
authority: canon
depends_on:
  []
---
# Operating Model

## Core loop
`RESEARCH -> PROPOSAL -> REVIEW -> DECISION -> SPEC -> IMPLEMENTATION -> TEST -> MERGE`

## Project Harvest sidecar
After a meaningful PR, ADR, milestone, experiment, incident, or delivery, perform a lightweight Project Harvest assessment:

`MEANINGFUL EVENT -> HARVEST ASSESSMENT -> optional HARVEST RECORD -> downstream routing`

This is a **non-blocking sidecar**, not a new mandatory stage in the core loop. Routine/low-signal work creates no record. Harvest records capture reusable knowledge but do not change canon and never authorize automatic publication.

Protocol: `docs/10-knowledge-harvest/PROJECT_HARVEST_PROTOCOL.md`.

## Parallel workstreams
Workstreams are defined capability-first; current executors may change without changing the workstream contract (see ADR-0005).

- Brand Direction — ChatGPT + human
- Agency Master Plan — Claude Code / CoWork capability
- Asset Factory Architecture — Jules (generator-agnostic; Gemini remains a possible later generation provider)
- Neutral Technical Foundation — Jules (Antigravity remains an optional later experimentation environment)
- Repo Hardening — Jules

## Convergence gates
1. Brand/Business Fit Review
2. Strategy + Brand Freeze
3. Implementation readiness
4. Launch readiness

## Governance
Substantial work is proposed through branches/PRs. `main` represents reviewed project truth, but files still carry status metadata so approved, frozen, superseded and research artifacts remain distinguishable.
