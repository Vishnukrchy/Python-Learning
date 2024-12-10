# Customizing Exception

class SalaryRangeError(Exception):
    """Exception raised for errors in the input salary.

    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """
    def __init__(self, salary, message="Salary is not in range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)

    

salary=int(input("Enter the salary: "))
if not 20000<salary<50000:
    raise SalaryRangeError(salary)  

# expected output
# Enter the salary: 60000
# Traceback (most recent call last):
#   File "C:\Users\harsh\OneDrive\Desktop\python\python\Day3_DataTypes\Practice\CustomExptions2.py", line 24, in <module>
#     raise SalaryRangeError(salary)

