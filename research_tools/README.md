# Lightweight Q1 Research Utilities

These tools are intentionally dependency-free and CPU-friendly.

## Dataset leakage audit

Prepare a CSV manifest with required columns `sample_id,split` and optional columns `sha256,group_id,source_id`.

Example:

```csv
sample_id,split,sha256,group_id,source_id
img-001,train,abc123,orchard-a/tree-01,session-01
img-002,train,def456,orchard-a/tree-01,session-01
img-003,test,987xyz,orchard-b/tree-02,session-09
```

Run:

```bash
python research_tools/leakage_audit.py data_manifest.csv --output leakage_report.json
```

Exit codes: 0 = passed, 1 = leakage or manifest errors, 2 = fatal input/schema error.

The audit checks duplicate sample IDs and whether identical hashes, groups or source IDs cross dataset splits. It cannot prove that a dataset is leakage-free: choose grouping keys that reflect the true independent sampling unit (e.g. orchard/tree/capture session, site/time, building/layout, route/vehicle/rider). It does not inspect image pixels or infer hidden near-duplicates.

## Tests

```bash
python -m unittest discover -s research_tools -p 'test_*.py'
```

No third-party package is required.
