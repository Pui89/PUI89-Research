#!/usr/bin/env python3
"""Audit a CSV dataset manifest for duplicate and cross-split leakage.

Required columns: sample_id, split.
Optional grouping columns: sha256, group_id, source_id.
Uses only the Python standard library. Exits 1 when leakage is detected.
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any


REQUIRED = {"sample_id", "split"}
GROUP_FIELDS = ("sha256", "group_id", "source_id")


def audit_rows(rows: list[dict[str, str]]) -> dict[str, Any]:
    errors: list[dict[str, Any]] = []
    seen_ids: dict[str, int] = {}
    values: dict[str, dict[str, set[str]]] = {
        field: defaultdict(set) for field in GROUP_FIELDS
    }

    for line_number, row in enumerate(rows, start=2):
        sample_id = (row.get("sample_id") or "").strip()
        split = (row.get("split") or "").strip().lower()
        if not sample_id:
            errors.append({"type": "missing_sample_id", "line": line_number})
        if not split:
            errors.append({"type": "missing_split", "line": line_number})
        if sample_id:
            if sample_id in seen_ids:
                errors.append({
                    "type": "duplicate_sample_id",
                    "sample_id": sample_id,
                    "first_line": seen_ids[sample_id],
                    "line": line_number,
                })
            else:
                seen_ids[sample_id] = line_number

        for field in GROUP_FIELDS:
            value = (row.get(field) or "").strip().lower()
            if value and split:
                values[field][value].add(split)

    leakage: list[dict[str, Any]] = []
    for field, grouped in values.items():
        for value, splits in grouped.items():
            if len(splits) > 1:
                leakage.append({
                    "type": f"{field}_cross_split",
                    "value": value,
                    "splits": sorted(splits),
                })

    return {
        "rows": len(rows),
        "required_columns": sorted(REQUIRED),
        "grouping_columns_checked": list(GROUP_FIELDS),
        "errors": errors,
        "cross_split_leakage": leakage,
        "passed": not errors and not leakage,
    }


def audit_file(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        columns = set(reader.fieldnames or [])
        missing = REQUIRED - columns
        if missing:
            raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")
        return audit_rows(list(reader))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path, help="CSV manifest to audit")
    parser.add_argument("--output", type=Path, help="Optional JSON report path")
    args = parser.parse_args()

    try:
        report = audit_file(args.manifest)
    except (OSError, UnicodeError, csv.Error, ValueError) as exc:
        print(json.dumps({"passed": False, "fatal_error": str(exc)}, indent=2))
        return 2

    rendered = json.dumps(report, indent=2, ensure_ascii=False)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
