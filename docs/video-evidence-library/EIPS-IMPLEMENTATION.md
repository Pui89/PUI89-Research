# PUI89 Evidence Intelligence & Protection System (EIPS)
**Implementation specification | Six-product evidence library**

## 1. Purpose and implementation boundary

EIPS maintains a link-only register of candidate video and dataset sources for the six active PUI89 products. It protects provenance, licensing decisions, metadata integrity and review history.

This phase implements the data contract and operating rules. It does **not** implement a live crawler, download pipeline, model-training pipeline, scheduler or autonomous approval system. No media is downloaded, no software is installed, and no paid service is required or authorized.

## 2. Product scope

| Product ID | Product | In-scope evidence themes |
|---|---|---|
| coconut-harvest-ai | Coconut Harvest AI | Coconut orchards, fruit, maturity appearance, harvesting |
| sentinel | PUI89 Sentinel | General security monitoring, facility observation, event/anomaly detection |
| ai-home | AI HOME | Indoor mobile robotics, navigation, obstacle encounters, human-aware interaction |
| ai-nomad | AI NOMAD | Outdoor mobile robotics, trails, uneven terrain, outdoor navigation |
| ai-robot-car | AI Robot Car | Road scenes, traffic, vehicles, pedestrians, road hazards |
| easyrider-ai-scooter | EasyRide AI Step-Through Scooter | Scooters, motorcycles, rider viewpoint, road and rider safety |

**Excluded:** narcotics detection/screening, related datasets, X-ray screening and forensic spectra. The removed Extreme Flood Rescue AI product is not part of this six-product scope.

## 3. Required record contract

The machine-readable contract is `schemas/evidence-record.schema.json`. Each record must include:

- Stable `evidence_id`; do not recycle identifiers.
- One or more allowed `product_ids`.
- Exact original asset/page URL and publisher identity.
- Country/origin assessment with evidence reference; unknown remains pending.
- Licence name, exact terms URL, checked date and evidence snapshot reference.
- Independent permission decisions for website, research, AI training, commercial use and redistribution.
- Link, integrity, review and approval states.
- Technical metadata only when observed from a reliable source.
- Review notes and append-only history references.

Use one record per individual clip or dataset asset. Search-result pages are discovery sources, not approved asset records.

## 4. Approval states

`discovered` → `pending_review` → `approved_limited` or `rejected` or `quarantined`.

- `discovered`: candidate URL only; no rights or origin are implied.
- `pending_review`: checks incomplete or awaiting a human decision.
- `approved_limited`: human-approved for explicitly listed purposes only.
- `rejected`: source is unsuitable or rights/provenance fail.
- `quarantined`: a material change, suspicious redirect, rights conflict or integrity concern requires review.

An approval for one purpose never grants another purpose. Unknown or conflicting rights must not be interpreted as permission.

## 5. Protection controls

### Source and provenance
- Preserve the original URL and publisher; record redirects separately.
- Do not infer country of origin from domain, language, hosting location or an uploader's display name.
- Chinese-origin and unclear-origin sources are not eligible for approval under the current PUI89 policy.
- A source with insufficient origin evidence remains `pending_review` or `quarantined`.

### Licence and rights
- Verify the individual asset's applicable terms, not just a platform summary.
- Record separate decisions for website display, research, AI training, commercial use and redistribution.
- Re-check terms after a material change or before a new purpose of use.
- A free-to-view or free-to-download label is not an AI-training or commercial-use licence.

### Integrity and history
- Keep prior approved record versions; never silently overwrite or delete.
- Record who/what changed a field, when, previous value, new value and reason.
- A checksum may detect a changed metadata snapshot; it does not prove source authenticity or legal rights.
- Broken links, changed redirects, changed licence references and changed publisher identity trigger review.

### Safe operation
- Read-only link and metadata checks by default.
- No scraping, bulk extraction, account creation, downloads, installs, or paid/metred APIs without explicit approval and a separate rights review.
- No automatic approval, deletion, replacement or merge.
- Changes should be proposed as reviewable Git commits/PRs; preserve branch protection and the default branch.

## 6. Quality and coverage measurement

Report these separately; do not collapse them into a single score that hides a failed rights check:

1. **Coverage:** six product registers present; count candidate/verified records per product and evidence category.
2. **Provenance completeness:** percentage of records with supported publisher and origin evidence.
3. **Rights completeness:** percentage with explicit decisions for each intended use.
4. **Link health:** working, redirected, broken and unchecked counts.
5. **Integrity health:** unchanged, changed, suspicious and unchecked counts.
6. **Freshness:** age since last licence/provenance review.
7. **Traceability:** percentage with review rationale and change history.
8. **Quality suitability:** relevance, resolution, duration, FPS and modality where available.

Suggested gates before use: 100% provenance evidence, 100% purpose-specific rights review, human approval, and zero unresolved critical warnings. A record failing any gate cannot be used for that purpose.

## 7. Monitoring and reporting policy

A future no-cost monitor may check public page reachability, redirects and visible licence-page changes at a conservative rate, subject to each provider's terms and robots/access rules. It must not scrape prohibited services or download media.

Every report should show:
- Six-product coverage and gaps.
- New candidates (not auto-approved).
- Broken/redirected links.
- Licence or provenance changes.
- Quarantined records and reasons.
- Records overdue for review.
- Pending human decisions.
- Actions taken and actions deliberately not taken.

If no permitted free scheduler is available, use an on-demand/manual review. Do not claim continuous monitoring is active until it has been deployed and tested. GitHub Actions quota was reported exhausted on 25 November 2026; no workflow depending on Actions should be treated as operational until quota availability is confirmed.

## 8. Acceptance tests

- Reject an invalid product ID.
- Reject an asset record without an exact asset URL.
- Keep unknown origin pending; do not auto-approve.
- Keep unclear licence permissions pending for each intended use.
- Ensure website permission does not imply AI-training permission.
- Flag a changed licence URL or material licence snapshot as requiring review.
- Flag a broken link without deleting its record.
- Preserve old values when a record is updated.
- Ensure a duplicate URL is flagged for review, not silently discarded.
- Ensure all six product IDs are represented in the coverage report.
- Ensure Sentinel records cannot introduce excluded narcotics/X-ray/forensic scope.

## 9. Current implementation status

- [x] Six-product scope and exclusions documented.
- [x] Evidence record schema defined.
- [x] Human-review lifecycle and protection rules defined.
- [x] Measurement and acceptance criteria defined.
- [ ] Validator and automated tests implemented.
- [ ] Monitoring runner implemented and tested.
- [ ] Scheduler selected and deployed.
- [ ] First individual assets verified and approved.

This specification is a design/contract deliverable. It is not evidence that monitoring, validation automation or any individual source approval is already active.
