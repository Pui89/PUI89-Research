# PUI89 Six-Product Prototype BOM & Cost Framework

**Version:** 1.0  
**Review date:** 28 November 2026  
**Status:** Planning template only. No purchase, supplier commitment, selected hardware configuration or validated prototype cost is implied.

This document establishes a consistent way to scope hardware, materials, components and prototype costs across the six active PUI89 products. Unknown selections and prices must remain **TBD**. Do not invent manufacturer, part number, country of origin, supplier, quotation or cost.

## 1. Costing rules

1. Define a versioned prototype configuration and quantity before estimating.
2. Record manufacturer, exact model/part number, country of manufacture/origin evidence, supplier, source URL, quotation date, currency, unit price, quantity, shipping, tax and lead time.
3. Separate quoted prices, observed public list prices, historical prices and engineering allowances. Never present them as equivalent.
4. Record exchange-rate source/date for non-THB prices.
5. Include fabrication, integration, test fixtures, consumables, freight, duties/tax and contingency as separate lines.
6. State exclusions and assumptions. A budgetary estimate is not a supplier quote or procurement approval.
7. Do not select or purchase components until compatibility, safety, rights/provenance and user approval are established.
8. Prefer non-Chinese-origin hardware and suppliers where required; origin must be supported by evidence, not inferred from a brand's headquarters.

## 2. Common BOM categories

| Category | Record |
|---|---|
| Compute modules | SBC/edge computer, CPU/GPU/NPU module, carrier board, cooling, storage |
| Embedded control | MCU board, motor-control board, safety controller, I/O |
| Memory and storage | RAM, flash, SSD, removable storage |
| Perception sensors | RGB/CMOS cameras, depth, thermal, LiDAR, radar, microphones, encoders |
| Position and motion | IMU, GNSS, wheel odometry, magnetometer, localization aids |
| Connectivity | Ethernet, Wi-Fi, Bluetooth, cellular modem, antennas |
| Actuation | Motors, servos, gearboxes, motor drivers, brakes, steering or drive assemblies |
| Power | Battery cells/packs, BMS, charger, DC-DC, fuses, contactors, wiring |
| Mechanical and materials | Frame, chassis, enclosure, wheels/legs, joints, fasteners, protective covers |
| Safety and protection | Emergency stop, bump/contact sensors, interlocks, thermal protection, ingress protection |
| Fabrication and integration | Machining, printing, welding, assembly, harnessing, calibration |
| Test and logistics | Test fixtures, consumables, shipping, duties, taxes, packaging |

**No double counting:** If a purchased board/module already contains a CPU, GPU, NPU, MCU, memory, CMOS sensor, IMU, GNSS receiver, motor driver or power IC, list the complete board/module as the purchased line. Record embedded chips as specifications, not additional cost lines, unless separately purchased.

## 3. Product-specific BOM planning

| Product | Initial component groups to scope | Configuration decisions still open |
|---|---|---|
| Coconut Harvest AI | RGB camera(s), edge compute, lighting, camera mount, calibration target, optional distance/depth sensor, protective enclosure, data-storage and test equipment | Camera count/lens, working distance, illumination, mounting, compute board and whether any actuator is in the first demonstrator |
| Sentinel — All-Terrain Inspection Robot Dog | Quadruped base/platform, locomotion actuators and drivers, RGB, depth, thermal, 360° LiDAR, IMU, compute, battery/BMS, communications, emergency stop, protective enclosure | First supervised mission, payload/mass budget, locomotion platform, sensor placement, runtime, operating environment and safety envelope |
| AI HOME | Four-wheel chassis, motors/gearboxes/drivers, RGB/depth sensing as justified, compute, MCU, battery/BMS, charging, bump/contact sensors, emergency stop, enclosure and wiring | Final dimensions, 4–6 kg target mass (10 kg maximum), sensor set, runtime and indoor test course |
| AI NOMAD | Four-wheel outdoor chassis, motors/gearboxes/drivers, handle structure, RGB/depth sensing as justified, IMU, compute, MCU, battery/BMS, wheel/terrain interface, protective enclosure and safe-stop hardware | Practical assistance task, approximately 7 kg target mass (10 kg maximum), terrain envelope, handle loads, runtime and stability tests |
| AI Global SUV | Vehicle platform and powertrain architecture, perception sensor suite, compute/edge modules, vehicle-network interface, power conditioning, thermal/environmental protection, driver-warning HMI and test instrumentation | RWD-first with AWD capability, Full HEV and 700 mm wading target are research preferences only; vehicle platform, sensor package, interface permissions and regulatory scope remain TBD |
| AI Step-Through Scooter | Step-through frame/platform, two-wheel running gear, drive/powertrain components as selected, braking and lighting interfaces, perception sensors, compute, MCU, power management, rider HMI and protective enclosures | Powertrain/energy architecture, sensor suite, packaging, rider ergonomics, water-warning requirements and test platform remain TBD |

These groups are research scoping categories, not selected parts or validated designs. For the SUV and scooter, vehicle-level systems must be engineered and validated by qualified specialists under applicable regulations.



## 3A. Current prototype-cost status by product

| Product | First prototype scope to cost | Verified prototype cost | Main unresolved cost drivers |
|---|---|---|---|
| Coconut Harvest AI | Controlled RGB vision bench demonstrator; not a complete orchard-harvesting robot | **TBD** | Camera/lens, lighting, mount, compute reuse, calibration and fabrication configuration |
| Sentinel — All-Terrain Inspection Robot Dog | Supervised quadruped inspection demonstrator with a defined sensor payload | **TBD** | Quadruped base, actuators, sensor payload, compute, battery, safety equipment and integration |
| AI HOME | Four-wheel indoor assistance demonstrator | **TBD** | Chassis, drive modules, sensor configuration, compute reuse, battery and safety integration |
| AI NOMAD | Four-wheel outdoor/mobile-assistance demonstrator with manual handling handle | **TBD** | Wheel/drive design, frame/handle, terrain requirements, sensors, compute and battery |
| AI Global SUV | Removable advisory-only perception/compute research kit on a compatible existing vehicle or bench rig; donor vehicle excluded | **TBD** | Vehicle compatibility, automotive-grade sensors/compute, protected power, read-only interfaces and controlled testing; full vehicle development is out of scope for this kit estimate |
| AI Step-Through Scooter | Removable advisory-only sensor/compute research kit on a compatible existing scooter or bench rig; donor scooter excluded | **TBD** | Rider-safe mounting, weather/vibration protection, sensors, compute, power and controlled testing; full vehicle development is out of scope for this kit estimate |

The table intentionally reports **TBD** for every verified prototype cost. Any preliminary range shown elsewhere on the website is an unverified planning allowance only and must not be represented as a current supplier-backed cost.

## 4. Prototype cost worksheet

Create one line per purchasable item or service:

| Field | Required value |
|---|---|
| Product / prototype revision | TBD |
| Category / item description | TBD |
| Manufacturer / exact part number | TBD |
| Country of manufacture / origin evidence | TBD |
| Supplier / source URL | TBD |
| Unit price / currency / quote date | TBD |
| Quantity / extended price | TBD |
| Shipping / duties / tax | TBD |
| Fabrication / integration / calibration | TBD |
| Test equipment / consumables | TBD |
| Lead time / warranty / lifecycle | TBD |
| Compatibility and safety review | TBD |
| Evidence status / reviewer | TBD |

Calculate:
- **Hardware subtotal** = sum of verified item unit prices × quantities.
- **Fabrication and integration** = separately evidenced labour/service/material lines.
- **Logistics and tax** = separately stated shipping, duties and taxes.
- **Contingency** = explicitly stated allowance with rationale.
- **Prototype budget** = sum of the above, with exclusions listed.

Until quotations and configuration evidence exist, the prototype cost for each product is **TBD — not yet responsibly estimable**.

## 5. Shared engineering toolkit

Track shared tools separately from product BOMs so they are not charged six times. Examples include measurement tools, soldering/rework equipment, crimping tools, calibration targets, safety fixtures, test computers and reusable development boards. Record ownership, availability, condition and allocation method. No tool purchase is authorized by this document.

## 6. Evidence and change control

- Preserve source URLs, snapshots or quote files and access dates.
- Verify the exact country of manufacture/origin for each part; brand nationality alone is insufficient.
- Check export restrictions, radio approvals, battery transport rules, electrical safety and applicable vehicle regulations before procurement or testing.
- Recheck discontinued parts, lifecycle notices, firmware support and security advisories.
- Update English and Thai BOMs together.
- Keep proposed, quoted, purchased, integrated and tested states distinct.
- No supplier is selected and no purchase or commitment is authorized by this framework.

**ภาษาไทย:** [กรอบ BOM และต้นทุนต้นแบบ 6 ผลิตภัณฑ์ (ภาษาไทย)](PROTOTYPE_BOM_AND_COST_FRAMEWORK.th.md)
