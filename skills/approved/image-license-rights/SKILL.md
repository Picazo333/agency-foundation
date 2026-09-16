---
name: project-image-license-rights-adapter
description: Safe project adapter for the pinned upstream Image License & Usage Rights skill. Use as rights-hygiene gate for reference and production imagery.
license: MIT (upstream)
---
# Image License & Usage Rights — Project Adapter

## Upstream source
- Repository: `SkillMedev/skills`
- Commit: `a28c4ce9366b5a8540577bed8f70b6a60f8fde27`
- Path: `skills/image-license-rights/SKILL.md`
- License: MIT

Execution mode: `REFERENCE_ONLY`.

## Local authority
Authority: **rights/provenance hygiene**, not legal advice. It may classify intended use, inspect source/license terms, identify attribution/release constraints and produce per-asset rights records.

It may NOT:
- declare ambiguous material universally cleared;
- infer a license from a repost or remembered platform policy;
- override the Asset Factory provenance state machine;
- give final legal advice where counsel is required.

## DIVINIVID use
Use while building the Reference Atlas to record source/provenance and before any reference-derived or third-party asset moves toward commercial production. Historical/public-domain material must still carry source metadata. AI-generated assets must record provider/model and applicable use terms when known.

## Default rule
Ambiguity resolves to the more restrictive project state. `REFERENCE_ONLY`, `UNKNOWN_RIGHTS` and `UNVERIFIED_LICENSE` remain blocked from production approval.