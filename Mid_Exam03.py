#เขียนโปรแกรมสร้าง class ชื่อ Car โดยมี attribute และ method ดังนี้
#attribute
#brand เป็นยี่ห้อของรถ
#model เป็นรุ่นของรถ
#ㆍ year เป็นปีของรถ
#ㆍ color เป็นสีของรถ
#method
#new_color) รับพารามิเตอร์ 1 ตัว ชื่อว่า color ทำหน้าที่แสดงสีใหม่ของรถที่ต้องการเปลี่ยน

class Car:
    car_type = "Sedan"

    def __init__(self, name, mileage):
        self.name = name
        self.mileage = mileage

    def description(self):
        return f"The {self.name} car gives the mileage of {self.mileage}km/l"

    def max_speed(self, speed):
        return f"The {self.name} runs at the maximum speed of {speed}km/hr"