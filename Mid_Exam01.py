#เขียนโปรแกรมสร้าง class ชื่อ Driver โดยมี attribute และ method ดังนี้
#attribute
#ㆍ HP เป็นพลังชีวิต
#ㆍ generated_money เป็นเงินที่ทำหาได้#
#method
#ㆍ dive) ท่าหน้าที่แสดงค่าพลังชีวิต และเงินที่หามาได้ หลังจากขับแท็กซี่ โดยจะลด HP 10 หน่วย แต่จะ
#เพิ่ม generated_money 10 หน่วย
#care[) ทำหน้าที่แสดงค่าพลังชีวิต และเงินที่หามาได้ หลังจากพักผ่อน โดยจะเพิ่ม HP 10 หน่วย แต่จะ
#ลด generated_money 10 หน่วย

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.HP =  HP  
