#Polymorphism in python
#=> Polymorphism is a feature in object-oriented programming that allows objects of different classes to be treated as if they are of the same class.
#=> Polymorphism is a way of representing a complex system in a simplified way that is easier to understand and use.
# -> polymorphism is tpye of machanism by which member of class can behave diffrently with same name


#example 1  method overriding=>
class A:
    def show(self):
        print("in A show")

class B(A):
    def show(self):
        print("in B show")

a=A()
b=B()
a.show()
b.show()


#example 2 =>
class Vihicle:
    def __init__(self,name,color,brand,price):
        self.name=name
        self.color=color
        self.brand=brand
        self.price=price
    def info(self):
        print("Vihicle info")
        print(f"Name : {self.name} , Color : {self.color}, Brand : {self.brand}, Price : {self.price}")

class Car(Vihicle):
    def info(self):
        print("Car info")
        print(f"Name : {self.name} , Color : {self.color}, Brand : {self.brand}, Price : {self.price}")

c=Car("BMW","black","BMW",1000000)
c.info()
