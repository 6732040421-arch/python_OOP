#FnClassObkect
# ฟะงก์ชั่นที่ทำว่นร่วมกับ class และ object

# isinstance และ dia

class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def showData(self):
        print('ชื่อพนักงาน = {}'.format(self.name))
        print('เงินเดือน = {}'.format(self.salary))
        print('แผนก = {}'.format(self.department))



emp1 = Employee('วริศรา', 2000,'ปวส')
emp2 = Employee('นาแก้ว' ,20000, 'ปวช')
emp3 = Employee('Aoom' ,20000, 'นักศึกษา')

print(isinstance(emp1, Employee)) #ตรวจสอบว่า obj ถูกสร้างจาก  class ที่ตรวจสอบไหม
print(dir(emp1))
print(emp1.__class__)

