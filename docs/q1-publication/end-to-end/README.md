# End-to-End Research Execution Plans — All Six PUI89 Projects

**Snapshot date:** 25 November 2026  
**Status:** Research protocols and execution plans; not evidence of completed data collection, experiments, validation, product readiness or publication.

This directory turns the six study blueprints into project-specific, end-to-end research workflows. Each plan follows the same traceable lifecycle:

1. Define the scientific problem, intended contribution and boundaries.
2. Review literature and verify the gap before claiming novelty.
3. Obtain lecturer/domain-expert feedback and approve the protocol.
4. Discover global datasets and real images; verify source, licence, privacy and permitted use asset by asset.
5. Curate, annotate, adjudicate and freeze dataset versions.
6. Create group-aware train/validation/test splits and an untouched external test where feasible.
7. Establish reproducible baselines and resource-aware candidate models.
8. Run pre-registered experiments, ablations, robustness and failure analysis.
9. Evaluate statistics, uncertainty, domain shift and deployment constraints.
10. Produce evidence records, model cards, reproducibility package and a manuscript.
11. Conduct independent review, verify the target journal's current quartile and submit only when evidence supports it.
12. Maintain monthly and annual status, with dated evidence and explicit blockers.

## Project plans

| Project | End-to-end plan | Central research question |
|---|---|---|
| Coconut Harvest AI | [01 — Coconut](01-coconut-harvest-ai.md) | Can coconut maturity be classified reliably across orchards, trees, seasons and cameras? |
| PUI89 Sentinel | [02 — Sentinel](02-pui89-sentinel.md) | Can permitted facility-event monitoring preserve evidence provenance and handle uncertainty better than score-only methods? |
| AI HOME | [03 — HOME](03-ai-home.md) | Can a compact indoor assistant navigate and assist reliably around people and changing layouts? |
| AI NOMAD | [04 — NOMAD](04-ai-nomad.md) | Can a compact outdoor robot estimate traversability and hazards across terrain and weather? |
| AI Robot Car | [05 — Robot Car](05-ai-robot-car.md) | Can road-hazard warnings remain timely and calibrated across routes and adverse conditions? |
| EasyRide AI Step-Through Scooter | [06 — Scooter](06-easyride-scooter.md) | How does rider-view perception affect hazard-warning reliability for two-wheel mobility? |

## Shared controls

- **Shared AI Core:** all research adapters use version-pinned Observation, WorldState, ActionProposal, FailureReport and Evidence Passport contracts. Research integration is advisory; no direct actuation is authorised by these plans.
- **PUI89 model ownership:** a model is called PUI89-owned only when ownership, training contribution, data rights, code, weights, lineage, licence and evaluation evidence are documented. Registry inclusion is gated; reference or wrapper use is not ownership.
- **Thai-language delivery:** provide Thai explanations, protocols, annotation guides, consent/privacy notices and lectures. For language-capable models, test Thai separately and report Thai metrics independently. Translation alone is not model validation.
- **Global data:** “global” is a coverage objective, not a claim. Report actual countries, sites, seasons, conditions, camera viewpoints and missing strata. Do not scrape or redistribute images without rights.
- **No fabricated results:** planned/not recorded is not zero, complete or failed. No performance, Q1 acceptance, novelty or field-safety claim without reproducible evidence.
- **Resource constraints:** prefer open-source, non-Chinese-origin, provenance-clear and lightweight tools; CPU-first baselines. Do not incur paid API, cloud GPU, subscription or metered costs. Do not download/install tools or models without explicit approval.
- **Safety:** simulations, offline datasets and physical tests are separate evidence classes. Physical trials require risk assessment, supervision and applicable permissions.

## Research gates

| Gate | Exit evidence |
|---|---|
| G0 Scope | Approved research question, intended use, exclusions and risk boundary |
| G1 Literature | Search strategy, dated evidence map, gap statement and novelty uncertainty |
| G2 Protocol | Lecturer/domain review, hypotheses, endpoints, power/precision plan and analysis plan |
| G3 Data rights | Asset manifest, licence/permission, privacy/ethics and permitted-use decisions |
| G4 Dataset | Versioned annotations, quality review, group IDs and frozen split manifests |
| G5 Baseline | Reproducible baseline, pinned environment and experiment record |
| G6 Evaluation | Locked test, uncertainty intervals, subgroup/shift analysis and failure cases |
| G7 Core/model | Model card, provenance, weights hash, Thai/target-domain evaluation and conformance evidence |
| G8 Manuscript | Complete paper, evidence-linked claims, independent technical/statistical review |
| G9 Submission | Journal scope and current quartile verified on submission date; all authors approve |

No gate is considered passed because a document exists; the required evidence must be attached and reviewed.

## Monthly dashboard fields

For every project record: reporting month; gate; research question version; literature references screened/included; lecturer feedback; data sources and countries verified; images/assets with rights status; annotations and agreement; dataset version; split manifest hashes; experiments completed; model revision; primary metric with confidence interval; robustness/failure results; compute/hardware; Thai evaluation; blockers; next actions; evidence links; reviewer and review date.

## Current portfolio-wide status (2026-11-25)

These plans have been authored as research specifications. Project-specific approved protocols, rights-cleared image inventories, completed annotations, frozen splits, measured experiments, validated PUI89-owned weights and accepted manuscripts are **not established by this planning change**. Populate status only from project records and reproducible evidence.
