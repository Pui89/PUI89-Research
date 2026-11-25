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

## PUI89 model research and Thai-language support

The Shared AI Core is the common integration and governance layer; it is not a claim that one universal model is already trained or validated. Research may produce PUI89-owned model artefacts and project-specific adapters, then register eligible artefacts in the Shared AI Core model registry only after the required evidence gates pass.

Every candidate PUI89 model record should include:
- model name, task, owner and semantic version;
- upstream architecture/base model, exact revision and provenance;
- training-data manifest/version, source rights, geographic/condition coverage and exclusions;
- training code/configuration, reproducibility instructions and model-weight hash;
- licence and redistribution/derivative-work permissions;
- evaluation dataset/split, baselines, metrics, uncertainty, subgroup results and failure cases;
- supported hardware, runtime, memory and resource measurements;
- model card, intended use, out-of-scope use, known limitations and human-review requirements;
- links to experiment records and Evidence Passports.

### Thai edition is a first-class evaluation target

Provide Thai-language documentation, lecture material, user-facing explanations and research records alongside English. Where a model handles language, evaluate Thai separately rather than assuming English performance transfers. Define task-appropriate Thai test sets, regional/dialect and code-switching coverage where relevant, expert-reviewed translations, tokenisation/Unicode handling, Thai OCR/ASR quality where used, and subgroup error analysis. Report English and Thai metrics separately; do not combine them into one score that hides differences.

For non-language perception tasks, Thai localisation still requires Thai labels, annotation instructions, safety messages, units, date/time formats and human-review workflows. Translation alone does not constitute Thai model validation.

### Model lifecycle gates

- **M0 — Candidate:** identified; provenance and licence not yet approved.
- **M1 — Provenance/licence cleared:** origin, terms and permitted training/use/redistribution checked.
- **M2 — Data cleared:** data rights, privacy, ethics and dataset manifests approved.
- **M3 — Reproducible training:** code/configuration, seed, environment and model hash recorded.
- **M4 — Benchmark evaluated:** frozen splits, baselines, statistical plan and failure analysis completed.
- **M5 — Thai/target-domain evaluated:** Thai and relevant geography/condition testing completed where applicable.
- **M6 — Core-eligible:** model card, Evidence Passport, integration tests, security review and maintainer approval complete.
- **M7 — Released:** approved version, licence, documentation and change history published.

Do not label a model “PUI89 model” merely because it is referenced or wrapped by a project. Ownership, training contribution, rights and evaluation must be explicit. A model is not core-eligible until its gates are evidenced.

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
3. Retain exact evidence references, timestamps, source provenance and uncertainty.
4. Preserve unknowns, missing values and conflicting observations.
5. Keep ActionProposal advisory-only; `execution_authorized=false`.
6. Record failures and negative results through FailureReport.
7. Create an Evidence Passport for material manuscript claims.
8. Include positive and negative fixtures and retain the exact conformance report and commit pins.

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
- PUI89-owned trained model artefacts: not yet claimed by this research record.
- Thai-language model evaluation: planned; no Thai model benchmark results claimed.
- Q1 manuscripts, experiments and journal quartile verification: not yet completed.
