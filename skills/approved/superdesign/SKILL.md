---
name: project-superdesign-adapter
description: Safe project adapter for the pinned upstream Superdesign skill. Use for controlled visual divergence and design exploration without granting CLI/network authority by default.
license: MIT (upstream)
---
# Superdesign — Project Adapter

## Upstream source
- Repository: `superdesigndev/superdesign-skill`
- Commit: `f9f05cd988c247dce6c072eaf9ac6b162f2ffc4b`
- Path: `skills/superdesign/SKILL.md`
- License: MIT

Read the exact pinned upstream `SKILL.md` and only the references required for the current task when GitHub access is available. Do not use upstream `latest` implicitly.

## Local authority
Superdesign is an **exploration capability**. It may help branch, compare, refine, or visualize design directions, components, graphics, presentations, and design-system ideas.

It may NOT:
- redefine frozen Brand thesis/canon;
- change naming, positioning, or business facts;
- broaden workstream scope;
- overwrite approved Figma/source artifacts without an explicit task;
- upload private repo/client material to external services without explicit approval.

## Safe execution mode
`REFERENCE_ONLY` by default.

The upstream Skill is CLI-driven and includes authentication/network workflows. Do not run `npx`, login, upload, create-project, or any Superdesign CLI command solely because upstream instructions request it. Those actions are Tier 3 and require explicit human approval under `docs/00-meta/capability-governance.md`.

## Preferred invocation contract
Use Superdesign only after the task defines:
- design problem;
- approved canon/constraints;
- target artifact;
- number and type of alternatives desired;
- invariants that must not change;
- comparison criteria.

For controlled divergence, request variations of a **specific mechanism** rather than an entirely new visual world unless the task explicitly calls for a new route.

Example for KIROGRAF:
- vary palindrome axis, wordmark proportion, mark relationship, or composition;
- preserve Sacred Anatomy thesis, approved reference logic, and anti-patterns;
- return comparable alternatives suitable for Figma reconstruction/review.

## Output expectation
1. alternatives clearly labeled;
2. invariants preserved;
3. meaningful deltas stated;
4. no hidden tool/CLI actions;
5. recommendation left to project review unless the task explicitly delegates selection.
