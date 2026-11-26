# Coconut Harvest AI — Preliminary Literature Review & Research Gap Matrix

**Version:** 0.1 (scoping review, not systematic review)  
**Review date:** 2026-11-26  
**Status:** Preliminary evidence map; requires database-level search, full-text screening and domain-expert review.  
**Research status:** No PUI89 dataset, annotation, experiment or performance result is claimed in this document.

## 1. Working research direction

**Working question:** How reliably can a lightweight, image-based model distinguish four operational coconut maturity classes — young green, mature green, yellow and brown — when evaluated on genuinely independent trees, capture sessions and orchards, while reporting uncertainty and CPU resource use?

This is a candidate question, not a confirmed research gap. The four PUI89 labels are an operational proposal. They must be mapped to a defensible horticultural maturity reference before data collection. Colour alone must not be treated as ground truth.

### Candidate objectives

1. Define and validate a maturity-label protocol with a coconut domain expert.
2. Compare simple colour/texture and compact CNN baselines under identical data splits.
3. Evaluate generalisation across tree/session/orchard groups rather than random image splits alone.
4. Measure class-wise precision, recall, macro-F1, balanced accuracy, calibration, abstention coverage, CPU latency and peak RAM.
5. Analyse failure cases under illumination change, occlusion, blur, distance and ambiguous maturity.

## 2. Search method and limitations

This version is a **targeted web-based scoping search conducted on 2026-11-26** using combinations of: coconut maturity classification, coconut computer vision, deep learning, maturity ground truth, physical properties, orchard dataset split and leakage prevention.

It is not a PRISMA systematic review. No claim is made that all relevant papers have been found. Publisher pages and abstracts were available for some records; full texts were not available for all. Bibliographic details, methods and reported results must be checked against the publisher's version before manuscript use.

## 3. Preliminary evidence map

| Study | Data/task reported | Method / reported finding | Relevance and limitation for PUI89 |
|---|---|---|---|
| Terdwongworakul et al. (2009), *Biosystems Engineering* 103(2), 208–216. [Publisher/record](https://doi.org/10.1016/j.biosystemseng.2009.03.006) | Fresh young Thai coconuts; physical, mechanical, physiological and acoustic properties | Flesh thickness was strongly related to days after pollination; a multivariate model using physical properties and a non-destructive resonant-frequency model were reported. | Important for ground-truth design: visual colour labels need validation against horticultural/physical criteria. It is not an RGB image-classification benchmark. |
| *Detection of maturity stages of coconuts in complex background using Faster R-CNN model* (2021), *Biosystems Engineering* 202, 119–132. [DOI](https://doi.org/10.1016/j.biosystemseng.2020.12.002) | Farm images; tender/mature coconut bunch detection | Faster R-CNN with ResNet-50 compared with SSD, YOLOv3 and R-FCN. | Establishes prior work in complex farm backgrounds; its two-stage task is not equivalent to PUI89's proposed four-class fruit-level task. |
| Megalingam et al. (2024), *Neural Computing and Applications*. [DOI](https://doi.org/10.1007/s00521-023-09402-2) | 10,000 training images; two test sets (real-time images and cropped images) | Mask R-CNN plus fuzzy colour/shape/scratch features; reported 86.3% real-time accuracy. | Shows multi-feature fusion and multiple maturity classes have been studied. Full label definitions, split independence and transfer conditions need full-text verification. |
| Mandava et al. (2024), *Materials Today: Proceedings* 103, 410–414. [DOI](https://doi.org/10.1016/j.matpr.2023.09.071) | 1,001 images; raw/ripened categories | YOLOv5s, YOLOv4-Tiny and MobileNet-SSD compared; paper notes the dataset is small. | Relevant lightweight detector baselines, but two broad classes do not validate four operational classes or orchard-level generalisation. |
| Perera & Perera (2025), *Asian Journal of Research in Computer Science* 18(9), 76–90. [DOI](https://doi.org/10.9734/ajrcos/2025/v18i9755) | Coconut image classification plus harvest-timeline prediction | Hybrid EfficientNetB0 + DenseNet121 classifier and MobileNetV2 regression; very high accuracy is reported, with dataset-scope limitations acknowledged by the authors. | Demonstrates that classification and timeline prediction are already explored. Reported metrics must not be compared directly across differing datasets/splits. |
| Luthfie & Alamsyah (2025), *Journal of Information System Exploration and Research* 3(2). [DOI](https://doi.org/10.52465/joiser.v3i2.595) | 230 images; young vs mature | CNN and YOLOv8; reported mAP 90.5%, precision 99.3%, recall 94.2%, F1 96.6%. | Small two-class dataset; motivates careful scrutiny of sample independence and external validation. |
| *Coconut Maturity Level Classification using Image Preprocessing and Deep Transfer Learning* (2025 conference; IEEE Xplore record added 2026). [DOI](https://doi.org/10.1109/RIVF68649.2025.11365215) | 3,000 images; young, pre-mature and mature | VGG16 reported 96.17% accuracy; MobileNetV2 and EfficientNet also evaluated. | Three classes and transfer learning are relevant; full split, cultivar and external-site details require verification. |
| *Coconut Bunch Intelligence System* (2026, IEEE conference). [DOI](https://doi.org/10.1109/ICIPRoB69625.2026.11497814) | 3,000 images; four labels (Immature, Mature, Over-mature, Unknown) | MobileNetV2 CNN reported 99.0% accuracy; YOLOv8n used for bunch nut counting. | Directly overlaps four-class image-based maturity classification. PUI89 must establish whether its class definitions, independent split and target population differ meaningfully; this is a major novelty risk. |
| *Tender Coconut Maturity Stage Detection Using YOLOv8-v10...* (2026), *Procedia Computer Science*. [DOI](https://doi.org/10.1016/j.procs.2026.05.062) | 2,121 field images under varying light/occlusion | YOLOv8/9/10 compared; YOLOv10 reported mAP@0.5 of 82%. | Supports field-condition and model-comparison relevance; label scheme and cross-orchard independence need verification. |
| Sailangka et al., KVIS student research project (web record/PDF; non-peer-reviewed evidence). [Project record](https://app.kvis.ac.th/kvis-awards/list.php?code=COMP019) | 150 Nam Hom coconuts; tapping audio | Spectrogram CNN approach reported high accuracy. | Useful Thai cultivar/context lead and a reminder that maturity reference may use tapping; not direct evidence for RGB classification and not a peer-reviewed journal paper. |

## 4. Preliminary research-gap matrix

| Candidate gap | What the initial search indicates | Evidence needed before claiming a gap | Priority |
|---|---|---|---|
| Four PUI89 visual classes with defensible horticultural ground truth | Existing papers use different two-, three- and four-class taxonomies; a 2026 four-label study is already reported. | Compare exact class definitions, cultivar, fruit/bunch unit, harvest use and reference measurements across full texts. | Critical |
| Independent tree/session/orchard evaluation | Several papers report image datasets and accuracy; independence is not clear from abstracts. | Inspect data/split protocols and author supplements; determine whether external orchard testing is absent or insufficient. | Critical |
| Uncertainty, calibration and abstention | Not established by the abstracts screened so far. | Full-text search for calibration, selective prediction, confidence thresholds and human review; search broader agricultural CV literature. | High |
| CPU-first deployment with measured latency/RAM | Lightweight models and edge deployment appear in prior work. | Compare exact hardware, preprocessing, model size, latency distribution and memory protocol. | High |
| Label ambiguity and expert agreement | Maturity is assessed using colour and other physical/acoustic properties; label boundaries vary. | Find cultivar-specific maturity standards and design expert adjudication / inter-rater agreement protocol. | Critical |
| Cross-cultivar, seasonal and illumination robustness | Complex backgrounds and field lighting have been considered in prior studies. | Verify whether tests span independent cultivars, seasons, farms and cameras. | High |

**Preliminary conclusion:** “Coconut maturity classification with deep learning” is not novel by itself. The strongest candidate contribution may be a rigorously grounded, leakage-resistant and uncertainty-aware evaluation under independent orchard conditions, with CPU resource reporting. This is only a hypothesis for further review, not a novelty claim.

## 5. Proposed research protocol — not yet approved or executed

### 5.1 Label and reference design
- Retain the four PUI89 labels only as provisional visual classes.
- Obtain a written label guide from a coconut horticulture expert.
- Define cultivar, intended market/use and maturity reference separately.
- Where feasible and ethically/operationally permitted, pair images with independent reference observations (e.g. days after pollination where known, fruit/flesh measurements, harvest assessment or accepted local grading). Do not destructively sample without owner approval and a documented protocol.
- Include an **uncertain / needs expert review** route; do not force ambiguous fruit into a confident class.

### 5.2 Data provenance and sampling
For each fruit/image record: unique fruit ID; tree/plot/orchard ID; capture-session ID; date/time; cultivar if known; camera/device; distance/viewpoint; lighting/weather notes; provisional label; labeler; reference method; consent/land access; licence/permission evidence; and source-file hash.

Collect multiple views only if the sampling plan records them. All views, crops and derived/augmented versions of one fruit or capture event must remain in the same partition.

### 5.3 Leakage-resistant evaluation
- Split by the true independent sampling unit, initially tree and capture session; reserve an orchard/site for external testing if feasible.
- Perform duplicate and near-duplicate checks before freezing the split.
- Apply augmentation only to training data after splitting.
- Freeze the test manifest and its hash before model selection.
- If only one orchard is available, report that limitation and do not claim cross-orchard generalisation.

### 5.4 Baselines and metrics
- Baselines: majority-class; simple colour/texture features where scientifically appropriate; compact CNN; one compact detector only if object localisation is part of the task.
- Primary metrics: macro-F1 and balanced accuracy, with per-class precision/recall and confusion matrix.
- Secondary metrics: calibration (e.g. Brier score and reliability plot), risk-versus-coverage for abstention, CPU latency distribution, throughput, peak RAM and model size.
- Report confidence intervals and repeated-run variability. Choose one primary endpoint and statistical plan before opening the test set.

## 6. Immediate action register

| ID | Action | Deliverable | Status |
|---|---|---|---|
| COC-LR-01 | Verify bibliographic metadata and obtain/read full texts where lawfully accessible | Reference verification log | Not started |
| COC-LR-02 | Expand search across Scopus/Web of Science/Google Scholar/CAB Abstracts and Thai repositories | Search strings, dates, export and screening log | Not started |
| COC-GAP-01 | Compare maturity taxonomies, cultivars and ground-truth methods | Completed evidence matrix | In progress — preliminary only |
| COC-DATA-01 | Confirm expert reviewer and maturity-label reference | Signed/recorded protocol decision | Blocked — reviewer not confirmed |
| COC-DATA-02 | Confirm orchard access, permissions and sampling unit | Rights and sampling register | Blocked — access not confirmed |
| COC-PROT-01 | Finalise split, metrics and analysis plan | Versioned protocol | Pending expert/data decisions |

## 7. References

1. Terdwongworakul, A., Chaiyapong, S., Jarimopas, B., & Meeklangsaen, W. (2009). Physical properties of fresh young Thai coconut for maturity sorting. *Biosystems Engineering, 103*(2), 208–216. https://doi.org/10.1016/j.biosystemseng.2009.03.006
2. Detection of maturity stages of coconuts in complex background using Faster R-CNN model. (2021). *Biosystems Engineering, 202*, 119–132. https://doi.org/10.1016/j.biosystemseng.2020.12.002
3. Megalingam, R. K., Manoharan, S. K., & Maruthababu, R. B. (2024). Integrated fuzzy and deep learning model for identification of coconut maturity without human intervention. *Neural Computing and Applications*. https://doi.org/10.1007/s00521-023-09402-2
4. Mandava, R. K., Mittal, H., & Hemalatha, N. (2024). Identifying the maturity level of coconuts using deep learning algorithms. *Materials Today: Proceedings, 103*, 410–414. https://doi.org/10.1016/j.matpr.2023.09.071
5. Perera, P. A., & Perera, P. M. (2025). Dual-stage deep learning framework for hybrid coconut maturity classification and harvest timeline prediction. *Asian Journal of Research in Computer Science, 18*(9), 76–90. https://doi.org/10.9734/ajrcos/2025/v18i9755
6. Luthfie, A. A., & Alamsyah, A. (2025). Identifying coconut maturity levels using CNN and YOLOv8 deep learning algorithms. *Journal of Information System Exploration and Research, 3*(2). https://doi.org/10.52465/joiser.v3i2.595
7. Coconut maturity level classification using image preprocessing and deep transfer learning. (2025 conference record; indexed 2026). https://doi.org/10.1109/RIVF68649.2025.11365215
8. Coconut bunch intelligence system: Image-based maturity classification and nut count prediction. (2026 conference record). https://doi.org/10.1109/ICIPRoB69625.2026.11497814
9. Tender coconut maturity stage detection using YOLOv8-v10: Comparative analysis with DETR, EfficientDet and Vision Transformers. (2026). *Procedia Computer Science*. https://doi.org/10.1016/j.procs.2026.05.062
10. Sailangka, W., Puasantikul, P., & Sriboonrat, P. (student research project; year and formal publication status to verify). Nondestructive evaluation of *Cocos nucifera* of Nam Hom variety maturity stage using deep learning. Kamnoetvidya Science Academy. https://app.kvis.ac.th/kvis-awards/list.php?code=COMP019

---
**Evidence integrity:** This document records a preliminary search and candidate protocol only. It does not establish novelty, complete literature coverage, approved ethics/permissions, a dataset, trained models, measured performance, Q1 suitability or manuscript readiness.


## 8. Evidence audit addendum — version 0.2 (26 November 2026)

This addendum supersedes conflicting metadata or preliminary interpretations above. It records additional publisher-level checks; it does not convert the work into a systematic review.

### 8.1 Verified correction: Thai young-coconut maturity reference

The publisher record for Terdwongworakul, Chaiyapong, Jarimopas and Meeklangsaen (2009), *Biosystems Engineering*, 103(2), 208–216 gives DOI **10.1016/j.biosystemseng.2009.03.006**. The earlier DOI ending `.012` in Section 3 and Reference 1 was incorrect and must not be cited. The study examined young Thai “Nahm Wahn” coconuts sampled from 170 to 206 days after pollination. Flesh thickness was the physical parameter best correlated with days after pollination; the authors also report a non-destructive resonant-frequency model. This is useful evidence for defining a reference maturity protocol, but it is not a visual RGB classifier and its cultivar/young-coconut scope must not be generalized to all coconut types or harvest markets. Publisher record: https://doi.org/10.1016/j.biosystemseng.2009.03.006.

### 8.2 New primary evidence: fruit-disjoint acoustic classification (2026)

Sánchez-Gendriz, Gomes and Guedes (2026), “Non-Destructive Coconut Maturity Classification from Tapping Sounds Using Frozen CLAP Embeddings and Multi-Event Aggregation,” *AgriEngineering*, 8(9), 395, DOI https://doi.org/10.3390/agriengineering8090395, is a peer-reviewed, directly relevant coconut maturity study.

Publisher full text reports:
- Public acoustic cohort: 127 fruits; three source classes (immature, mature, overmature); 381 ridge-level recordings.
- Five fruits were excluded by the stated event-selection eligibility rule, leaving 122 fruits: 72 training, 12 validation and 38 test.
- The fruit was the split unit; all ridge recordings and derived candidate segments from one fruit remained in one partition. This is direct evidence that fruit-disjoint evaluation has already been implemented in coconut maturity research, albeit for acoustic rather than RGB input.
- CLAP–MLP balanced accuracy was 64.72% at candidate-event level and 93.06% after fruit-level aggregation. These are study-specific results and must not be compared directly with image-paper accuracy.
- The CLAP encoder is approximately 68.6 million parameters; the paper reports roughly 0.3 s CPU extraction per segment in its implementation and notes compression or off-device computation would be needed for embedded deployment. A compact Mel-band alternative is reported at approximately 0.5 ms feature extraction and a roughly 1 MB LightGBM model. These are not PUI89 measurements.
- The authors call for larger, more balanced data across varieties and independent acquisition conditions, and for recording fruit geometry, mass, tapping force and internal composition.

This study weakens any broad claim that coconut maturity research lacks independent-unit evaluation, repeated-measurement aggregation, or CPU/resource discussion. It does **not** resolve RGB image generalisation, independent-orchard testing, Thai cultivar transfer, or the validity of PUI89's four proposed visual labels.

### 8.3 Four-class image work: overlap and limits

The IEEE Xplore record for “Coconut Bunch Intelligence System: Image-Based Maturity Classification and Nut Count Prediction” (2026), DOI https://doi.org/10.1109/ICIPRoB69625.2026.11497814, describes 3,000 images with four labels (Immature, Mature, Over-mature, Unknown), a MobileNetV2 classifier with reported 99.0% accuracy, and a separate YOLOv8n bunch-count task. This is a direct prior-art overlap with four-label image classification. The publisher abstract available in this audit does not establish whether the split was grouped by fruit, bunch, tree, capture session or orchard; it also does not establish that its labels are equivalent to young green, mature green, yellow and brown. Those questions require full-paper and supplementary-material verification. Do not infer a methodological flaw from missing abstract detail.

### 8.4 Revised research-gap matrix

| Candidate contribution | Evidence status after audit | What remains unverified / required | Decision |
|---|---|---|---|
| “Four-class coconut image classification” as novelty | Contradicted as a broad novelty claim by the 2026 IEEE four-label image study. The label taxonomy is not yet shown to match PUI89. | Compare full label definitions, target (fruit vs bunch), cultivar, image source, intended harvest market, split unit and evaluation protocol. | Do not claim novelty. |
| Horticulturally defensible labels for a defined Thai cultivar/use | The 2009 Thai young-coconut study provides physical/maturity evidence for Nahm Wahn and days-after-pollination/flesh-thickness relationships. KVIS also records a Nam Hom acoustic maturity project with owner-assigned classes. | Establish the intended PUI89 cultivar and market/use; obtain expert-defined labels and independent reference observations. Colour alone is insufficient. | Strong candidate requirement; gap not yet proven. |
| RGB evaluation on independent fruit/tree/session/orchard units | Acoustic fruit-disjoint evaluation exists in 2026. The abstract-level evidence for the 2026 four-class image study does not reveal its grouping unit. | Full-text extraction of image-study split procedure; broader review of image-based studies; prospective held-out orchard/site if access permits. | Potentially useful, but narrow the claim to RGB and external-site evaluation only if confirmed. |
| Cross-cultivar / cross-orchard robustness | The 2026 acoustic paper explicitly requests more varieties and independent acquisition conditions; this is evidence of a limitation in that acoustic cohort, not proof for all image studies. | Compare studies by cultivar, site, season, camera and collection protocol; plan independent target-domain testing. | Candidate gap requiring systematic screening. |
| Uncertainty, calibration and human abstention | Not established by the coconut primary records inspected in this audit. | Search full texts and broader fruit/agricultural vision studies; distinguish confidence scores from calibrated uncertainty and evaluated selective prediction. | Candidate gap, not confirmed. |
| CPU-first performance | Edge/compact approaches already exist; the 2026 acoustic paper reports CPU feature extraction and model/encoder size. | Benchmark on the explicitly named target CPU and report end-to-end preprocessing + inference latency, peak RAM, throughput and energy if measurable. | Product-relevant evaluation, not a novelty claim by itself. |
| Multi-view / repeated-observation aggregation | Directly studied for acoustic taps in 2026. | Determine whether RGB multi-view or repeated capture adds robust value under fruit-disjoint evaluation; compare single-view and aggregation baselines. | Candidate comparative question, not a new concept. |

### 8.5 Updated working question and claim boundary

A defensible working question is now narrower:

**For a clearly specified Thai coconut cultivar and harvest use, can a compact RGB model provide reliable fruit-level maturity assistance under expert-defined reference labels and evaluation on independent acquisition groups, with calibrated abstention and measured CPU resource use?**

This is a research question, not a novelty conclusion. Before using it in a proposal or manuscript, the team must verify the 2026 IEEE full paper, screen all relevant coconut image studies, and obtain domain-expert agreement on the cultivar-specific label protocol. If the four proposed colour labels do not map to a valid maturity/market standard, revise the taxonomy rather than forcing it into the dataset.

### 8.6 Source verification register

| Record | Source checked in this audit | Verification outcome |
|---|---|---|
| Terdwongworakul et al. (2009) | ScienceDirect publisher record, DOI 10.1016/j.biosystemseng.2009.03.006 | Title, journal, volume/pages, DOI and abstract-level methods checked; previous DOI corrected. |
| Megalingam et al. (2024) | Amrita institutional publication record and Springer DOI metadata | Authors and abstract-level dataset/method/result checked; full publisher article still needs detailed extraction. |
| Coconut Bunch Intelligence System (2026) | IEEE Xplore record and conference program | Title, four labels, dataset size and abstract-reported results checked; full split/ground-truth details remain unverified. |
| Sánchez-Gendriz et al. (2026) | Full open-access *AgriEngineering* article | Full text inspected for dataset, fruit-disjoint split, results, compute reporting, limitations and data availability. |
| Nam Hom student project | KVIS project record and 2023 abstract/guidebook | Project-level, non-peer-reviewed evidence only; must not be represented as a journal paper. |

**Audit boundary:** Publisher pages and accessible full text were checked for the records above. No Scopus, Web of Science, CAB Abstracts or institutional subscription database export has been obtained. The review remains a targeted scoping review, not a systematic or exhaustive review.
