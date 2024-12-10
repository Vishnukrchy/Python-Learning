# Exception handling in python
# try block
# except block
# else block
# finally block

# try:
#     # code that may raise an exception
# except:
#     # code that run if an exception is raised
# else:
#     # code that run if no exception is raised
# finally:
#     # code that run regardless of whether an exception is raised or not

# Way 1 =>> try and except block
# try:
#     numrator = int(input("Enter the numerator: "))
#     denominator = int(input("Enter the denominator: "))
#     result = numrator // denominator
#     print(result)
# except :
#     print("You can't divide by zero")

#print("Program is finished")

# Way 2 =>> try and except block with specific exception
try:
    numrator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numrator // denominator
    print(result)

    my_list = [1,2,3]
    print(my_list[int(input("Enter the index: "))])
except ZeroDivisionError: 
    print("You can't divide by zero")
except IndexError:
    print("Your index is out of range")    

