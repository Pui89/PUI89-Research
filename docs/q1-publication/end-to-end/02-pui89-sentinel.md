# 02 — PUI89 Sentinel: End-to-End Research Plan

**Working study title:** Evidence-aware multimodal anomaly and event detection for privacy-constrained facility monitoring.  
**Status:** Proposed protocol; no deployment, event benchmark or field validation is claimed.

## 1. Scope and boundaries

Study lawful, privacy-preserving facility observation, event/anomaly detection, evidence provenance, uncertainty and human review. Explicitly exclude narcotics detection/screening, X-ray screening, related datasets and forensic spectral research. Do not reintroduce excluded scopes through renamed tasks or borrowed datasets. Avoid identity recognition, biometric identification, profiling or automated enforcement.

**Research question:** Does an evidence-aware method that preserves source provenance, missingness, conflicting observations and abstention improve event-level reliability and reviewer traceability over score-only or conventional fusion baselines?

## 2. Literature and expert review

Review event detection, video anomaly detection, multimodal sensor fusion, calibration, open-set recognition, privacy-preserving monitoring, human factors, alarm fatigue and evidence provenance. Verify the gap against recent surveys and benchmark papers. Seek review from computer vision, privacy/data-protection, facility operations and human-factors experts. Lecturer review must approve the event taxonomy, legal/ethical scope and false-alarm analysis.

## 3. Data and real-world coverage

Use only public datasets with verified terms, institution-provided data with written permission, or controlled recordings with appropriate notices/consent/legal basis. Record jurisdiction, camera/site, field of view, timestamps, retention, privacy masking, modalities and event prevalence. Cover normal activity as well as rare events; synthetic scenarios may supplement but must be labelled synthetic and never presented as real-world evidence. Do not publish identifiable footage or sensitive facility details.

## 4. Event taxonomy and annotation

Define a narrow, operational event taxonomy with normal, uncertain, out-of-scope and sensor-fault labels. Annotate event start/end, location zone at safe granularity, confidence, evidence source and reviewer decision. Create a bilingual annotation handbook. Use independent reviewers on a subset and adjudicate disagreements. Do not infer intent, guilt or identity from appearance or anomaly scores.

## 5. Dataset splits

Group by site, camera, recording session and time block; avoid adjacent frames crossing partitions. Test on unseen sites/cameras where feasible. Maintain a sealed test set. Report event prevalence, camera-hours, missing streams and privacy filtering. Use an external dataset only after licence, taxonomy compatibility and domain differences are documented.

## 6. Models and baselines

Compare rule-based event logic, single-modality detector/anomaly baseline, late-fusion baseline and proposed evidence-aware fusion. Add uncertainty calibration/abstention as a controlled factor. Use only modalities actually available and approved. Exact model provenance, revision, licence and hardware requirements must be cleared. Do not assume that adding modalities improves performance.

## 7. Experiments

- E1: taxonomy and annotation agreement audit.
- E2: single-modality baselines.
- E3: late-fusion versus evidence-aware fusion on identical data.
- E4: missing modality, timestamp drift, camera outage and conflicting evidence fault injection.
- E5: threshold/calibration/abstention analysis.
- E6: unseen site/camera/time test and event prevalence sensitivity.
- E7: human reviewer study only with ethics approval, informed consent and a predeclared protocol.
- E8: edge resource and latency benchmark where a target device is available.

Primary endpoint: event-level recall at a predeclared false-alarm rate, or false alarms per camera-hour with a fixed minimum recall. Choose one before evaluation. Secondary outcomes: precision, missed-event rate, detection delay, PR-AUC, calibration, abstention, evidence-trace completeness and reviewer agreement.

## 8. Statistical plan

Account for clustering by site/camera/session and event prevalence. Report confidence intervals, false alarms per camera-hour, event-level confusion and subgroup performance. Avoid frame-level accuracy as the sole result. Predefine event matching tolerance and handling of overlapping events. Include negative/failure cases and uncertainty.

## 9. Shared AI Core and model governance

Observation stores each permitted sensor/stream event with provenance, timestamp, quality and uncertainty. WorldState represents current, time-bounded facility context and conflicts. ActionProposal is advisory only (e.g., request human review); no enforcement or autonomous intervention. FailureReport records missing streams, clock drift, model failures and false alerts. Evidence Passport links every paper claim to source segments and reviewer status. PUI89-owned weights require cleared lineage, licence, data manifest, training reproducibility, model card, test evidence and approval.

## 10. Thai edition

Provide Thai/English event definitions, privacy notices, reviewer instructions and incident explanations. If language models or speech/text are included, evaluate Thai separately for local vocabulary, code-switching, dialect, transcription/OCR errors and false interpretation. Do not infer Thai performance from English benchmarks.

## 11. Risks and controls

Key risks: privacy harm, false accusation, alarm fatigue, rare-event bias, camera/site leakage and synthetic-to-real confusion. Controls: data minimisation, lawful basis, human review, abstention, event-level metrics, group splits, independent privacy review and strict no-identity/no-enforcement boundary.

## 12. Deliverables

Literature map; approved scope and risk assessment; bilingual event taxonomy; data-rights register; privacy-reviewed dataset manifest; grouped split hashes; baselines and fault-injection suite; statistical analysis; model card; Evidence Passports; manuscript and reproducibility package.

**Exit criteria:** all portfolio gates G0–G9 are supported by reviewable evidence. A synthetic software test passing is not evidence of model accuracy or field effectiveness.
