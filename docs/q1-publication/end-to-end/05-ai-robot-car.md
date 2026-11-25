# 05 — AI Robot Car: End-to-End Research Plan

**Working study title:** Evidence-aware road-hazard perception and uncertainty-calibrated driver warnings under adverse conditions.  
**Status:** Proposed research; no autonomous-driving capability is claimed.

## 1. Research question and safety boundary

Can a vision/perception system provide timely, calibrated warnings for pre-defined road hazards and vulnerable road users across unseen routes, weather and lighting? The research scope is driver assistance and warnings only. It does not authorise autonomous steering, throttle or braking.

## 2. Literature and lecturer review

Review road-scene detection/segmentation, hazard prediction, temporal tracking, adverse-weather perception, calibration, uncertainty, warning design, false-alarm burden and edge inference. Compare public benchmarks, geographic coverage, camera placement, event definitions and evaluation protocols. Obtain review from computer vision, transport safety, human factors and privacy experts.

## 3. Data acquisition

Use verified public road datasets, institution partnerships or controlled collection with lawful permissions. Aim for varied countries/regions, road types, traffic density, day/night, rain, glare, road works and camera viewpoints. Record jurisdiction, route/session, vehicle/camera mounting, weather, speed if lawfully available, licence and anonymisation. Public-road images can contain personal data; review applicable privacy law and blur faces/plates where required. Do not publish sensitive locations or identifiable footage.

## 4. Annotation

Define a bounded hazard taxonomy: road users, obstacles, road-surface hazards and selected event types. Label bounding boxes/masks, track IDs, event intervals, hazard severity only when a defensible rubric exists, and warning-relevant time-to-event only with valid geometry/temporal ground truth. Use bilingual instructions and independent review.

## 5. Leakage-resistant split

Group by route, drive, vehicle, camera and recording session. Adjacent frames, overlapping clips and near-duplicates remain in one partition. Hold out routes/geographies/weather for external generalisation. Freeze test manifests and report actual geographic coverage; do not call the corpus global without evidence.

## 6. Baselines and models

Compare conventional object detector, detector plus fixed warning rules, context-only baseline and proposed context/uncertainty-aware warning method. Tracking is evaluated only on video with identity continuity ground truth. Metric depth or time-to-collision claims require calibrated sensor/geometry; monocular estimates must be labelled as estimates. Clear model origin, licence, revision and compute compatibility before use.

## 7. Experiments

- E1: data/annotation audit and benchmark reproduction.
- E2: detector and event baseline on held-out routes.
- E3: warning-rule and context-aware comparison.
- E4: rain/night/glare/occlusion/road-work subgroup evaluation.
- E5: calibration and abstention; false-alert versus missed-hazard trade-off.
- E6: temporal tracking and warning lead-time analysis with valid ground truth.
- E7: sensor/camera fault injection and distribution shift.
- E8: edge latency/resource evaluation on named hardware.
- E9: human warning usability study only with ethics approval and a safe simulator/controlled protocol.

Primary endpoint: hazard-event recall at a predeclared false-alert rate, or a fixed false-alert rate at a minimum recall. Secondary metrics: precision, PR-AUC, false alerts per driving hour, warning lead time, calibration, subgroup performance and edge latency.

## 8. Statistical plan

Use route/drive-level clusters, confidence intervals and event-level matching rules. Report class prevalence and uncertainty for rare hazards. Compare models with paired route-level evaluation where appropriate. Do not treat frames as independent samples. Include failure cases and nuisance-alert analysis.

## 9. Shared AI Core and PUI89 models

Observation stores camera/sensor evidence and provenance. WorldState records road users, hazards, route/time context and uncertainty. ActionProposal contains warning-only advice; execution is false. FailureReport captures missed hazards, false alerts, sensor faults and stale timestamps. Evidence Passport traces every claim to clips and annotations. Register PUI89-owned model artefacts only after rights, lineage, reproducibility, safety boundary and benchmark gates pass.

## 10. Thai edition

Provide Thai hazard taxonomy, traffic vocabulary, road-user annotation manual, driver-warning wording and lecturer materials. Evaluate Thai ASR/OCR/NLP separately if voice or text is used. For visual-only models, assess Thai label consistency and local road-condition coverage; translation is not model validation.

## 11. Risks and controls

Risks: privacy, rare-event underrepresentation, geographic bias, false reassurance, warning distraction and invalid metric geometry. Controls: data minimisation, rights gate, route-held-out test, calibrated uncertainty, human-driver responsibility, no vehicle actuation and safe usability protocol.

## 12. Deliverables

Literature map; scope/safety protocol; data-rights register; bilingual hazard manual; anonymised manifest; route-grouped splits; baselines; warning evaluation; statistical and edge reports; model card; Evidence Passports; manuscript. No autonomous vehicle or safety certification claim follows from this research.
