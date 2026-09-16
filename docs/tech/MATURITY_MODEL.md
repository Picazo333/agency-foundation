# S0–S4 Technical Maturity Contract

This model describes implementation maturity for a surface or capability. It is not a mandatory ladder for every component: a static marketing block may legitimately stop before S2, and **S4 is optional** unless AI/MCP behavior is an actual product requirement.

A stage may only be claimed when its exit criteria are evidenced. Experimental work remains in `labs/` until a separate implementation decision promotes it.

## S0 — Visual
**Focus:** visual composition, responsive layout and brand-system feasibility.

- **Entry:** a defined visual intent plus the minimum token/schema context needed to render it.
- **Exit:** the specimen renders coherently at the target viewport classes; typography, spacing and major states are represented; no production functionality is implied.
- **Typical location:** `labs/visual/` or an approved design/specimen environment.

## S1 — Interactive
**Focus:** input behavior, state transitions and interaction accessibility.

- **Entry:** S0 evidence exists and the interaction contract is defined.
- **Exit:** pointer and keyboard behavior work; focus states are intentional; semantic controls are used; ARIA is added only where semantics require it; reduced-motion behavior exists where animation is non-essential; interaction errors do not trap the user.
- **Typical location:** `labs/interaction/` until promoted.

## S2 — Mock-data integrated
**Focus:** data/state contracts without live backend dependency.

- **Entry:** the surface genuinely needs data/state and S1 requirements relevant to it are satisfied.
- **Exit:** realistic typed/structured mock data drives the surface; loading, empty, error and success states are represented where applicable; deterministic fixtures make visual/behavioral testing possible.

## S3 — Backend wired
**Focus:** authenticated/authorized end-to-end integration where applicable.

- **Entry:** API/data contracts, ownership and authorization behavior are defined; S2 fixtures exist for regression/testing.
- **Exit:** the surface integrates with an approved staging/production backend; reads and mutations behave correctly; authorization boundaries are enforced server-side; network/retry/error states are handled; sensitive data is not exposed to the client unnecessarily; observability needed for the feature is defined.

## S4 — AI / MCP / agentic (optional)
**Focus:** model- or tool-mediated behavior for surfaces that actually require it.

- **Entry:** the underlying non-AI workflow is sufficiently mature; prompt/tool schemas, permissions, data boundaries and failure modes are documented.
- **Exit:** tool/model outputs are schema-validated where feasible; permissions and human-confirmation boundaries are enforced; prompt/data handling follows project privacy/security rules; fallbacks exist for unavailable or invalid model/tool responses; material actions are logged/auditable where required.

**S4 is not a badge of higher quality.** Do not add AI/MCP behavior merely to advance a maturity label.

## Promotion rule
Moving experimental work into production code requires a separate implementation decision/PR. A maturity label does not by itself authorize copying lab code into `apps/` or `packages/`.
