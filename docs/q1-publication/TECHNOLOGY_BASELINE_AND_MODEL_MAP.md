# PUI89 Six-Project Technology Baseline for Q1 Research

**Review date:** 25 November 2026  
**Purpose:** Bring the latest technology profiles recorded across the six product repositories and Shared AI Core into PUI89-Research so the Q1 study designs use the actual PUI89 engineering direction.  
**Status:** Repository/document review only. This is not proof of model adoption, hardware selection, physical integration, benchmark results, field validation or publication readiness.

## 1. How to read this baseline

Every technology is labelled by evidence state:

- **Repository-defined:** named in a current product/shared-core design or configuration.
- **Candidate / proposed:** under consideration; not selected for deployment.
- **Adapter present:** code interface exists, but weights may not be present and inference may not have been evaluated.
- **Implemented utility:** software implementation exists; this does not mean product integration or field validation.
- **Measured / validated:** only use this label when a dated, reproducible test report supports it.

A model appearing in a YAML file, model registry or architecture diagram is not proof that it has been downloaded, installed, run, trained, benchmarked or deployed.

## 2. Shared technology foundation — reuse across all six products

### 2.1 Shared AI Core contracts and evidence

All product research adapters should reuse the pinned Shared AI Core contracts:

- Observation
- WorldState
- ActionProposal
- FailureReport
- Evidence Passport

Shared research utilities to reuse where applicable:

- Sensor Intelligence Core: observation validation; freshness, health, calibration and quality admissibility; conservative numeric fusion for independent, same-unit readings.
- Dataset manifest and file-integrity gates; annotation-quality review; duplicate and split-leakage checks.
- Offline model-evaluation harness; experiment records; ProofBench synthetic contract/failure tests.
- CPU-first training and edge benchmark protocols.
- Cross-project conformance tests and model-origin/supply-chain registry.

**Limits:** Sensor Intelligence Core does not connect to hardware, calibrate sensors, infer unmeasured properties or authorize actions. Numeric fusion does not fuse arbitrary images, audio or unlike physical units. ProofBench and contract tests are software evidence, not model-performance or field-safety evidence.

### 2.2 Shared specialist capability families

Use task-specific combinations, not one model for every job:

| Capability | Candidate families / methods | Research use |
|---|---|---|
| Object detection | DETR family; compact detectors; OWLv2 where open-vocabulary proposals are useful | Fruit, people, vehicles, animals and obstacles |
| Segmentation | SAM 2 family; product-specific semantic/instance segmentation | Object boundaries, terrain, road regions and scene masks |
| Tracking | ByteTrack / SORT-style tracking with detector outputs | Persistent IDs in genuine video sequences |
| Depth / geometry | Stereo or RGB-D geometry; calibrated LiDAR; monocular depth candidates | Spatial context; metric claims require calibrated ground truth |
| Scene / vision-language | Gemma 4 family; SmolVLM family as restricted research candidates | Grounded descriptions and human-review assistance |
| Temporal / anomaly | Time-series forecasting and anomaly-detection families | Event sequences, battery/thermal trends and equipment changes |
| Sensor fusion / state estimation | Kalman/complementary filters, factor graphs; learned fusion only when justified | Asynchronous sensor state and uncertainty |
| Robotics VLA / imitation | SmolVLA, GR00T, OpenVLA, pi0, ACT and Diffusion Policy research families | Candidate high-level actions or demonstration learning; not direct actuation |
| Navigation / mapping | ROS 2 Nav2, SLAM Toolbox, RTAB-Map | Mapping, localisation and path-planning research |
| Manipulation | MoveIt 2, OMPL, RRT* | Kinematics and collision-aware planning research |
| Simulation | Isaac Sim, Isaac Lab, Gazebo, MuJoCo; CARLA and SUMO for road/mobility scenarios | Synthetic scenarios, fault injection and controlled simulation |
| Edge optimisation | ONNX Runtime, OpenVINO, quantisation, pruning, distillation; TensorRT only where compatible hardware exists | CPU/GPU/NPU efficiency and deployment-resource experiments |

These are research families and software options, not a mandate to install every component. Exact revisions, origins, base-model lineage, licences, dataset terms, dependencies, hardware needs and commercial-use rights must pass the PUI89 trust gate before any adoption. Chinese-origin or unclear-origin models/resources remain excluded or held under PUI89 policy.

### 2.3 Heterogeneous compute research

The shared platform research direction is workload-aware use of CPU, GPU, NPU, MCU, memory, sensors and power. Each experiment should record:

- Exact device and hardware revision; CPU/GPU/NPU/MCU roles.
- Model and operator compatibility, precision and quantisation.
- Peak RAM/VRAM, storage, memory bandwidth and concurrent workload.
- Latency distribution, throughput, queueing and deadline misses.
- Power measurement boundary, thermal state and energy per task when measurable.
- Fallback behaviour and whether the fallback itself has been validated.

Do not claim energy efficiency or real-time performance from theoretical specifications or results measured on different hardware.

## 3. Product-specific technology baselines

### 3.1 Coconut Harvest AI

**Research domain:** orchard perception, coconut bunch/fruit detection, four-class maturity assessment, spatial context and future supervised harvesting research.

**Latest repository-defined technology direction:**

- Vision: RGB and RGB-D; optional LiDAR; orchard imagery and video.
- Segmentation: SAM 3 configured for image/video segmentation; tracking enabled in the current reference configuration.
- 3D: Open3D point-cloud processing, RGB-D/LiDAR geometry and semantic mapping.
- Vision-language reasoning: `google/gemma-4-31B-it` is named in the product configuration for image/text scene reasoning and task interpretation.
- Action-policy research: SmolVLA is marked selected in the product reference configuration; NVIDIA GR00T N1.7, OpenVLA and pi0 are also listed as candidates. `FLUX-3-Action-Base` is listed as a further action/world-model candidate and requires separate lineage/licence review.
- Planning: ROS 2, Nav2, MoveIt 2, OMPL/RRT* and collision checking.
- Simulation: Isaac Sim and Isaac Lab, domain randomisation and sim-to-real research.
- Synthetic media/scenarios: LTX-2.5-Diffusers is listed for orchard video/audio and rare-condition scenario generation; licence and resource review required.
- Training/evaluation ecosystem: PyTorch, Transformers, LeRobot workflow references; ONNX/TensorRT/vLLM are listed as deployment/runtime options subject to hardware compatibility.
- Safety architecture: deterministic workspace, collision, human/animal exclusion, joint/force/velocity, confidence and emergency-stop checks; foundation models remain advisory.

**Important status correction:** the current `config/ai_stack.yaml` marks the previous detector integration as permanently removed and says no replacement detector is selected. Do not present YOLO26 as the current active detector. Earlier YOLO26 adapter work is historical/retired unless a new explicit selection is made.

**Research questions to evaluate:** four-class maturity classification; orchard-level generalisation; segmentation and tracking under occlusion; calibrated spatial estimation; uncertainty/abstention; CPU-first versus heterogeneous compute; simulation-to-real gap.

**Ground truth:** keep young green, mature green, yellow and brown as four distinct classes. Appearance labels require human review and a defensible agronomic reference. Tree height or metric distance requires measured ground truth; monocular relative depth is not a measurement.

**Status:** technologies are repository-defined/configured or candidate entries. No claim here that weights were downloaded, inference benchmarked, harvesting action trained, or physical harvesting validated.

### 3.2 PUI89 Sentinel

**Research domain:** general security observation, facility/environmental monitoring, multimodal event and anomaly detection, evidence reliability and human-reviewed alerts.

**Technology baseline for research:**

- Multimodal observation framework with modality-specific adapters and provenance.
- Candidate visual pipeline: object/person/event detection, segmentation where useful, temporal tracking and scene/context understanding.
- Candidate non-visual signals only where lawful and actually available: thermal, acoustic/event audio, vibration, motion/IMU, environmental and equipment-state telemetry.
- Temporal anomaly detection and sensor-health/freshness/quality assessment.
- Evidence fusion with explicit missing, stale, contradictory and unknown states.
- LLM/VLM may organise evidence and draft explanations for human review; they do not establish identity, guilt, threat certainty or enforcement disposition.
- Shared AI Core Observation, WorldState, ActionProposal, FailureReport and Evidence Passport for traceability.
- Synthetic scenarios and authorised, privacy-reviewed datasets for early experiments.

**Model selection:** no Sentinel-specific model checkpoint is confirmed by the current six-product research evidence. DETR/compact detection, SAM-family segmentation, ByteTrack/SORT, time-series anomaly methods and compact VLM/LLM families remain candidate families only, pending the full origin/licence/resource gate.

**Strict scope exclusions:** do not include narcotics detection/screening, narcotics datasets, X-ray screening, NIST DART-MS, NIR forensic spectra or chemical-forensic screening. Do not import the retired screening-robot architecture as Sentinel's current technology stack.

**Research questions to evaluate:** event-level anomaly detection; multimodal missing-sensor robustness; false-alert rate; uncertainty and abstention; evidence traceability; human-review agreement; privacy-preserving operation.

### 3.3 PUI89 AI HOME

**Research domain:** indoor four-wheel home assistant, indoor awareness, event triage, resident alerts and supervised assistance.

**Latest repository-defined technology direction:**

- Optional local Hugging Face vision adapter exists in the repository.
- `google/owlv2-base-patch16-ensemble`: text-conditioned open-vocabulary object-localisation candidate.
- `Intel/dpt-hybrid-midas`: optional monocular **relative** depth candidate; not metric distance.
- Adapter dependencies are documented as local PyTorch, Transformers, Pillow and NumPy; CPU inference is the default.
- Sensor interface specification begins with temperature and relative humidity channels. No physical sensor part, bus or electrical interface is selected.
- Optional audio and vibration/IMU context appears in the shared capability profile; these are not confirmed installed sensors.
- Indoor navigation research: deterministic synthetic 2D grid/graph scenarios for return/recall, blocked route, localisation loss, low-energy verdict, emergency stop and manual override.
- Candidate robotics foundations for later research: ROS 2/Nav2, SLAM Toolbox or RTAB-Map, Gazebo/MuJoCo. No physical navigation integration is claimed.
- Shared AI Core contracts, evidence quality, baseline/change tracking and human-reviewed proposals.

**Status:** adapter code is present, but model weights are not downloaded and inference is not benchmarked in the repository. Indoor navigation document is a synthetic simulation specification, not a navigation controller or field result.

**Research questions to evaluate:** open-vocabulary object localisation in indoor environments; relative-depth limitations; privacy-aware event understanding; sensor missingness/fault handling; layout generalisation; safe-hold/return proposal logic.

### 3.4 PUI89 AI NOMAD

**Research domain:** compact dog-inspired four-wheel mobile assistant with handle; supervised outdoor and everyday mobile assistance.

**Technology baseline:**

- Candidate perception: object/person/obstacle detection, tracking, depth/near-field spatial context and terrain/scene understanding.
- Repository-listed vision adapter candidates: `google/owlv2-base-patch16-ensemble` for text-conditioned object proposals and `Intel/dpt-hybrid-midas` for relative monocular depth.
- Candidate outdoor robotics foundations: ROS 2/Nav2, SLAM Toolbox, RTAB-Map, sensor fusion and local mapping; Gazebo/MuJoCo for simulation.
- Candidate multimodal context: RGB/RGB-D where available, IMU/motion and environmental/weather observations only when supported by a real sensor record.
- Shared AI Core contracts preserve evidence, uncertainty, conflicts and human-reviewed navigation proposals.

**Status:** adapter code is present in the product repository; model weights are not downloaded and inference is not benchmarked. The candidate navigation/sensor stack is not evidence of physical integration. The current product boundary remains supervised mobility assistance; no unsupervised public-space autonomy claim.

**Research questions to evaluate:** obstacle/path perception; outdoor scene and terrain generalisation; relative-depth usefulness and failure; sensor dropout; localisation robustness; safe proposal abstention across uneven terrain.

### 3.5 PUI89 AI Robot Car

**Research domain:** public-road vehicle driver-awareness and decision support. The current engineering repository uses the name PUI89 AI Global SUV; retain AI Robot Car as the user's portfolio label/legacy alias.

**Latest repository-defined technology direction:**

- AI-01 multi-camera surround-vision profile: front and rear cameras initially; side/rear-quarter cameras are optional and require a coverage study.
- AI-02 object/obstacle perception: cars, trucks/buses, motorcycles, bicycles, pedestrians, animals, cones, barriers, road-work equipment, debris, curbs and walls; unknown/other must remain available.
- AI-03 vulnerable-road-user awareness/protection profile and AI-04 driver-behaviour awareness are capability areas in the shared vehicle architecture; do not assume every profile is implemented.
- Candidate perception: DETR/compact object detection, segmentation for lanes/drivable area, tracking, depth/spatial cues, road-scene/sign understanding and context-aware warnings.
- Candidate temporal intelligence: vehicle-state, battery/thermal and predictive-maintenance trend analysis where reliable read-only signals exist.
- Simulation candidates: CARLA and SUMO for road/traffic scenarios; Gazebo/MuJoCo where appropriate for robotics/sensor-system simulation.
- Shared AI Core handles evidence-linked advisory records and global/local context freshness.

**Status:** product profiles and software-only architecture are defined; no camera, model, compute hardware, vehicle integration, road testing or certification is established. No autonomous steering, throttle, braking, propulsion or vehicle-bus connection.

**Research questions to evaluate:** multi-camera coverage and calibration; per-camera object detection; VRU detection; road-scene segmentation; hazard event timing; adverse-weather robustness; uncertainty-calibrated driver warnings; CPU/edge latency.

### 3.6 EasyRide AI Step-Through Scooter

**Research domain:** two-wheel step-through scooter, rider-first road awareness and advisory safety support.

**Latest repository-defined technology direction:**

- AI-01 multi-direction vision profile: forward and rear cameras initially; optional side/rear-quarter cameras only if coverage, mounting, power and ergonomics justify them.
- Explicit uncovered-area representation: front/rear cameras do not establish full 360-degree coverage or eliminate blind spots.
- AI-02 object/obstacle detection and AI-03 vulnerable-road-user awareness are shared vehicle capability areas; scooter-specific rider viewpoint must be evaluated separately from car-view data.
- AI-04 rider-behaviour awareness profile: optional read-only speed, yaw/lean or IMU context only if a documented, calibrated interface exists. No gaze, fatigue, intoxication, health or fitness-to-ride inference.
- Candidate perception: road-user detection/tracking, road-surface/obstacle segmentation, near-field context, depth where ground truth supports it, weather and vehicle-state context.
- Candidate temporal intelligence: battery/thermal and supported vehicle-health trends.
- Candidate simulation: CARLA/SUMO for road/traffic scenarios; Gazebo/MuJoCo where useful for sensor/robotics components.
- Rider-facing alerts must be brief, glanceable and distraction-tested; local warnings must not depend on cloud connectivity.

**Status:** product profiles are proposed; no camera, model, compute hardware, functioning scooter, rider trial, road validation or certification is established. Rider retains full control; no autonomous steering, throttle, braking, balance or propulsion.

**Research questions to evaluate:** rider-view versus car-view transfer; road-surface and hazard detection; front/rear coverage limits; VRU event timing; vibration/lean/weather robustness; alert false-positive rate and human-factors/distraction evaluation.

## 4. Model registry decisions and conflicts to resolve

The current Shared AI Core model registry/radar is a research shortlist, not deployment approval:

- Google Gemma 4 E2B: trial candidate for shared multimodal research; Thai grounding, CPU/RAM and quantised performance require measurement.
- Google Gemma 4 E4B: watch candidate; higher resource demand expected.
- IBM Granite 4.2 3B: trial candidate for structured report/maintenance/quality triage; Thai performance is unverified.
- SmolVLM2 500M Video Instruct: watch/offline human-assistance only; not for high-stakes decisions.
- DETR ResNet-50 and SAM 2.1 Hiera Tiny: candidates in the central registry; resource and task evaluation required.
- OWLv2 and Intel DPT-Hybrid: product-repository adapters for HOME/NOMAD; weights absent and inference unbenchmarked.
- Coconut configuration names Gemma-4-31B-it, while the central model radar prioritises Gemma 4 E2B/E4B. This is a model-selection/resource-policy conflict, not a resolved choice. Keep the 31B entry as a repository-configured research candidate pending explicit provenance, licence and hardware review.
- Coconut's detector is currently disabled/retired with no replacement selected. Do not silently reactivate YOLO26 or substitute another detector.
- GR00T N1.7, SmolVLA, OpenVLA, pi0 and FLUX-3-Action-Base are action-policy research candidates in Coconut configuration, not approved motor-control systems.

No model should be downloaded, installed, executed or promoted without explicit approval and the complete seven-layer origin/supply-chain, licence, resource and safety review.

## 5. Q1 paper mapping — required technology-specific experiments

| Project | Primary technology comparison | Critical evaluation |
|---|---|---|
| Coconut Harvest AI | Detection/segmentation/tracking and maturity classifier; VLM only as a separate reasoning aid; spatial methods compared with measured ground truth | Orchard/tree/session split; four-class macro-F1; per-class recall; annotation agreement; calibration/abstention; spatial error only with metric ground truth; CPU/RAM/latency |
| PUI89 Sentinel | Single-modality versus multimodal anomaly/event methods; sensor-health gate and evidence-aware human review | Event-level precision/recall; false alarms per camera-hour or monitored-hour; detection delay; missing-modality robustness; reviewer agreement; privacy and provenance |
| AI HOME | OWLv2 versus conventional detection baseline; relative-depth assistance versus RGB-only; deterministic indoor state/proposal logic | Layout/session split; object/event metrics; localisation/route simulation results kept separate from physical tests; safe-hold fault injection; privacy review |
| AI NOMAD | Detection/tracking/depth/terrain-context combinations and sensor-fusion ablations | Route/site split; terrain-stratified performance; false-safe/false-hazard outcomes; localisation drift; interventions/stuck events only in approved trials |
| AI Robot Car | Per-camera versus fused multi-camera perception; detection, segmentation, tracking and VRU warning stack | Route/time split; AP/mAP with declared IoU; event-level recall; false alerts per driving hour; warning lead time; weather/lighting strata; latency |
| EasyRide Scooter | Rider-view-specific perception versus generic/car-view transfer; optional read-only motion-context ablation | Rider/route/session split; event-level hazard recall; false alerts per riding hour; warning lead time; uncovered camera regions; vibration/lean/weather and distraction tests |

Do not pool six products into one performance result. Each paper needs an independent research question, dataset protocol, baselines, primary outcome, statistical plan and claim-to-evidence matrix.

## 6. Immediate research-readiness gaps

1. Confirm a single, versioned technology manifest per product; resolve naming and model-version conflicts.
2. Verify model origin, base/teacher/adapter/quantisation lineage, licence, dataset provenance, dependencies and artifact size.
3. Establish lawful, product-specific datasets and annotation protocols; no model training until rights and labels pass review.
4. Pin baseline software/model revisions and record CPU-first resource constraints before any download.
5. Freeze primary metrics, leakage groups, sample-size rationale and statistical analysis before test-set evaluation.
6. Run reproducible software/contract tests, then synthetic benchmarks, then approved offline model evaluation; physical trials require separate approval and risk review.
7. Preserve all failures, unknowns, negative results and limitations; no Q1 novelty or performance claim until supported by current literature and real experiments.

## 7. Provenance of this technology review

Reviewed current repository records on 25 November 2026, including:

- `Pui89/Coconut-Harvest-AI`: `config/ai_stack.yaml`, `config/advanced_models.yaml`, `docs/AI_STACK.md`, `docs/PHYSICAL_AI_STACK.md`, `docs/AI_AGENT_REVIEW_PLAN.md`.
- `Pui89/AI-Home-Safety-Robot`: `docs/HUGGING_FACE_MODEL_INTEGRATION.md`, `docs/SENSOR_INTEGRATION_SPECIFICATION.md`, `docs/SYSTEM_ARCHITECTURE.md`.
- `Pui89/AI-Mobile-Assistant-Robot`: `docs/HUGGING_FACE_MODEL_INTEGRATION.md`, `docs/ARCHITECTURE.md`.
- `Pui89/PUI89-AI-Global-SUV`: `docs/AI01_SURROUND_VISION_PROFILE_V1.0.md`, `docs/AI02_OBJECT_OBSTACLE_DETECTION_PROFILE_V1.0.md`, `docs/AI_ARCHITECTURE.md`, `docs/FREE_AI_TECH_STACK.md`.
- `Pui89/AI-Step-Through-Scooter`: `docs/AI01_MULTI_DIRECTION_VISION_PROFILE_V1.0.md`, `docs/AI04_RIDER_BEHAVIOUR_AWARENESS_PROFILE_V1.0.md`, `docs/FREE_AI_TECH_STACK.md`.
- `Pui89/PUI89-Shared-AI-Core`: specialist model family matrix, Hugging Face model registry, non-Chinese open-model radar, master dataset/model mapping, sensor intelligence core, universal sensory intelligence and heterogeneous compute architecture.

**Scope note:** the Shared AI Core registry snapshot inspected during this review currently labels a five-product portfolio and omits Sentinel. This research document deliberately follows the user's current six-product scope and treats Sentinel as its own general-security research track. The registry discrepancy must be reconciled upstream; it must not be used to silently remove Sentinel or restore the retired screening scope.


## 8. End-to-end 360-degree perception research architecture

**Purpose:** define a common, testable surround-perception research architecture that can be adapted to all six projects. “360-degree perception” means a measured, time-synchronised and uncertainty-aware representation of the environment around a platform—not simply placing multiple cameras on a diagram. It does not guarantee complete visibility, zero blind spots, reliable detection in every condition or safe autonomous operation.

### 8.1 What 360-degree perception includes

1. **Sensor coverage design:** identify the platform, operating envelope, required fields of view, mounting locations, occlusions, overlap zones and blind/unobserved regions. Possible inputs include multiple RGB cameras, RGB-D/stereo, thermal, LiDAR, radar, IMU/odometry and permitted environmental sensors. Use only modalities actually present in a recorded experiment.
2. **Calibration and synchronisation:** intrinsic/extrinsic calibration, camera-to-platform coordinate frames, timestamps, rolling-shutter/motion effects, clock drift, sensor health and calibration version. Recalibration triggers and tolerances must be specified.
3. **Per-sensor perception:** detection, segmentation, tracking, depth/geometry and scene interpretation are evaluated per sensor before fusion. Preserve the original sensor identity and source timestamps.
4. **Spatial fusion:** transform observations into a common platform/world frame; represent occupied, free, unknown and occluded regions separately. Fuse only compatible measurements with justified uncertainty models. Do not turn missing coverage into “free space”.
5. **Temporal tracking and world model:** maintain track identity only when continuity is supported; record object state, velocity estimates, age, confidence, uncertainty and provenance. Handle duplicate detections in overlapping views without double-counting.
6. **Risk and context reasoning:** estimate task-relevant hazards and context, expose conflicting evidence and out-of-distribution conditions, and allow abstention. A VLM/LLM can help explain or summarise evidence but is not ground truth or a safety controller.
7. **Decision support and fallback:** publish bounded, advisory ActionProposal records with preconditions, uncertainty, freshness and reason codes. Stale, contradictory, uncalibrated or insufficient-coverage input must trigger unknown/abstain/safe-hold behaviour appropriate to the platform. These research plans do not authorise direct actuation.
8. **Evidence and audit:** retain dataset/model/calibration versions, sensor provenance, split manifest, timestamps, inference outputs, faults, reviewer decisions and experiment records so each result is reproducible.

### 8.2 Shared AI Core data flow

| Stage | Shared AI Core representation | Required evidence |
|---|---|---|
| Raw sensor capture | Observation | Sensor ID, modality, timestamp, frame, calibration ID, health, quality, source/hash and permitted-use metadata |
| Calibrated geometry | Observation + derived evidence | Coordinate frame, calibration version, transform, synchronisation error and uncertainty |
| Fused environment | WorldState | Coverage map, detected entities, tracks, free/occupied/unknown space, conflicts, age and confidence |
| Advisory response | ActionProposal | Proposed warning/route/assistive suggestion, evidence references, preconditions, expiry, uncertainty and abstention reason |
| Fault or degraded mode | FailureReport | Missing camera/sensor, occlusion, drift, dropped frames, calibration failure, false/missed detection and fallback outcome |
| Research traceability | Evidence Passport | Data split, code/model/weights hash, calibration, configuration, metric, test condition, reviewer and claim link |

The fusion layer must not infer a complete 360-degree view from partial sensors. Coverage should be represented as a measurable function of direction, range, elevation, distance, lighting and operating condition. Every derived estimate must retain links to the contributing observations.

### 8.3 Six-project 360-degree adaptation matrix

| Project | 360-degree perception objective | Candidate sensor/view configuration (not a selected BOM) | Project-specific evaluation |
|---|---|---|---|
| Coconut Harvest AI | Surrounding orchard/harvesting-scene awareness: fruit bunches, branches, trunks, workers, animals, obstacles and reachable workspace | Multi-view RGB; RGB-D/stereo or LiDAR only if available and calibrated; IMU/robot pose if recorded | Angular coverage and occlusion by canopy; fruit/bunch duplicate handling; four maturity classes; per-view and fused metrics; spatial error against measured ground truth; worker/animal exclusion-zone recall |
| PUI89 Sentinel | Privacy-constrained facility/environment event awareness across permitted camera zones and approved non-visual sensors | Fixed multi-camera views plus only authorised thermal, acoustic, vibration or environmental channels | Camera-zone coverage; event-level recall and false alarms per monitored hour; cross-camera duplicate events; missing-stream and clock-drift faults; privacy masking and evidence traceability. Narcotics/X-ray/forensic scope remains excluded |
| AI HOME | Indoor assistant awareness around the mobile base, including people, furniture, doors, obstacles and drop-offs | Forward/rear/side or panoramic RGB as justified; depth/short-range sensors and IMU/odometry only when installed and calibrated | Blind-zone and near-field coverage; dynamic human/obstacle recall; doorway and drop-off cases; localisation/layout split; safe-stop/abstention and intervention rates |
| AI NOMAD | Outdoor surround awareness for terrain, obstacles, people, animals, slopes and route boundaries | Multi-direction RGB; depth/LiDAR/IMU/odometry where actually available; environmental sensors only when recorded | Terrain/weather strata; ground-contact/near-field blind zones; false-safe versus false-hazard; route/site-held-out tests; vibration, mud, rain and sensor contamination |
| AI Robot Car | Vehicle surround awareness for road users, vulnerable road users, obstacles and road context | Existing repository direction begins with front/rear cameras; side and rear-quarter views are optional and require coverage/calibration study; radar/LiDAR only if approved and fitted | Per-camera and fused detection; angular/range coverage; overlap duplicates; VRU recall; route/weather-held-out event metrics; latency and warning lead time. No autonomous steering/throttle/braking |
| EasyRide AI Step-Through Scooter | Rider-centred surround awareness with explicit two-wheel blind-zone and camera-mount limitations | Repository direction begins with forward/rear views; side/rear-quarter or other sensors are candidates only after ergonomic, mounting, vibration and power assessment | Rider-view versus car-view; blind/unobserved region map; lean/turn/vibration/weather strata; hazard recall and false alerts per riding hour; distraction/usability. No autonomous steering/throttle/braking |

### 8.4 End-to-end experiment protocol

- **P0 — Operational envelope:** define platform, speed/range, environment, user/task, hazards, safety boundary and what “360” must cover.
- **P1 — Coverage and sensor design:** produce top/side coverage diagrams, field-of-view/range tables, overlap and blind-zone maps. Treat these as design artefacts until measured.
- **P2 — Calibration:** document calibration target/procedure, coordinate frames, reprojection or geometric residuals, timestamp synchronisation and acceptance thresholds.
- **P3 — Rights-cleared data:** collect/licence multi-view sequences with asset-level provenance, consent/legal basis, privacy handling and permitted training/test/publication use.
- **P4 — Annotation:** label objects/events across views, cross-camera correspondences where justified, occlusion, unknown zones and sensor faults. Use bilingual EN/TH guidance and independent adjudication.
- **P5 — Leakage-resistant splits:** group by site, route, orchard, building, vehicle/robot, capture session and time. All views and frames from the same physical event/session must remain in one partition. Hold out complete sites/routes/platforms for generalisation.
- **P6 — Baselines:** evaluate each sensor independently; then compare late fusion and geometry/state-based fusion. Include single-view and missing-sensor baselines so fusion benefit is measurable.
- **P7 — Robustness:** inject camera blackout, lens obstruction, glare, rain, low light, vibration, dropped frames, clock drift, calibration perturbation and conflicting detections. Measure safe abstention and recovery.
- **P8 — Locked evaluation:** report per-camera, per-angle, range, object class, environment and fused results. Use event/track-level metrics where applicable, calibration and uncertainty intervals; never report only aggregate accuracy.
- **P9 — Resource and deployment study:** measure actual device latency distribution, throughput, RAM/VRAM, storage, thermal state and energy with a documented measurement boundary. Compare CPU/GPU/NPU scheduling and fallback only on available hardware.
- **P10 — Independent review:** domain, robotics/vehicle safety, statistics, privacy and lecturer review; publish limitations and unresolved blind spots.

### 8.5 Minimum metrics and statistical safeguards

- Angular coverage: measured visible/observable proportion by azimuth/elevation and defined range bands; state how occlusion and out-of-range regions are counted.
- Detection/segmentation: per-class precision, recall, AP/mAP or IoU/Dice as appropriate, per-camera and fused.
- Tracking: IDF1/HOTA/MOTA or a justified task metric, ID switches, fragmentation and cross-camera association error.
- Geometry: calibration residual, depth/position error and uncertainty against independent measured ground truth.
- Event/hazard performance: event recall, precision, false alerts per operating hour, missed-event rate and detection/warning delay.
- Reliability: calibration error, uncertainty quality, abstention coverage, degraded-mode detection, stale-data rate and fault-recovery time.
- Compute: p50/p95/p99 latency where sample size supports it, throughput, peak memory and measured power/energy.
- Statistics: cluster resampling at the independent site/route/session/platform level; confidence intervals; predeclared primary endpoint; no frame-level pseudo-replication.

### 8.6 Safety, privacy and claim boundaries

- 360-degree perception is not equivalent to collision avoidance, autonomy or safety certification.
- No camera arrangement guarantees zero blind spots; document blind, occluded, uncalibrated and unsupported regions.
- Human subjects, public-road/facility recordings and sensitive locations require applicable permissions, privacy review and ethics approval.
- Research adapters remain advisory. Vehicle products must not command steering, throttle or braking; mobile robots require separate safety engineering, emergency stop and supervised testing.
- Do not claim full 360-degree coverage, real-time performance, global generalisation or safe operation until measured under a disclosed protocol.
- Synthetic simulation, offline dataset testing and physical trials are separate evidence classes and must be reported separately.

### 8.7 Thai-language research and lecturer materials

Provide Thai/English versions of the sensor glossary, calibration procedure, coverage/occlusion annotation guide, fault taxonomy, experiment protocol, safety notices and result dashboard. Thai translation supports comprehension; it does not validate perception. If Thai speech/text/VLM functions are used, evaluate Thai language performance independently, including local terms and code-switching. Present lecturers with a simple sensor-layout diagram, a worked example from raw views to fused WorldState, a blind-zone failure case, the metrics and the evidence required to pass each gate.

### 8.8 Current 360-degree research status (2026-11-25)

- Common architecture and project-specific study requirements: **specified in this document**.
- Per-project final sensor BOM and physical camera placements: **not selected/verified here**.
- Calibrated 360-degree coverage maps: **not recorded**.
- Rights-cleared synchronized multi-view datasets: **not recorded**.
- Cross-camera fusion models trained and independently tested: **not recorded**.
- Physical surround-perception validation: **not recorded**.

This is a research and engineering specification, not a claim that any PUI89 product currently has functioning 360-degree perception.

## 9. ภาคภาษาไทย — กรอบวิจัยการรับรู้รอบทิศทาง 360 องศาแบบครบวงจร

**วัตถุประสงค์:** กำหนดสถาปัตยกรรมวิจัยร่วมสำหรับการรับรู้สภาพแวดล้อมรอบแพลตฟอร์มทั้ง 6 โครงการ โดยคำว่า 360 องศาหมายถึงระบบหลายเซนเซอร์/หลายมุมมองที่ผ่านการวัดพื้นที่ครอบคลุม การปรับเทียบเวลาและตำแหน่ง และการจัดการความไม่แน่นอน ไม่ได้หมายความว่ามองเห็นทุกจุด ไม่มีจุดบอด หรือทำงานปลอดภัยโดยอัตโนมัติ

### 9.1 องค์ประกอบหลัก

1. **ออกแบบพื้นที่มองเห็น:** ระบุตำแหน่งกล้อง มุมรับภาพ ระยะทำงาน พื้นที่ซ้อนทับ สิ่งบดบัง และจุดที่มองไม่เห็น
2. **ปรับเทียบและซิงโครไนซ์:** ตรวจสอบ Intrinsic/Extrinsic Calibration กรอบพิกัด เวลา ความคลาดเคลื่อนของนาฬิกา และสถานะเซนเซอร์
3. **ประมวลผลแยกตามเซนเซอร์:** ตรวจจับ แบ่งส่วน ติดตาม และประเมินระยะ/รูปทรง โดยคงข้อมูลแหล่งที่มา
4. **รวมข้อมูลเชิงพื้นที่:** แปลงข้อมูลเข้าสู่กรอบพิกัดร่วม และแยกพื้นที่ที่พบวัตถุ พื้นที่ว่าง พื้นที่ไม่ทราบ และพื้นที่ถูกบดบังอย่างชัดเจน
5. **สร้าง World Model:** ระบุตำแหน่ง วัตถุ การเคลื่อนที่ อายุข้อมูล ความเชื่อมั่น และความไม่แน่นอน
6. **ประเมินบริบทและความเสี่ยง:** แสดงข้อมูลขัดแย้ง สภาวะที่ไม่เคยพบ และยอมงดตัดสินใจเมื่อหลักฐานไม่เพียงพอ
7. **เสนอแนวทางแบบมีข้อจำกัด:** ส่ง ActionProposal เพื่อการแจ้งเตือนหรือข้อเสนอแนะเท่านั้น ไม่อนุญาตให้ควบคุมยานยนต์หรือหุ่นยนต์โดยตรงจากแผนวิจัยนี้
8. **จัดเก็บหลักฐาน:** เชื่อมโยงข้อมูล รุ่นโมเดล การปรับเทียบ การทดลอง ข้อผิดพลาด และผลการประเมินให้ตรวจสอบย้อนหลังได้

### 9.2 การประยุกต์ใช้กับทั้ง 6 โครงการ

| โครงการ | เป้าหมายการรับรู้รอบทิศทาง |
|---|---|
| Coconut Harvest AI | รับรู้ผลมะพร้าว กิ่ง ลำต้น คน สัตว์ และพื้นที่ทำงานรอบอุปกรณ์เก็บเกี่ยว พร้อมจัดการภาพซ้ำและสิ่งบดบัง |
| PUI89 Sentinel | เฝ้าสังเกตพื้นที่และเหตุการณ์ในสถานที่ที่ได้รับอนุญาต พร้อมรักษาความเป็นส่วนตัวและหลักฐาน โดยไม่รวมงานยาเสพติด/X-ray/นิติวิทยาศาสตร์ที่ถูกยกเว้น |
| AI HOME | รับรู้คน เฟอร์นิเจอร์ ประตู สิ่งกีดขวาง และพื้นที่เสี่ยงรอบหุ่นยนต์ภายในอาคาร |
| AI NOMAD | รับรู้เส้นทาง ภูมิประเทศ สิ่งกีดขวาง คน สัตว์ ความลาดชัน และสภาพอากาศรอบหุ่นยนต์ภายนอก |
| AI Robot Car | รับรู้รถ คนเดินเท้า ผู้ใช้ถนน สิ่งกีดขวาง และบริบทถนนรอบรถ โดยต้องประเมินมุมกล้องด้านหน้า หลัง และด้านข้างจริง |
| EasyRide Scooter | รับรู้ถนนและอันตรายในมุมมองผู้ขับขี่สองล้อ พร้อมประเมินจุดบอด การเอียง การสั่นสะเทือน และข้อจำกัดการติดตั้งกล้อง |

### 9.3 ขั้นตอนวิจัยครบวงจร

- P0 กำหนดขอบเขตการทำงานและความหมายของ 360 องศาสำหรับแต่ละโครงการ
- P1 ออกแบบตำแหน่งเซนเซอร์ แผนภาพพื้นที่ครอบคลุม และจุดบอด
- P2 ปรับเทียบกล้อง/เซนเซอร์และตรวจสอบการซิงโครไนซ์
- P3 จัดหาภาพและข้อมูลหลายมุมมองที่มีสิทธิ์ใช้งานถูกต้อง
- P4 ทำ Annotation สองภาษา พร้อมผู้ตรวจสอบอิสระและการตัดสินกรณีเห็นต่าง
- P5 แบ่ง Train/Validation/Test โดยไม่ให้ภาพจากเหตุการณ์หรือรอบบันทึกเดียวกันข้ามชุดข้อมูล
- P6 เปรียบเทียบโมเดลรายเซนเซอร์กับวิธีรวมข้อมูลหลายเซนเซอร์
- P7 ทดสอบความทนทานต่อกล้องดับ เลนส์ถูกบัง ฝน แสงน้อย การสั่น เวลาเหลื่อม และการปรับเทียบคลาดเคลื่อน
- P8 ประเมินผลบนชุดทดสอบที่ล็อกไว้ แยกตามกล้อง มุม ระยะ คลาส และสภาพแวดล้อม
- P9 วัดเวลา หน่วยความจำ อุณหภูมิ และพลังงานบนฮาร์ดแวร์จริง
- P10 ให้ผู้เชี่ยวชาญ อาจารย์ และผู้ตรวจสอบด้านสถิติ/ความปลอดภัย/ความเป็นส่วนตัวประเมิน

### 9.4 ตัวชี้วัดและข้อควรระวัง

ต้องรายงานพื้นที่มองเห็นจริง จุดบอด ความแม่นยำรายกล้องและหลังรวมข้อมูล การติดตามวัตถุ ความคลาดเคลื่อนเชิงพื้นที่ อัตราแจ้งเตือนผิดพลาด ความล่าช้า ความเชื่อมั่น การงดตัดสินใจ และทรัพยากรประมวลผล พร้อมช่วงความเชื่อมั่นทางสถิติ โดยคำนึงถึงการจัดกลุ่มข้อมูลตามสถานที่ เส้นทาง และรอบบันทึก ไม่ถือว่าแต่ละเฟรมเป็นตัวอย่างอิสระ

### 9.5 สถานะ ณ 25 พฤศจิกายน 2026

- กรอบสถาปัตยกรรมและข้อกำหนดวิจัย 360 องศา: **ระบุไว้ในเอกสารนี้แล้ว**
- การเลือกฮาร์ดแวร์และตำแหน่งติดตั้งจริง: **ยังไม่มีการยืนยัน**
- แผนที่พื้นที่ครอบคลุมที่ผ่านการปรับเทียบ: **ยังไม่มีบันทึก**
- ชุดข้อมูลหลายมุมมองที่ตรวจสอบสิทธิ์แล้ว: **ยังไม่มีบันทึก**
- โมเดลรวมภาพหลายกล้องที่ฝึกและทดสอบอิสระ: **ยังไม่มีบันทึก**
- การตรวจสอบกับฮาร์ดแวร์จริง: **ยังไม่มีบันทึก**

เอกสารนี้เป็นข้อกำหนดสำหรับการวิจัย ไม่ใช่หลักฐานว่าผลิตภัณฑ์ PUI89 มีระบบรับรู้ 360 องศาที่ทำงานได้จริงแล้ว
