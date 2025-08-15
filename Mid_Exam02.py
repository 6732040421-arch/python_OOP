#เขียนโปรแกรมสร้าง class ชื่อ Cashier โดยมี attribute และ method ดังนี้
#attribute
#ㆍ products เป็น list ที่เก็บชื่อสินค้า
#method
#recommend) ทำหน้าที่แนะนำสินสินค้า โดยเมื่อเรียกใช้ โปรแกรมจะพิมพ์ We have <product>. ออกมา

class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        print("Object was created")

    def getName(self):
        return self.firstName + " " + self.lastName

    def __del__(self):
        print("Object was destroyed")