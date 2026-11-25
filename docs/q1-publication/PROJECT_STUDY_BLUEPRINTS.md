# Six Project — Q1-Oriented Study Blueprints

**Status: Candidate study designs for literature review and protocol development. These are not confirmed research gaps, novelty claims, approved protocols, or completed experiments.**

Each study must first establish that its question is genuinely unresolved in the current literature. The candidate titles below are working titles only.

## 01 — Coconut Harvest AI

**Working title:** Leakage-resistant, uncertainty-aware coconut maturity assessment from orchard imagery under field variation.

- **Scientific question:** How reliably can image-based models distinguish the four defined coconut maturity classes across independent trees, capture sessions, orchards and changing illumination?
- **Classes:** young green; mature green; yellow; brown. The annotation guide must define borderline and ambiguous cases.
- **Hypothesis to test:** A carefully evaluated vision pipeline with calibrated uncertainty and an abstention option may improve dependable class-wise performance over simple image-classification baselines under orchard-level distribution shift. This is a hypothesis, not a result.
- **Data design:** Real coconut images with asset-level provenance, orchard/plot and capture-session grouping, camera and lighting metadata, expert label review and adjudication. Establish a defensible maturity ground truth; appearance-only labels may be insufficient for borderline fruit.
- **Leakage control:** Split by orchard/plot and capture session; keep near-duplicates and images from the same tree/session in one partition. Seal the final test set.
- **Baselines:** majority/class-prior; classical colour/texture features where appropriate; a small conventional CNN; a reviewed lightweight detector/classifier. Compare like-for-like inputs and tuning budgets.
- **Primary outcomes:** macro-F1 and balanced accuracy, with per-class precision/recall and confusion matrix. Select one primary endpoint before the test.
- **Secondary outcomes:** calibration (Brier score / reliability diagram; ECE only with stated binning), selective risk versus coverage, CPU latency distribution, throughput, peak RAM and model size.
- **Robustness:** backlight, shade, glare, occlusion, blur, distance, camera changes, seasonal/orchard shift and ambiguous maturity.
- **Critical confounders:** fruit age/variety, cultivar, season, orchard management, camera settings, annotator expertise and maturity ground-truth method.
- **Publication gate:** independent orchard/site evaluation or an explicit limitation if unavailable; annotation agreement and ground-truth protocol documented.

## 02 — PUI89 Sentinel

**Working title:** Evidence-aware multimodal anomaly and event detection for privacy-constrained facility monitoring.

- **Scientific question:** Does provenance-aware fusion of permitted visual/contextual signals improve event-level detection and uncertainty handling compared with single-modality baselines in defined facility-monitoring scenarios?
- **Scope:** General security observation, facility monitoring, event/anomaly detection and human review only. Narcotics screening, related datasets, X-ray screening and forensic spectra are excluded.
- **Hypothesis to test:** Explicit evidence provenance, conflict representation and abstention may reduce unsupported alerts or improve reviewer traceability compared with a conventional score-only pipeline.
- **Data design:** Rights-cleared, privacy-reviewed facility/event datasets or controlled synthetic scenarios. Document consent/legal basis, retention, de-identification, camera placement, scene coverage and jurisdictional restrictions.
- **Baselines:** rule-based event logic; single-modality detector; single-modality anomaly baseline; late-fusion baseline; proposed evidence-aware fusion. Do not claim multimodal benefit unless each modality is actually present and evaluated.
- **Primary outcomes:** event-level precision/recall, false alarms per camera-hour, missed-event rate and detection delay.
- **Secondary outcomes:** PR-AUC for imbalanced events, calibration, abstention coverage, cross-camera/site generalisation, reviewer agreement and evidence-trace completeness.
- **Robustness:** lighting changes, occlusion, camera movement, missing streams, timestamp drift, noisy metadata, conflicting signals, unseen event types and distribution shift.
- **Critical confounders:** event prevalence, camera field of view, site layout, privacy masking, annotation policy and temporal overlap between train/test.
- **Publication gate:** privacy/ethics review and event-level independent test split; no identity-recognition or enforcement claims unless separately authorised and ethically justified.

## 03 — AI HOME

**Working title:** Evidence-grounded perception and human-aware navigation for compact indoor mobile assistants.

- **Scientific question:** How do perception quality, uncertainty handling and environment-aware planning affect navigation/task reliability in defined indoor spaces with people and dynamic obstacles?
- **Hypothesis to test:** A perception-and-planning approach that preserves uncertainty and safely pauses on ambiguous evidence may improve task completion and reduce unsafe encounters versus a fixed-threshold or non-uncertainty baseline.
- **Data design:** Indoor maps/scenes and controlled trials across room, corridor, doorway, furniture, lighting and human-presence conditions. Separate simulated from physical trials.
- **Baselines:** geometric/navigation baseline; conventional perception baseline; fixed-threshold planner; proposed uncertainty-aware approach.
- **Primary outcomes:** task success rate and intervention rate under predeclared scenarios.
- **Secondary outcomes:** collision/contact and near-miss counts, minimum clearance, path length/efficiency, time-to-goal, localisation error, recovery rate, energy and compute latency.
- **Robustness:** moved furniture, narrow passages, reflective surfaces, low light, occlusion, moving people, sensor dropout and map mismatch.
- **Critical confounders:** map quality, trial operator, route familiarity, human behaviour, robot speed, floor material and sensor calibration.
- **Publication gate:** repeatable scenario protocol, risk review, clear distinction between simulation and physical trials, and independent replication across layouts.

## 04 — AI NOMAD

**Working title:** Robust perception and traversability estimation for compact outdoor mobile robots under terrain and weather variation.

- **Scientific question:** How robustly can a compact outdoor robot estimate traversability and detect navigation hazards across changing terrain, illumination and weather?
- **Hypothesis to test:** Combining visual and available non-visual context with explicit uncertainty may improve hazard awareness and reduce failed traversals versus a single-condition visual baseline.
- **Data design:** Stratified trails, grass, gravel, soil, slopes and uneven surfaces; record weather, illumination, surface condition, sensor configuration and route/session identity. Simulation is a separate evidence class.
- **Baselines:** visual-only baseline; geometric/depth baseline where available; conventional traversability baseline; proposed multimodal/uncertainty-aware method.
- **Primary outcomes:** traversability classification or hazard-detection performance on held-out routes/sites, selected before evaluation.
- **Secondary outcomes:** route completion, intervention/stuck/slip events, localisation drift, false-safe and false-hazard rates, latency, energy and resource use.
- **Robustness:** wet/dry surfaces, shadows, glare, foliage motion, loose terrain, slopes, sensor dropout and unfamiliar routes.
- **Critical confounders:** route selection, operator intervention, speed, payload, wheel/tyre condition, weather and repeated traversal of the same path.
- **Publication gate:** independent routes or sites, documented operating envelope, and explicit separation of simulated evidence from measured field trials.

## 05 — AI Robot Car

**Working title:** Evidence-aware road-hazard perception and uncertainty-calibrated driver warnings under adverse conditions.

- **Scientific question:** Can a perception pipeline provide timely, well-calibrated warnings for defined road hazards and vulnerable road users across changing road and weather conditions?
- **Hypothesis to test:** A context-aware warning approach with uncertainty and abstention may improve the trade-off between missed hazards and nuisance alerts compared with a fixed-threshold baseline.
- **Data design:** Rights-cleared road-scene video/sensor datasets and, where approved, controlled data collection. Record sensor modality, camera pose, route, time, weather and annotation protocol.
- **Baselines:** conventional object detector; object detector plus fixed warning rules; context-only baseline; proposed context/uncertainty-aware warning method.
- **Primary outcomes:** hazard/event-level recall at a predeclared false-alert rate, or another single predeclared primary endpoint.
- **Secondary outcomes:** precision, PR-AUC, warning lead time, false alerts per driving hour, calibration, range/condition-stratified performance and edge latency.
- **Robustness:** rain, glare, night, occlusion, road works, unusual objects, camera vibration, motion blur and sensor degradation.
- **Critical confounders:** route overlap, adjacent video frames, vehicle/camera mounting, speed, weather imbalance and event prevalence.
- **Publication gate:** leakage-resistant route/time split, independent test routes, transparent warning-only boundary and no autonomous-driving claim.

## 06 — EasyRide AI Step-Through Scooter

**Working title:** Rider-view road-hazard perception and warning reliability for two-wheel mobility under real traffic variation.

- **Scientific question:** Which road-hazard and traffic-context cues can be detected reliably from a two-wheel rider viewpoint, and what warning trade-offs arise under changing road conditions?
- **Hypothesis to test:** Rider-view-specific training and context-aware thresholds may improve hazard warning quality over car-view transfer or generic object detection. This must be tested against matched baselines.
- **Data design:** Rights-cleared scooter/motorcycle rider-view data with explicit capture permissions, safety protocol, anonymisation and route/session metadata. Car-only footage is not scooter validation.
- **Baselines:** generic object detector; car-view pretrained baseline (if licence permits); rider-view fine-tuned baseline; proposed context/uncertainty-aware warning method.
- **Primary outcomes:** event-level hazard recall at a predeclared nuisance-warning rate, or a predeclared warning lead-time endpoint.
- **Secondary outcomes:** precision, false alerts per riding hour, warning lead time, calibration, per-hazard performance, edge latency and rider-review workload.
- **Robustness:** rain/wet road, low light, vibration, helmet/camera mounting variation, occlusion, road-surface defects and dense traffic.
- **Critical confounders:** camera position, helmet/handlebar mounting, rider speed, route familiarity, weather, vehicle type and traffic density.
- **Publication gate:** ethical and safety-approved data collection, rider-view independent test routes, and explicit no-autonomous-throttle/steering/braking boundary.

## Cross-project design rules

1. Do not use one metric set for all six papers; choose metrics that match the scientific question and unit of analysis.
2. Determine sample size from power/precision analysis and expected clustering; do not choose a convenient number and call it statistically sufficient.
3. Use grouped splits at the level where leakage can occur: orchard/tree/session, camera/site/time, indoor layout/trial, outdoor route/site, road route/time, or rider/route/session.
4. Predefine primary outcomes and analysis. Label post-hoc analyses exploratory.
5. Compare against strong, relevant baselines with matched data, preprocessing, hardware and tuning budgets.
6. Report effect sizes and uncertainty intervals, not only point estimates or p-values.
7. Keep negative results and failure cases.
8. A Q1 submission requires a defensible contribution relative to current literature, not merely a working prototype or a high metric.
