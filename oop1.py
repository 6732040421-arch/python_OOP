# ชื่อ   ,เวินเดือน
class Emplovee: #การสร้าง  class
  # สร้าง method
    def detail(self, name, salary, department):
        # สราง Attribute
        self.name = name
        self.salary = salary
        self.department = department

        def showData(self):
        print('ชื่อพนักงาน = {}'.format(self.name))
        print('เงินเดือน = {}'.format(self.salary))
        print('แผนก = {}'.format(self.department))

# Attributeเป็นกลไกที่กำหนดตุณสมบัติให้กับ  class
# การสร้าง Attributeเ
# self.name =ชื้อพนักงาน
# self.salary =เงินเดือน
#  self.age =อายุจองพนักงาน

#Method เป็นกลไกที่กำหนดพฤติกรรมให้กัน  cclass
#การสร้าง Method
# def getN
# re
# Method

# คีย์เวิร์ด self
#   การใช้คีย์เวิร์ด self จะเป็นตัวชี้หรือบ่งบอกว่าตอนนี้เราทำงานกับวัตถุใด
#   ให้บอกตัวตนของวัตถุนั้น ๆ เช่น การกำหนดคุณสมบัติต่าง ๆ ในวัตถุ เป็นต้น

# Constructor
# เป็น method พิเศษที่จะถูกใช้งานเมื่อตอนเริ่มสร้างวัตถุ (ไม่ระบุก็ได้)
# โครงสร้าง constructor
#   def __init__(self):

#การสร้างวัสถุ
emp1 = Emplovee()
emp1.detail( 'วริศรา', 2000,'ปวส')
emp1. showDats()
emp2 = Emplovee()
emp2.detail('นาแก้ว' ,20000, 'ปวช')
emp2. showDats()
emp3 = Emplovee()
emp3.detail('Aoom' ,20000, 'นักศึกษา')
emp3. showDats()