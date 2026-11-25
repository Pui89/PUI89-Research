# Shared AI Core Integration for PUI89-Research

**Upstream snapshot:** `Pui89/PUI89-Shared-AI-Core`, inspected `main` commit `50e756588ce23aa23463e72fca208b08ff50d1d3` (25 November 2026 repository snapshot).

## Purpose

PUI89-Research reuses the shared contracts and research controls already developed in PUI89 Shared AI Core. It does not create a competing contract framework. The five schema snapshots in `schemas/shared-ai-core/v0.1.0/` are copied byte-for-byte from the upstream paths listed in `upstream-manifest.json`.

The upstream repository is private. Keeping the exact schemas and their source SHAs in this research repository makes the research data contract inspectable without requiring a journal reviewer to access the private upstream repository. This snapshot does not replace the upstream implementation or claim runtime integration.

## Contract mapping

| Shared contract | Research function | Minimum retained evidence |
|---|---|---|
| Observation | Record source observations from dataset, human annotation, sensor, simulation or software | Source ID/type, modality, timestamp, quality, uncertainty, provenance |
| WorldState | Preserve time-bounded scientific/environment estimates | Evidence references, entities, unknowns and conflicts |
| ActionProposal | Represent advisory-only recommendations or next-step proposals | Objective, preconditions, risk, evidence references, human approval required, execution false |
| FailureReport | Preserve negative results, anomalies, near misses and protocol failures | Severity, expected/observed result, evidence references, response and verification |
| Evidence Passport | Trace a paper claim or AI conclusion to its evidence | Supporting/conflicting/missing references, provenance, uncertainty, review and verification status |

## Other upstream research assets to reuse by reference

- `docs/contracts/SHARED_CONTRACTS_V0.1.md`
- `docs/contracts/CROSS_PROJECT_CONFORMANCE_V0.2.md`
- `docs/benchmarks/PUI89_EXPERIMENT_RECORD_TEMPLATE_V0.1.md`
- `docs/benchmarks/PUI89_PROOFBENCH_V0.1.md`
- `docs/research/PUI89_OFFLINE_MODEL_EVALUATION_HARNESS_V0.1.md`
- `docs/research/PUI89_OBJECT_DETECTION_DATASET_MANIFEST_GATE_V0.1.md`
- `docs/research/PUI89_AI02_ANNOTATION_QUALITY_GATE_V0.1.md`
- `docs/benchmarks/PUI89_COCONUT_CPU_FIRST_EDGE_BENCHMARK_PROTOCOL_V1.0.md`
- `docs/benchmarks/PUI89_ANOMALY_DETECTION_BENCHMARK_V0.1.md`
- `docs/compute/PUI89_COMPUTE_BENCHMARK_V0.2.md`
- `docs/standards/PUI89_EVIDENCE_BASED_ENGINEERING_PRODUCT_READINESS_STANDARD_V1.0.md`

These references describe existing upstream assets; they are not claims that every feature is deployed, adopted by all six projects, or validated on real data. In particular, ProofBench is a synthetic software test suite, and a passing result is not a model benchmark or field validation.

## Research-side adapter rule

Each project adapter should:
1. Pin the Shared AI Core contract version and this snapshot's upstream commit.
2. Map project-specific observations to the common contract without discarding domain metadata.
3. retain exact evidence references, timestamps, source provenance and uncertainty.
4. preserve unknowns, missing values and conflicting observations.
5. keep ActionProposal advisory-only; `execution_authorized=false`.
6. record failures and negative results through FailureReport.
7. create an Evidence Passport for material manuscript claims.
8. include positive and negative fixtures and retain the exact conformance report and commit pins.

The adapter must not claim conformance until its fixtures have been executed against the pinned schemas and the exact project/core revisions are independently verified.

## Snapshot update policy

- Do not silently edit a copied upstream schema.
- To update, inspect a new upstream commit, compare every copied file, document breaking/semantic changes, update the manifest and add migration tests.
- Keep previous snapshots for already published experiments; a paper must continue to identify the exact contract version it used.
- A research record referencing one version must not be silently reinterpreted under a later schema.
- No automatic promotion, deletion or overwrite is allowed.

## Current status

- Five shared contract schemas copied as version-pinned snapshots: complete in this change.
- Source commit and upstream blob SHAs recorded: complete in this change.
- Research publication workflow and six study blueprints: specified in this change.
- Project adapters and fixture suites: not yet implemented.
- Runtime integration and cross-project conformance: not yet executed.
- Q1 manuscripts, experiments and journal quartile verification: not yet completed.
