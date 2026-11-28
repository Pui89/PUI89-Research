# PUI89 Canonical Product Register

**Version:** 1.1  
**Status:** Proposed source of truth for portfolio alignment  
**Last reviewed:** 28 November 2026

This register defines the six active PUI89 product identities used by the independent research programme. It is an identity and scope register, not evidence that any product is built, validated, certified, commercially available, or ready for deployment.

## 1. Active products

| No. | Canonical product name | Product identity | Scope boundary |
|---:|---|---|---|
| 1 | **Coconut Harvest AI** | Agricultural AI for coconut maturity assessment and harvesting-support research. | Image-based maturity understanding and evidence-led harvesting research. Do not claim validated harvesting or field performance without evidence. |
| 2 | **PUI89 Sentinel — All-Terrain Inspection Robot Dog** | Supervised quadruped robot concept for environmental inspection, situational awareness and evidence capture. | Inspection and environmental perception only. Narcotics detection/screening, X-ray screening and associated forensic datasets are excluded. No autonomous all-terrain capability is implied. |
| 3 | **PUI89 AI HOME — Indoor Assistance Robot** | Compact four-wheel indoor assistance robot; proposed complete-system mass target 4–6 kg and maximum 10 kg, including battery and installed hardware. These are design targets, not measured prototype mass. | Indoor assistance and environment awareness. Distinct from NOMAD; no validated home-safety protection or autonomous operation is implied. |
| 4 | **PUI89 AI NOMAD — Compact Four-Wheel Mobile Assistant** | Compact, dog-inspired four-wheel mobile assistant with an integrated carrying/handling feature; proposed target mass approximately 7 kg and maximum 10 kg. These are design targets, not measured prototype mass. | User-directed mobile assistance. It is not a suitcase/travel-luggage product and is not claimed to autonomously follow a person. Distinct from indoor-focused HOME. |
| 5 | **PUI89 AI Global SUV** | Five-door, five-seat global SUV concept with AI-assisted mobility and driver-support research. Current research preferences are RWD-first with AWD capability, Full HEV, and a 700 mm wading-depth target; none is a validated vehicle specification. | Vehicle perception, road/environment context and advisory intelligence. “AI Robot Car” is a legacy shorthand, not the canonical product name. No autonomous steering, throttle or braking is implied. |
| 6 | **PUI89 AI Step-Through Scooter** | Rider-first two-wheel step-through scooter concept with AI-assisted mobility and safety-support research. | Road/obstacle awareness, environmental warnings and vehicle-condition information. “EasyRide AI” and “AI Motorcycle” are legacy names. No autonomous steering, throttle or braking is implied. |

## 2. Shared platform capabilities — not additional products

- **PUI89 Shared AI Core:** common software contracts, perception/inference interfaces, resource-aware execution, uncertainty handling and evidence governance.
- **PUI89 Security Core:** shared defensive security and assurance capabilities.
- **PUI89 Intelligence Factory:** research, evaluation and evidence-production workflow.

These are platform capabilities and must not be counted as products.

## 3. Research hub — not a product

**PUI89-Research** is the central research portfolio and governance repository supporting the six products. It is not a seventh product.

## 4. Retired or historical scope

- **Extreme Flood Rescue AI:** excluded from the current six-product active portfolio. Preserve historical records and prior evidence; do not silently delete or rewrite archived work. Flood awareness may be studied as a bounded capability/use case within a relevant product where justified.
- **Legacy Sentinel narcotics/X-ray screening work:** outside the active Sentinel and research scope. Do not reintroduce related datasets, forensic spectra or screening requirements through shared documentation.
- Legacy product names may remain in historical records, commit history or archived material. Where they appear in current navigation or active product descriptions, label them as legacy and point to the canonical identity.

## 5. Portfolio-wide evidence rules

Every repository and public page must distinguish:
1. **Concept / proposed:** design intent or hypothesis only.
2. **Software implemented:** code exists; this does not establish physical capability.
3. **Simulation tested:** results apply only to the stated simulation and assumptions.
4. **Bench tested:** a specified component or subsystem was tested under stated conditions.
5. **Physical prototype tested:** a physical prototype was tested; report setup, sample size, conditions and failures.
6. **Field validated / independently verified:** only when documented evidence supports the exact operating envelope and claim.

Do not infer sensor installation, model performance, safety, certification, payload, range, water resistance, autonomous operation or commercial readiness from a concept or architecture document.

## 6. Change control

- This register is the proposed canonical identity reference for alignment work.
- Product identity changes require explicit owner review and a versioned update.
- Update English and Thai documentation together.
- Preserve historical material; use clear legacy/retired labels rather than destructive bulk replacement.
- Before merging any alignment change, check affected product READMEs, website pages, research plans, Shared AI Core registry and open PR conflicts.

## 7. Alignment checklist

- [ ] Six active product names and descriptions match this register.
- [ ] NOMAD is consistently represented as the dog-inspired compact four-wheel assistant, never as a suitcase.
- [ ] Sentinel uses the All-Terrain Inspection Robot Dog identity and excludes narcotics/X-ray screening.
- [ ] AI Global SUV is the canonical vehicle name; AI Robot Car is legacy shorthand only.
- [ ] AI Step-Through Scooter is canonical; EasyRide AI / AI Motorcycle are legacy names only.
- [ ] Research hub and shared platform capabilities are not counted as products.
- [ ] Retired Flood Rescue history is preserved and not presented as an active seventh product.
- [ ] English and Thai pages have matching scope and evidence status.

---

**ภาษาไทย:** [ทะเบียนผลิตภัณฑ์ฉบับภาษาไทย](CANONICAL_PRODUCT_REGISTER.th.md)


## 8. Research preferences and prototype-cost governance (28 November 2026)

- **AI Global SUV:** RWD-first with AWD capability, Full HEV (not PHEV), and 700 mm target wading depth are research preferences only. They are not supplier-selected components, engineering sign-offs, test results or production specifications.
- **Prototype cost:** do not publish a single-point prototype cost until the configuration, quantities, manufacturer/part number, country-of-origin evidence, dated supplier quotation, shipping, tax and integration assumptions are recorded. Mark unknown prices as **TBD** rather than estimating unsupported totals.
- **BOM discipline:** separate complete boards/modules from their embedded chips to avoid double-counting CPU, GPU, NPU, MCU, memory, CMOS, IMU, GNSS, motor-driver and power-management ICs.
