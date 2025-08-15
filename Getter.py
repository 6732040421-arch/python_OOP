#  Getter  /   Setter  method
#  Setter  การกำหนดค่าฃ
#Getter ดึงค่าออก

#Ex_Setter
  #  def  setName (self ,  mewname)
  #   self.__name  = newname
#Ex_Getter
  # def  getName(self):
  # return  self,__nane

class Employee:
    def __init__(self, name, salary, department):
        # public attribute
        self.name = name
        self.salary = salary
        self.department = department

    # private method


def _showData(self):
    print('ชื่อพนักงาน = {}'.format(self.__name))
    print('เงินเดือน = {}'.format(self.__salary))
    print('แผนก = {}'.format(self.__department))

    # setter method
def setName(self, newname):
    self.__name = newname
def setSalary(self, newsalary):
    self.__salary = newsalary
def setDepartment(self, newdepartment):
    self.__department = newdepartment

    # getter method
def getName(self):
    return self.__name
def getSalary(self):
    return self.__salary
def getDepartment(self):
    return self.__department


emp1 = Employee('วริศรา', 2000,'ปวส')
print('พนักงานดีเด่นประจำปี = {}'.format(emp1.getName()))
print('เงินเดือน = {}'.format(emp1.getSalary))
print('แผนก = {}'.format(emp1.getDepartment))