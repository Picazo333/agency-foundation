"""Local preflight for an image-generation request; never issues Brand approval."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def check_binding(record: dict) -> list[str]:
    errors: list[str] = []
    if not record.get("call_id") or not record.get("phase"):
        errors.append("call_id and phase are required")
    executor = record.get("executor") or {}
    if not executor.get("id") or executor.get("supports_image_references") is not True:
        errors.append("executor must be identified and support image references")
    request = record.get("request") or {}
    if not request.get("evidence_ref"):
        errors.append("the actual request evidence reference is required")
    attached = request.get("attached_reference_ids")
    if (
        not isinstance(attached, list)
        or not attached
        or any(not isinstance(item, str) or not item for item in attached)
        or len(attached) != len(set(attached))
    ):
        errors.append("the actual request must list distinct attached reference IDs")
        attached = []
    references = record.get("approved_root_references")
    if not isinstance(references, list) or not references:
        errors.append("at least one approved root reference is required")
        references = []
    approved_ids: set[str] = set()
    for ref in references:
        if (
            not isinstance(ref, dict)
            or not isinstance(ref.get("id"), str)
            or not ref.get("id")
            or not isinstance(ref.get("approval_ref"), str)
            or not ref.get("approval_ref")
        ):
            errors.append("each root needs an ID and approval evidence")
            continue
        if ref.get("available") is not True:
            errors.append(f"{ref['id']}: approved reference is unavailable")
        approved_ids.add(ref["id"])
    if approved_ids and not approved_ids.issubset(set(attached)):
        errors.append("an approved root is available but absent from the actual request")
    rejected = set(record.get("rejected_descendant_ids") or [])
    if rejected.intersection(attached):
        errors.append("the actual request includes a rejected descendant")
    if set(attached) - approved_ids:
        errors.append("the actual request includes a reference outside the approved roots")
    if record.get("generated_descendants_excluded") is not True:
        errors.append("generated descendants must be explicitly excluded")
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python reference_binding_guard.py REQUEST_RECORD.json", file=sys.stderr)
        return 2
    record = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    errors = check_binding(record)
    for error in errors:
        print(f"FAIL: {error}")
    if errors:
        return 1
    print("READY_FOR_DOMAIN_QA: request binding is structurally attested; effectiveness and Brand approval remain unverified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
