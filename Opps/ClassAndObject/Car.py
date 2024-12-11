class Car:
    name=""
    color=""
    brand=""
    price=0
# create object
# syntax => objectname = class()    

car1=Car()
#assign value
car1.name="BMW"
car1.color="black"
car1.brand="BMW"
car1.price=1000000
print(f"Name : {car1.name} , Color : {car1.color}, Brand : {car1.brand}, Price : {car1.price}")
print(car1)# it will print memory location
car2=Car()
car2.name="Audi"
car2.color="white"
car2.brand="Audi"
car2.price=2000000    
print(f"Name : {car2.name} , Color : {car2.color}, Brand : {car2.brand}, Price : {car2.price}")
print(car2)