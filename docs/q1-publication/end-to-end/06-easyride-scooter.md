# 06 — EasyRide AI Step-Through Scooter: End-to-End Research Plan

**Working study title:** Rider-view road-hazard perception and warning reliability for two-wheel mobility under real traffic variation.  
**Status:** Proposed research; no road validation or vehicle-control capability is claimed.

## 1. Research question and boundary

Which road hazards and traffic-context cues can be detected reliably from a two-wheel rider viewpoint, and how do camera mounting, vibration, weather and traffic conditions affect warning quality? The product direction is a practical step-through scooter. Research is advisory only: no autonomous throttle, steering or braking.

**Central comparison:** Does rider-view-specific training and evaluation outperform transfer from generic/car-view data on genuinely independent rider-view routes?

## 2. Literature and expert review

Review motorcycle/scooter rider-view datasets, road hazard detection, two-wheel camera vibration, helmet/handlebar mounting, road-surface defect detection, vulnerable road users, warning usability, adverse-weather vision and edge inference. Seek review from transport safety, motorcycle human factors, computer vision, privacy and vehicle engineering specialists.

## 3. Real-world data acquisition

Prioritise licensed rider-view datasets and permissioned controlled collection. Cover road types, traffic density, country/region, wet/dry surfaces, rain, night, glare, potholes, debris, lane markings, vehicles, pedestrians and camera positions (helmet/handlebar/vehicle-fixed). Record vehicle type, mount, field of view, vibration, speed where lawful, route/session, weather, licence, consent and privacy processing. Car dashcam data is useful as a comparison domain but is not a substitute for scooter rider-view validation.

## 4. Annotation and ground truth

Create a bilingual taxonomy for road users, obstacles, surface defects and warning-worthy events. Annotate event intervals, bounding boxes/masks, distance only when calibrated, and warning lead time only when valid temporal ground truth exists. Define uncertain/unknown classes. Use independent annotators and adjudication. Avoid severity labels without a validated rubric.

## 5. Split design

Group by rider, vehicle, camera mount, route, recording session and date. Hold out entire riders/routes/mount types for generalisation. Do not split frames from one ride across train and test. Keep test data sealed and record manifest hashes. Compare car-view and rider-view domains explicitly.

## 6. Baselines and methods

Compare generic detector, car-view pretrained detector where rights permit, rider-view fine-tuned detector and proposed context/uncertainty-aware warning method. Include camera-motion stabilisation only as a separately evaluated factor. Track objects only where continuous video and valid identity annotations exist. Verify exact model lineage, licence, non-Chinese provenance policy and edge compatibility.

## 7. Experiments

- E1: rider-view dataset audit and annotation agreement.
- E2: generic/car-view transfer baseline.
- E3: rider-view fine-tuning comparison.
- E4: mounting position, vibration, lighting and weather robustness.
- E5: warning threshold, calibration and abstention.
- E6: unseen rider/route external test.
- E7: controlled simulator/usability test for warnings, with ethics approval.
- E8: edge latency, memory and power benchmark on actual hardware.
- E9: sensor failure and degraded-camera tests.

Primary endpoint: event-level hazard recall at a predeclared nuisance-warning rate, or warning lead-time under a valid protocol. Secondary outcomes: precision, false alerts per riding hour, missed-event rate, calibration, per-hazard performance, edge latency and reviewer workload.

## 8. Statistical plan

Account for clustering by rider, ride, route and camera mount. Report confidence intervals, per-condition results and uncertainty for rare events. Compare car-view and rider-view results on matched event categories. Do not claim a benefit from fine-tuning if the test routes/riders overlap with training.

## 9. Shared AI Core

Observation stores rider-view sensor evidence, mount metadata, timestamp and uncertainty. WorldState represents road context and hazards with explicit unknowns. ActionProposal is warning-only and advisory; no actuation is permitted. FailureReport captures missed hazards, false warnings, camera vibration, occlusion and sensor faults. Evidence Passport links paper claims to the exact ride/event records. PUI89-owned weights require full data rights, provenance, training recipe, hash, licence and held-out rider-view evaluation.

## 10. Thai edition

Develop Thai road-hazard terms, bilingual annotation instructions, Thai warning messages, rider study materials and lecturer notes. Include Thai roads and locally relevant traffic conditions only where permissions and data quality permit. If speech or language is included, test Thai ASR/NLU separately, including dialect and code-switching. Report language results separately.

## 11. Safety and ethics

No data collection by an operator while actively riding and interacting with equipment. Use passive, securely mounted recording under an approved safety protocol, or controlled closed-course testing with trained personnel and protective equipment. Follow local road law, consent and privacy rules. Human-subject warning studies require ethics approval. Never test autonomous actuation on public roads.

## 12. Deliverables

Literature map; lecturer-approved protocol; data-rights and safety register; bilingual rider-view taxonomy; anonymised manifest; rider/route-held-out splits; baseline and ablation results; warning usability evidence; statistical/edge reports; model card; Evidence Passports; manuscript and reproducibility materials. No vehicle safety certification or autonomous-driving claim is implied.
