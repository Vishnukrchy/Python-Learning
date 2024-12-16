# Abstraion in python => Abstraction is a concept in object-oriented programming that allows you to hide the internal details of an object and expose only the necessary information to the outside world.
# Abstraction is a way of representing a complex system in a simplified way that is easier to understand and use.

#exple 1
class Car:
    def __init__(self, name, color, brand, price):
        self.name = name
        self.color = color
        self.brand = brand
        self.price = price
        self.acc=False

    def start(self):
        print("Car started")
        self.acc=True

    def stop(self):
        print("Car stopped")
        self.acc=False