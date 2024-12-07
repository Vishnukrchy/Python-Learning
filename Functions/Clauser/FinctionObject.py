# in python function is an object

# example 1 =>
def outer_function():
    print("Outer function")    
    def inner_function():
        print("Inner function")
    return inner_function

val=outer_function()# its only called outer function and return inner function
print(val)#return inner function  as object
val()

print("===============  2 ================")
# example 2 alias of function =>
def outer_function():
    print("Outer function 2")    
    def inner_function():
        print("Inner function 2")
    return inner_function
al=outer_function
# Calling Outer FUnctionby  by alias
inn=al() # return inner function
inn()# call inner function
 # we can call outer  and inner function by alias
al()()# both inner and outer function is called

