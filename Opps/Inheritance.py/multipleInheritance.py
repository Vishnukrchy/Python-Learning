#Multiple inheritance in python
#=> Multiple inheritance is a feature in object-oriented programming that allows a class to inherit properties and methods from multiple parent classes.
#=> When a class inherits from multiple parent classes, it can access the attributes and methods of all parent classes.

#example 1 =>

class ParentClass1:
    def method1(self):
        print("Parent class 1 method")
    

class ParentClass2:
    def method2(self):
        print("Parent class 2 method1")

class ChildClass(ParentClass1, ParentClass2):   
    def method3(self):
        print("Child class method")

obj = ChildClass()
obj.method1()  # Output: Parent class 1 method
obj.method2()  # Output: Parent class 2 method
obj.method3()  # Output: Child class method 

class Mammal:
    def mammal_info(self):
        print("Mammals can give direct birth.")

class WingedAnimal:
    def winged_animal_info(self):
        print("Winged animals can flap.")

class Bat(Mammal, WingedAnimal):
    pass

# create an object of Bat class
b1 = Bat()

b1.mammal_info()
b1.winged_animal_info()