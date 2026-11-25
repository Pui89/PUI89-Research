# PUI89 Video Evidence Library
**Six-product source register | Link-only discovery | English / ภาษาไทย**

> **Status:** Initial source directory and verification workflow. This document contains discovery links, not a claim that individual clips or datasets have been reviewed, approved, downloaded, or validated.
>
> **Collection rule:** Links only. Do not download, install, scrape, bulk-copy, create accounts, call paid APIs, or use metered services without explicit user approval. PUI89 development pause remains in effect; this documentation-only proposal does not authorize other development work.

## Purpose / วัตถุประสงค์

Maintain a traceable, rights-aware collection of free video-source links for all six active PUI89 products, separated into:
1. **Website library** — presentation and illustrative footage.
2. **AI research library** — candidate material for research, annotation and model experiments, only where the rights explicitly permit the intended use.
3. **Validation library** — independently sourced footage for controlled evaluation. Stock footage is not proof of product performance or field validation.

**Important:** A free-to-view or free-to-download video is not automatically licensed for AI training, dataset redistribution, commercial deployment, or use in safety claims. Verify the individual asset page and applicable terms before any use.

## Portfolio coverage / ผลิตภัณฑ์ทั้ง 6

### 01 — Coconut Harvest AI
**Collection topics:** coconut orchard scenes; coconut bunches and fruit; harvesting workflows; maturity appearance; occlusion, lighting and viewpoint variation.

- [Pexels — coconut farm videos](https://www.pexels.com/search/videos/coconut%20farm/)
- [Pexels — coconut videos](https://www.pexels.com/search/videos/coconut/)
- [Pixabay — coconut videos](https://pixabay.com/videos/search/coconut/)
- [AI in Agriculture — dataset discovery](https://aiinagriculture.org/datasets/)

**Research checks:** Confirm that the footage actually depicts coconuts (not generic palms), record maturity labels only when supported by qualified annotation, and do not infer ground truth from appearance alone.

### 02 — PUI89 Sentinel
**Collection topics:** general security monitoring; facility inspection; access-area observation; object/person tracking; anomaly and event-recognition scenarios.

- [Pexels — security camera videos](https://www.pexels.com/search/videos/security%20camera/)
- [Pexels — surveillance videos](https://www.pexels.com/search/videos/surveillance/)
- [Pixabay — surveillance videos](https://pixabay.com/videos/search/surveillance/)
- [Kinetics research dataset portal](https://deepmind.google/discover/blog/kinetics/)
 
**Scope boundary:** General security and evidence-aware monitoring only. Narcotics detection/screening, related datasets, X-ray screening and forensic spectra are excluded from the active Sentinel scope.

**Research checks:** Review privacy, consent, identifiable-person, surveillance and jurisdictional restrictions. Do not repurpose footage for identity recognition or other purposes not permitted by the source rights.

### 03 — AI HOME
**Collection topics:** indoor mobile robots; room and corridor navigation; obstacle encounters; human-aware interaction; household environments.

- [Pexels — indoor robot videos](https://www.pexels.com/search/videos/robot/)
- [Pexels — smart home videos](https://www.pexels.com/search/videos/smart%20home/)
- [Pixabay — robot videos](https://pixabay.com/videos/search/robot/)
- [Habitat Matterport 3D Research Dataset (HM3D)](https://aihabitat.org/datasets/hm3d/)

**Research checks:** HM3D is a research dataset, not automatically cleared for commercial product use. Review its current terms and any source-specific restrictions before use.

### 04 — AI NOMAD
**Collection topics:** outdoor mobile robots; paths and trails; grass, gravel and uneven terrain; changing illumination and weather; localization and navigation scenes.

- [Pexels — outdoor robot videos](https://www.pexels.com/search/videos/robot%20outdoor/)
- [Pexels — trail videos](https://www.pexels.com/search/videos/trail/)
- [Pixabay — nature trail videos](https://pixabay.com/videos/search/nature%20trail/)
- [TartanAir dataset](https://tartanair.org/)

**Research checks:** TartanAir is a candidate for simulation/visual-navigation research, not a substitute for real-world validation. Verify the current dataset licence, attribution requirements and permitted use.

### 05 — AI Robot Car
**Collection topics:** road scenes; vehicles and pedestrians; intersections; road hazards; rain and low-light scenes; road-surface and flood-context footage.

- [Pexels — traffic videos](https://www.pexels.com/search/videos/traffic/)
- [Pexels — dashcam videos](https://www.pexels.com/search/videos/dashcam/)
- [Pixabay — road videos](https://pixabay.com/videos/search/road/)
- [Waymo Open Dataset](https://waymo.com/open/)
- [nuScenes dataset](https://www.nuscenes.org/)

**Research checks:** Waymo and nuScenes have dataset-specific terms and restrictions. Do not assume commercial use, redistribution, or training rights. Record the exact version and terms.

**Safety boundary:** Research footage and AI warnings do not establish autonomous-driving capability. No autonomous steering, throttle or braking is implied.

### 06 — EasyRide AI Step-Through Scooter
**Collection topics:** scooters and motorcycles; rider viewpoint; two-wheel traffic interactions; road hazards; wet roads; visibility and weather variation.

- [Pexels — motorcycle videos](https://www.pexels.com/search/videos/motorcycle/)
- [Pexels — scooter videos](https://www.pexels.com/search/videos/scooter/)
- [Pexels — road traffic videos](https://www.pexels.com/search/videos/road%20traffic/)
- [Pixabay — motorcycle videos](https://pixabay.com/videos/search/motorcycle/)
- [nuScenes dataset](https://www.nuscenes.org/) — only if the relevant sensor data and terms fit the research question.

**Research checks:** Confirm the clip depicts a two-wheel vehicle and relevant rider/road context. Car-only footage must not be represented as scooter validation.

**Safety boundary:** No autonomous throttle, steering or braking is implied.

## Shared source and licence registry / ทะเบียนแหล่งข้อมูลและใบอนุญาต

For every individual clip or dataset, create a record with these fields:

| Field | Required record |
|---|---|
| Asset ID | Stable internal identifier |
| Product | One or more of the six products |
| Library | Website / AI Research / Validation |
| Original asset URL | Exact page for the individual clip or dataset |
| Publisher / creator | Original uploader or dataset owner |
| Country / origin | Evidence for publisher and data origin; mark unknown if unverified |
| Access date | Date checked (UTC) |
| Exact licence | Name and URL of the licence/terms |
| Website use | Allowed / prohibited / unclear |
| AI training | Allowed / prohibited / unclear |
| Commercial use | Allowed / prohibited / unclear |
| Redistribution | Allowed / prohibited / unclear |
| Privacy / releases | Relevant people, property, trademarks and consent checks |
| Technical details | Duration, resolution, FPS, modalities, where available |
| Decision | Verified / Pending / Rejected |
| Reviewer notes | Restrictions, evidence and rationale |

**Do not mark a source Verified** until the individual asset's provenance and the intended use are checked. A platform-wide licence does not resolve every third-party privacy, trademark, property, or publicity right.

## Initial platform-level licence notes

These notes describe platform terms only; they do not approve any individual clip for AI training.

- [Pexels licence](https://www.pexels.com/license/) — states free personal and commercial use for its content, subject to restrictions. [Pexels terms](https://www.pexels.com/terms-of-service/) also prohibit scraping, bulk/systematic copying and unauthorized data extraction, including for machine-learning purposes. **Do not use Pexels as an AI-training data source without separate explicit permission and legal review.**
- [Pixabay Content License Summary](https://pixabay.com/service/license-summary/) — permits free use and adaptation subject to prohibited-use restrictions and third-party rights. It does not by itself settle whether a particular asset may be used for AI training.
- [Mixkit licence](https://mixkit.co/license/) — different items may carry different licences. Some stock videos have a Restricted License that excludes commercial projects. Check each clip's displayed licence; exclude restricted clips from commercial use.

## Non-Chinese-origin filter

- Exclude sources, publishers, datasets, collection pipelines and model/data providers with Chinese origin or unclear provenance.
- Do not infer origin from a website domain, language, hosting provider or contributor name alone.
- Record the publisher, institution, dataset creators and collection provenance where available.
- If origin cannot be established confidently, mark **Pending — origin unverified** and do not approve the asset.
- This filter is a provenance requirement, not a claim that every item on a listed platform has the same origin.

## Acceptance workflow

1. Discover candidate links only.
2. Open the individual asset page and identify the original creator/publisher.
3. Read the exact licence and terms applicable to that asset.
4. Check website, research, AI-training, commercial and redistribution rights separately.
5. Check privacy, consent, model/property releases and visible trademarks where relevant.
6. Verify non-Chinese origin and document evidence.
7. Record technical metadata and known limitations.
8. Assign **Verified**, **Pending** or **Rejected**.
9. Obtain explicit approval before downloading or using any asset.
10. Preserve source URL, licence snapshot/reference and review date for auditability.

## Status

- Product coverage: **6 / 6**
- Library categories defined: **3**
- Individual video assets verified: **0**
- Downloads / installations performed: **0**
- AI-training permissions confirmed: **0**
- Commercial-use permissions confirmed for individual clips: **0**

This is an initial link-only discovery register. It is not a dataset, a download manifest, a claim of completed licence review, or evidence of product performance.

---

## ภาษาไทย

### ขอบเขต
คลังนี้รวบรวมลิงก์แหล่งวิดีโอฟรีสำหรับผลิตภัณฑ์ PUI89 ทั้ง 6 รายการ โดยแบ่งเป็นวิดีโอสำหรับเว็บไซต์ งานวิจัย AI และการทดสอบ/ประเมินผล

### หลักเกณฑ์
- ใช้แหล่งข้อมูลที่ตรวจสอบประเทศต้นทาง ผู้เผยแพร่ และเจ้าของข้อมูลได้
- ไม่ใช้แหล่งข้อมูลที่มีต้นกำเนิดจากจีน หรือแหล่งที่ไม่สามารถยืนยันที่มาได้
- ตรวจสอบสิทธิ์การใช้งานรายคลิป แยกการใช้บนเว็บไซต์ การฝึก AI การใช้เชิงพาณิชย์ และการเผยแพร่ต่อ
- วิดีโอที่ดูหรือดาวน์โหลดได้ฟรี ไม่ได้หมายความว่าอนุญาตให้นำไปฝึก AI หรือใช้เชิงพาณิชย์ได้โดยอัตโนมัติ
- ห้ามดาวน์โหลด ติดตั้ง สมัครบัญชี ใช้ API แบบเสียค่าใช้จ่าย หรือเก็บข้อมูลจำนวนมากโดยไม่ได้รับอนุญาตอย่างชัดเจน
- ไม่ใช้วิดีโอประชาสัมพันธ์เป็นหลักฐานยืนยันประสิทธิภาพของผลิตภัณฑ์

### ผลิตภัณฑ์ที่ครอบคลุม
1. Coconut Harvest AI — สวนมะพร้าว ผลมะพร้าว การเก็บเกี่ยว และการประเมินความแก่
2. PUI89 Sentinel — การเฝ้าระวังทั่วไป การตรวจสอบความผิดปกติ และการติดตามเหตุการณ์ โดยไม่รวมงานคัดกรองยาเสพติด
3. AI HOME — หุ่นยนต์ภายในบ้าน การนำทาง สิ่งกีดขวาง และการทำงานร่วมกับมนุษย์
4. AI NOMAD — หุ่นยนต์กลางแจ้ง สภาพภูมิประเทศ เส้นทาง และการนำทาง
5. AI Robot Car — ถนน การจราจร รถยนต์ คนเดินเท้า และอันตรายบนถนน
6. EasyRide AI Step-Through Scooter — รถจักรยานยนต์/สกูตเตอร์ ผู้ขับขี่ การจราจร และสภาพถนน

### สถานะเริ่มต้น
- ครอบคลุมผลิตภัณฑ์ 6/6 รายการ
- กำหนดหมวดคลังข้อมูล 3 หมวดแล้ว
- ยังไม่มีคลิปที่ผ่านการตรวจสอบรายรายการ
- ยังไม่มีการดาวน์โหลดหรือติดตั้ง
- ยังไม่มีการอนุมัติสิทธิ์การฝึก AI สำหรับคลิปรายรายการ

**สถานะนี้เป็นเพียงทะเบียนลิงก์สำหรับค้นหาและตรวจสอบ ไม่ใช่การรับรองสิทธิ์ของคลิปหรือการยืนยันประสิทธิภาพของผลิตภัณฑ์**
