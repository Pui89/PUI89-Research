# 360-Degree Perception Validation and Benchmark Protocol

**Version:** 1.0  
**Record date:** 25 November 2026  
**Status:** Proposed protocol template. No product has passed these validation gates unless a dated experiment record and retained evidence demonstrate it.

## 1. Purpose and relationship to existing research documents

This protocol operationalises the 360-degree architecture in the [Technology Baseline & Model Map](TECHNOLOGY_BASELINE_AND_MODEL_MAP.md). It defines how to measure sensor coverage, calibration, perception quality, fusion benefit, robustness, uncertainty, failure handling and edge-resource performance across all six PUI89 projects.

Use this document together with:
- [End-to-End Research Plans — All Six Projects](end-to-end/README.md)
- [Global Real-World Image & Dataset Protocol](GLOBAL_IMAGE_DATA_AND_TRAIN_TEST_PROTOCOL.md)
- [Manuscript and Statistical Standard](MANUSCRIPT_AND_STATISTICAL_STANDARD.md)
- [Shared AI Core Integration](SHARED_AI_CORE_INTEGRATION.md)

This is not a hardware bill of materials, a safety certification, or evidence that any PUI89 product already provides working 360-degree perception.

## 2. Validation principles

1. **Measure coverage, do not infer it from camera count.** A multi-camera platform is not automatically 360-degree capable.
2. **Represent unknown space honestly.** Distinguish observed-free, occupied, occluded, out-of-range, invalid and unobserved regions.
3. **Evaluate each sensor before fusion.** Fusion must demonstrate measurable benefit over single-sensor baselines.
4. **Synchronise and calibrate before spatial claims.** Uncalibrated or time-misaligned observations cannot support reliable geometric fusion claims.
5. **Keep independent groups independent.** All views and frames from one physical event/session remain in one dataset partition.
6. **Test degraded operation.** Sensor loss, obstruction, drift and disagreement must be detected and handled explicitly.
7. **Pre-register primary endpoints.** Set acceptance criteria and analysis before unlocking the final test set; do not invent universal thresholds after seeing results.
8. **Separate evidence classes.** Simulation, public benchmarks, controlled lab tests and field trials are reported separately.
9. **Retain negative results.** A failed gate is a research finding, not a reason to silently omit the condition.
10. **No automatic actuation.** The six research plans do not authorise direct steering, throttle, braking or unsupervised robot motion.

## 3. Validation layers and required evidence

| Layer | Required measurements | Evidence artefact |
|---|---|---|
| L0 — Requirements | Operating envelope, task, required directions/ranges, hazards, platform and safety boundary | Versioned requirements and risk register |
| L1 — Physical coverage | Azimuth/elevation, range bands, overlap, occlusion, blind/unobserved regions, mounting constraints | Measured coverage map and test photographs/geometry |
| L2 — Calibration | Intrinsic/extrinsic parameters, reprojection/geometric residuals, coordinate transforms, timestamp offset/drift | Calibration report, calibration files and acceptance decision |
| L3 — Sensor health | Frame loss, dropped packets, stale data, exposure/blur, obstruction, thermal/power status where measurable | Sensor health and fault log |
| L4 — Per-sensor perception | Per-camera/per-modality detection, segmentation, tracking or task-specific output | Per-sensor evaluation report |
| L5 — Fusion | Association accuracy, duplicate suppression, spatial consistency, fusion gain and conflict handling | Single-sensor versus fusion comparison |
| L6 — World model | State freshness, occupancy/unknown handling, track continuity, uncertainty and provenance | WorldState conformance and scenario report |
| L7 — Degraded mode | Fault detection, abstention, safe hold/warning, recovery and false-safe outcomes | Fault-injection matrix and failure reports |
| L8 — Deployment | Latency distribution, throughput, RAM/VRAM, CPU/GPU/NPU use, energy and thermal conditions | Reproducible hardware benchmark |
| L9 — Independent validation | Locked test, external site/route where feasible, independent review and limitations | Signed evaluation report and Evidence Passport |

A gate passes only if its acceptance criteria were defined in advance, evidence is retained, and a reviewer records the decision. Missing evidence means **not evaluated**, not pass.

## 4. Coverage and calibration measurement

### 4.1 Coverage map

For every sensor, record:
- sensor identifier, modality, lens/FOV, resolution, frame rate and mounting pose;
- platform coordinate frame and transformation version;
- measured horizontal and vertical field of view;
- validated near/far range by target size and operating condition;
- overlap with adjacent sensors;
- blind, occluded, out-of-range and invalid regions;
- performance by lighting, weather, vibration and platform configuration.

Report angular coverage by azimuth/elevation bins and by defined range bands. State the target visibility criterion used for each bin. Do not count a direction as covered merely because it lies inside a nominal lens field of view; target visibility and usable image quality must be tested. Coverage is task-specific and can vary with target size, contrast, lighting, distance and occlusion.

### 4.2 Calibration

For cameras, report intrinsic calibration, distortion model, reprojection residual distribution and calibration target/procedure. For multi-sensor geometry, report extrinsic transform method, coordinate-frame convention, residuals against independent reference measurements and calibration date/version.

For synchronisation, measure timestamp offset, drift and frame-arrival jitter under load. Define maximum acceptable errors from the task's spatial/temporal error budget before testing. Do not copy a universal tolerance across a stationary orchard camera, indoor robot, outdoor robot, car and scooter.

Repeat checks after mounting changes, impacts, vibration, repair, temperature changes or any observed calibration degradation. Calibration data must be versioned and linked to every experiment.

## 5. Perception and fusion benchmark design

Run at least these comparisons where supported by the available sensors and task:
- **B0:** simple task-specific non-learning or rule-based reference;
- **B1:** each sensor/view independently;
- **B2:** strongest relevant single-view model;
- **B3:** late fusion of independently generated predictions;
- **B4:** geometry/state-aware fusion;
- **B5:** proposed uncertainty-aware method with explicit unknown/abstention;
- **B6:** degraded/faulted sensor configuration.

Use matched training data, evaluation splits, tuning budgets and hardware where possible. If a baseline cannot be run fairly, explain why. A fusion method is not better merely because it uses more cameras or parameters.

### 5.1 Metrics

Select task-appropriate metrics and predeclare primary/secondary outcomes.

- **Detection:** per-class precision, recall, AP/mAP, false positives and false negatives.
- **Segmentation:** IoU/Dice and boundary quality where relevant.
- **Tracking:** HOTA, IDF1 or a justified alternative; ID switches, fragmentation and cross-view association errors.
- **Geometry:** position/depth error against independent ground truth; calibration residual and uncertainty coverage.
- **Events/hazards:** event recall, precision, false alerts per operating hour, missed events and warning/detection delay.
- **Fusion:** incremental performance versus the best single sensor, duplicate rate, association errors, conflict rate and performance when one sensor is absent.
- **Coverage:** validated angular/range coverage and target visibility by condition; blind-zone detection rate.
- **Reliability:** calibration error, uncertainty quality, abstention coverage, false-safe rate, stale-data rate, fault-detection delay and recovery time.
- **Compute:** p50/p95/p99 latency where sample size permits, throughput, peak RAM/VRAM, CPU/GPU/NPU utilisation, energy and thermal throttling.

Always include per-class and per-condition breakdowns. Aggregate scores alone can conceal critical blind zones or rare-class failures.

## 6. Fault-injection and robustness matrix

Test only faults relevant to the actual system and record the injection method and severity.

| Fault/condition | What to measure | Expected system response to verify |
|---|---|---|
| Camera blocked/covered | Detection of degraded view, coverage loss | Mark region unknown; no false free-space assertion |
| Camera disconnected/black frame | Fault detection delay and stale-data handling | Isolate failed stream and report reduced coverage |
| Timestamp offset/drift | Synchronisation error and fusion degradation | Reject or down-weight invalidly aligned observations |
| Calibration perturbation | Geometric residual and inconsistency detection | Flag calibration invalid; prevent unsupported spatial claims |
| Glare/low light/rain/dust | Per-condition performance and uncertainty | Calibrated degradation/abstention, not false confidence |
| Motion blur/vibration | Detection/tracking degradation | Report uncertainty and recovery |
| Dropped frames/latency spike | Freshness and temporal tracking | Expire stale state; issue bounded degraded status |
| Overlapping duplicate views | Duplicate and association errors | Avoid double-counting the same entity/event |
| Conflicting sensors | Conflict detection and resolution | Preserve conflict/uncertainty; do not hide disagreement |
| Out-of-distribution scene | OOD detection and abstention quality | Mark unsupported condition and request human review as appropriate |
| Power/thermal constraint | Throughput, latency and thermal state | Enter documented resource-degraded mode |

For every fault, report detection rate, time to detect, false alarm rate, recovery time, residual risk and whether the response itself failed. Never use only a successful nominal demonstration.

## 7. Six-project benchmark matrix

| Project | Ground-truth priority | Independent test grouping | Primary evaluation focus |
|---|---|---|---|
| Coconut Harvest AI | Expert-confirmed maturity class for each fruit/bunch; fruit identity and location only where measured | Orchard, tree, harvest session, camera and date/season | Four maturity classes; per-view/fused classification or detection; canopy occlusion; duplicate bunches; distance/position error only with valid reference |
| PUI89 Sentinel | Approved event definitions and independently adjudicated event intervals | Facility/site, camera zone, recording session and time | Event-level recall, false alerts per monitored hour, cross-camera association, privacy masking, evidence provenance and missing-stream handling; excluded narcotics/X-ray/forensic scope stays excluded |
| AI HOME | Measured obstacle/person/doorway/drop-off annotations and safe-navigation outcomes under an approved protocol | Building, room/layout, trial and session | Near-field blind zones, dynamic obstacle/person awareness, drop-off detection, safe-stop/abstention and intervention rate |
| AI NOMAD | Terrain/traversability labels checked against documented expert or physical reference | Outdoor site, route, terrain segment and trial | Terrain/weather generalisation, near-field coverage, traversability error, false-safe rate, sensor contamination and degraded operation |
| AI Robot Car | Road-user/hazard labels and event timing; geometry only with calibrated reference | Entire drive, route, vehicle, camera setup and geography | Vulnerable-road-user/hazard event recall, false alerts per driving hour, warning delay, view/fusion gain and route/weather generalisation; no autonomous actuation |
| EasyRide Scooter | Rider-view road-user/hazard labels and event timing; mount/vibration metadata | Rider, ride, route, vehicle, mount and recording session | Rider-view versus car-view transfer, blind-zone coverage, vibration/lean/weather robustness, false alerts per riding hour and warning delay; no autonomous actuation |

Do not force identical labels or a single primary metric across all six projects. Each project requires its own validated ground-truth protocol and research question.

## 8. Ground truth, sampling and statistics

- Define the unit of analysis before collection: fruit/bunch, event, room trial, terrain segment, drive/ride event or tracked entity as appropriate.
- Record who or what establishes ground truth, the instrument/procedure, uncertainty, annotation version and adjudication process.
- Use independent annotators on a predeclared subset; report suitable agreement statistics and disagreements.
- Group splits at the level where dependence/leakage occurs. Never split adjacent frames or synchronized camera views from one event across train and test.
- Use site/route/orchard/building/rider-held-out evaluation when claiming generalisation to unseen environments.
- Determine sample size from the primary endpoint, expected prevalence, desired precision/power, clustering and feasibility. Do not select a convenient sample count and call it sufficient.
- Report confidence intervals and effect sizes. Use cluster-aware bootstrap or an appropriate hierarchical/paired method where the data structure requires it.
- For rare hazards/events, report event counts and uncertainty; do not hide the small denominator.
- Lock the final test set and analysis plan before evaluation. Mark any post-hoc analysis as exploratory.
- Report exclusions, missing labels, class imbalance, domain shift, negative results and protocol deviations.

## 9. Edge and heterogeneous-compute benchmark

Evaluate only on hardware actually available and approved. Record exact device/CPU/GPU/NPU/MCU, RAM, operating system, runtime, model hash, precision/quantisation, input resolution, number of active streams and thermal/power conditions.

Measure:
- cold-start and steady-state latency separately;
- end-to-end capture-to-result latency, not just model-forward time;
- p50/p95/p99 latency where enough samples exist;
- throughput and dropped-frame rate for concurrent streams;
- peak memory and sustained memory;
- CPU/GPU/NPU utilisation and fallback transitions;
- power/energy only with a documented meter and measurement boundary;
- thermal throttling and performance after sustained operation.

Compare CPU-only and heterogeneous scheduling with matched model outputs and accuracy constraints. A faster result is not useful if it increases missed hazards or produces stale world state. No paid cloud/GPU/API or automatic downloads are required by this protocol.

## 10. Shared AI Core conformance and evidence traceability

Every test case should map to the versioned contracts:
- **Observation:** sensor ID, modality, timestamp, calibration, health, provenance and quality.
- **WorldState:** coordinate frame, entities/tracks, observed/free/occupied/unknown regions, uncertainty, freshness and source references.
- **ActionProposal:** advisory warning/recommendation, evidence references, preconditions, expiry and abstention reason; no direct actuation.
- **FailureReport:** sensor/model faults, missed/false events, calibration drift, stale data, degraded mode and recovery.
- **Evidence Passport:** dataset/split hash, model/code/configuration hash, calibration version, hardware, experiment record, metrics, failures, reviewer and claim link.

Run schema validation and deterministic fixture tests before model evaluation. A schema passing does not prove perception quality or runtime integration.

## 11. Gate and decision record

| Gate | Pass evidence | If not passed |
|---|---|---|
| V0 Requirements frozen | Approved task, operating envelope, primary endpoint and safety boundary | Return to scope definition |
| V1 Coverage measured | Per-sensor coverage map with blind/unknown regions | Redesign or narrow claimed envelope |
| V2 Calibration accepted | Calibration and synchronisation report meets predeclared task tolerances | Recalibrate or block fusion |
| V3 Ground truth ready | Rights/ethics cleared data and reviewed labels | Block model training/evaluation |
| V4 Baselines reproducible | Single-sensor and relevant reference baselines reproduced | Resolve protocol/environment issues |
| V5 Fusion benefit demonstrated | Predeclared comparison supports meaningful improvement without unacceptable regressions | Retain simpler baseline or revise hypothesis |
| V6 Robustness demonstrated | Fault and subgroup results meet predeclared criteria | Restrict operating envelope or redesign fallback |
| V7 Edge constraints met | Measured sustained performance on named hardware | Resize/schedule model or state limitation |
| V8 Independent review complete | Reproducibility, safety, statistics and domain review recorded | Address findings before manuscript claims |

Record gate, date, reviewer, evidence links, deviations, decision and next action. “Not evaluated” is a valid status; it must not be represented as pass/fail.

## 12. Current status

As of 25 November 2026, this protocol is a proposed research standard. The following are **not established by authoring this document**: measured per-product coverage maps, accepted calibration tolerances, rights-cleared synchronized multi-view corpora, completed ground truth, baseline/fusion benchmark results, fault-injection results, sustained edge benchmarks or passed validation gates.

---

## 13. ภาษาไทย — แนวทางตรวจสอบและประเมินผลระบบรับรู้รอบทิศทาง 360 องศา

**สถานะ:** เป็นกรอบระเบียบวิธีวิจัย ไม่ใช่ผลการทดสอบผลิตภัณฑ์จริง

### 13.1 หลักการ

1. ต้องวัดพื้นที่ครอบคลุมจริง ไม่ใช้จำนวนกล้องเป็นหลักฐานแทน
2. แยกพื้นที่ที่มองเห็น พื้นที่ว่าง พื้นที่มีวัตถุ พื้นที่ถูกบัง และพื้นที่ไม่ทราบให้ชัดเจน
3. ประเมินแต่ละกล้อง/เซนเซอร์ก่อนรวมข้อมูล และพิสูจน์ว่าการรวมข้อมูลให้ประโยชน์จริง
4. ต้องปรับเทียบตำแหน่งและเวลาให้เหมาะสมก่อนอ้างผลด้านมิติหรือระยะทาง
5. ภาพจากเหตุการณ์หรือรอบบันทึกเดียวกันต้องอยู่ในชุดข้อมูลเดียวกัน เพื่อป้องกัน Data Leakage
6. ทดสอบกรณีเซนเซอร์ขัดข้อง กล้องถูกบัง เวลาเหลื่อม และข้อมูลขัดแย้ง
7. กำหนดตัวชี้วัดหลักและเกณฑ์ผ่านก่อนเปิดชุดทดสอบสุดท้าย
8. แยกผล Simulation, Public Dataset, ห้องทดลอง และการทดสอบภาคสนาม
9. เก็บผลลบและกรณีล้มเหลวไว้ในรายงาน
10. แผนวิจัยนี้ไม่อนุญาตให้ควบคุมพวงมาลัย คันเร่ง เบรก หรือการเคลื่อนที่ของหุ่นยนต์โดยตรง

### 13.2 ขั้นตอนการตรวจสอบ

| ขั้นตอน | สิ่งที่ต้องวัด/ตรวจสอบ | หลักฐาน |
|---|---|---|
| V0 ข้อกำหนด | งาน สภาพแวดล้อม ระยะ มุม และขอบเขตความปลอดภัย | เอกสารข้อกำหนด |
| V1 พื้นที่ครอบคลุม | มุมมอง ระยะ พื้นที่ซ้อนทับ จุดบอดและสิ่งบดบัง | แผนที่ Coverage |
| V2 Calibration | ค่าปรับเทียบ ความคลาดเคลื่อน และการซิงโครไนซ์เวลา | Calibration Report |
| V3 Ground Truth | สิทธิ์ข้อมูล จริยธรรม และคุณภาพป้ายกำกับ | Dataset/Annotation Record |
| V4 Baseline | ผลโมเดลแยกกล้องและวิธีพื้นฐาน | Baseline Report |
| V5 Sensor Fusion | เปรียบเทียบผลรวมข้อมูลกับกล้องเดี่ยว | Fusion Benchmark |
| V6 Robustness | ฝน แสงน้อย กล้องเสีย การสั่น และข้อมูลขัดแย้ง | Fault Test Report |
| V7 Edge AI | เวลา หน่วยความจำ พลังงาน และอุณหภูมิบนฮาร์ดแวร์จริง | Hardware Benchmark |
| V8 Independent Review | ตรวจสอบโดยผู้เชี่ยวชาญและอาจารย์ | Review Record |

### 13.3 จุดเน้นเฉพาะโครงการ

- **Coconut Harvest AI:** ความถูกต้องของ 4 ระดับความสุก การบดบังจากใบ/กิ่ง และการนับผลหรือทะลายซ้ำ
- **PUI89 Sentinel:** ความแม่นยำระดับเหตุการณ์ อัตราแจ้งเตือนผิดพลาด ความเป็นส่วนตัว และการเชื่อมโยงหลักฐาน โดยไม่รวมขอบเขตยาเสพติด/X-ray/นิติวิทยาศาสตร์ที่ยกเว้น
- **AI HOME:** จุดบอดระยะใกล้ คน เฟอร์นิเจอร์ ประตู ขอบต่างระดับ และการหยุดอย่างปลอดภัย
- **AI NOMAD:** ภูมิประเทศ สภาพอากาศ สิ่งกีดขวาง การประเมินทางผ่าน และการทำงานเมื่อเซนเซอร์สกปรกหรือขัดข้อง
- **AI Robot Car:** ผู้ใช้ถนน อันตราย การแจ้งเตือน และการทดสอบแยกเส้นทาง/สภาพอากาศ โดยไม่ควบคุมรถอัตโนมัติ
- **EasyRide Scooter:** มุมมองผู้ขับขี่สองล้อ จุดบอด การสั่น การเอียง สภาพถนน และการแจ้งเตือน โดยไม่ควบคุมคันเร่ง/พวงมาลัย/เบรก

### 13.4 ตัวชี้วัด

เลือกใช้ Precision, Recall, AP/mAP, IoU/Dice, HOTA/IDF1, ความคลาดเคลื่อนด้านระยะ/ตำแหน่ง, Event Recall, False Alerts ต่อชั่วโมง, Detection Delay, Calibration Error, Abstention, Fault Detection และ p50/p95/p99 Latency ตามความเหมาะสมของงาน ต้องรายงานผลแยกตามกล้อง มุม ระยะ คลาส และสภาพแวดล้อม ไม่รายงานเฉพาะค่าเฉลี่ยรวม

### 13.5 เกณฑ์ความถูกต้องของงานวิจัย

- กำหนด Ground Truth และหน่วยวิเคราะห์ก่อนเก็บข้อมูล
- ใช้ผู้ตรวจ Annotation อิสระและรายงานความสอดคล้อง
- แบ่งข้อมูลตามสวน อาคาร สถานที่ เส้นทาง ผู้ขับขี่ และรอบบันทึกตามความเสี่ยง Data Leakage
- กำหนดขนาดตัวอย่างจากตัวชี้วัดหลัก ความแปรปรวน และการจัดกลุ่มข้อมูล
- รายงาน Confidence Interval, Effect Size, ข้อผิดพลาด และผลลบ
- ล็อกชุดทดสอบก่อนประเมินผลขั้นสุดท้าย
- หากไม่มีหลักฐาน ให้ระบุว่า “ยังไม่ได้ประเมิน” ไม่ใช่ “ผ่าน”

### 13.6 สถานะ

เอกสารนี้ยังไม่ใช่หลักฐานว่ามีแผนที่ 360 องศาที่ผ่านการวัด ชุดข้อมูลหลายกล้องที่ผ่านการตรวจสอบ โมเดล Sensor Fusion ที่ผ่านการทดสอบ หรือผล Benchmark บนฮาร์ดแวร์จริงแล้ว
