# Field Kit — data templates

Machine-readable templates for the field-kit logs. **Headers only.** Open in a spreadsheet and work
there; the `.md` instrument files are the field dictionaries and the rules.

| File | Instrument | Hypotheses |
|---|---|---|
| `target_account_ledger.csv` | `../02_TARGET_ACCOUNT_LEDGER.md` | H-03, H-07, H-03b |
| `interview_index.csv` | `../08_INTERVIEW_RECORD_TEMPLATE.md` | all |
| `resonance_log.csv` | `../10_PROBLEM_RESONANCE_LOG.md` | H-10 |
| `price_signal_log.csv` | `../11_PRICE_SIGNAL_LOG.md` | H-04 |
| `sales_attempt_log.csv` | `../12_DIAGNOSTIC_SALES_ATTEMPT_LOG.md` | H-01 |
| `time_log.csv` | `../13_EXPERIMENT_RUNBOOK.md` §3b | H-12, `A-13`, `A-14`, M-10, M-41 |

## Privacy — binding

**No personal contact details in this repository.** No email addresses, no phone numbers, no
personal names of individuals who have not consented. Identify people by **role + initials**
(`Ops Dir / M.R.`). Business names are acceptable — they are public.

Keep contact details in the CRM or a git-ignored local file. This repository is the *evidence*
system, not the *contact* system (`GOVERNANCE_RISK_SECURITY_CHECKLIST.md` §4.1, `DR-2`, `DR-6`).

## Evidence-grade rule

`FACT` is permitted in one circumstance only: **money received and cleared.** Everything else is at
most `SIGNAL` (`EVIDENCE_AND_ASSUMPTIONS_REGISTER.md` §5 rule 2).

These files contain no data. Any example rows live in the `.md` instruments, are labelled
**SYNTHETIC EXAMPLE — NOT EVIDENCE**, and must be deleted before use.
