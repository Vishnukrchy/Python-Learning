#MRO
class vihicle:
    def __init__(self,name,color,brand,price):
        self.name=name
        self.color=color
        self.brand=brand
        self.price=price
    def info(self):
        print("Vihicle info")
        print(f"Name : {self.name} , Color : {self.color}, Brand : {self.brand}, Price : {self.price}")
class Car:
    def __init__(self,name,color,brand,price):
        self.name=name
        self.color=color
        self.brand=brand
        self.price=price

    def info(self):
        print("Car info")
        print(f"Name : {self.name} , Color : {self.color}, Brand : {self.brand}, Price : {self.price}")


class child(Car,vihicle):
    def __init__(self,name,color,brand,price):
        self.name=name
        self.color=color
        self.brand=brand
        self.price=price

c=child("BMW","black","BMW",1000000)
c.info()#it will print Car info because of MRO

