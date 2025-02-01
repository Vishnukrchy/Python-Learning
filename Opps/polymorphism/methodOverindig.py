#method overriding  in python
#=> Method overriding is a feature in object-oriented programming that allows a subclass to provide a different implementation of a method that is already defined in its parent class.
#=> When a method is overridden in a subclass, the method in the subclass has the same name and parameters as the method in the parent class, but with a different implementation.
#=> The overridden method in the subclass has the same name and parameters as the method in the parent class, but with a different implementation.

#example 1 =>
from math import pi

class Shape:
    def __init__(self,name):
        self.name = name
    def area(self):
        pass
    def perimeter(self):
        pass
    def facts(self):
        print(f"This is a {self.name}")

class Cricle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return pi * self.radius * self.radius
    def perimeter(self):
        return 2 * pi * self.radius
    def facts(self):
        print(f"This is a circle with radius {self.radius}")
        

c=Cricle(5)
c.facts()
print(c.area())
print(c.perimeter())

class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2 * (self.length + self.breadth)
    def facts(self):
        print(f"This is a rectangle with length {self.length} and breadth {self.breadth}")
        
r=Rectangle(10,20)
r.facts()
print(r.area())
print(r.perimeter())
