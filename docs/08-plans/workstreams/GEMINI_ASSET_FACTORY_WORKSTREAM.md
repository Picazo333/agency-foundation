---
status: approved
owner: asset-factory
updated: 2026-09-15
authority: canon
depends_on:
  []
---
# Workstream — Asset Factory Architecture

> Legacy filename retained for link stability. The workstream is no longer Gemini-specific.

## Current executor
Jules, governed by Issue #3 and the branch `asset/jules-asset-factory-architecture`.

## Mission
Design a future **generator-agnostic** factory that can mass-produce brand-consistent assets **after** Brand V1 is frozen.

The architecture must allow Gemini or another generation provider to be plugged in later without changing Brand canon or the core asset lifecycle.

## Define
- input Brand Pack contract
- asset taxonomy
- SVG/illustration/pattern/icon/frame/diagram/social/deck/web categories
- generation request / prompt contracts
- output metadata schema
- provenance/licensing schema
- QA checklist and gates
- invent-vs-ask rules
- responsive behavior and variants
- generated -> staging -> reviewed -> approved/rejected lifecycle
- naming/versioning
- failure/rejection/regeneration
- duplicate/sprawl controls
- handoff manifest to implementation

## Forbidden now
- Do not mass-produce final assets.
- Do not reinterpret or freeze Brand canon.
- Do not make the architecture depend on one model/vendor without an explicit reason and adapter boundary.
