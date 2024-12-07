#
g=3# global variable
print("Global variable ",g)
def outer_function():
    global g
    g=2
    n=4# non local variable
    print("Outer function g,n ",g,n)
    def inner_function():
        nonlocal n
        n=5
        l=6
        print("Inner function g,n",g,n)
        print("Inner function l",l)
    inner_function()

outer_function()





print("=======================")

def outer_function():
    a=1
    print("Outer function a ",a)
    def inner_function():
        a=4 # local variable here we can access a variable outside the function and inside the function because its nonlocal variable and can only be accessed within that function.
        print("Inner function a ",a)#4
    inner_function()
    print("Outer function a ",a)#1

outer_function()#1