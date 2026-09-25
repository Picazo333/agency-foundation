# Reference binding local guard

Status: implementation candidate for the next authorized image-generation call. This file and its validator do not authorize a new generation or change P6's pending human gate.

Before a material call, the DIVINIVID adapter records one JSON object per call with `call_id`, `phase`, executor ID and image-reference support, the exact approved root IDs with approval references and availability, the actual request evidence reference and attached IDs, rejected descendant IDs, and explicit exclusion of generated descendants. Run `python reference_binding_guard.py REQUEST_RECORD.json` before using the output as Brand evidence. Failure stops that call.

The validator checks structural request binding only. Availability does not imply attachment. Attachment does not prove effective visual conditioning. Brand QA must compare the generated result with its own canon and anti-canon, record the observed result and provenance, and obtain the existing human gate before promotion. Noema Trace is not a substitute for any of those assertions.

Synthetic negative cases run with `python -m unittest test_reference_binding_guard.py` from this directory. No real reference pixels, rejected images, generated output or private material are stored here.
