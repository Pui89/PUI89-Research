# PUI89 Research Lectures and Contributor Framework

**Record date:** 2026-11-25  
**Status:** Proposed learning and governance framework. No lecturer, supervisor, co-author or institution is appointed by this document.

## English — Learn it before building it

Each project page should include a short lecture that explains the problem in plain language, then connects it to the scientific method. Every lecture should include: (1) a 5-minute overview, (2) key terms, (3) one worked example, (4) a simple diagram or workflow, (5) common mistakes, (6) a short knowledge check, (7) primary references, and (8) a “what evidence would change our mind?” section. Lectures must distinguish established knowledge, open questions, PUI89 hypotheses and measured results.

### Lecture series

| Lecture | Plain-language topic | Project relevance | Learning outcome |
|---|---|---|---|
| L01 | How to turn a product idea into a testable research question | All six | State question, hypothesis, population/environment and measurable outcome. |
| L02 | What Q1 means—and what it does not mean | All six | Verify journal category/year and avoid treating Q1 as a quality guarantee. |
| L03 | How to read a paper and find a real research gap | All six | Compare prior methods, data, metrics and limitations; avoid invented novelty. |
| L04 | Images, labels and ground truth: how AI learns | Coconut, Sentinel, HOME, NOMAD, Car, Scooter | Explain sampling, annotation quality, label noise and domain shift. |
| L05 | Train, validation and test: preventing data leakage | All six | Split by independent orchard/site/session/route/subject/device as appropriate. |
| L06 | Baselines, ablations and fair comparisons | All six | Explain why a proposed method must beat relevant simple and strong baselines. |
| L07 | Metrics, confidence intervals and statistical testing | All six | Interpret precision, recall, F1, AP, calibration, effect size and uncertainty correctly. |
| L08 | Robustness, failure analysis and human review | All six | Report failures, unknown conditions, abstention and human escalation. |
| L09 | Edge AI and the Shared AI Core | All six | Understand model size, latency, memory, energy, CPU/GPU/NPU and shared interfaces. |
| L10 | Dataset rights, privacy, ethics and research integrity | All six | Check licence, consent, lawful basis, safety, attribution and redistribution separately. |
| L11 | From experiment record to Q1 manuscript | All six | Produce reproducible methods, results, limitations and declarations. |
| L12 | Thai/English scientific communication | All six | Explain the same method and evidence consistently in Thai and English. |

### Who should be brought into the research?

Invite people by **verified expertise and a defined responsibility**, not by title or prestige alone. A credible core team for each paper is:

1. **Lead academic supervisor / senior researcher:** relevant publication record in the exact field; reviews research question, novelty, study design and journal fit.
2. **Domain expert:** e.g. coconut agronomist/plant physiologist; security/privacy specialist; human–robot interaction or robotics expert; road-safety/vehicle engineering expert. Validates whether the task and ground truth make sense.
3. **AI/Computer Vision or Robotics researcher:** designs models, baselines, ablations, data splits and failure analysis.
4. **Statistician / experimental-design reviewer:** independently reviews sample size, unit of analysis, power/precision, clustering, confidence intervals, multiple comparisons and test-set discipline.
5. **Dataset and data-governance lead:** records provenance, licences, consent/privacy, annotation protocol, versioning and access.
6. **Independent validation reviewer:** challenges assumptions and checks whether reported conclusions follow from the evidence. Prefer someone not responsible for building the model.

For robotics/mobility studies, add a **functional-safety / human-factors / transport-safety reviewer** appropriate to the exact scope. For Sentinel, add a **privacy, cybersecurity governance and responsible-monitoring specialist**; do not expand the excluded narcotics/X-ray/forensic scope.

### Minimum credible author/contributor mix

- One accountable academic lead with a relevant track record.
- One domain specialist who can validate the data and real-world meaning.
- One technical lead for AI/robotics methods.
- One independent statistics reviewer.
- One data-rights/ethics reviewer (may be institutional support rather than an author).
- An independent reviewer for high-risk safety claims.

Authorship must follow actual intellectual contribution and the target journal's policy. Agree roles before submission using a contribution taxonomy such as [CRediT](https://credit.niso.org/). Do not add honorary authors, promise authorship for access, or list a lecturer as an author before they contribute. A lecturer may act as supervisor, reviewer or co-author depending on actual work and agreement.

### How to assess candidates

Ask for: relevant publications from the last 5 years; methods/datasets they know; experience with Q1 journals in the exact category; availability; conflicts of interest; willingness to review negative results; and a clear scope of contribution. Verify identity, affiliation and publications independently. No names are nominated here because no candidate's availability or consent has been verified.

### Shared AI Core teaching model

Teach the core as a common research infrastructure:
- **Observation:** what was sensed or annotated, when, by which source, with what provenance and uncertainty.
- **WorldState:** the current evidence-backed estimate, including unknowns and conflicts.
- **ActionProposal:** an advisory recommendation only; execution remains disabled in research.
- **FailureReport:** preserve errors, near misses, degraded conditions and negative results.
- **Evidence Passport:** connect every important paper claim to supporting, conflicting and missing evidence.

PUI89-specific models remain research candidates until evaluated. Keep model weights, training code, licences, dataset versions, evaluation cards and limitations traceable. A shared model must not erase project-specific differences or silently mix datasets.

---

## ภาษาไทย — เรียนรู้ให้เข้าใจก่อนพัฒนา

หน้าโครงการแต่ละเรื่องควรมีบทเรียนสั้นที่อธิบายปัญหาด้วยภาษาง่าย แล้วเชื่อมโยงกับวิธีวิจัย บทเรียนควรประกอบด้วย (1) ภาพรวม 5 นาที (2) คำศัพท์สำคัญ (3) ตัวอย่างที่อธิบายทีละขั้น (4) แผนภาพหรือขั้นตอน (5) ข้อผิดพลาดที่พบบ่อย (6) คำถามทบทวน (7) เอกสารอ้างอิงหลัก และ (8) คำถามว่า “หลักฐานแบบใดที่จะทำให้เราเปลี่ยนข้อสรุป” ต้องแยกองค์ความรู้ที่ยอมรับแล้ว คำถามที่ยังไม่มีคำตอบ สมมติฐานของ PUI89 และผลการทดลองที่วัดได้

### ชุดบทเรียน

| บทเรียน | หัวข้อแบบเข้าใจง่าย | โครงการที่เกี่ยวข้อง | สิ่งที่ต้องเข้าใจ |
|---|---|---|---|
| L01 | เปลี่ยนแนวคิดผลิตภัณฑ์ให้เป็นคำถามวิจัยที่ทดสอบได้ | ทั้ง 6 | ระบุคำถาม สมมติฐาน กลุ่มเป้าหมาย/สภาพแวดล้อม และผลลัพธ์ที่วัดได้ |
| L02 | Q1 คืออะไร และไม่ได้หมายความว่าอะไร | ทั้ง 6 | ตรวจสอบสาขาและปีของวารสาร ไม่ถือว่า Q1 รับประกันคุณภาพ |
| L03 | อ่านบทความและค้นหาช่องว่างวิจัยจริง | ทั้ง 6 | เปรียบเทียบวิธี ข้อมูล ตัวชี้วัด และข้อจำกัด ไม่สร้างข้ออ้างความใหม่ |
| L04 | ภาพ ป้ายกำกับ และ Ground Truth: AI เรียนรู้อย่างไร | ทั้ง 6 | เข้าใจการสุ่มตัวอย่าง คุณภาพป้ายกำกับ และ Domain Shift |
| L05 | Train, Validation, Test และการป้องกัน Data Leakage | ทั้ง 6 | แบ่งตามสวน/สถานที่/รอบเก็บภาพ/เส้นทาง/บุคคล/อุปกรณ์ที่เป็นอิสระ |
| L06 | Baseline, Ablation และการเปรียบเทียบอย่างเป็นธรรม | ทั้ง 6 | วิธีใหม่ต้องเปรียบเทียบกับวิธีพื้นฐานและวิธีที่แข็งแรง |
| L07 | Metrics, Confidence Interval และสถิติ | ทั้ง 6 | เข้าใจ Precision, Recall, F1, AP, Calibration และความไม่แน่นอน |
| L08 | Robustness, Failure Analysis และ Human Review | ทั้ง 6 | รายงานความล้มเหลว เงื่อนไขที่ไม่รู้จัก และการส่งต่อให้มนุษย์ |
| L09 | Edge AI และ Shared AI Core | ทั้ง 6 | เข้าใจขนาดโมเดล เวลา หน่วยความจำ พลังงาน CPU/GPU/NPU และ Interface |
| L10 | สิทธิ์ข้อมูล ความเป็นส่วนตัว จริยธรรม และความซื่อตรง | ทั้ง 6 | ตรวจสอบใบอนุญาต ความยินยอม กฎหมาย ความปลอดภัย และการเผยแพร่ |
| L11 | จากบันทึกการทดลองสู่บทความ Q1 | ทั้ง 6 | จัดทำวิธีวิจัย ผล ข้อจำกัด และคำประกาศที่ตรวจสอบได้ |
| L12 | การสื่อสารวิทยาศาสตร์ภาษาไทยและอังกฤษ | ทั้ง 6 | อธิบายวิธีและหลักฐานให้ตรงกันทั้งสองภาษา |

### ควรเชิญใครเข้าร่วมงานวิจัย

เชิญจาก **ความเชี่ยวชาญที่ตรวจสอบได้และหน้าที่ชัดเจน** ไม่ใช่ดูจากตำแหน่งหรือชื่อเสียงเพียงอย่างเดียว ทีมหลักที่น่าเชื่อถือสำหรับแต่ละบทความประกอบด้วย:

1. **อาจารย์ที่ปรึกษาหลัก/นักวิจัยอาวุโส:** มีผลงานในสาขาที่ตรงกับงาน ตรวจสอบคำถาม ความใหม่ วิธีวิจัย และความเหมาะสมของวารสาร
2. **ผู้เชี่ยวชาญเฉพาะด้าน:** เช่น นักปฐพี/พืชสวน/สรีรวิทยาพืช ผู้เชี่ยวชาญความปลอดภัยและความเป็นส่วนตัว ผู้เชี่ยวชาญปฏิสัมพันธ์มนุษย์กับหุ่นยนต์ หรือวิศวกรรมยานยนต์/ความปลอดภัยทางถนน
3. **นักวิจัย AI/Computer Vision/Robotics:** ออกแบบโมเดล Baseline, Ablation, การแบ่งข้อมูล และการวิเคราะห์ความล้มเหลว
4. **ผู้เชี่ยวชาญสถิติ/การออกแบบการทดลอง:** ตรวจสอบขนาดตัวอย่าง หน่วยวิเคราะห์ Power/Precision, Clustering, Confidence Interval และการใช้ชุดทดสอบ
5. **ผู้รับผิดชอบชุดข้อมูลและธรรมาภิบาลข้อมูล:** บันทึกที่มา ใบอนุญาต ความยินยอม ความเป็นส่วนตัว วิธี Annotation และเวอร์ชัน
6. **ผู้ทบทวนอิสระ:** ท้าทายสมมติฐานและตรวจว่าข้อสรุปสอดคล้องกับหลักฐาน โดยควรเป็นผู้ที่ไม่ได้พัฒนาโมเดลเอง

งานหุ่นยนต์และยานยนต์ควรเพิ่มผู้ทบทวนด้าน Functional Safety, Human Factors หรือ Transport Safety ตามขอบเขตจริง ส่วน Sentinel ควรมีผู้เชี่ยวชาญด้านความเป็นส่วนตัว ธรรมาภิบาลความมั่นคงปลอดภัยไซเบอร์ และการเฝ้าระวังอย่างรับผิดชอบ โดยไม่ขยายกลับไปยังขอบเขตยาเสพติด/X-ray/นิติวิทยาศาสตร์ที่ถูกยกเว้นไว้

### องค์ประกอบขั้นต่ำของทีมผู้เขียนที่น่าเชื่อถือ

- หัวหน้าวิชาการหนึ่งคนที่มีผลงานตรงสาขา
- ผู้เชี่ยวชาญโดเมนที่ตรวจสอบข้อมูลและความหมายในโลกจริงได้
- หัวหน้าด้าน AI/Robotics
- ผู้ตรวจสอบสถิติอิสระ
- ผู้ตรวจสอบสิทธิ์ข้อมูล/จริยธรรม
- ผู้ตรวจสอบอิสระสำหรับข้อกล่าวอ้างด้านความปลอดภัยที่มีความเสี่ยงสูง

การเป็นผู้เขียนต้องขึ้นกับผลงานทางวิชาการจริงและนโยบายวารสาร ควรตกลงหน้าที่ก่อนส่งบทความโดยใช้กรอบ [CRediT](https://credit.niso.org/) ห้ามเพิ่มชื่อผู้เขียนเพื่อเป็นเกียรติหรือแลกกับการเข้าถึงข้อมูล และห้ามระบุอาจารย์เป็นผู้เขียนก่อนมีส่วนร่วมจริง อาจารย์อาจเป็นที่ปรึกษา ผู้ทบทวน หรือผู้เขียนร่วมตามบทบาทที่ตกลงกัน

### วิธีประเมินผู้เชี่ยวชาญ

ขอข้อมูลผลงานตีพิมพ์ใน 5 ปีล่าสุด วิธีวิจัย/ชุดข้อมูลที่เชี่ยวชาญ ประสบการณ์วารสาร Q1 ในสาขาที่ตรง เวลาที่พร้อมให้ความช่วยเหลือ ผลประโยชน์ทับซ้อน ความพร้อมทบทวนผลลบ และขอบเขตงานที่รับผิดชอบ ตรวจสอบตัวตน สังกัด และผลงานจากแหล่งอิสระก่อน ยังไม่มีการเสนอชื่อบุคคลในเอกสารนี้ เพราะยังไม่ได้ตรวจสอบความพร้อมหรือความยินยอมของผู้สมัคร

### โมเดลการสอน Shared AI Core

- **Observation:** สิ่งที่เซนเซอร์หรือผู้กำกับป้ายกำกับบันทึกไว้ พร้อมเวลา ที่มา และความไม่แน่นอน
- **WorldState:** การประเมินสถานการณ์จากหลักฐาน รวมสิ่งที่ยังไม่ทราบและข้อมูลที่ขัดแย้ง
- **ActionProposal:** ข้อเสนอแนะเพื่อประกอบการตัดสินใจเท่านั้น ปิดการสั่งงานจริงในงานวิจัย
- **FailureReport:** เก็บข้อผิดพลาด เหตุการณ์เกือบเกิดอุบัติเหตุ สภาพระบบเสื่อม และผลลบ
- **Evidence Passport:** เชื่อมข้อกล่าวอ้างสำคัญในบทความกับหลักฐานที่สนับสนุน ขัดแย้ง หรือยังขาดอยู่

โมเดลเฉพาะของ PUI89 ยังเป็นโมเดลที่ต้องวิจัยและประเมินก่อนใช้งานจริง ต้องตรวจสอบย้อนกลับได้ทั้งน้ำหนักโมเดล โค้ดฝึก ใบอนุญาต รุ่นชุดข้อมูล Evaluation Card และข้อจำกัด โมเดลส่วนกลางต้องไม่ลบความแตกต่างของแต่ละโครงการหรือรวมชุดข้อมูลโดยไม่มีการบันทึก
