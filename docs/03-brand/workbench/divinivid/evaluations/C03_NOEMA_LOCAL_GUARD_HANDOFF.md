# C03 — Noema visual reference local guard

Status: `PARTIAL`. Baseline: `4cfb2df` on `main`. Scope is limited to this evaluations directory. P6 remains at `PENDING_HUMAN_REVIEW`; this change does not authorize P7 or a generation call.

## Work order

Objective: implement a local preflight check that distinguishes an approved reference being available from being attached to the actual image request. Read `AGENTS.md`, `noema.project.yaml`, the current generation state, the active Brand gate and the September 22 conditioning postmortem. Allowed writes: the guard, its synthetic tests and this handoff. Forbidden effects: generate assets, edit canon, change the generation state, issue visual approval, or promote a Noema harvest candidate.

## Evidence and checks

Before: `python scripts/repo-health/validate_repo.py`, `python -m noema lint .` and `python -m noema audit .` passed. The postmortem records an available reference that was not proven attached to the call. After: run the same checks and `python -m unittest test_reference_binding_guard.py -v` in this directory. The synthetic tests cover available-but-unattached, rejected descendants, incompatible executor and absent request evidence.

The request adapter must capture the actual request evidence and attached IDs for each call. `reference_binding_guard.py` rejects incomplete or mismatched records before the call is used as Brand evidence. It returns only `READY_FOR_DOMAIN_QA`; Brand QA must judge effective conditioning and the human owner must issue the gate. A validator result is never a Noema or Brand approval.

## Remaining and rollback

Apply the preflight to the next separately authorized generation and retain its request evidence and domain QA result. Until then, the structural check is tested with synthetic data only. Revert this isolated evaluations change if it conflicts with the approved adapter, after comparing later Brand work; do not reset the generation branch or its human gate.
