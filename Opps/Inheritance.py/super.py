# super() => super() is a built-in function in Python that is used to access the parent class of a child class.
# super() is used to call the parent class constructor and access the parent class methods and attributes.
# super() is used to call the parent class constructor and access the parent class methods and attributes.

# example 1 calling parrent class constructor =>
class ParentClass:
    def __init__(self):
        print("Parent class constructor is called")

class ChildClass(ParentClass):
    def __init__(self):
        super().__init__()  # calling parent class constructor
        print("Child class constructor is called")

obj = ChildClass()
print(obj)
class GrandChildClass(ChildClass):
    def __init__(self):
        super().__init__()  # calling parent class constructor
        print("Grand child class constructor is called")
print("========================================")
obj = GrandChildClass()
print(obj)

p=ParentClass()



print("========================================")

# example 2 calling parret class method =  >

class ParentClass:
    def __init__(self):
        print("Parent class constructor is called")

    def parent_method(self):
        print("Parent class method is called")


class ChildClass(ParentClass):
    def __init__(self):
        super().__init__()  # calling parent class constructor  
        print("Child class constructor is called")

    def child_method(self):
        super().parent_method()  # calling parent class method
        print("Child class method is called")

obj = ChildClass()
obj.child_method()  
