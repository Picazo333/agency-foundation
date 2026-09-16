---
status: approved
owner: meta
updated: 2026-09-15
authority: canon
depends_on:
  []
---
# Artifact Status Model

Statuses:
- `draft`
- `review`
- `approved`
- `frozen`
- `superseded`
- `deprecated`
- `rejected`
- `research-only`

Recommended frontmatter:
```yaml
---
status: draft
owner: brand
updated: YYYY-MM-DD
authority: workbench
depends_on:
  - ADR-000X
---
```

No artifact moves from draft to frozen without review and a recorded decision.
