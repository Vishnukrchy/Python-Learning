#method overriding  in python
#=> Method overriding is a feature in object-oriented programming that allows a subclass to provide a different implementation of a method that is already defined in its parent class.
#=> When a method is overridden in a subclass, the method in the subclass has the same name and parameters as the method in the parent class, but with a different implementation.
#=> The overridden method in the subclass has the same name and parameters as the method in the parent class, but with a different implementation.

from math import pi


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "I am a two-dimensional shape."

    def __str__(self):
        return self.name


class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length**2

    def fact(self):
        return "Squares have each angle equal to 90 degrees."


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi*self.radius**2


a = Square(4)
b = Circle(7)
print(b)
print(b.fact())
print(a.fact())
print(b.area())
