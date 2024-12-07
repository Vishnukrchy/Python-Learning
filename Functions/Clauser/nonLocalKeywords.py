#Non Local Keywords => nonlocal keyword is used to access a variable in the outer scope of a function.
#example 1 =>

def outer_function():
    nv=5
    print("Outer function nv ",nv)
    def inner_function():
        nonlocal nv
        # here we can access nv variable outside the function and inside the function because its nonlocal variable and can only be accessed within that function.
        nv=6
        print("Inner function nv ",nv)
    inner_function()
    print("Outer function nv ",nv)

outer_function()