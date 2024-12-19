#Method Overriding in python
#=> Method overriding is a feature in object-oriented programming that allows a subclass to provide a different implementation of a method that is already defined in its parent class.
#=> When a method is overridden in a subclass, the method in the subclass has the same name and parameters as the method in the parent class, but with a different implementation.
#=> The overridden method in the subclass has the same name and parameters as the method in the parent class, but with a different implementation.

#example 1 => 

class Animal:
    name = "Animal"
    def __init__(self):
        print("Animal is created")
    def eat(self):
        print("Animal is eating")

class Dog(Animal):
    name = "Dog"
    def __init__(self):
        print("Dog is created")
    def eat(self):
        print("Dog is eating")

# Dog Object
dog = Dog()# Dog is created
dog.eat()# Dog is eating 
#Here the eat() method in the Dog class overrides the eat() method in the Animal class.
#In other words, the eat() method in the Dog class has the same name and parameters as the eat() method in the Animal class, but with a different implementation

# For Animal class
animal = Animal()# Animal is created
animal.eat()# Animal is eating
# here the eat() method in the Animal class is overridden by the eat() method in the Dog class