# 04 — AI NOMAD: End-to-End Research Plan

**Working study title:** Robust perception and traversability estimation for compact outdoor mobile robots under terrain and weather variation.  
**Status:** Proposed research; outdoor operation and field robustness are not yet demonstrated.

## 1. Research question

Can a compact outdoor mobile assistant estimate traversability and detect hazards across unseen routes, surface types, illumination and weather? NOMAD is a distinct outdoor four-wheel concept, not AI HOME. Its current design target is 8–10 kg payload with a 10 kg maximum target; these are design targets, not measured performance.

## 2. Literature and expert review

Review traversability estimation, terrain classification, outdoor SLAM, visual/depth/LiDAR perception, adverse-weather robustness, domain generalisation, uncertainty and compact mobile robotics. Seek review from robotics, field operations, terrain/agricultural engineering and safety specialists. Establish a clear operational envelope before experiments.

## 3. Global real-world data plan

Collect or license imagery/sensor data covering trails, grass, gravel, soil, mud, slopes, uneven ground, vegetation, puddles, wet/dry surfaces, shadows, glare and day/night. Seek multiple sites and climate zones via permission-based field partners and verified open datasets. Log weather, route, surface, sensor pose, robot speed, payload and session. Never infer traversability ground truth from appearance alone; use documented expert labels and safe physical measurements where possible.

## 4. Annotation

Define traversable, conditionally traversable, non-traversable, obstacle and unknown classes. Annotate terrain masks/regions, hazard type, slope/roughness where measured, wetness only when observable/verified, and confidence. Preserve unknown labels. Use independent annotators and adjudication. Ground-truth sensor geometry must be calibrated.

## 5. Dataset splits

Group by site, route, date/session and weather episode; keep repeated passes on the same route in one partition. Hold out entire routes/sites for generalisation. Avoid video-frame leakage. Freeze manifests and hashes before training and seal the final test.

## 6. Baselines and candidate methods

Compare visual-only classification/segmentation, geometric/depth baseline where valid sensors exist, conventional traversability estimation and proposed multimodal uncertainty-aware fusion. Include simple rules as a sanity baseline. Exact sensor and model configurations must be recorded; a sensor modality cannot be claimed if absent from the experiment. Review model lineage/licence and hardware fit.

## 7. Experiment matrix

- E1: terrain label validity and sensor calibration.
- E2: baseline traversability/hazard detection on held-out routes.
- E3: wet/dry, slope, vegetation, lighting and weather strata.
- E4: sensor dropout, noisy depth, glare and occlusion fault injection.
- E5: uncertainty/abstention and false-safe versus false-hazard trade-off.
- E6: unseen site/route external evaluation.
- E7: controlled physical trials only after safety review; compare simulation and field data separately.
- E8: edge compute, latency, memory and energy benchmark on actual hardware.

Primary outcome: predeclared traversability or hazard-detection metric on held-out routes. Secondary outcomes: route completion, intervention/stuck/slip events, localisation drift, false-safe and false-hazard rates, latency and energy if measured.

## 8. Statistical analysis

Account for route/site clustering, repeated traversals, weather and payload. Report confidence intervals, per-terrain results and failures. Distinguish perception metrics from robot navigation outcomes. Do not infer safe operation from offline image accuracy.

## 9. Shared AI Core

Observation records sensor inputs, timestamps, calibration and provenance. WorldState represents terrain, obstacles, route context and unknowns. ActionProposal is an advisory route/traversability suggestion; no direct motor control is authorised. FailureReport records slips, stalls, localisation loss, sensor faults and incorrect safe classifications. Evidence Passport connects all manuscript claims to trial records.

## 10. Thai edition

Provide Thai field manuals, terrain vocabulary, annotation guide, safety notices and result summaries. Include Thai regional terminology for surfaces/weather where it affects annotation. If Thai speech/language features are studied, create expert-reviewed Thai test sets and report separate results.

## 11. Safety and risks

Risks include slope/rollover, water ingress, loss of traction, moving vehicles/people, weather exposure and misleading safe classification. Use controlled test sites, speed limits, emergency stop, safety observer, weather stop criteria and mechanical inspection. No public-road autonomy or operation in hazardous floodwater is implied.

## 12. Deliverables

Literature map; operating-envelope definition; global source register; data-rights and safety reviews; bilingual terrain manual; calibrated data manifest; site-held-out splits; baselines; fault-injection results; field protocol; statistics; model card; Core evidence links and manuscript. G0–G9 require evidence, not plan completion alone.
