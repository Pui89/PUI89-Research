# Hybrid End-to-End Multimodal AI — Six-Project Research Adoption Plan

**Status:** Research plan only. No experiment, novelty, model superiority, Q1 acceptance or product validation is claimed.

## Purpose

Evaluate whether joint/end-to-end multimodal learning improves a clearly defined task over strong modular baselines. The programme adopts the PUI89 Shared AI Core architecture without assuming that every project needs the same model or modality.

## Six project tracks

| Track | Research focus | First low-risk measurable task |
|---|---|---|
| Coconut Harvest AI | visual maturity and fruit/scene understanding | image classification/detection with licensed data and CPU baseline |
| PUI89 Sentinel — All-Terrain Inspection Robot | terrain/scene interpretation and inspection context | offline visual scene or traversability assessment; no autonomous traversal claim |
| AI HOME | indoor scene and assistance context | offline object/room context and task-intent benchmark |
| AI NOMAD | outdoor scene understanding and navigation context | offline outdoor perception under lighting/weather variation |
| AI Global SUV | road-scene and hazard context | advisory road-scene perception benchmark; no vehicle control |
| AI Step-Through Scooter | rider/road awareness | advisory road/obstacle perception benchmark; no vehicle control |

## Common experimental protocol

1. Define one narrow research question and intended operating conditions.
2. Verify dataset rights, provenance, consent/privacy constraints and redistribution terms.
3. Establish a reproducible modular baseline before introducing joint learning.
4. Use identical leakage-resistant train/validation/test splits for all comparisons.
5. Compare modular, shared-representation and E2E candidates only where data and compute justify them.
6. Run modality ablations, missing-modality tests, corruption tests and distribution-shift analysis.
7. Report task metrics, calibration, uncertainty, abstention, failure cases, runtime, memory and energy where measurable.
8. Record seeds, software/model versions, hardware, configuration and all exclusions.
9. Separate offline metrics, simulation, controlled hardware tests and field validation.
10. Publish negative results and limitations; do not select a model from headline accuracy alone.

## Cross-project governance

- Use the versioned contracts: Observation, WorldState, ActionProposal, FailureReport and Evidence Passport.
- Product repositories own domain data, task definitions, action boundaries and acceptance criteria.
- Shared AI Core owns reusable contracts and common evaluation rules.
- Never pool project datasets without separate rights, privacy, domain-shift and governance review.
- No model is promoted across products solely because it performed well in another domain.

## Research gates

- R0: question, scope and baseline approved.
- R1: data rights and split integrity verified.
- R2: baseline reproduced.
- R3: candidate comparison and ablations completed.
- R4: uncertainty, robustness and resource analysis completed.
- R5: reproducibility package and limitations reviewed.
- R6: product integration considered separately; research success does not authorize physical deployment.

## Resource constraints

Prioritize open-source tools with clear non-Chinese provenance, CPU-feasible baselines, small datasets that have verified rights, and local reproducibility. Do not use paid APIs, subscriptions, metered cloud services or cloud GPUs without explicit approval. Do not download or install tools/models without approval.

## Publication integrity

A Q1 target is an aspiration, not a guarantee. Novelty, statistical significance and journal quartile must be verified. Do not fabricate results, metrics, citations, dataset rights or hardware validation.
