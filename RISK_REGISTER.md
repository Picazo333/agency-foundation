---
status: approved
owner: meta
updated: 2026-09-16
authority: canon
depends_on:
  []
---
# Risk Register

| Risk | Probability | Impact | Mitigation |
|---|---:|---:|---|
| Aesthetic preference drives business choice | Medium | High | Brand V0 only; mandatory Brand/Business Fit Review |
| Research inference becomes canon | High | High | Research/canon split + evidence labels + ADRs |
| Multiple agents overwrite each other | Medium | High | branch/worktree isolation + ownership + PRs |
| AI agent silently expands scope | High | Medium | task contracts + forbidden scope + DoD |
| Asset provenance/licensing lost | Medium | High | manifests + licensing gate + source metadata |
| Experimental UI mistaken for functional system | Medium | High | Aesthetic/Functional/System spines + maturity stages |
| Generic AI-agency positioning | Medium | High | strategy reconciliation + BOLD contrarian input |
| Secrets committed | Low | Critical | `.gitignore`, `.env.example`, GitHub/deployment secrets |
| Repository becomes documentation landfill | Medium | Medium | status model + canon/workbench split + deprecation |
| Too much parallel work without convergence | Medium | High | dependency map + explicit gates + handoff contracts |

## Business-operation risks

Added by the Claude/CoWork Agency Master Plan workstream (Issue #2). These concern the *operating
business* rather than the *program*, and are proposals pending review.

| ID | Risk | Probability | Impact | Mitigation |
|---|---|---:|---:|---|
| R-14 | **Planning substitutes for market contact** — an excellent strategy, refined indefinitely, never tested | High | **Critical** | Stop rule (`AGENCY_THESIS.md` §11); D3 access gate at day 30; `RED_TEAM_REVIEW.md` RT-01 |
| R-15 | No evidence the founder can sell; the critical path depends on it entirely | Medium | **Critical** | Low-pressure entry instrument; outcome measured at D3/D5; designed exits P-C and P-D (`RED_TEAM_REVIEW.md` RT-02) |
| R-16 | No defensibility for 18–24 months; the benchmark moat arrives after it is needed | High | High | Accept; accumulate from engagement 1; rely on obscurity + relationships in the interim (`RED_TEAM_REVIEW.md` RT-05) |
| R-17 | Data-protection breach involving client customer data | Low | **Critical** | `GOVERNANCE_RISK_SECURITY_CHECKLIST.md` §4–5; `RF-7` prohibits clinical records; counsel before first healthcare engagement |
| R-18 | Operating without legal/tax formalisation | Medium | High | Accountant before first invoice; lawyer before first SOW ⚖️ |
| R-19 | Founder unavailability halts all delivery | Medium | **Critical** | Documentation-first; client-operable runbooks; no 24/7 SLA. **Accepted residual at solo scale** (`OPERATING_MODEL.md` §8) |
| R-20 | Margin destroyed by scope creep and rework | High | High | Change control; `A-13` measured from engagement 1; triggers T-1/T-2 |
| R-21 | Outcome claim challenged as misleading | Low | High | Ethical claim rules `EC-1`–`EC-10`; no claim without a captured baseline |
| R-22 | Opportunity cost exceeds expected value — the founder's skills may be worth more elsewhere | Unknown | High | Stated openly (`RED_TEAM_REVIEW.md` RT-09); `U-02`/`U-03` elevated to day-0 blocking questions; pivot P-D is a legitimate outcome |
