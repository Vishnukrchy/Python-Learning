# Inheriance in python
# Python is a dynamically typed language, which means that the type of a variable is determined at runtime based on the value assigned to it.
# Inheriance is a concept in object-oriented programming that allows a class to inherit properties and methods from another class.
# Inhenritance is type of machansim by which we can raparsent parant chiled relationship in python  where chid class can enhrite the all properties of parent class  but it can not override the properties of parent class and parent class not acess the properties of child class

#Synntax
# define a superclass
#class super_class:
    # attributes and method definition

# inheritance
#class sub_class(super_class):
    # attributes and method of super_class
    # attributes and method of sub_class

# example 1 =>
class Animal:
    # attribute and method of the parent class
    name=""
    
    def eat(self):
        print("Animal is eating")
#inherit  from Animal class
class Dog(Animal):
    #new attribute and method of the child class

    def display(self):
        #acess parent class attribute and method
        print("Dog name is",self.name)
        #acess parent class method
        
 #Creating  object of child class
dog=Dog()
# acess the attribute of parent class
dog.name="Tommy"   
#call the method of child class      
dog.display()
dog.eat()  

# Inheritance repercent is-a relationship between classes
# explanation => A dog is an animal. A dog is a type of animal.

