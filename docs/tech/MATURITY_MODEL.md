# S0–S4 Technical Maturity Contract

This document defines the entry and exit criteria for technical prototypes and components transitioning through maturity stages.

## S0: Visual
*Focus: Aesthetics, layout, and responsiveness.*
- **Entry:** Design tokens (schema or values) exist; conceptual layout required.
- **Exit:** Component renders correctly across target breakpoints. Code is isolated in `labs/visual` or a conceptual viewer. No complex interactivity exists.

## S1: Interactive
*Focus: UI behavior, state changes, and accessibility.*
- **Entry:** Component passes S0. Interaction design (e.g., hover states, accordions) is defined.
- **Exit:** Component responds to user input (click, hover, focus). Keyboard navigation is functional. ARIA attributes (if necessary) are applied. Code is isolated in `labs/interaction`.

## S2: Mock Data
*Focus: Data binding and state management (Frontend).*
- **Entry:** Component passes S1. Data schema for the component is defined.
- **Exit:** Component successfully renders using a static JSON payload or a client-side mock store. Loading and error states are visually handled.

## S3: Backend Wired
*Focus: End-to-end data flow and API integration.*
- **Entry:** Component passes S2. API endpoints and authorization methods are defined.
- **Exit:** Component fetches data from a live backend (staging or production). Data mutations (POST/PUT) succeed. Network errors are gracefully handled by the UI.

## S4: AI / MCP
*Focus: Agentic capability and Model Context Protocol integrations.*
- **Entry:** Component passes S3. AI prompt parameters and MCP tool schemas are defined. Security constraints are documented.
- **Exit:** System safely executes AI/MCP workflows. Outputs are validated against schemas before rendering. Logging and auditing are functional.
