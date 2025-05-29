# Network Security Tools

เครื่องมือสำหรับการตรวจสอบความปลอดภัยของเครือข่าย ประกอบด้วย Banner Grabber และ Port Scanner ที่พัฒนาด้วยภาษา Python

## รายการเครื่องมือ

### 1. Banner Grabber (`BannerGrabber.py`)

**คำอธิบาย:**
Banner Grabber เป็นเครื่องมือที่ใช้สำหรับดึงข้อมูล Banner จาก Server ที่ระบุ โดย Banner คือข้อมูลที่ Server ส่งกลับมาเมื่อมีการเชื่อมต่อ ซึ่งมักจะประกอบด้วยข้อมูลเกี่ยวกับ Service ที่ทำงานอยู่ เช่น ชื่อ Software, เวอร์ชัน, หรือข้อมูลอื่นๆ ที่เป็นประโยชน์ในการประเมินความปลอดภัย

**คุณสมบัติ:**
- รองรับการเชื่อมต่อ TCP ผ่าน IPv4
- มี Timeout 2 วินาที เพื่อป้องกันการค้างการเชื่อมต่อ
- รับข้อมูล Banner สูงสุด 1024 ไบต์
- ตรวจสอบ Input และ Port Range (1-65535)
- จัดการ Error อย่างครบถ้วน
- ใช้งานง่ายผ่าน Command Line Interface

### 2. Port Scanner (`portScanner.py`)

**คำอธิบาย:**
Port Scanner เป็นเครื่องมือที่ใช้สำหรับตรวจสอบสถานะของ Port บน Server ว่าเปิดหรือปิดอยู่ หาก Port เปิดอยู่ จะพยายามดึงข้อมูล Banner จาก Service ที่ทำงานบน Port นั้นด้วย เครื่องมือนี้มีประโยชน์ในการสำรวจ Service ที่ทำงานบน Server และประเมินความปลอดภัย

**คุณสมบัติ:**
- ตรวจสอบสถานะ Port (เปิด/ปิด)
- ดึง Banner จาก Service หาก Port เปิดอยู่
- ตรวจสอบ Input และ Port Range (1-65535)
- จัดการ Error และแสดงผลที่เหมาะสม
- มี Timeout 2 วินาที เพื่อป้องกันการค้างการเชื่อมต่อ
- ปิดการเชื่อมต่ออย่างปลอดภัยหลังใช้งาน

## วิธีการใช้งาน

### การเตรียมความพร้อม

1. **ให้สิทธิ์ในการรันไฟล์ (สำหรับ Linux/macOS):**
```bash
chmod +x BannerGrabber.py    # ให้สิทธิ์รันไฟล์ Banner Grabber
chmod +x portScanner.py      # ให้สิทธิ์รันไฟล์ Port Scanner
```

### การรันโปรแกรม

2. **รัน Banner Grabber:**
```bash
python BannerGrabber.py      # รันโปรแกรม Banner Grabber
```

3. **รัน Port Scanner:**
```bash
python portScanner.py        # รันโปรแกรม Port Scanner
```

### ตัวอย่างการใช้งาน

**Banner Grabber:**
```
$ python BannerGrabber.py
Enter IP address: 192.168.1.1
Enter port: 22
SSH-2.0-OpenSSH_8.0
```

**Port Scanner:**
```
$ python portScanner.py
Please Enter the IP you want to scan: 192.168.1.1
Port: 22
Port 22 is open on 192.168.1.1
Banner: SSH-2.0-OpenSSH_8.0

$ python portScanner.py
Please Enter the IP you want to scan: 192.168.1.1
Port: 999
Port 999 is closed on 192.168.1.1
```

## ข้อควรระวัง

⚠️ **คำเตือน:** เครื่องมือเหล่านี้ควรใช้เพื่อการทดสอบความปลอดภัยในระบบของคุณเองเท่านั้น การใช้กับระบบของผู้อื่นโดยไม่ได้รับอนุญาตอาจผิดกฎหมาย

## ข้อกำหนดระบบ

- Python 3.x
- โมดูล `socket` (มาพร้อม Python โดยค่าเริ่มต้น)
- สิทธิ์ในการเข้าถึงเครือข่าย

## การแก้ไขปัญหา

หากเกิดข้อผิดพลาดในการเชื่อมต่อ:
- ตรวจสอบ IP address และ Port ที่ระบุ (Port: 1-65535)
- ตรวจสอบการเชื่อมต่อเครือข่าย
- ตรวจสอบ Firewall ที่อาจบล็อกการเชื่อมต่อ
- หาก Timeout เกิดขึ้น ลองเพิ่มเวลา timeout ในโค้ด
