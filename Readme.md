E-learning web application for teaching & analyzing Thai students's English pronunciation using End-to-end Automatic speech recognition and Intelligent tutoring system

Collab with - Nattapol kritsuthikul (NECTEC researcher)

Demo - soon

Paper - soon?



ระบบถูกพัฒนาเป็น web application โดยใช้ Flask ซึ่งเป็น  Web Framework ที่ได้รับความนิยมของภาษา Python 

ในสถาปัตยกรรมของงาน เราได้ใช้ Automatic Speech Recognition (ASR) ในแนวทางที่เรียกว่า End-to-end ASR ซึ่งเป็น deep learning algorithm ชนิดนึง ที่มีจุดเด่นสำคัญคือ ใช้ข้อมูลสำหรับการสอน (train) เพียงเสียง และ ข้อความอ้างอิง ทำให้สามารถเตรียมข้อมูลได้ง่ายและยังไม่จำเป็นต้องใช้นักภาษาศาสตร์ช่วยในการเตรียมข้อมูล 

ในงานนี้เราได้นำ ASR หลายชุดมาใช้ประกอบกันเพื่อใช้เป็นเครื่องมือในการประเมินความสามารถในการออกเสียงของผู้ใช้งานระบบโดยใช้คะแนนความเชื่อมั่น (confidential score) ที่ได้จาก ASR แต่ละชุดเป็นเกณฑ์พิจารณาร่วมกัน โดยเราได้ออกแบบ ASR เป็น 2 ชุด ได้แก่ 
- Thai Accent ASR แทนคลังเสียงการออกเสียงที่แบบสำเนียงคนไทย 
- Native Accent ASR แทนคลังเสียงการออกเสียงแบบสำเนียงเจ้าของภาษา(US)


