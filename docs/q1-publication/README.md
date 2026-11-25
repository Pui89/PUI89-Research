# PUI89-Research — Q1 Publication Engineering Programme

**Status: Research framework and publication-readiness specification. No manuscript, experiment, Q1 acceptance, or product validation is claimed.**

PUI89-Research is the central research programme for the six active PUI89 projects. Its job is to turn each project into a defensible, reproducible scientific study: research question → literature gap → protocol → rights-cleared evidence → controlled experiment → statistical analysis → independently reviewable manuscript.

A Q1 journal target is an ambition, not a guarantee. Journal quartiles change by database, subject category and year. A paper is ready only when its evidence and reporting meet the selected journal's current requirements and it survives peer review.

## 1. Six project research tracks

| ID | Project | Research domain | Research boundary |
|---|---|---|---|
| `coconut-harvest-ai` | Coconut Harvest AI | Agricultural computer vision; coconut maturity assessment | Four defined maturity classes; ground truth and orchard-level generalisation must be established |
| `sentinel` | PUI89 Sentinel | General security monitoring; multimodal event/anomaly evidence | No narcotics screening, related datasets, X-ray screening or forensic spectra |
| `ai-home` | AI HOME | Indoor mobile robotics; human-aware navigation and assistance | Simulation and real-world evidence reported separately; no unsupported safety claims |
| `ai-nomad` | AI NOMAD | Outdoor mobile robotics; terrain-robust perception and navigation | Distinct from AI HOME; terrain, weather and lighting conditions explicitly stratified |
| `ai-robot-car` | AI Robot Car | Road-scene perception and hazard-awareness | Driver-assistance research only; no autonomous steering, throttle or braking claim |
| `easyrider-ai-scooter` | EasyRide AI Step-Through Scooter | Two-wheel rider-view perception and road-safety warnings | Scooter/motorcycle evidence must be distinguished from car-only evidence; no autonomous control claim |

Each project must have its own protocol, dataset manifest, experiment records, analysis, failure register and manuscript. A shared method does not make the six studies one pooled experiment.

## 2. Reuse Shared AI Core — do not rebuild it

The research programme adopts a version-pinned snapshot of the research-relevant Shared AI Core contracts. The copied schemas are in `schemas/shared-ai-core/v0.1.0/`; their upstream file paths, blob SHAs and source commit are recorded in `schemas/shared-ai-core/upstream-manifest.json`.

| Shared Core asset | Research use |
|---|---|
| Observation | Standardise sourced sensor, human, dataset, simulation and software observations |
| WorldState | Record time-bounded estimates, evidence references, unknowns and conflicts |
| ActionProposal | Record advisory recommendations; execution remains disabled |
| FailureReport | Capture failures, near misses, degraded conditions and unexpected results |
| Evidence Passport | Trace each scientific conclusion to supporting, conflicting and missing evidence |
| Experiment record | Pin protocol, dataset, code, model, hardware, metrics, seeds and results |
| ProofBench | Test evidence-handling and fail-closed software behaviour using synthetic fixtures only |
| Cross-project conformance | Check project adapters against the pinned shared contracts |
| Dataset manifest / integrity gates | Track sample identity, rights, labels, split leakage and file hashes |
| CPU-first benchmark protocols | Compare edge configurations under controlled, repeatable conditions |

The research repository stores the pinned schema snapshots needed for independent review. Shared Core remains the upstream source of truth; do not silently edit a copied schema. Any update requires a new upstream pin, a documented diff, migration notes and conformance tests.

## 3. Publication workflow and gates

1. **P0 — Research question:** define the intended use, population/environment, unit of analysis, primary question and falsifiable hypothesis.
2. **P1 — Literature and gap:** search current peer-reviewed work; build a claim-to-source matrix; compare methods, datasets, limitations and reported baselines. Novelty remains unconfirmed until reviewed.
3. **P2 — Ethics and rights:** confirm data ownership, licence, consent/privacy, institutional ethics requirements, safety review and permitted publication. Unknown rights block use.
4. **P3 — Protocol freeze:** preregister or timestamp the protocol where appropriate; define inclusion/exclusion criteria, primary/secondary outcomes, sample-size rationale, splits, baselines, metrics and statistical plan before test-set access.
5. **P4 — Dataset readiness:** retain a manifest, provenance, annotation guide, quality review, leakage-resistant splits and a sealed test set.
6. **P5 — Implementation and conformance:** pin code/model/runtime versions; validate Shared AI Core contracts; retain test reports. Contract tests are not model-performance evidence.
7. **P6 — Controlled experiments:** run baselines, proposed method, ablations, robustness and resource tests; retain raw outputs, seeds, logs and failures.
8. **P7 — Statistical analysis:** report effect sizes, uncertainty intervals, appropriate paired/grouped analyses, multiple-comparison handling and negative results.
9. **P8 — Independent review:** a reviewer not responsible for implementation checks protocol deviations, data rights, analysis, figures, limitations and claim-to-evidence traceability.
10. **P9 — Manuscript and journal fit:** complete the reporting checklist, authorship/COI/ethics/data availability statements and journal-specific formatting; verify the current Q1 category and year using an authoritative database.
11. **P10 — Submission and response:** retain submitted version, reviewer comments, revisions, response-to-reviewers and final decision.

A gate may be marked `PASS`, `PARTIAL`, `BLOCKED` or `NOT ASSESSED`. No automated check can declare novelty, ethics approval, scientific validity, Q1 status or manuscript acceptance.

## 4. Minimum research package for every paper

- Research protocol and dated version history.
- Literature review matrix and explicit gap statement.
- Dataset manifest, source/rights evidence, annotation guide and split manifest.
- Shared-contract adapter fixtures and conformance report, where applicable.
- Experiment record for every run, including unsuccessful runs.
- Baseline and proposed-method configurations.
- Statistical analysis plan and analysis code.
- Raw, de-identified results and integrity hashes, subject to data rights and privacy.
- Model card / method description and exact model revision.
- Hardware, runtime, software, compute and energy measurement details where relevant.
- Failure, robustness, uncertainty and limitation analysis.
- Figures/tables generated from retained result files.
- Claim-to-evidence matrix linking each manuscript claim to a result and evidence record.
- Independent review record.
- Manuscript, supplementary material and journal submission checklist.

## 5. Scientific integrity rules

- Never invent results, sample counts, statistical significance, citations, novelty or journal rankings.
- Do not tune the final test set or change primary metrics after viewing results without clearly labelling the analysis exploratory.
- Separate synthetic, simulated, estimated and measured evidence.
- Avoid random frame-level splits when samples share a tree, orchard, camera, site, route, subject, session or time sequence.
- Report all exclusions, missing data, protocol deviations, negative findings and material limitations.
- A software test, simulation, demonstration or third-party benchmark does not prove field performance or physical safety.
- No data acquisition, download, installation, model execution, hardware purchase or paid service is authorised by this framework alone.

## 6. Current status

This framework and the pinned contract snapshots are research infrastructure. It does not mean that any dataset is rights-cleared, any experiment has run, any hypothesis is supported, or any manuscript is submission-ready. The first scientific priority is to complete one rigorous, independently reviewable study at a time while maintaining separate evidence registers for all six projects.
