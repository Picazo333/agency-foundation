---
name: project-color-accessibility-adapter
description: Safe project adapter for the pinned upstream Color Accessibility skill. Use to verify real color pairings after palette construction.
license: MIT (upstream)
---
# Color Accessibility — Project Adapter

## Upstream source
- Repository: `SkillMedev/skills`
- Commit: `a28c4ce9366b5a8540577bed8f70b6a60f8fde27`
- Path: `skills/color-accessibility/SKILL.md`
- License: MIT

Execution mode: `REFERENCE_ONLY`.

## Local authority
Authority: **accessibility validation and bounded remediation**. Enumerate actual foreground/background pairings, compute contrast, detect color-only meaning, check dark-mode pairings and recommend token-level fixes.

It may NOT:
- redesign the brand palette from scratch;
- claim formal legal/regulatory conformance;
- treat artistic imagery and functional text as the same requirement without considering placement;
- weaken the visual thesis unnecessarily when a role-specific accessible variant solves the problem.

## DIVINIVID use
Use after Color Palette Builder and again during Digital/Stress Test. Preserve historical pigment character while making text, controls and required UI states usable. Decorative gold, carmine or ultramar need not be text colors.

## Output contract
Measured pairing table; pass/fail by role; corrected token proposals; non-color cues; color-vision notes; dark-mode verification.