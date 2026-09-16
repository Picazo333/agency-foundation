# SVG Lab

SVG generation, validation, optimization and component-conversion experiments belong here before production adoption.

## Experiment Record: SVG sanitization/optimization proof of concept
- **Hypothesis:** A lightweight lab can demonstrate classes of unsafe SVG content and the ordering of a future pipeline: inspect/validate -> sanitize -> optimize -> review/convert.
- **Setup:** `scripts/tech-labs/svg-optimizer.js` flags/removes a very small test set (`<script>` and double-quoted inline event handlers) from `sample-unoptimized.svg`.
- **Evidence:** The proof of concept detects and removes the specific fixtures included in the sample.
- **Dependencies:** None.
- **Performance implications:** The demo strips comments only; it is **not** a production optimizer.
- **Accessibility implications:** Production SVG handling must separately preserve/author appropriate titles, labels, decorative roles, focus behavior and contrast.
- **Security implications:** **Regex removal is not a safe general-purpose SVG sanitizer.** SVG/XML can carry many additional active-content and reference vectors. Treat all third-party/generated SVG as untrusted. Production adoption requires a vetted parser/sanitizer policy, explicit allowed content, URI/reference handling, tests against adversarial fixtures and security review.
- **Decision:** Keep strictly as an educational/experimental POC; never promote this script itself as the production security control.
- **Removal path:** Delete `scripts/tech-labs/svg-optimizer.js` and the sample fixture when a real pipeline supersedes the experiment.

## Production gate
No output from this lab is `production-safe` merely because the demo reports that its known patterns were removed. Production assets still require the Asset Factory provenance/licensing gates and the future approved SVG security pipeline.
