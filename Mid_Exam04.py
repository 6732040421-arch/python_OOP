#เขียนโปรแกรมสร้าง class ชื่อ Dog โดยมี attribute และ method ดังนี้
#attribute
#breed เป็น พันธุ์สุนัข
#color เป็นสีของสุนัข
#height เป็นส่วนสูง (หน่วยเปียเซนดิเมตร)
#ㆍ weight เป็นน้ำหนัก (หน่วยเป็นกิโลกรัม)
#method
#growth) ทำหน้าที่แสดงความสูงและน้ำหนักที่เพิ่มขึ้นของสุนัขอย่างละ 10%

class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        print("Object was created")

    def getName(self):
        return self.firstName + "10%" + self.lastName

    def __del__(self):
        print("Object was destroyed")