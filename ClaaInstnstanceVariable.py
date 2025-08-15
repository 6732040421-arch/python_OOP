#ClaaInstnstanceVariable

# Class  Variable  คือ  ตัวแปรงที่มำงานภายในclass
# ส่วนอี่นสามรถเข้าถึงข้อมูลส่วนนี้ไดเลย (static  attribute)
# โดยไม่จำเป็นต้องสร้างU object  ขึเนมา

# instance  Variable  คือตัวแปรที่อยูภายใน  object
#  สามารถเข้าถึงข้อมูลส่วนนี้โดยต้องสร้าง  Object  ขึ้นมา

# class  variarble
class Employee:
    __minsalary  = 12000
    __maxSalary  = 25000
    _companyName  = 'บริษัท XYZ จำกัด'
    def __init__(self, name, salary, department):
        #  instance  variable
        self.__name = name
        self.__salary = salary
        self.__department = department

    def _showData(self):
        print('ชื่อพนักงาน = {}'.format(self.__name))
        print('เงินเดือน = {}'.format(self.__salary))
        print('แผนก = {}'.format(self.__department))



emp1 = Employee('วริศรา', 2000,'ปวส')
#print('เงินเดือนขั้นต่ำ = '+str(Employee._minSalary))
print(Employee._companyName)