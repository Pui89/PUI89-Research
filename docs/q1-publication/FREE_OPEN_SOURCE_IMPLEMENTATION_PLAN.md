# Free/Open-Source Implementation Plan for Six Independent Q1 Studies

**Status:** implementation blueprint and lightweight research utilities; not evidence of trained models, completed experiments or product deployment.  
**Scope:** six independent papers, one per active product. Sentinel remains included. Extreme Flood Rescue AI is outside this six-study scope.

## 1. Operating rules

- Prefer locally runnable, open-source software and public datasets with explicit research-use rights.
- No paid API, hosted inference, metered service, paid cloud GPU or subscription dependency.
- CPU-first baselines; GPU/NPU are optional comparison arms only when hardware already exists.
- Do not download weights, install packages, or connect physical sensors/robots without separate approval.
- Verify code licence, model-weight licence, dataset licence, upstream lineage, dependency licence and commercial-use restrictions separately. "Open source" code does not automatically make weights or datasets open.
- Pin commit, release, model revision, preprocessing, random seed, split manifest and environment record.
- Keep simulated, offline replay, bench and physical results in separate result strata.
- Preserve negative results, failure cases, unknowns and abstentions.

## 2. Recommended shared research stack

| Layer | First-choice open-source tools | Why / boundary |
|---|---|---|
| Core ML | Python, PyTorch, torchvision, scikit-learn | Reproducible CPU-capable baselines and classical statistical comparators |
| Data and annotation | CSV/JSON manifests, CVAT Community, FiftyOne | Human-reviewed labels, dataset inspection and export; self-host only |
| Vision / geometry | OpenCV, Open3D, SAM 2 as an optional annotation/segmentation comparator | Use only where task and exact model/weight terms pass review |
| Model interoperability | ONNX, ONNX Runtime CPU | Portable inference and a common runtime comparison |
| Edge optimisation | OpenVINO CPU first; ONNX Runtime execution providers where supported | Compare precision, latency and memory on the same hardware |
| Experiment tracking | Local MLflow or versioned JSON/CSV records | No hosted tracking service required |
| Robotics / simulation | ROS 2 + Gazebo for robot workflows; MuJoCo for dynamics; CARLA/SUMO for road scenes | Use only for the specific study that needs it; simulation is not field validation |
| Statistical analysis | SciPy, statsmodels, scikit-learn; bootstrap confidence intervals | Pre-register primary endpoints and analysis choices |
| Integrity / reproducibility | SHA-256 manifests, Git commit pins, environment lock files, Python standard-library audit tools | Detect leakage and make experiments traceable |

Official project references:
- PyTorch: https://github.com/pytorch/pytorch
- ONNX Runtime: https://github.com/microsoft/onnxruntime
- OpenVINO: https://github.com/openvinotoolkit/openvino
- SAM 2: https://github.com/facebookresearch/sam2
- Open3D: https://github.com/isl-org/Open3D
- CVAT: https://github.com/cvat-ai/cvat
- ROS 2: https://github.com/ros2/ros2
- Gazebo: https://github.com/gazebosim/gz-sim
- MuJoCo: https://github.com/google-deepmind/mujoco
- CARLA: https://github.com/carla-simulator/carla
- MLflow: https://github.com/mlflow/mlflow

The repositories above are starting points, not blanket approval. Audit exact version, transitive dependencies, weights, dataset and simulator assets before adoption. For example, OpenVINO describes itself as an open-source inference toolkit; ONNX Runtime's repository states MIT licensing; SAM 2's code repository states Apache-2.0, but every downloaded checkpoint and dataset still needs its own terms checked.

## 3. Six independent Q1 implementation tracks

### Study 1 — Coconut Harvest AI
**Primary question:** Can a resource-aware vision pipeline classify four coconut maturity classes and localise fruit/bunches robustly across unseen orchard sites?

- Labels: young green, mature green, yellow, brown; agronomic label guide and expert adjudication.
- Baselines: colour/texture + classical classifier; MobileNetV3 or ResNet-18 image classifier; a separately selected object detector only after detector choice is formally approved.
- Segmentation: compare manual masks with an optional SAM 2-assisted annotation workflow; human correction remains ground truth.
- Spatial arm: RGB-only vs RGB-D; report metric error only against calibrated measured ground truth.
- Ablations: colour normalisation, segmentation, temporal tracking, depth, orchard/site adaptation, uncertainty threshold.
- Metrics: macro-F1, per-class recall, calibration, abstention coverage, AP/IoU for detection/segmentation, spatial MAE only with metric truth, CPU latency/RAM.
- Split: orchard/tree/session grouped split; no frames from the same capture sequence across train and test.

### Study 2 — PUI89 Sentinel
**Primary question:** Does evidence-aware multimodal event detection improve event recall without increasing false alerts, and how does it behave when sensors are missing or unreliable?

- Scope: general facility/environment/equipment events only; privacy-reviewed and authorised data.
- Baselines: rules/statistical thresholds; Isolation Forest or one-class baseline; modality-specific classifier; late-fusion comparator.
- Ablations: visual-only, each lawful available modality, fused model, sensor-quality gate, missing-modality mask, uncertainty/abstention.
- Metrics: event precision/recall, false alerts per monitored hour, event delay, calibration, missing-modality degradation, human-review agreement.
- No identity/guilt/threat-certainty conclusions; human review is mandatory for consequential decisions.
- Exclude narcotics, X-ray, forensic chemical screening, NIST DART-MS and NIR forensic spectra.

### Study 3 — AI HOME
**Primary question:** Can lightweight indoor perception plus explicit uncertainty and safe-hold logic improve supervised indoor assistance under layout changes and sensor faults?

- Baselines: RGB-only conventional detector; OWLv2 adapter as an open-vocabulary comparator only after weight/licence/resource review; relative-depth arm only as relative geometry.
- Simulation: deterministic 2D grid/graph scenarios first; Gazebo/ROS 2 only if the later robot model and sensor definitions are available.
- Ablations: RGB vs RGB+depth; detector vs open-vocabulary; sensor freshness gate; missing/contradictory observations; safe-hold and manual override.
- Metrics: object/event metrics, route completion in simulation, false-safe/false-hazard cases, fault recovery, latency/RAM.
- Simulation scores must not be described as physical navigation performance.

### Study 4 — AI NOMAD
**Primary question:** How robust is a compact supervised outdoor assistant's perception and navigation proposal under terrain variation, occlusion and sensor dropout?

- Baselines: RGB detector/tracker; OWLv2 adapter comparator after approval; relative-depth comparator; classical geometry where depth sensors exist.
- Simulation: synthetic route/terrain grid first; Gazebo or MuJoCo only for a defined robot/sensor model.
- Ablations: RGB vs RGB-D, terrain cues, temporal tracking, sensor-health gate, missing modality, uncertainty/abstention.
- Metrics: terrain-stratified object/event recall, route-proposal success in simulation, localisation drift where ground truth exists, false-safe/false-hazard outcomes.
- No unsupervised public-space autonomy claim; physical intervention metrics require an approved trial protocol.

### Study 5 — AI Robot Car
**Primary question:** Does multi-camera evidence fusion improve road-user/hazard event awareness over a single-camera baseline, under weather, lighting and camera-coverage limits?

- Baselines: per-camera detector; shared-weight multi-camera late fusion; tracking-assisted event baseline.
- Simulation/data: public road datasets with clear licence and CARLA/SUMO scenarios; keep simulated and real data results separate.
- Ablations: front only, rear only, per-camera, fused cameras, tracking, weather/lighting strata, uncertainty threshold.
- Metrics: per-class AP/mAP, VRU recall, event recall, false alerts per driving hour, warning lead time, calibration, latency and uncovered field-of-view.
- No vehicle actuation, vehicle-bus connection or autonomous driving claim.

### Study 6 — EasyRide AI Step-Through Scooter
**Primary question:** How well do rider-view perception and advisory alerts transfer across rider viewpoints, vibration, road surface and weather, compared with generic/car-view baselines?

- Baselines: rider-view detector; car-view transfer baseline; tracking/event comparator; optional read-only IMU context only if a calibrated interface and lawful data exist.
- Ablations: rider-view vs car-view, front vs rear camera, motion/vibration context, weather, uncertainty/abstention, alert threshold.
- Metrics: hazard-event recall, false alerts per riding hour, warning lead time, calibration, vibration/weather strata, camera blind/uncovered regions and distraction/human-factors outcomes.
- No gaze, fatigue, intoxication, health or fitness-to-ride inference. No autonomous steering, throttle, braking, balance or propulsion.

## 4. Required protocol for every paper

1. Freeze one primary research question, primary endpoint and hypotheses before test-set access.
2. Publish a dataset card, annotation guide, consent/rights record and SHA-256 manifest.
3. Split by the true independent unit (orchard/tree/session, site/time, building/layout, route/vehicle/rider), not random frames.
4. Run a simple reproducible baseline before any complex model.
5. Compare model families on identical splits, preprocessing, hardware and evaluation code.
6. Run one-factor-at-a-time ablations plus justified interaction tests.
7. Report confidence intervals, effect sizes, class-wise results and failure slices; account for repeated measures and clustered samples.
8. Report calibration, uncertainty, abstention and missing-modality robustness.
9. Benchmark batch size 1 and realistic concurrency; record p50/p95 latency, throughput, peak RAM/VRAM, device/driver, thermal state and energy only when directly measured.
10. Keep simulation, offline replay, bench and physical trials separate.
11. Retain failed runs and publish scripts/configuration/seed/environment records where data rights allow.
12. Do not claim Q1 novelty or acceptance until a current literature review and completed, independently reproducible experiments support it.

## 5. Implementation sequence

**Stage A — no model downloads:** implement manifest integrity/leakage audit, experiment metadata schema, split protocol, metric definitions, failure taxonomy and six project configs.

**Stage B — approved public data only:** select datasets after licence/provenance review; annotate a small pilot; establish CPU baselines.

**Stage C — controlled comparison:** run model comparisons, ablations, robustness and uncertainty evaluation; log all resource measurements.

**Stage D — simulation:** only add a simulator where it directly answers the paper's research question; pin simulator and asset versions.

**Stage E — physical validation:** separate approval, safety/risk review, calibrated hardware and independent test protocol required.

No package installation, model-weight download, sensor connection, physical trial, paid service or default-branch merge is part of this plan.
