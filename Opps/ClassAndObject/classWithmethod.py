# Class With Method
# Every  can have there own behaviour and properties
class Room:
    length = 0
    breadth = 0
    
    # method to calculate area
    #self => it is a reference variable that refers to the current instance of the class
    def calculateArea(self):
        area=self.length*self.breadth
        print("Area of room is",area)
        return area

# creating object of Room class
study_Room=Room()
#assign value
study_Room.length=10
study_Room.breadth=20
#call method inside class
study_Room.calculateArea() 

print("========= Person ============")

class Person:
    name=""
    age=0
    city=""
    # create method for print details
    def printDetails(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("City: ",self.city)
    def setDetails(self,name,age,city):
        self.name=name
        self.age=age
        self.city=city  

person=Person()
person.setDetails("Vishnu",23,"Noida")
person.printDetails()

class Bike:
    name=""
    clour=""
    def setDetails(self,name,clour):
        self.name=name
        self.clour=clour    
    def printDetails(self):
        print("Name: ",self.name)
        print("Clour: ",self.clour)

b=Bike()
b.setDetails("Yamaha","Red")
b.printDetails()
