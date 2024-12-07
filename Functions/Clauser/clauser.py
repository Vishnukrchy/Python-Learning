# clouser in python => 
# In Python, a closure is a function that has access to its own scope and the scope of its outer functions, even when the outer functions have finished executing.
# example 1 =>

def outer_function(x):
    def inner_function(y):
        print("X is ",x)
        print("Y is ",y)
        return x + y
    return inner_function
closerr=outer_function(5)# here afetr executing outer function it will return inner function 
# even  outer function finish executing it will take x value  because of clouser
res=closerr(10)
print(res)


# example 2 =>

def outer_function():
    str="Mohan in outer function"
    def inner_function(x):
        print(str)
        print("X is ",x)
        return str+x
    return inner_function
  

outer_function()

