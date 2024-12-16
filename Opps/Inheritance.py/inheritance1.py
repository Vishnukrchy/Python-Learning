class vihicle:
    def __init__(self,name,color,brand,price):
        self.name=name
        self.color=color
        self.brand=brand
        self.price=price

    def printVihicle(self):
            print(f"Name : {self.name} , Color : {self.color}, Brand : {self.brand}, Price : {self.price}")

class Car(vihicle):
    
    def start(self):
        print("Car started")
    def stop(self):
        print("Car stopped")
    