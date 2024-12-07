#In Python we can define a function inside another function. This is called a nested function.
#  inner function is called by outer function 
# we can not call inner function by outer function directly by function name to call inner function we have to call outer function

def outer_function():
    print("Outer function")
    def inner_function():
        print("Inner function")
    inner_function() # when outer function is called then inner function is called
#inner function can not be called by outer function directly by function name to call inner function we have to call outer function

val=outer_function()   
print(val)#None

#case 2 return statement
def outer_function():
    print("Outer function")
    def inner_function():
        print("Inner function")
    return inner_function() # when outer function is called then inner function not called
#inner function can not be called by outer function directly by function name to call inner function we have to call outer function

val=outer_function()
print(val)#None



#case 3 return statement    
def outer_function():
    print("Outer function")
    def inner_function():
        print("Inner function")
    return inner_function # when outer function is called then inner function not called
#inner function can not be called by outer function directly by function name to call inner function we have to call outer function

val=outer_function()# its only called outer function and return inner function
print(val)#return inner function
val()

