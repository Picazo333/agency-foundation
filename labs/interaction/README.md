# Interaction Lab

Navigation, scrollytelling, UI behavior and interaction prototypes belong here with clear separation between visual proof-of-concept and production functionality.

## Experiment Record: Neutral Accordion Behavior
- **Hypothesis:** Basic interaction patterns can be prototyped neutrally before committing to a framework component library.
- **Setup:** Vanilla HTML/JS accordion toggle.
- **Evidence:** Section toggles display state properly.
- **Dependencies:** None.
- **Performance implications:** Negligible (vanilla JS).
- **Accessibility implications:** Needs proper ARIA attributes (`aria-expanded`, `aria-controls`) in the production version.
- **Security implications:** None.
- **Decision:** Keep as POC.
- **Removal path:** Delete `index.html`.
