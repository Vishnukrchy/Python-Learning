#Cunstructor in python
#=> A constructor is a special method that is called when an object is created from a class.
#=> The constructor is used to initialize the object's attributes and perform any other setup steps.
#=> The constructor is called automatically when an object is created, and it can be used to assign initial values to object attributes

#syntax
# class_name():
#     def __init__(self,parameter):
#         self.parameter=parameter

#Earlier we assigned a default value to a class attribute,
class Bike:
    name=""
b=Bike()
# Way 1 to initialize class attribute => by using arugument and class reference
b.name="Yamaha"
print(b.name)
# Way 2 to initialize class attribute => by using setter method
class Bike:
    name=""
    clour=""
    def setDetails(self,name,clour):
        self.name=name
        self.clour=clour
b=Bike()
b.setDetails("Yamaha","Red")


# Constructor in python=> By using constructor we can initialize class attribute
# __init__(self,parameter) => in Python all class have a specail cunstructor function called __init__ 
#=> __init__ function is a special method that is called when an object is created from a class
#syntax
# class_name():
#     def __init__(self,parameter):
#         self.parameter=parameter

#self =>  the self parameter is a reference to the current instance of the class and is used to access class attributes and methods

class Employee:
    #Create a constructor
    def __init__(self,name,salary,city):
        print("Constructor is called")
        self.name=name
        self.salary=salary
        self.city=city
# when we create an object of a class we need to pass the arguments to the constructor and then the constructor will be called automatically
emp1=Employee("rahul",50000,"Noida")
print(emp1.name)#rahul
print(emp1.salary)
print(emp1.city)

empl2=Employee("vishnu",60000,"Noida")
print(empl2.name)
print(empl2.salary)
print(empl2.city)




