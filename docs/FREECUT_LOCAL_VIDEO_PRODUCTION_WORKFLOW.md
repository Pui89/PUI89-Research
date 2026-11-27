# PUI89 FreeCut — Local Video Production Workflow

**Status:** Documentation and workflow specification only. FreeCut has not been installed, downloaded, forked, executed, security-audited or integrated as a software dependency by this repository.

**Purpose:** Use the independent, open-source [FreeCut](https://github.com/walterlow/freecut) browser editor as an optional local-first tool for producing research explainers, methods walkthroughs, simulation recordings and project communication videos.

**Official links:** [FreeCut project](https://github.com/walterlow/freecut) · [FreeCut web app](https://freecut.net/) · [Official documentation](https://freecut.net/docs)

## 1. Scope and separation of evidence

FreeCut is a communication and media-editing tool. It is not a research compute environment, dataset repository, experiment tracker, annotation ground-truth system or scientific validation method.

PUI89's website documents seven product communication tracks: Coconut Harvest AI, Extreme Flood Rescue AI, Sentinel, AI HOME, AI NOMAD, PUI89 AI Global SUV and AI Step-Through Scooter / EasyRide. The active PUI89-Research programme currently defines six research studies; Extreme Flood Rescue AI is not part of that six-study publication scope. Do not change the research portfolio count or imply that a video-production use case creates a new research study.

Every video must distinguish clearly among:
- Concept art and design intent.
- Synthetic or simulated scenes and outputs.
- Recorded bench or controlled-test observations.
- Measured physical or field results.
- Independently reviewed or verified evidence.

A polished video, animation, simulation or rendered overlay is never evidence of real-world product performance, safety, field validation, certification, scientific novelty or commercial readiness.

## 2. Local-first operating requirements

- Use a local browser workspace and locally stored source media where supported by the current FreeCut build.
- Do not upload confidential, personal, restricted, unpublished or rights-uncleared source material to cloud editors, remote AI providers or public model services.
- Before enabling any AI function, identify the exact provider, model, model revision, licence, model origin, processing location and whether a first-run model download is required.
- Prefer explicitly on-device inference. A browser-based interface alone does not prove that inference is local.
- Review browser permissions, extensions, network requests and optional integrations before using sensitive material. Do not assume the complete application is offline.
- No paid API, subscription, hosted inference, metered service or cloud GPU is part of this workflow.
- Do not install packages, download software or model weights, create accounts, connect external services or purchase hardware under this document. Each requires separate explicit approval.
- Retain project files, source-media references, export settings and local backups under user control. Confirm backup integrity before deleting temporary files.

## 3. Suitable editorial use cases

| Product / research track | Suitable video outputs | Evidence boundary |
|---|---|---|
| Coconut Harvest AI | Four maturity-class explainers; annotation and evaluation-method walkthroughs | Label illustrative imagery and simulated examples; measured agronomic results require traceable data |
| Extreme Flood Rescue AI | Flood scenario and rescue-system simulation walkthroughs | Clearly mark simulation duration, assumptions and unvalidated physical elements |
| Sentinel | Environmental inspection concept, sensor architecture and human-review workflow | No identity, guilt or threat-certainty conclusions; no excluded narcotics/X-ray/forensic screening scope |
| AI HOME | Indoor assistant concept, perception workflow and supervised scenarios | Simulation and physical trials remain separate |
| AI NOMAD | Outdoor mobility concept, terrain scenarios and perception research explainers | Simulation does not establish physical navigation capability |
| PUI89 AI Global SUV | Driver-support concept, road-scene research and Full HEV engineering explainers | AI is advisory; no autonomous steering, throttle or braking claims |
| AI Step-Through Scooter / EasyRide | Step-through concept, rider-view perception and safety-requirement explainers | No autonomous steering, throttle, braking or balance claims |

## 4. Recommended production sequence

1. Define the audience, purpose, intended claims and evidence category before editing.
2. Create a local project folder and keep an untouched copy of original media.
3. Record each asset's source, creator, licence, consent/permission, capture date and permitted use.
4. Build a short storyboard. Add on-screen labels for concept, simulation, measured result and unverified assumption.
5. Edit a short, low-resolution test before a full project. Check audio sync, text legibility, transitions, rendering and export.
6. If using AI, test only non-sensitive material first and document the exact local provider/model and resource use.
7. Export a review copy; inspect playback, dimensions, frame rate, audio, captions, codec and file integrity.
8. Have a human reviewer compare every factual statement and visual claim against source evidence.
9. Preserve the editable project, source/rights register, export settings and review notes alongside the final media.

## 5. Research integrity and reproducibility

For any video accompanying a paper, dataset release or experiment report:

- Cite the relevant protocol, dataset card, experiment record, code revision and result source in the description or end credits.
- Do not use generated visuals as a substitute for dataset samples, ground truth, measured plots or original evidence.
- Do not alter axes, crop failures, hide uncertainty or selectively edit results in a way that changes interpretation.
- Retain an unedited source recording for material demonstrations where rights and privacy permit.
- Record all generated or AI-assisted media, model/provider details and substantial edits.
- Use only rights-cleared music, fonts, images, footage and logos.
- Blur or omit personal, confidential, sensitive and unauthorised information.
- Keep a claim-to-evidence review record for all quantitative, safety or performance statements.

FreeCut project files and video exports are communication artefacts. They do not replace experiment records, source datasets, statistical analysis, source-code review or the Evidence Passport.

## 6. Browser and hardware compatibility checks

FreeCut's upstream project documentation describes a browser-based workflow using WebGPU, WebCodecs and browser storage/file APIs, and recommends current Chromium-based browsers. Actual support varies by browser version, operating system, GPU driver, codec and hardware.

The previously identified PUI89 workstation (Acer Nitro AN515-57, Intel Core i7-11800H, 16 GB RAM and NVIDIA RTX 3050 Laptop GPU) is a candidate for a small trial, not a verified compatibility result. Before relying on it, manually check browser WebGPU availability, available VRAM, thermals, free disk space, media decode support and export speed. Begin with short 1080p clips or proxies.

Codec/container names such as MP4, WebM, MOV and MKV do not guarantee that every codec or encoder is available on every browser/device combination. Verify the actual export options and test the output on a separate player.

## 7. Adoption gate

FreeCut may be listed as an optional recommended editor, not a mandatory dependency. Before sensitive or regular use, complete and record:

- [ ] Current upstream repository, release/commit and MIT licence checked.
- [ ] Application source/build provenance reviewed.
- [ ] Exact AI providers and model licences/origin reviewed.
- [ ] Local vs remote processing behaviour checked for each enabled feature.
- [ ] Browser permissions and network behaviour reviewed.
- [ ] Small non-sensitive sample project exported and verified.
- [ ] Local workspace backup and recovery checked.
- [ ] Accessibility, captions and human factual review completed.

**Current gate status: NOT ASSESSED.** This repository change documents the intended workflow only. It does not certify FreeCut's security, privacy, performance, licence compatibility of every model, or suitability for confidential research.

---

# ภาษาไทย

## PUI89 FreeCut — แนวทางผลิตวิดีโอภายในเครื่อง

**สถานะ:** เพิ่มเอกสารและข้อกำหนด Workflow เท่านั้น Repository นี้ยังไม่ได้ติดตั้ง ดาวน์โหลด Fork เรียกใช้งาน ตรวจสอบความปลอดภัย หรือผนวก FreeCut เป็น Software Dependency

**วัตถุประสงค์:** ใช้ [FreeCut](https://github.com/walterlow/freecut) ซึ่งเป็นโปรแกรมตัดต่อวิดีโอ Open Source ผ่าน Browser เป็นเครื่องมือเสริมสำหรับสร้างวิดีโออธิบายงานวิจัย ขั้นตอนวิธี การจำลองสถานการณ์ และการสื่อสารโครงการ โดยเน้นจัดเก็บสื่อไว้ในเครื่อง

**ลิงก์ทางการ:** [โครงการ FreeCut](https://github.com/walterlow/freecut) · [เว็บแอป FreeCut](https://freecut.net/) · [คู่มือทางการ](https://freecut.net/docs)

### 1. ขอบเขตและการแยกประเภทหลักฐาน

FreeCut เป็นเครื่องมือสื่อสารและตัดต่อสื่อ ไม่ใช่สภาพแวดล้อมประมวลผลงานวิจัย คลัง Dataset ระบบบันทึกการทดลอง ระบบ Ground Truth หรือวิธีตรวจสอบความถูกต้องทางวิทยาศาสตร์

เว็บไซต์ PUI89 มีแนวทางสื่อสารผลิตภัณฑ์ 7 รายการ ได้แก่ Coconut Harvest AI, Extreme Flood Rescue AI, Sentinel, AI HOME, AI NOMAD, PUI89 AI Global SUV และ AI Step-Through Scooter / EasyRide ขณะที่ PUI89-Research กำหนดงานวิจัยที่ดำเนินการอยู่ 6 เรื่อง โดย Extreme Flood Rescue AI ไม่อยู่ในขอบเขตแผนตีพิมพ์ 6 เรื่องนี้ การเพิ่ม Workflow วิดีโอไม่ได้เปลี่ยนจำนวนโครงการวิจัย

วิดีโอทุกชิ้นต้องแยกให้ชัดเจนระหว่าง:
- ภาพแนวคิดและเจตนารมณ์การออกแบบ
- ฉากและผลลัพธ์สังเคราะห์หรือจำลองสถานการณ์
- การบันทึกจากการทดสอบบนโต๊ะหรือการทดสอบควบคุม
- ผลการวัดจริงทางกายภาพหรือภาคสนาม
- หลักฐานที่ผ่านการทบทวนหรือยืนยันโดยอิสระ

วิดีโอที่ตัดต่อสวยงาม Animation Simulation หรือภาพ Render ไม่ใช่หลักฐานยืนยันสมรรถนะจริง ความปลอดภัย การทดสอบภาคสนาม การรับรอง ความใหม่ทางวิชาการ หรือความพร้อมเชิงพาณิชย์

### 2. ข้อกำหนดการทำงานแบบ Local-first

- ใช้ Browser Workspace และจัดเก็บสื่อต้นฉบับในเครื่องตามความสามารถของ FreeCut เวอร์ชันที่ตรวจสอบแล้ว
- ห้ามอัปโหลดข้อมูลลับ ข้อมูลส่วนบุคคล ข้อมูลจำกัดสิทธิ์ งานที่ยังไม่เผยแพร่ หรือสื่อต้นฉบับที่ยังไม่ได้รับอนุญาต ไปยัง Cloud Editor, Remote AI Provider หรือบริการโมเดลสาธารณะ
- ก่อนเปิดใช้ AI ต้องระบุ Provider, Model, Model Revision, Licence, แหล่งที่มา ตำแหน่งประมวลผล และตรวจสอบว่าต้องดาวน์โหลดโมเดลครั้งแรกหรือไม่
- ให้ความสำคัญกับ On-device Inference ที่ระบุชัดเจน การทำงานผ่าน Browser ไม่ได้ยืนยันว่า AI ประมวลผลในเครื่องโดยอัตโนมัติ
- ตรวจสอบ Browser Permissions, Extensions, Network Requests และบริการเสริมก่อนใช้ข้อมูลสำคัญ ห้ามสมมติว่าทั้งระบบ Offline
- ไม่ใช้ Paid API, Subscription, Hosted Inference, Metered Service หรือ Cloud GPU
- เอกสารนี้ไม่อนุญาตให้ติดตั้งแพ็กเกจ ดาวน์โหลดซอฟต์แวร์หรือโมเดล สร้างบัญชี เชื่อมต่อบริการภายนอก หรือซื้อฮาร์ดแวร์ ต้องได้รับอนุมัติแยกต่างหาก
- เก็บไฟล์โปรเจกต์ ตำแหน่งสื่อต้นฉบับ การตั้งค่า Export และ Backup ไว้ภายใต้การควบคุมของผู้ใช้ ตรวจสอบ Backup ก่อนลบไฟล์ชั่วคราว

### 3. แนวทางผลิตสื่อสำหรับผลิตภัณฑ์

| โครงการ | วิดีโอที่เหมาะสม | ขอบเขตหลักฐาน |
|---|---|---|
| Coconut Harvest AI | อธิบายมะพร้าว 4 ระยะ การกำกับป้ายกำกับ และวิธีประเมินผล | ระบุภาพตัวอย่างและ Simulation ให้ชัดเจน |
| Extreme Flood Rescue AI | อธิบายสถานการณ์น้ำท่วมและระบบช่วยเหลือผ่าน Simulation | ระบุสมมติฐานและส่วนที่ยังไม่ผ่านการทดสอบจริง |
| Sentinel | แนวคิดการตรวจสอบพื้นที่ สถาปัตยกรรมเซนเซอร์ และ Human Review | ไม่สรุปตัวบุคคล ความผิด หรือภัยคุกคามอย่างเด็ดขาด และไม่รื้อฟื้นขอบเขตคัดกรองยาเสพติด/X-ray/นิติวิทยาศาสตร์ |
| AI HOME | แนวคิดหุ่นยนต์ในอาคารและสถานการณ์ที่มีมนุษย์กำกับ | แยก Simulation จากการทดสอบจริง |
| AI NOMAD | แนวคิดการเคลื่อนที่ภายนอกและการรับรู้สภาพพื้นผิว | Simulation ไม่ใช่หลักฐานสมรรถนะการเคลื่อนที่จริง |
| PUI89 AI Global SUV | แนวคิด Driver Support, Road Scene และ Full HEV | AI ให้คำแนะนำเท่านั้น ไม่กล่าวอ้างการควบคุมรถอัตโนมัติ |
| AI Step-Through Scooter / EasyRide | แนวคิด Step-through, Rider-view และข้อกำหนดความปลอดภัย | ไม่กล่าวอ้างการควบคุมพวงมาลัย คันเร่ง เบรก หรือการทรงตัวอัตโนมัติ |

### 4. ขั้นตอนผลิตวิดีโอ

1. กำหนดผู้ชม วัตถุประสงค์ ข้อกล่าวอ้าง และประเภทหลักฐานก่อนเริ่มตัดต่อ
2. สร้างโฟลเดอร์โปรเจกต์ในเครื่องและเก็บสำเนาสื่อต้นฉบับที่ไม่ผ่านการแก้ไข
3. บันทึกแหล่งที่มา ผู้สร้าง ใบอนุญาต ความยินยอม/การอนุญาต วันที่บันทึก และขอบเขตการใช้งาน
4. จัดทำ Storyboard พร้อมป้ายกำกับ Concept, Simulation, Measured Result และ Unverified Assumption
5. ทดลองโปรเจกต์สั้นและความละเอียดต่ำก่อน ตรวจสอบเสียง ตัวอักษร Transition การ Render และ Export
6. หากใช้ AI ให้ทดลองกับข้อมูลที่ไม่สำคัญก่อน พร้อมบันทึก Provider/Model และทรัพยากรที่ใช้
7. Export ไฟล์สำหรับตรวจทาน ตรวจสอบการเล่น ขนาดภาพ Frame Rate เสียง คำบรรยาย Codec และความสมบูรณ์ของไฟล์
8. ให้มนุษย์ตรวจสอบข้อเท็จจริงและภาพประกอบทุกส่วนเทียบกับหลักฐานต้นทาง
9. เก็บโปรเจกต์ที่แก้ไขได้ ทะเบียนสิทธิ์สื่อ การตั้งค่า Export และบันทึกการตรวจทานไว้ร่วมกับวิดีโอฉบับสมบูรณ์

### 5. ความถูกต้องทางวิจัยและการทำซ้ำ

- อ้างอิง Protocol, Dataset Card, Experiment Record, Code Revision และแหล่งผลลัพธ์ที่เกี่ยวข้องในคำอธิบายหรือเครดิตท้ายวิดีโอ
- ห้ามใช้ภาพที่สร้างขึ้นแทนตัวอย่าง Dataset, Ground Truth, กราฟผลการวัด หรือหลักฐานต้นฉบับ
- ห้ามปรับแกนกราฟ ตัดกรณีล้มเหลว ซ่อนความไม่แน่นอน หรือเลือกตัดต่อผลลัพธ์จนเปลี่ยนความหมาย
- เก็บไฟล์บันทึกต้นฉบับที่ไม่ตัดต่อสำหรับการสาธิตที่มีสาระสำคัญ หากสิทธิ์และความเป็นส่วนตัวอนุญาต
- บันทึกสื่อที่สร้างด้วย AI หรือมี AI ช่วยสร้าง รวมถึง Provider/Model และการแก้ไขที่มีนัยสำคัญ
- ใช้เพลง ฟอนต์ ภาพ วิดีโอ และโลโก้ที่มีสิทธิ์ใช้งานเท่านั้น
- เบลอหรือตัดข้อมูลส่วนบุคคล ข้อมูลลับ ข้อมูลอ่อนไหว และข้อมูลที่ไม่ได้รับอนุญาต
- จัดทำบันทึกการตรวจสอบ Claim-to-Evidence สำหรับข้อความเชิงปริมาณ ความปลอดภัย หรือสมรรถนะ

ไฟล์ FreeCut Project และวิดีโอ Export เป็นสื่อประกอบการสื่อสาร ไม่สามารถใช้แทน Experiment Record, Dataset ต้นฉบับ, Statistical Analysis, Code Review หรือ Evidence Passport ได้

### 6. การตรวจสอบ Browser และฮาร์ดแวร์

เอกสารโครงการ FreeCut ระบุการทำงานผ่าน Browser โดยใช้ WebGPU, WebCodecs และ Browser Storage/File APIs พร้อมแนะนำ Browser กลุ่ม Chromium รุ่นปัจจุบัน การรองรับจริงขึ้นกับเวอร์ชัน Browser ระบบปฏิบัติการ GPU Driver และ Codec

เครื่อง PUI89 ที่เคยระบุ (Acer Nitro AN515-57, Intel Core i7-11800H, RAM 16 GB และ NVIDIA RTX 3050 Laptop GPU) เป็นเพียงเครื่องที่ควรนำมาทดลอง ไม่ใช่ผลยืนยันความเข้ากันได้ ควรตรวจสอบ WebGPU, VRAM, อุณหภูมิ พื้นที่ดิสก์ การถอดรหัสสื่อ และความเร็ว Export ด้วยตนเอง เริ่มจากคลิปสั้นหรือ Proxy 1080p

ชื่อ Container เช่น MP4, WebM, MOV และ MKV ไม่ได้รับประกันว่า Browser/อุปกรณ์ทุกเครื่องรองรับ Codec หรือ Encoder ทุกชนิด ต้องตรวจสอบตัวเลือก Export จริงและทดสอบไฟล์ด้วยโปรแกรมเล่นแยกต่างหาก

### 7. เกณฑ์ก่อนอนุมัติใช้งาน

FreeCut เป็นเครื่องมือตัดต่อเสริมที่แนะนำได้ ไม่ใช่ Dependency ที่บังคับใช้ ก่อนใช้กับข้อมูลสำคัญหรือใช้งานเป็นประจำ ต้องตรวจสอบและบันทึก:

- [ ] ตรวจสอบ Repository, Release/Commit และ MIT Licence ปัจจุบัน
- [ ] ตรวจสอบที่มาของ Application และ Build
- [ ] ตรวจสอบ AI Provider, Model Licence และแหล่งที่มาของโมเดล
- [ ] ตรวจสอบการประมวลผล Local/Remote ของแต่ละฟีเจอร์
- [ ] ตรวจสอบ Browser Permissions และ Network Behaviour
- [ ] ทดลองโปรเจกต์ตัวอย่างที่ไม่มีข้อมูลสำคัญและตรวจสอบไฟล์ Export
- [ ] ตรวจสอบการสำรองและกู้คืน Local Workspace
- [ ] ตรวจสอบ Accessibility, Captions และข้อเท็จจริงโดยมนุษย์

**สถานะเกณฑ์ปัจจุบัน: NOT ASSESSED (ยังไม่ได้ประเมิน)** การแก้ไข Repository ครั้งนี้เป็นเพียงเอกสาร Workflow ไม่ใช่การรับรองความปลอดภัย ความเป็นส่วนตัว ประสิทธิภาพ ใบอนุญาตของโมเดลทุกตัว หรือความเหมาะสมกับข้อมูลงานวิจัยที่เป็นความลับ
