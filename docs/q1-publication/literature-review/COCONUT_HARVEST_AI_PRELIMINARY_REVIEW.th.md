# Coconut Harvest AI — ทบทวนวรรณกรรมเบื้องต้นและตารางช่องว่างงานวิจัย

**เวอร์ชัน:** 0.1 (Scoping Review ไม่ใช่ Systematic Review)  
**วันที่ค้น:** 26 พฤศจิกายน 2026  
**สถานะ:** แผนที่หลักฐานเบื้องต้น ยังต้องค้นฐานข้อมูลวิชาการ คัดกรองฉบับเต็ม และให้ผู้เชี่ยวชาญตรวจทาน  
**ความถูกต้องของหลักฐาน:** เอกสารนี้ไม่ได้อ้างว่ามีชุดข้อมูล การกำกับป้ายกำกับ การทดลอง หรือผลประสิทธิภาพของ PUI89 แล้ว

## 1. ทิศทางคำถามวิจัยเบื้องต้น

**คำถามทำงาน:** โมเดลภาพขนาดเล็กสามารถจำแนกระดับความแก่มะพร้าว 4 กลุ่มที่กำหนดไว้ ได้แก่ เขียวอ่อน เขียวแก่ เหลือง และน้ำตาล ได้เชื่อถือเพียงใด เมื่อทดสอบกับต้นมะพร้าว รอบการถ่ายภาพ และสวนที่เป็นอิสระจากชุดฝึก พร้อมรายงานความไม่แน่นอนและทรัพยากร CPU?

คำถามนี้ยังเป็นเพียงข้อเสนอ ไม่ใช่ Research Gap ที่ยืนยันแล้ว ป้ายกำกับ 4 ระดับเป็นนิยามเชิงปฏิบัติการเบื้องต้น ต้องให้ผู้เชี่ยวชาญด้านมะพร้าวตรวจสอบและเชื่อมโยงกับเกณฑ์ความแก่ทางพืชสวนก่อนเก็บข้อมูลจริง ห้ามใช้สีเพียงอย่างเดียวเป็น Ground Truth

### วัตถุประสงค์ที่เสนอ
1. กำหนดและตรวจสอบแนวทางกำกับป้ายกำกับความแก่ร่วมกับผู้เชี่ยวชาญ
2. เปรียบเทียบ Baseline ด้านสี/พื้นผิวกับ Compact CNN โดยใช้ชุดแบ่งข้อมูลเดียวกัน
3. ประเมินการใช้งานข้ามต้น รอบถ่ายภาพ และสวน ไม่ใช้การสุ่มแบ่งภาพอย่างเดียว
4. วัด Precision, Recall, Macro-F1, Balanced Accuracy, Calibration, Abstention Coverage, เวลา CPU และ RAM สูงสุด
5. วิเคราะห์ความล้มเหลวจากแสง การบังภาพ ความเบลอ ระยะถ่าย และตัวอย่างที่ไม่ชัดเจน

## 2. วิธีค้นและข้อจำกัด

เอกสารรุ่นนี้เป็น **การค้นเว็บเชิงสำรวจแบบเจาะจง ณ วันที่ 26 พฤศจิกายน 2026** โดยใช้คำค้นเกี่ยวกับการจำแนกความแก่มะพร้าว Computer Vision, Deep Learning, เกณฑ์ Ground Truth, คุณสมบัติทางกายภาพ การแบ่งชุดข้อมูลระดับสวน และ Data Leakage

ยังไม่ใช่ PRISMA Systematic Review และไม่อ้างว่าครอบคลุมงานทั้งหมด บางรายการตรวจสอบได้เพียงหน้า Publisher หรือ Abstract และบางรายการยังไม่ได้อ่าน Full Text ต้องตรวจสอบรายละเอียดบรรณานุกรม วิธีวิจัย และผลลัพธ์กับฉบับตีพิมพ์ก่อนนำไปใช้ในต้นฉบับบทความ

## 3. แผนที่หลักฐานเบื้องต้น

| งานวิจัย | ข้อมูล/โจทย์ที่รายงาน | วิธี/ผลที่รายงาน | ความเกี่ยวข้องและข้อจำกัด |
|---|---|---|---|
| Terdwongworakul et al. (2009), *Biosystems Engineering* 103(2), 208–216. [DOI](https://doi.org/10.1016/j.biosystemseng.2009.03.012) | มะพร้าวอ่อนพันธุ์ไทย ศึกษาคุณสมบัติทางกายภาพ กลศาสตร์ สรีรวิทยา และเสียง | ความหนาเนื้อสัมพันธ์กับจำนวนวันหลังผสมเกสร และมีแบบจำลองจากคุณสมบัติทางกายภาพ/ความถี่เรโซแนนซ์ | สำคัญต่อการออกแบบ Ground Truth สีภายนอกต้องไม่ถูกถือเป็นเกณฑ์อ้างอิงโดยอัตโนมัติ |
| *Detection of maturity stages of coconuts in complex background using Faster R-CNN model* (2021), *Biosystems Engineering* 202, 119–132. [DOI](https://doi.org/10.1016/j.biosystemseng.2020.12.002) | ภาพจากสวน ตรวจจับทะลายมะพร้าวอ่อน/แก่ | Faster R-CNN + ResNet-50 เปรียบเทียบกับ SSD, YOLOv3 และ R-FCN | ยืนยันว่ามีงานในฉากสวนซับซ้อนแล้ว แต่โจทย์สองกลุ่มระดับทะลายไม่เท่ากับ 4 กลุ่มระดับผลของ PUI89 |
| Megalingam et al. (2024), *Neural Computing and Applications*. [DOI](https://doi.org/10.1007/s00521-023-09402-2) | ภาพฝึก 10,000 ภาพ และชุดทดสอบสองชุด | Mask R-CNN ร่วมกับ Fuzzy Features ด้านสี รูปร่าง และรอยขีดข่วน รายงานความแม่นยำภาพจริง 86.3% | มีงาน Fusion และหลายระดับความแก่แล้ว ต้องตรวจนิยามคลาสและความเป็นอิสระของชุดแบ่งข้อมูลจากฉบับเต็ม |
| Mandava et al. (2024), *Materials Today: Proceedings* 103, 410–414. [DOI](https://doi.org/10.1016/j.matpr.2023.09.071) | 1,001 ภาพ แบ่งดิบ/สุก | เปรียบเทียบ YOLOv5s, YOLOv4-Tiny และ MobileNet-SSD พร้อมระบุข้อจำกัดของชุดข้อมูลขนาดเล็ก | เกี่ยวข้องกับโมเดลขนาดเล็ก แต่สองคลาสยังไม่ยืนยัน 4 คลาสหรือการใช้งานข้ามสวน |
| Perera & Perera (2025), *Asian Journal of Research in Computer Science* 18(9), 76–90. [DOI](https://doi.org/10.9734/ajrcos/2025/v18i9755) | จำแนกความแก่และพยากรณ์ช่วงเวลาเก็บเกี่ยว | Hybrid EfficientNetB0 + DenseNet121 และ MobileNetV2 Regression รายงาน Accuracy สูง พร้อมระบุข้อจำกัดของขอบเขตข้อมูล | งาน Classification และ Timeline Prediction มีแล้ว ห้ามเปรียบเทียบตัวเลขข้ามงานหากชุดข้อมูลและวิธีแบ่งต่างกัน |
| Luthfie & Alamsyah (2025), *Journal of Information System Exploration and Research* 3(2). [DOI](https://doi.org/10.52465/joiser.v3i2.595) | 230 ภาพ แบ่งมะพร้าวอ่อน/แก่ | CNN และ YOLOv8 รายงาน mAP 90.5%, Precision 99.3%, Recall 94.2%, F1 96.6% | ชุดข้อมูลสองคลาสขนาดเล็ก เป็นเหตุให้ต้องตรวจสอบความเป็นอิสระของตัวอย่างและ External Validation |
| *Coconut Maturity Level Classification using Image Preprocessing and Deep Transfer Learning* (บันทึกการประชุม 2025; IEEE เพิ่มดัชนีปี 2026). [DOI](https://doi.org/10.1109/RIVF68649.2025.11365215) | 3,000 ภาพ แบ่ง young, pre-mature, mature | VGG16 รายงาน Accuracy 96.17% และเปรียบเทียบ MobileNetV2/EfficientNet | เกี่ยวข้องกับ 3 คลาสและ Transfer Learning แต่ต้องตรวจสอบการแบ่งชุด พันธุ์ และการทดสอบต่างพื้นที่ |
| *Coconut Bunch Intelligence System* (บันทึกการประชุม IEEE 2026). [DOI](https://doi.org/10.1109/ICIPRoB69625.2026.11497814) | 3,000 ภาพ มี 4 ป้ายกำกับ Immature, Mature, Over-mature, Unknown | MobileNetV2 รายงาน Accuracy 99.0%; YOLOv8n ใช้นับผลในทะลาย | มีความทับซ้อนกับโจทย์ 4 คลาสโดยตรง เป็นความเสี่ยงสำคัญด้าน Novelty ต้องเทียบคำนิยามคลาส ชุดทดสอบอิสระ และประชากรเป้าหมาย |
| *Tender Coconut Maturity Stage Detection Using YOLOv8-v10...* (2026), *Procedia Computer Science*. [DOI](https://doi.org/10.1016/j.procs.2026.05.062) | 2,121 ภาพภาคสนาม มีความต่างของแสงและการบัง | เปรียบเทียบ YOLOv8/9/10 โดย YOLOv10 รายงาน mAP@0.5 82% | สนับสนุนความสำคัญของสภาพภาคสนาม แต่ต้องตรวจสอบนิยามคลาสและการแบ่งข้อมูลข้ามสวน |
| Sailangka et al., โครงงานวิจัยนักเรียน KVIS (หลักฐานโครงการ ไม่ใช่งานวารสาร Peer-reviewed). [โครงการ](https://app.kvis.ac.th/kvis-awards/list.php?code=COMP019) | มะพร้าวน้ำหอม 150 ผล ใช้เสียงเคาะ | ใช้ Spectrogram และ CNN รายงานผลความแม่นยำสูง | เป็นข้อมูลบริบทพันธุ์ไทยและแนวทางกำหนดเกณฑ์ความแก่ แต่ไม่ใช่งานจำแนกภาพ RGB และยังไม่ใช่หลักฐานวารสาร Peer-reviewed |

## 4. ตารางช่องว่างงานวิจัยเบื้องต้น

| ช่องว่างที่อาจศึกษา | สิ่งที่พบจากการค้นเบื้องต้น | หลักฐานที่ต้องตรวจเพิ่มก่อนอ้างว่าเป็น Gap | ความสำคัญ |
|---|---|---|---|
| 4 คลาสภาพที่มี Ground Truth ทางพืชสวน | งานเดิมมีทั้ง 2, 3 และ 4 คลาส และมีงาน 4 คลาสในปี 2026 แล้ว | เปรียบเทียบนิยามคลาส พันธุ์ หน่วยผล/ทะลาย วัตถุประสงค์การเก็บเกี่ยว และวิธีอ้างอิงจาก Full Text | วิกฤต |
| ทดสอบข้ามต้น/รอบถ่าย/สวนอย่างอิสระ | หลายงานรายงานชุดภาพและ Accuracy แต่ Abstract ไม่ชัดเรื่องความเป็นอิสระ | ตรวจ Data Split และ Supplementary Materials ว่าขาดการทดสอบสวนอิสระจริงหรือไม่ | วิกฤต |
| Uncertainty, Calibration และ Abstention | Abstract ที่ตรวจเบื้องต้นยังไม่ยืนยันประเด็นนี้ | ตรวจ Full Text และงาน Agricultural CV ที่เกี่ยวข้องเรื่อง Calibration, Selective Prediction และ Human Review | สูง |
| CPU-first พร้อมวัด Latency/RAM | มีงานใช้โมเดลเบาและ Edge Deployment แล้ว | เทียบ Hardware, Preprocessing, Model Size, Latency Distribution และ RAM ด้วยวิธีเดียวกัน | สูง |
| ความกำกวมของป้ายกำกับและความเห็นผู้เชี่ยวชาญ | งานเดิมใช้สีและคุณสมบัติทางกายภาพ/เสียง แต่ขอบเขตคลาสต่างกัน | หาเกณฑ์ตามพันธุ์และออกแบบ Expert Adjudication / Inter-rater Agreement | วิกฤต |
| ความทนทานข้ามพันธุ์ ฤดูกาล และแสง | มีงานกล่าวถึงฉากซับซ้อนและสภาพแสงภาคสนามแล้ว | ตรวจว่ามีการทดสอบข้ามพันธุ์ ฤดู สวน และกล้องจริงหรือไม่ | สูง |

**ข้อสรุปเบื้องต้น:** การ “ใช้ Deep Learning จำแนกความแก่มะพร้าว” ไม่ใช่ความใหม่ในตัวเอง แนวทางที่อาจสร้างคุณค่าได้มากกว่าคือการประเมินที่มี Ground Truth ชัดเจน ป้องกัน Data Leakage รองรับความไม่แน่นอน ทดสอบกับสวนอิสระ และรายงานทรัพยากร CPU อย่างเป็นระบบ ทั้งหมดนี้ยังเป็นสมมติฐานเพื่อการทบทวนต่อ ไม่ใช่การอ้าง Novelty

## 5. แนวทางวิธีวิจัยที่เสนอ — ยังไม่อนุมัติและยังไม่ได้ดำเนินการ

### 5.1 นิยามคลาสและเกณฑ์อ้างอิง
- คง 4 คลาสของ PUI89 เป็นป้ายกำกับภาพเบื้องต้นเท่านั้น
- ให้ผู้เชี่ยวชาญด้านมะพร้าวจัดทำคู่มือป้ายกำกับเป็นลายลักษณ์อักษร
- ระบุพันธุ์ วัตถุประสงค์ตลาด และเกณฑ์ความแก่แยกจากกัน
- หากทำได้ ให้จับคู่ภาพกับข้อมูลอ้างอิงอิสระ เช่น วันหลังผสมเกสร การวัดผล/เนื้อ การประเมินหลังเก็บเกี่ยว หรือเกณฑ์คัดเกรดท้องถิ่นที่ยอมรับ ห้ามเก็บตัวอย่างแบบทำลายโดยไม่มีการอนุมัติจากเจ้าของและระเบียบวิธีที่บันทึกไว้
- ต้องมีทางเลือก “ไม่แน่ใจ/ส่งให้ผู้เชี่ยวชาญตรวจ” ไม่บังคับตัวอย่างกำกวมให้เป็นคลาสที่มั่นใจ

### 5.2 ที่มาและการสุ่มตัวอย่าง
บันทึกข้อมูลอย่างน้อย: Fruit ID, Tree/Plot/Orchard ID, Capture Session ID, วันเวลา, พันธุ์ (ถ้าทราบ), กล้อง, ระยะ/มุมถ่าย, สภาพแสง/อากาศ, ป้ายกำกับเบื้องต้น, ผู้กำกับป้ายกำกับ, วิธีอ้างอิง, หลักฐานความยินยอม/สิทธิ์เข้าพื้นที่, ใบอนุญาต และ Hash ของไฟล์ต้นฉบับ

ภาพหลายมุม ภาพ Crop และไฟล์ Augmentation ของผลเดียวกันหรือเหตุการณ์ถ่ายเดียวกันต้องอยู่ใน Partition เดียวกัน

### 5.3 การประเมินที่ป้องกัน Data Leakage
- แบ่งข้อมูลตามหน่วยอิสระที่แท้จริง โดยเริ่มจาก Tree และ Capture Session; กันสวน/พื้นที่ไว้ทดสอบภายนอกหากทำได้
- ตรวจภาพซ้ำและ Near-duplicate ก่อนล็อกชุดข้อมูล
- ทำ Augmentation เฉพาะข้อมูลฝึกหลังแบ่งชุดแล้ว
- ล็อก Test Manifest และ Hash ก่อนเลือกโมเดล
- หากมีเพียงสวนเดียว ต้องรายงานข้อจำกัดและห้ามอ้างว่า Generalize ข้ามสวน

### 5.4 Baseline และตัวชี้วัด
- Baseline: Majority Class, คุณลักษณะสี/พื้นผิวแบบง่ายเมื่อเหมาะสม, Compact CNN และ Compact Detector เฉพาะกรณีที่โจทย์ต้องระบุตำแหน่งวัตถุ
- ตัวชี้วัดหลัก: Macro-F1 และ Balanced Accuracy พร้อม Precision/Recall รายคลาสและ Confusion Matrix
- ตัวชี้วัดรอง: Calibration เช่น Brier Score/กราฟ Reliability, Risk-versus-Coverage สำหรับ Abstention, การกระจายเวลา CPU, Throughput, RAM สูงสุด และ Model Size
- รายงาน Confidence Interval และความแปรปรวนจากการรันซ้ำ กำหนด Primary Endpoint และแผนสถิติก่อนเปิด Test Set

## 6. ทะเบียนงานถัดไป

| ID | งาน | ผลส่งมอบ | สถานะ |
|---|---|---|---|
| COC-LR-01 | ตรวจข้อมูลบรรณานุกรมและอ่าน Full Text ที่เข้าถึงได้อย่างถูกสิทธิ์ | Reference Verification Log | ยังไม่เริ่ม |
| COC-LR-02 | ขยายการค้น Scopus/Web of Science/Google Scholar/CAB Abstracts และคลังงานวิจัยไทย | Search Strings, วันที่ค้น, Export และ Screening Log | ยังไม่เริ่ม |
| COC-GAP-01 | เปรียบเทียบ Taxonomy, พันธุ์ และ Ground Truth | Evidence Matrix ที่ตรวจครบ | กำลังทำ — เบื้องต้นเท่านั้น |
| COC-DATA-01 | ยืนยันผู้เชี่ยวชาญและเกณฑ์ความแก่ | บันทึกการตัดสินใจ/Protocol | ติดขัด — ยังไม่ยืนยันผู้ทบทวน |
| COC-DATA-02 | ยืนยันสิทธิ์เข้าสวน การอนุญาต และหน่วยสุ่มตัวอย่าง | Rights & Sampling Register | ติดขัด — ยังไม่ยืนยันพื้นที่ |
| COC-PROT-01 | สรุป Split, Metrics และ Analysis Plan | Protocol ที่มีเวอร์ชัน | รอการตัดสินใจเรื่องผู้เชี่ยวชาญ/ข้อมูล |

## 7. เอกสารอ้างอิง

1. Terdwongworakul, A., Chaiyapong, S., Jarimopas, B., & Meeklangsaen, W. (2009). Physical properties of fresh young Thai coconut for maturity sorting. *Biosystems Engineering, 103*(2), 208–216. https://doi.org/10.1016/j.biosystemseng.2009.03.012
2. Detection of maturity stages of coconuts in complex background using Faster R-CNN model. (2021). *Biosystems Engineering, 202*, 119–132. https://doi.org/10.1016/j.biosystemseng.2020.12.002
3. Megalingam, R. K., Manoharan, S. K., & Maruthababu, R. B. (2024). Integrated fuzzy and deep learning model for identification of coconut maturity without human intervention. *Neural Computing and Applications*. https://doi.org/10.1007/s00521-023-09402-2
4. Mandava, R. K., Mittal, H., & Hemalatha, N. (2024). Identifying the maturity level of coconuts using deep learning algorithms. *Materials Today: Proceedings, 103*, 410–414. https://doi.org/10.1016/j.matpr.2023.09.071
5. Perera, P. A., & Perera, P. M. (2025). Dual-stage deep learning framework for hybrid coconut maturity classification and harvest timeline prediction. *Asian Journal of Research in Computer Science, 18*(9), 76–90. https://doi.org/10.9734/ajrcos/2025/v18i9755
6. Luthfie, A. A., & Alamsyah, A. (2025). Identifying coconut maturity levels using CNN and YOLOv8 deep learning algorithms. *Journal of Information System Exploration and Research, 3*(2). https://doi.org/10.52465/joiser.v3i2.595
7. Coconut maturity level classification using image preprocessing and deep transfer learning. (บันทึกการประชุม 2025; เพิ่มดัชนีปี 2026). https://doi.org/10.1109/RIVF68649.2025.11365215
8. Coconut bunch intelligence system: Image-based maturity classification and nut count prediction. (บันทึกการประชุม 2026). https://doi.org/10.1109/ICIPRoB69625.2026.11497814
9. Tender coconut maturity stage detection using YOLOv8-v10: Comparative analysis with DETR, EfficientDet and Vision Transformers. (2026). *Procedia Computer Science*. https://doi.org/10.1016/j.procs.2026.05.062
10. Sailangka, W., Puasantikul, P., & Sriboonrat, P. (โครงงานนักเรียน; ต้องตรวจสอบปีและสถานะการตีพิมพ์). Nondestructive evaluation of *Cocos nucifera* of Nam Hom variety maturity stage using deep learning. Kamnoetvidya Science Academy. https://app.kvis.ac.th/kvis-awards/list.php?code=COMP019

---
**ความซื่อตรงของหลักฐาน:** เอกสารนี้บันทึกการค้นเบื้องต้นและแนวทางวิจัยที่เสนอเท่านั้น ยังไม่ยืนยัน Novelty ความครอบคลุมของวรรณกรรม การอนุมัติจริยธรรม/สิทธิ์ ชุดข้อมูล โมเดลที่ฝึกแล้ว ผลวัดประสิทธิภาพ ความพร้อม Q1 หรือความพร้อมส่งต้นฉบับ
