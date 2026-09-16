# Motion Lab

Explore CSS/SVG/GSAP/scroll-linked motion with reduced-motion fallbacks and performance/accessibility notes. Experimental only until approved.

## Experiment Record: CSS Motion & Reduced-Motion Accessibility
- **Hypothesis:** CSS transitions and animations can be cleanly disabled for users preferring reduced motion.
- **Setup:** CSS classes with `transition` and `animation`, overridden by `@media (prefers-reduced-motion: reduce)`.
- **Evidence:** Emulating reduced motion in dev tools successfully disables the hover scaling and infinite spinning.
- **Dependencies:** None.
- **Performance implications:** Hardware-accelerated transforms used (`transform`) for 60fps capability.
- **Accessibility implications:** Safely respects OS-level reduced motion preferences.
- **Security implications:** None.
- **Decision:** Keep.
- **Removal path:** Delete `index.html`.
