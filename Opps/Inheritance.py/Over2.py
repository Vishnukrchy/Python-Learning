#Overrinding

class Vihicle:
    def __init__(self,name,color,brand,price):
        self.name=name
        self.color=color
        self.brand=brand
        self.price=price
    def printVihicle(self):
        print(f"Name : {self.name} , Color : {self.color}, Brand : {self.brand}, Price : {self.price}")
    def start(self):
        print(f"{self.name} is started")
    def stop(self):
        print(f"{self.name} is stopped")

class Car(Vihicle):
    def __init__(self,name,color,brand,price):
        self.name=name
        self.color=color
        self.brand=brand
        self.price=price
    def start(self):
        print(f"{self.name} is started")    
    def stop(self):
        print(f"{self.name} is stopped")
    def printVihicle(self):
        print("car details is printed")
        print(f"Name : {self.name} , Color : {self.color}, Brand : {self.brand}, Price : {self.price}")    

#create object
car1=Car("BMW","black","BMW",1000000)
car1.start()
car1.stop()
car1.printVihicle()            