# PUI89 Q1 Manuscript, Statistics and Reproducibility Standard

**Status: Required checklist proposal. Apply and tailor it per study and target journal.**

## 1. Manuscript structure

Use the target journal's required format. A conventional empirical paper should contain:

1. **Title and abstract:** state task, data domain, method, primary result and limitation accurately.
2. **Introduction:** problem importance, current state of the art, precise gap, research question, contribution and scope.
3. **Related work:** systematic and reproducible search strategy; explain inclusion/exclusion and compare methods/datasets rather than listing papers.
4. **Materials and methods:** study design, ethics, data provenance, sampling, annotation, splits, methods, baselines, hardware/software, metrics and statistical plan.
5. **Results:** primary endpoint first; uncertainty intervals; baseline comparisons; ablations; robustness; resource results; failures and negative results.
6. **Discussion:** interpret findings against literature; distinguish evidence from speculation; discuss external validity and limitations.
7. **Conclusion:** answer the research question without extending beyond the tested scope.
8. **Declarations and supplements:** ethics, consent, data/code availability, funding, conflicts, author contributions, protocol deviations and supplementary methods.

## 2. Literature review and novelty

- Search at least two suitable scholarly indexes plus publisher databases; record search date, query strings, filters and screening decisions.
- Prioritise peer-reviewed primary research, benchmark papers, dataset papers and authoritative standards. Use preprints as leads, not substitutes for peer-reviewed evidence when the latter exists.
- Build a literature matrix with: citation/DOI, year, journal/category, task, dataset, sample size, split design, baseline, metrics, results, limitations, licence and relevance.
- Map each proposed contribution to prior work and identify what is genuinely different: research question, data, method, evaluation setting, theory or reproducibility.
- Do not call a gap "novel" until a sufficiently broad, current search and expert review support that conclusion.
- Do not fabricate citations, DOIs, journal quartiles or impact factors.

## 3. Dataset and evidence governance

For every dataset and individual asset, record:
- Stable dataset and sample IDs; exact source and original publisher.
- Collection method, date, geographic/site class where safe, device/sensor and modality.
- Ownership, exact licence/terms, permission for research, AI training, publication figures and redistribution separately.
- Consent, privacy, personal-data handling, anonymisation and retention.
- Inclusion/exclusion rules, missingness, class balance and known sampling bias.
- Annotation guide version, annotator roles, independent review and adjudication.
- Hashes, immutable dataset version, manifest and access controls.
- Split membership and leakage-group identifiers.

Unknown or conflicting rights block use. A platform licence is not automatically permission for AI training, redistribution or commercial use. Do not publish raw data if rights, privacy or safety restrictions prohibit it.

## 4. Statistical analysis plan

Freeze the plan before opening the final test set.

- Define one primary outcome and its unit of analysis. Specify secondary and exploratory outcomes separately.
- State the estimand, comparison, inclusion/exclusion criteria and missing-data handling.
- Justify sample size using power analysis or target confidence-interval precision, accounting for clustering, repeated measures and expected event prevalence.
- Use grouped or temporal splits to avoid leakage. Do not treat correlated frames, objects, trials or repeated runs as independent samples.
- Select statistical tests that match the outcome distribution and dependence structure. Use paired comparisons when the same cases are evaluated by multiple methods.
- Report effect sizes and 95% confidence intervals where appropriate; explain the resampling unit for bootstrap intervals.
- Correct or control for multiple comparisons when many models, classes, conditions or endpoints are tested.
- Report class-wise performance and confusion matrices for imbalanced classification; report PR-AUC alongside ROC-AUC where prevalence makes it informative.
- For detection, report the relevant mAP/IoU protocol plus per-class precision/recall and operating-point trade-offs. Define IoU thresholds and evaluator versions.
- For event detection, report event-level metrics, false alarms per unit time and detection delay; frame-level metrics alone may mislead.
- For robotics, define trial-level success/failure, intervention, collision/near-miss and route/environment units; report physical trials separately from simulation.
- For calibration, document method and split; report reliability plots and proper scoring rules such as Brier score or log loss where appropriate. ECE depends on binning and must not stand alone.
- For compute studies, report repeated latency distributions, throughput, peak memory, energy/power measurement boundary, thermal state and exact software/hardware configuration.
- Preserve negative findings, failed runs, protocol deviations and all predeclared primary outcomes.

A p-value is not an effect size, practical significance, novelty or proof of generalisation.

## 5. Baselines, ablations and robustness

Every paper must justify:
- A simple baseline and a strong current baseline.
- The proposed method compared under matched data, preprocessing and compute budgets.
- Ablations that isolate the contribution of each major component.
- Sensitivity to thresholds, input resolution, modality availability and relevant hyperparameters.
- Robustness under realistic distribution shifts, missing/noisy inputs and known failure modes.
- External validation on a distinct site, route, orchard, camera, layout, season or capture period when feasible.

Do not cherry-pick a single favourable seed or test condition. Record all runs and state the selection rule.

## 6. Reproducibility package

Subject to licence and privacy:
- Protocol version and timestamp.
- Code repository URL and exact commit SHA.
- Model architecture, checkpoint hash and exact revision.
- Dataset manifest/version/hash; public download instructions only where permitted.
- Split manifest or reproducible split-generation code.
- Random seeds and deterministic settings.
- Dependencies, versions, operating system, CPU/GPU/NPU, RAM, runtime and configuration.
- Training and inference commands, preprocessing, post-processing and thresholds.
- Raw metrics, logs, plots and analysis scripts.
- Known non-determinism and reproduction limitations.

If data cannot be redistributed, provide a legally permitted access route, synthetic test fixtures and sufficient metadata to understand the study without exposing restricted data.

## 7. Ethics, authorship and responsible publication

- Obtain institutional ethics review or a documented determination where human participants, identifiable people, surveillance footage, animal subjects or sensitive environments are involved.
- Follow applicable local law, consent requirements, data-protection obligations and the target journal's policies.
- Do not publish identifiable people, private locations, confidential government/workplace data or restricted security information without lawful basis and appropriate approval.
- Define authorship by substantive scholarly contribution and obtain agreement from all authors before submission.
- Record funding, conflicts of interest, affiliations, contributions, use of AI writing/coding tools where required, and any sponsor role.
- Do not submit the same manuscript simultaneously to multiple journals; avoid duplicate publication and plagiarism.
- Use reporting guidelines appropriate to the study design and discipline; state when no specific guideline applies.

## 8. Q1 journal selection and verification

Before submission:
1. Identify journals whose scope genuinely matches the paper and readership.
2. Check the journal's current quartile in the named database (for example, JCR or SCImago) and the exact subject category and year. These systems can differ.
3. Verify indexing directly in the relevant database; do not rely only on journal marketing.
4. Check peer-review process, publisher, editorial board, publication ethics, fees/APCs, waiver policy, data policy, preprint policy and article type.
5. Check for retractions, suspicious solicitation, hijacked journal websites and predatory-publishing indicators.
6. Record the target journal, category, database, quartile, year, date checked and source evidence.
7. Re-check at submission; never state "Q1 journal" without the database/category/year context.

No Q1 quartile or acceptance is promised. Editorial fit, scientific contribution, reviewer assessment and journal metrics are outside the repository's control.

## 9. Pre-submission checklist

- [ ] Research question and contribution are precise and supported by current literature.
- [ ] Protocol, primary outcome and statistical plan were fixed before final test evaluation.
- [ ] Data rights, privacy, consent and ethics requirements are resolved.
- [ ] Dataset version, provenance, labels, splits and hashes are recorded.
- [ ] Leakage risks are assessed and controlled.
- [ ] Baselines, ablations and robustness tests are complete or limitations are explicit.
- [ ] Statistical analysis, effect sizes and uncertainty intervals are independently checked.
- [ ] Failures, negative results, exclusions and deviations are reported.
- [ ] Every manuscript claim maps to retained evidence.
- [ ] Code/model/runtime/hardware versions are pinned.
- [ ] Figures and tables can be regenerated from retained results.
- [ ] Limitations and prohibited interpretations are explicit.
- [ ] Ethics, authorship, funding, COI and data/code statements are complete.
- [ ] Independent scientific review is recorded.
- [ ] Target journal scope, indexing, quartile, category, fees and policies are verified for the current year.
