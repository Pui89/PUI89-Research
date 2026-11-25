# 03 — AI HOME: End-to-End Research Plan

**Working study title:** Evidence-grounded perception and human-aware navigation for a compact indoor mobile assistant.  
**Status:** Proposed research; physical robot capability and safety are not established by this plan.

## 1. Research question

How do perception reliability, uncertainty handling and environment-aware navigation affect task success and safe clearance in indoor spaces with people, furniture and changing layouts? Focus on a compact four-wheel indoor assistant; distinguish it from outdoor AI NOMAD. The current design target is approximately 8 kg payload with a 10 kg maximum target, not a validated specification.

## 2. Literature and lecturer review

Review indoor mobile robotics, SLAM/localisation, dynamic obstacle avoidance, human-aware navigation, assistive robotics, uncertainty-aware planning, safety metrics and sim-to-real evaluation. Compare sensors, robot footprint, speed, test environments and human participation. Obtain robotics, HRI and safety-engineering review before physical trials.

## 3. Data and scenarios

Create a scenario matrix for rooms, corridors, doorways, furniture, floor surfaces, reflective/glass surfaces, lighting, clutter, moving people and sensor dropouts. Use permissioned indoor datasets or controlled recordings with privacy notices/consent and de-identification. Synthetic simulation data must be labelled separately. Avoid collecting unnecessary identifiable human data.

## 4. Annotation and ground truth

Record traversable regions, static/dynamic obstacles, people as anonymous detections where needed, robot pose, map, route, minimum clearance, interventions and trial outcome. Establish ground truth using calibrated measurement or a documented reference system. Version scenario definitions and bilingual instructions.

## 5. Splits and leakage control

Group by physical site/layout, route, trial session and recording device. Keep the same room/map or near-identical simulation seeds out of both train and test when claiming unseen-layout generalisation. Use held-out layouts and, if feasible, a separately operated site. Do not split adjacent video frames randomly.

## 6. Methods and baselines

Compare a conventional geometric navigation baseline, standard perception-plus-planner, fixed-threshold obstacle policy and proposed uncertainty-aware perception/planning. Candidate ROS 2/Nav2, SLAM and simulation frameworks require provenance/licence/resource checks before adoption. Treat VLM/VLA outputs as advisory research signals, not trusted low-level control.

## 7. Experiments

- E1: mapping/localisation baseline and sensor calibration.
- E2: static obstacle navigation across held-out layouts.
- E3: dynamic people/obstacle scenarios under approved controlled conditions.
- E4: uncertainty, occlusion, reflective surface and sensor dropout ablations.
- E5: recovery and safe-stop/fallback tests.
- E6: simulation-to-physical comparison, reported as separate evidence strata.
- E7: resource benchmark on the intended CPU/GPU/NPU hardware.

Primary outcomes: task success rate and intervention rate on predeclared scenarios. Secondary outcomes: collision/contact and near-miss counts, minimum clearance, path length, time-to-goal, localisation error, recovery rate, latency, peak memory and energy if directly measured. Define what counts as contact, near miss and intervention before testing.

## 8. Statistical plan

Use repeated trials across independent layouts and scenario seeds. Account for clustering by layout and trial operator. Report confidence intervals and distributions, not just averages. For rare safety events, report exposure counts and uncertainty; absence of a collision in a small number of trials does not prove safety.

## 9. Shared AI Core integration

Observation represents sensor/map observations with calibration and freshness. WorldState carries pose, obstacles, free-space estimates and uncertainty. ActionProposal contains a candidate navigation intent with preconditions, risk and human approval; execution remains false in research adapters. FailureReport captures localisation loss, collision, near miss, sensor dropout and unsafe proposal. Evidence Passport links claims to scenario and trial records.

## 10. Thai edition and HRI

Provide Thai voice/text prompts only if the relevant interface is in scope; evaluate Thai ASR/NLU/TTS separately if used. Include Thai participant materials, consent, safety instructions and reviewer explanations. Do not claim language support without user testing.

## 11. Safety and risk

Physical tests require a documented risk assessment, low-speed controlled environment, emergency stop, safety observer, exclusion zones, secured payload and approved procedures. No unsupervised operation around vulnerable people. Simulation is not physical safety evidence.

## 12. Deliverables and gates

Literature map; scenario protocol; privacy/ethics review; bilingual annotation and participant material; site-grouped dataset; baseline and planner configs; safety/fault test reports; statistical analysis; model card; Core adapter conformance evidence; manuscript. Pass G0–G9 only with actual evidence, including independent layout testing and approved physical trials where claimed.
