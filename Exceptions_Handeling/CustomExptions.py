# Customs expetions in python
# => A custom exception is a user-defined exception that is raised when an error occurs during the execution of a program.
# = to define a custom exception we need to inherit from the Exception class

# class CustomException(Exception):
#     pass

# try:
#     raise CustomException("This is a custom exception")
# except CustomException as e:
#     print(e) # Output: This is a custom exception

# define Python user-defined exceptions
class InvalidAgeException(Exception):
    "Raised when the input value is less than 18"
    pass

# you need to guess this number
number = 18

try:
    age = int(input("Enter Your age: "))
    if age < number:
        raise InvalidAgeException
    else:
        print("Eligible to Vote")
        
except InvalidAgeException:
    print("Exception occurred: Invalid Age")