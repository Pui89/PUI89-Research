# Global Real-World Image and Dataset Protocol

**Record date:** 2026-11-25  
**Status:** Collection and curation protocol only. No global images have been downloaded, licensed, labelled or approved by this document.

## English

### Objective

Build a geographically and environmentally diverse evidence base for the six PUI89 research tracks. “Global” means deliberate coverage across relevant countries, climates, sites, seasons, camera types, viewpoints and operating conditions—not merely downloading a large image count. Use only sources whose provenance and terms can be checked. Avoid sources/models with unclear provenance and do not use Chinese-origin tools or models under the programme's current policy.

### Candidate discovery sources

These are discovery starting points, not blanket permissions:

- [Google Open Images](https://storage.googleapis.com/openimages/web/index.html) — object annotations and images; check version-specific licence and image-level conditions.
- [COCO](https://cocodataset.org/) — common detection/segmentation benchmark; use as a benchmark, not a substitute for field-domain evidence.
- [Wikimedia Commons](https://commons.wikimedia.org/) — inspect each file page for author, exact licence, attribution and restrictions.
- [Openverse](https://openverse.org/) — media discovery; verify the original hosting page and licence for every asset.
- [GBIF](https://www.gbif.org/) — biodiversity media and occurrence context; inspect each record's media rights and taxonomic correctness.
- [iNaturalist](https://www.inaturalist.org/) — potentially useful biological observations; check observation-level licence, quality grade, taxon, location privacy and image rights.
- [PlantVillage](https://doi.org/10.1038/s41597-018-0022-9) — plant disease image dataset reference; not a coconut maturity dataset and not automatically suitable for other tasks.

Do not scrape search-engine thumbnails or social-media images. Do not assume that “publicly visible”, “Creative Commons”, or “downloadable” automatically permits model training, commercial use, redistribution or publication. Check the exact licence and applicable law for each image and intended use. If terms are ambiguous, exclude the asset until written permission or legal review resolves it.

### Six-project data plan

| Project | Required real-world image/data strata | Important labels / metadata |
|---|---|---|
| Coconut Harvest AI | Multiple coconut-growing regions; orchard/site; cultivar where known; season; young green, mature green, yellow, brown; shade/backlight/rain; near/far and occlusion; multiple cameras. | Fruit ID, tree/orchard/session group, maturity ground truth, annotator, confidence, camera, date/season, lighting, distance. |
| PUI89 Sentinel | Only legally permitted facility/event data; varied indoor/outdoor scenes, camera positions, lighting and benign/rare event conditions. | Event definition, time interval, modality, privacy treatment, source rights, reviewer decision, false-alert/missed-event label. No excluded narcotics/X-ray/forensic data. |
| AI HOME | Indoor rooms across layouts, floors, lighting, furniture, people-presence conditions and camera heights. | Scene, traversability/obstacle class, human-presence privacy handling, viewpoint, floor/room group, lighting, annotation guide. |
| AI NOMAD | Outdoor paths and terrain, vegetation, gravel, mud, slopes, weather, day/night, shadows and sensor viewpoints. | Terrain/obstacle class, weather, lighting, location group, sensor, traversability ground truth and hazard annotation. |
| AI Robot Car | Public-road scenes where collection/use is lawful; countries, road types, traffic, weather, day/night and camera viewpoints. | Road-user/object classes, hazard/event, time, route/session, jurisdiction, weather, camera, anonymisation and licence. |
| EasyRide Scooter | Scooter/motorcycle rider-view footage and stills, with lawful permissions; road types, traffic, weather, day/night, helmet/camera mounting and viewpoint variation. | Rider-view object/hazard classes, event/time, route/session, camera position, road/weather, privacy and rights. Car datasets alone are not sufficient. |

### Train / validation / test rules

1. Create an immutable asset manifest before annotation or model training.
2. Record source URL, publisher/creator, capture date (if known), download/access date, licence text/URL, permitted purposes, attribution, geographic metadata at a privacy-safe level, file hash and dataset version.
3. Group related images before splitting: same tree/orchard/session, observation, video, route, person, vehicle, room/site, camera burst or near-duplicate cluster must not cross partitions.
4. Use site-, orchard-, route-, session- or geography-held-out evaluation when the scientific question is generalisation to unseen environments.
5. Keep train, validation and test manifests separate. Validation guides model selection; final test remains sealed until the protocol and model are frozen.
6. Avoid random frame-level splits for video or burst images. Use time- or group-based splits.
7. Report geographic and environmental coverage, class balance, missing strata and sampling bias. Do not call a dataset “global” if it represents only a few sources or countries.
8. Use a second independent annotator on a suitable subset; adjudicate disagreements and report agreement with a metric appropriate to the labels.
9. Maintain a separate external test set if rights and sample size permit. Never move test examples into training after seeing results without documenting a new study/version.
10. Use public benchmark datasets for reproducible comparison, then separately evaluate on rights-cleared target-domain data.

### Dataset quality and release gates

- **D0 — Discovery:** source identified; no use yet.
- **D1 — Rights cleared:** exact licence/permission and intended purposes verified.
- **D2 — Privacy/ethics cleared:** consent/legal basis, privacy and retention reviewed.
- **D3 — Curated:** metadata, hashes, duplicate checks and exclusions recorded.
- **D4 — Annotated:** guide versioned, annotators trained, quality reviewed and disagreements adjudicated.
- **D5 — Split frozen:** leakage groups and train/validation/test manifests fixed.
- **D6 — Approved for experiment:** protocol, dataset version, access and analysis plan signed off.
- **D7 — Publication-ready evidence:** all claims, figures, licences and reproducibility materials reviewed for release.

A source or image may be usable for internal research but not for publication figures or redistribution. Track those permissions separately.

### Image collection status as of 2026-11-25

- Global source catalogue: **planned; not yet verified as a complete catalogue**.
- Image assets acquired and rights-cleared: **not yet recorded in this repository**.
- Annotation completed: **not yet recorded**.
- Frozen train/validation/test manifests: **not yet recorded**.
- Real-world model training or test results: **not claimed**.

Do not replace “not yet recorded” with zero, complete or failed unless a measured inventory supports that status.

---

## ภาษาไทย

### วัตถุประสงค์

สร้างฐานหลักฐานภาพและข้อมูลจากโลกจริงที่มีความหลากหลายทางภูมิศาสตร์และสภาพแวดล้อมสำหรับงานวิจัย PUI89 ทั้ง 6 โครงการ คำว่า “ทั่วโลก” หมายถึงการวางแผนครอบคลุมประเทศ ภูมิอากาศ สถานที่ ฤดูกาล กล้อง มุมมอง และสภาพการทำงานที่เกี่ยวข้อง ไม่ใช่เพียงดาวน์โหลดภาพให้มีจำนวนมาก ต้องใช้เฉพาะแหล่งที่ตรวจสอบที่มาและเงื่อนไขได้ หลีกเลี่ยงเครื่องมือหรือโมเดลที่ไม่ทราบแหล่งที่มา และไม่ใช้เครื่องมือหรือโมเดลที่มีต้นกำเนิดจากจีนตามนโยบายปัจจุบันของโครงการ

### แหล่งค้นหาที่เสนอ

แหล่งเหล่านี้เป็นจุดเริ่มต้นในการค้นหา ไม่ใช่การอนุญาตให้ใช้ข้อมูลทั้งหมดโดยอัตโนมัติ:

- [Google Open Images](https://storage.googleapis.com/openimages/web/index.html) — ภาพและป้ายกำกับวัตถุ ต้องตรวจสอบใบอนุญาตตามรุ่นและเงื่อนไขรายภาพ
- [COCO](https://cocodataset.org/) — ชุด Benchmark ด้าน Detection/Segmentation ไม่ใช้แทนข้อมูลภาคสนามของโดเมนจริง
- [Wikimedia Commons](https://commons.wikimedia.org/) — ตรวจสอบผู้สร้าง ใบอนุญาต การให้เครดิต และข้อจำกัดในหน้าไฟล์ทุกภาพ
- [Openverse](https://openverse.org/) — ใช้ค้นหาสื่อ แต่ต้องตรวจสอบหน้าแหล่งต้นฉบับและใบอนุญาตรายไฟล์
- [GBIF](https://www.gbif.org/) — ข้อมูลความหลากหลายทางชีวภาพและภาพประกอบ ต้องตรวจสอบสิทธิ์สื่อและความถูกต้องของชนิดสิ่งมีชีวิต
- [iNaturalist](https://www.inaturalist.org/) — ข้อมูลสังเกตสิ่งมีชีวิต ต้องตรวจสอบใบอนุญาตรายรายการ คุณภาพข้อมูล ชนิดสิ่งมีชีวิต ความเป็นส่วนตัวของตำแหน่ง และสิทธิ์ภาพ
- [PlantVillage](https://doi.org/10.1038/s41597-018-0022-9) — แหล่งอ้างอิงชุดภาพโรคพืช ไม่ใช่ชุดข้อมูลระดับความแก่มะพร้าว และไม่ควรนำมาใช้แทนโดยไม่มีเหตุผล

ห้ามดึงภาพตัวอย่างจาก Search Engine หรือภาพจาก Social Media โดยไม่ตรวจสอบสิทธิ์ ห้ามถือว่าภาพที่มองเห็นสาธารณะ มี Creative Commons หรือดาวน์โหลดได้ หมายถึงได้รับอนุญาตให้ฝึกโมเดล ใช้เชิงพาณิชย์ เผยแพร่ต่อ หรือใช้ในบทความโดยอัตโนมัติ ต้องตรวจสอบใบอนุญาตและกฎหมายที่เกี่ยวข้อง หากเงื่อนไขไม่ชัดเจนให้พักการใช้จนกว่าจะได้รับอนุญาตเป็นลายลักษณ์อักษรหรือผ่านการตรวจสอบทางกฎหมาย

### แผนข้อมูลทั้ง 6 โครงการ

| โครงการ | กลุ่มภาพ/ข้อมูลโลกจริงที่ต้องครอบคลุม | ป้ายกำกับและข้อมูลประกอบ |
|---|---|---|
| Coconut Harvest AI | แหล่งปลูกมะพร้าวหลายภูมิภาค สวน/แปลง พันธุ์เมื่อทราบ ฤดูกาล ระดับ young green, mature green, yellow, brown แสงเงา/ย้อนแสง/ฝน ระยะใกล้ไกล สิ่งบดบัง และกล้องหลายชนิด | รหัสผล/ต้น/สวน/รอบเก็บภาพ Ground Truth ระดับความแก่ ผู้กำกับป้ายกำกับ ความมั่นใจ กล้อง วันที่ ฤดูกาล แสง และระยะ |
| PUI89 Sentinel | ข้อมูลสถานที่/เหตุการณ์ที่ได้รับอนุญาตตามกฎหมายเท่านั้น ครอบคลุมฉากใน/นอกอาคาร ตำแหน่งกล้อง แสง และเหตุการณ์ปกติ/เหตุการณ์หายาก | นิยามเหตุการณ์ ช่วงเวลา รูปแบบข้อมูล การคุ้มครองความเป็นส่วนตัว สิทธิ์แหล่งข้อมูล และผลตรวจทาน ไม่รวมข้อมูลยาเสพติด/X-ray/นิติวิทยาศาสตร์ที่ถูกยกเว้น |
| AI HOME | ห้องและอาคารหลายรูปแบบ พื้น แสง เฟอร์นิเจอร์ การมีบุคคล และระดับความสูงของกล้อง | ฉาก พื้นที่เดินได้/สิ่งกีดขวาง การคุ้มครองข้อมูลบุคคล มุมมอง กลุ่มห้อง/อาคาร แสง และคู่มือกำกับป้ายกำกับ |
| AI NOMAD | ทางเดินและพื้นผิวกลางแจ้ง พืช กรวด โคลน ทางลาด สภาพอากาศ กลางวัน/กลางคืน เงา และมุมมองเซนเซอร์ | ประเภทพื้นผิว/สิ่งกีดขวาง สภาพอากาศ แสง กลุ่มพื้นที่ เซนเซอร์ Ground Truth การเดินผ่านได้ และอันตราย |
| AI Robot Car | ฉากถนนสาธารณะที่เก็บและใช้ได้โดยชอบด้วยกฎหมาย หลายประเทศ ประเภทถนน การจราจร สภาพอากาศ กลางวัน/กลางคืน และมุมกล้อง | ประเภทยานพาหนะ/ผู้ใช้ถนน เหตุอันตราย เวลา เส้นทาง/รอบเก็บข้อมูล เขตอำนาจ สภาพอากาศ กล้อง การปกปิดตัวตน และสิทธิ์ |
| EasyRide Scooter | ภาพ/วิดีโอจากมุมมองผู้ขับขี่สกูตเตอร์/รถจักรยานยนต์ที่ได้รับอนุญาต ครอบคลุมถนน การจราจร อากาศ กลางวัน/กลางคืน หมวกกันน็อก ตำแหน่งติดกล้อง และมุมมอง | วัตถุ/อันตรายจากมุมมองผู้ขับขี่ เหตุการณ์/เวลา เส้นทาง/รอบเก็บภาพ ตำแหน่งกล้อง ถนน/อากาศ ความเป็นส่วนตัวและสิทธิ์ ข้อมูลรถยนต์เพียงอย่างเดียวไม่เพียงพอ |

### กฎแบ่ง Train / Validation / Test

1. สร้าง Manifest ของไฟล์ที่ไม่เปลี่ยนแปลงก่อนกำกับป้ายกำกับหรือฝึกโมเดล
2. บันทึก URL แหล่งข้อมูล ผู้เผยแพร่/ผู้สร้าง วันที่ถ่าย (ถ้าทราบ) วันที่เข้าถึง/ดาวน์โหลด ข้อความและ URL ใบอนุญาต วัตถุประสงค์ที่อนุญาต เครดิต พื้นที่ในระดับที่ไม่กระทบความเป็นส่วนตัว Hash และเวอร์ชันชุดข้อมูล
3. จัดกลุ่มภาพที่เกี่ยวข้องก่อนแบ่งชุด เช่น ต้น/สวน/รอบเก็บภาพเดียวกัน วิดีโอ เส้นทาง บุคคล รถ ห้อง/สถานที่ กล้องต่อเนื่อง หรือภาพซ้ำ ต้องไม่ข้ามชุดข้อมูล
4. ใช้การแยกตามสวน สถานที่ เส้นทาง รอบเก็บภาพ หรือภูมิศาสตร์ เมื่อคำถามวิจัยต้องการทดสอบการใช้กับสภาพแวดล้อมที่ไม่เคยพบ
5. แยก Manifest ของ Train, Validation และ Test ให้ชัด Validation ใช้เลือกโมเดล ส่วน Test สุดท้ายต้องปิดไว้จนกว่าโพรโทคอลและโมเดลจะถูกกำหนด
6. หลีกเลี่ยงการสุ่มแยกเฟรมจากวิดีโอหรือภาพถ่ายต่อเนื่อง ให้ใช้การแบ่งตามเวลา/กลุ่ม
7. รายงานความครอบคลุมภูมิศาสตร์และสภาพแวดล้อม สัดส่วนคลาส กลุ่มข้อมูลที่ขาด และอคติการสุ่มตัวอย่าง ห้ามเรียกชุดข้อมูลว่า “ทั่วโลก” หากมีเพียงไม่กี่แหล่งหรือไม่กี่ประเทศ
8. ใช้ผู้กำกับป้ายกำกับอิสระคนที่สองกับข้อมูลส่วนที่เหมาะสม ตัดสินข้อขัดแย้ง และรายงานค่าความสอดคล้องที่เหมาะกับชนิดป้ายกำกับ
9. จัดชุดทดสอบภายนอกแยกต่างหากเมื่อสิทธิ์และจำนวนข้อมูลเพียงพอ ห้ามย้ายข้อมูล Test ไป Train หลังเห็นผลโดยไม่บันทึกเป็นการศึกษา/เวอร์ชันใหม่
10. ใช้ Benchmark สาธารณะเพื่อเปรียบเทียบที่ทำซ้ำได้ แล้วประเมินแยกบนข้อมูลโดเมนเป้าหมายที่ได้รับอนุญาต

### เกณฑ์คุณภาพและอนุมัติชุดข้อมูล

- **D0 — Discovery:** พบแหล่งข้อมูลแล้ว แต่ยังไม่ได้รับอนุญาตให้ใช้
- **D1 — Rights cleared:** ตรวจสอบใบอนุญาต/การอนุญาตและวัตถุประสงค์แล้ว
- **D2 — Privacy/ethics cleared:** ตรวจสอบความยินยอม/ฐานกฎหมาย ความเป็นส่วนตัว และการเก็บรักษาแล้ว
- **D3 — Curated:** บันทึก Metadata, Hash, การตรวจภาพซ้ำ และการคัดออกแล้ว
- **D4 — Annotated:** มีคู่มือเวอร์ชัน ผู้กำกับป้ายกำกับผ่านการฝึก ตรวจคุณภาพ และตัดสินข้อขัดแย้งแล้ว
- **D5 — Split frozen:** กำหนดกลุ่มป้องกัน Leakage และ Manifest ของ Train/Validation/Test แล้ว
- **D6 — Approved for experiment:** อนุมัติโพรโทคอล เวอร์ชันชุดข้อมูล สิทธิ์เข้าถึง และแผนวิเคราะห์แล้ว
- **D7 — Publication-ready evidence:** ตรวจสอบข้อกล่าวอ้าง รูปประกอบ ใบอนุญาต และเอกสารทำซ้ำก่อนเผยแพร่แล้ว

ภาพบางภาพอาจใช้ภายในงานวิจัยได้ แต่ห้ามใช้เป็นรูปในบทความหรือเผยแพร่ต่อ ต้องแยกบันทึกสิทธิ์แต่ละวัตถุประสงค์

### สถานะการรวบรวมภาพ ณ 25 พฤศจิกายน 2026

- รายการแหล่งข้อมูลทั่วโลก: **อยู่ในแผน ยังไม่ยืนยันว่าเป็นรายการที่ตรวจสอบครบถ้วน**
- ภาพที่ได้มาและผ่านการตรวจสิทธิ์: **ยังไม่มีบันทึกใน Repository นี้**
- การกำกับป้ายกำกับเสร็จสิ้น: **ยังไม่มีบันทึก**
- Manifest ของ Train/Validation/Test ที่ล็อกแล้ว: **ยังไม่มีบันทึก**
- ผลฝึก/ทดสอบโมเดลจากโลกจริง: **ยังไม่มีการกล่าวอ้าง**

ห้ามเปลี่ยนสถานะ “ยังไม่มีการบันทึก” เป็นศูนย์ เสร็จสมบูรณ์ หรือล้มเหลว หากไม่มีบัญชีรายการที่ตรวจวัดรองรับ
