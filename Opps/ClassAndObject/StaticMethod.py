#Static Method in Python
# => A static method is a method that is bound to a class rather than an instance of a class.
# => Static methods are defined using the staticmethod decorator.
# => Static methods are called without an instance of the class, but they can access class attributes and methods.

#syntax
# class_name():
#     @staticmethod
#     def static_method():
#         pass
#Why we need static method?
#=>Static methods are used to define utility functions that are not associated with any particular instance of a class
# =. to make Static metgh.

#example 1 =>
class Employee:
    def __init__Z(self,name,salary,city):
        self.name=name
        self.salary=salary
        self.city=city

        #static method which i want to 
        @staticmethod
        def getEmployeeCount():
            return 500
        
