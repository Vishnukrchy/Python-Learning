#multilevel inheritance in python
#=> Multilevel inheritance is a feature in object-oriented programming that allows a class to inherit properties and methods from a parent class and also from a grandparent class.
#=> When a class inherits from a grandparent class, it can access the attributes and methods of both the parent and grandparent classes.

#SYNTAX
class SuperClass:
    # Super class code here
    pass

class DerivedClass1(SuperClass):
    # Derived class 1 code here
    pass

class DerivedClass2(DerivedClass1):
    # Derived class 2 code here
    pass

# example 1 =>

class SuperClass:
    def supper_class_method(self):
        print("Super class method")

class DerivedClass1(SuperClass):
    def derived1_class_method(self):
        print("Derived class method")

class DerivedClass2(DerivedClass1):
    def derived2_class_method(self):
        print("Derived class method")

obj = DerivedClass2()
obj.supper_class_method()
obj.derived1_class_method()
obj.derived2_class_method()
#Method Resolution Order (MRO) in Python
#=> The MRO is a list of classes that define the order in which methods are resolved during method lookup.
#=> The MRO is determined by the order in which classes are defined in the inheritance hierarchy.

#example 2 =>

class SuperClass1:
    def info(self):
        print("Superclass1 method")

   
class SuperClass2:
    def info(self):
        print("Superclass2 method")
class DerivedClass(SuperClass1,SuperClass2):
    pass

obj = DerivedClass()
obj.info()# in this case it will print Superclass1 method because it is first in the inheritance hierarchy
# Python follow the method resolution order (MRO) to determine the order in which methods are resolved during method lookup
# in this case it will print Superclass1 method because it is first in the inheritance hierarchy like its call left 