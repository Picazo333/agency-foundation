# Technical Labs

This area is intentionally minimal in the foundation baseline. See the relevant workstream spec before adding production content.

## Experiment Documentation Contract

Every meaningful experiment in this directory (e.g., in visual, motion, interaction, SVG labs) must document the following structure either in the lab's root README or inline within the experiment file:

- **Hypothesis:** What are we testing?
- **Setup:** How is it built?
- **Evidence:** What were the results?
- **Dependencies:** What external libraries are required?
- **Performance implications:** How does it affect load time and runtime?
- **Accessibility implications:** Does it meet WCAG standards (e.g., reduced-motion)?
- **Security implications:** Are there XSS or data leakage risks?
- **Decision:** Keep, reject, or undecided?
- **Removal path:** How do we safely remove this if rejected?
