# 01 — Coconut Harvest AI: End-to-End Research Plan

**Working study title:** Leakage-resistant, uncertainty-aware coconut maturity assessment from orchard imagery under field variation.  
**Status:** Proposed protocol; literature gap, ground truth, data rights and experiments require approval.

## 1. Purpose and research question

Determine whether a computer-vision system can distinguish four operational maturity classes across independent orchards, trees, seasons, camera types and lighting conditions. Classes: young green, mature green, yellow and brown. Define maturity biologically and operationally with an agronomy/plant-science expert; visual appearance alone may not establish ground truth for borderline fruit.

**Primary question:** How well does a frozen image model generalise to previously unseen trees/orchards and capture sessions, compared with transparent and strong lightweight baselines?

**Hypothesis to test:** A model trained with orchard-aware sampling, calibrated uncertainty and abstention may improve reliable class-wise performance under site shift versus a conventional classifier. This is not a result or novelty claim.

## 2. Literature and lecturer review

Search recent peer-reviewed work on coconut maturity grading, fruit maturity classification, orchard object detection, colour/illumination robustness, domain adaptation, calibration, selective classification and edge inference. Record databases, exact queries, dates, inclusion/exclusion criteria and DOI. Compare species/cultivar, labels, capture geometry, split method, ground truth, external validation and compute. Ask a lecturer with horticulture/agronomy expertise and a computer-vision researcher to challenge the maturity definitions, sampling design and novelty statement.

**Gap acceptance:** only retain a gap if the literature map shows that existing studies do not already answer the same question under comparable data and evaluation.

## 3. Data acquisition — real images worldwide

Build a source register for coconut-producing regions and climates, prioritising permission-based orchard partnerships, agricultural institutions, public datasets with verified licences and direct contributor consent. Target variation in cultivar (where known), orchard/site, season, tree age where relevant, fruit position, bunch, distance, viewpoint, camera, shade, backlight, glare, rain and occlusion. Do not claim global representation until the country/site inventory proves it.

For every image/video: immutable asset ID, creator/source, original URL or consent record, access date, licence/permission text, permitted research/publication/redistribution uses, file hash, capture date, country/site at privacy-safe precision, orchard/tree/bunch/session group, camera, weather/light, cultivar if known and exclusion reason. Public visibility does not equal training or publication permission.

## 4. Ground truth and annotation

Create a bilingual EN/TH annotation manual with visual criteria, maturity reference examples, borderline rules and an “uncertain/ungradable” option. Have qualified horticulture/agronomy reviewers define or validate the maturity ground truth; record whether independent destructive/chemical/physiological measures are available. Use at least two trained annotators on a justified subset, blinded where practical; adjudicate disagreements and report appropriate agreement and class-wise disagreement. Preserve original labels and adjudication history.

Annotate fruit/bunch boxes or masks only if localisation is part of the stated question. Do not silently mix fruit-level and bunch-level labels.

## 5. Dataset design and leakage prevention

Group by orchard/site, tree, bunch and capture session; near-duplicates and video frames remain together. Train/validation/test splits must not share trees or capture sessions. Prefer a site/orchard-held-out test for generalisation. Seal the final test manifest and record hashes. Stratify reporting by maturity class, site, season, camera and lighting. Determine sample size using expected class prevalence, clustering and precision/power calculations; do not choose a convenient image count.

## 6. Models and baselines

Start with class-prior/majority baseline, colour-space and texture features with a conventional classifier, a small CNN and a compact pretrained image model whose provenance/licence/resource profile is cleared. Detection/segmentation is a separate task if fruit localisation is required. Candidate models are not selected until exact upstream revisions, origin, licence and hardware fit are reviewed. Compare matched input resolution, training data and tuning budget. CPU-first inference is the reference deployment constraint.

## 7. Experiment matrix

- E1: label and dataset audit; class distribution and inter-annotator agreement.
- E2: baseline comparison on frozen grouped splits.
- E3: illumination/weather/camera/site subgroup evaluation.
- E4: calibration and selective prediction; report risk-versus-coverage and abstention.
- E5: ablations for augmentation, image resolution, class weighting and uncertainty method.
- E6: external orchard/site evaluation where rights and sample size allow.
- E7: CPU/edge benchmark: latency distribution, throughput, peak RAM, model size and energy only when measured with a documented power boundary.

Predefine one primary endpoint (recommended: macro-F1 or balanced accuracy on the held-out orchard test) and secondary metrics: per-class precision/recall, confusion matrix, calibration, abstention coverage and resource metrics. Do not choose the endpoint after viewing test results.

## 8. Statistics and reporting

Report confidence intervals using resampling that respects orchard/tree clusters. Include class-wise estimates, effect sizes against baselines, error examples and missing strata. If comparing models, predefine paired comparisons and multiplicity handling. Report all planned experiments, including negative findings. Avoid treating individual images from one tree as independent observations.

## 9. Shared AI Core and PUI89 model artefact

Map each image/annotation inference to Observation with provenance, timestamp, modality and uncertainty; represent time-bounded orchard estimates in WorldState; use ActionProposal only for advisory harvest-readiness recommendations with human confirmation required; record misclassification and sensor/data faults in FailureReport; link paper claims to Evidence Passports. A PUI89 model candidate needs code/config, training-data manifest, source rights, exact base lineage, weights hash, licence, model card, frozen evaluation and review before registry eligibility. No autonomous harvesting action is authorised.

## 10. Thai edition and knowledge transfer

Publish Thai/English annotation guides, agronomy terminology, data collection instructions, result explanations and lecture slides. Thai language model metrics are not applicable to a pure visual classifier, but Thai label quality, interface text, units and expert agreement must be evaluated. Include Thai orchard contributors and regional terminology where feasible.

## 11. Risks and controls

Risks: uncertain maturity ground truth; cultivar/season confounding; orchard leakage; image-rights gaps; class imbalance; domain shift; overclaiming harvest readiness. Controls: expert-defined labels, grouped splits, rights gate, predeclared endpoints, abstention and explicit operating limits. A 0–30 m harvesting capability remains a design challenge unless separately measured and validated; this image study does not prove reach or harvesting performance.

## 12. Deliverables and completion gates

Deliverables: literature evidence map; protocol; bilingual annotation manual; rights-cleared manifest; versioned dataset and split hashes; baseline code/config; experiment records; statistical report; model card; Evidence Passports; manuscript and reproducibility package.

**Exit criteria:** each G0–G9 gate in the [portfolio workflow](README.md) is evidence-backed. Until then, status remains planned/in progress/not recorded, not “validated”.
