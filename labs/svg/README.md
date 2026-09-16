# SVG Lab

SVG generation, validation, optimization and component-conversion experiments belong here before production adoption.

## Experiment Record: SVG Sanitization/Optimization Pipeline
- **Hypothesis:** We can safely validate and strip malicious code from SVGs before using them.
- **Setup:** Node.js script (`scripts/tech-labs/svg-optimizer.js`) using regex to detect `<script>` and `onclick`.
- **Evidence:** Script successfully flags and removes XSS vectors from `sample-unoptimized.svg`.
- **Dependencies:** None in the POC (would use SVGO in production).
- **Performance implications:** Optimization step reduces file size.
- **Accessibility implications:** None directly, though proper `title` tags should be enforced later.
- **Security implications:** Mitigates XSS risks from third-party SVGs.
- **Decision:** Keep.
- **Removal path:** Delete `scripts/tech-labs/svg-optimizer.js` and `sample-unoptimized.svg`.
