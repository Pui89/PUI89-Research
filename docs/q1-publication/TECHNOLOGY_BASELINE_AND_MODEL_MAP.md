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
