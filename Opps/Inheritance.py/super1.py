class Animal:
    def __init__(self):
        print("Animal is created")
    def whoAmI(self):
        print("Animal")
    def eat(self):
        print("Eating")
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog is created")
    def whoAmI(self):
        print("Dog")
    def eat(self):
        print("Dog is eating")
        super().eat()
dog=Dog()
dog.eat()                    