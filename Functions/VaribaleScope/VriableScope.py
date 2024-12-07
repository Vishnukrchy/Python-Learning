# vraible Scaope In Python
# there are two types of variable scope in python
# 1. Global variable
# 2. Local variable
# 3. Nonlocal Variables

#Local Variable => variable that is defined inside a function and can only be accessed within that function.
#example 1 =>

def sum():
    sumation=10+20
#print(sumation) #Error: name 'sumation' is not defined   
# => Here we can not access sumation outside the function
def greet():
    # local variable
    message = 'Hello'
    print('Local', message)

greet()
# try to access message variable 
# outside greet() function
print(message)

# Local Hello
# NameError: name 'message' is not defined

if 5>1:
    message = 'Hello'
print(message)
# here we are trying to access message variable outside the if block
# NameError: name 'message' is not defined becaused its local variable and we can not access it outside the block
