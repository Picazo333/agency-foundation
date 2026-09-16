# Visual Lab

Neutral visual experiments only. Do not treat prototypes as Brand V1 or production UI without explicit approval.

## Experiment Record: Neutral Token Mapping (index.html)
- **Hypothesis:** We can map neutral CSS variables to a basic visual component structure to prove out the `schema.json` without locking in brand values.
- **Setup:** Plain HTML/CSS defining `--color-*`, `--font-*`, `--spacing-*`, etc.
- **Evidence:** Components render structurally correct without opinionated branding.
- **Dependencies:** None.
- **Performance implications:** Negligible (plain CSS).
- **Accessibility implications:** Baseline contrast and font sizes assumed.
- **Security implications:** None.
- **Decision:** Keep (as a proof of concept).
- **Removal path:** Delete `index.html`.
