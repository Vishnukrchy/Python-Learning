# Non Local Varibale In Python
# => In Python a variable is said to be nonlocal if it is defined in an enclosing function and its scope extends outside of the function.
# => A nonlocal variable can be accessed in the inner function by using the nonlocal keyword.
# => tO create a nonlocal variable, you must use the nonlocal keyword inside the inner function.

# example 1 =>
def outer_function():
    mesaage="Local"
    print(" Massage in outer function scope ",mesaage)
    def inner_function():
        nonlocal mesaage
        mesaage="Nonlocal"
        print(" Massage in inner function scope "+mesaage)
    inner_function()
    print(mesaage)
outer_function()

# example 2 =>
def outer_function():
    sum=0
    print("Sum in outer function scope ",sum)#0
    def inner_function():
        nonlocal sum # here we can access sum variable outside the function and inside the function because its nonlocal variable and can only be accessed within that function.
        sum =12+90
        print("Sum in inner function scope ",sum)# 102
    inner_function()
    print("Sum in outer function scope ",sum)#102
outer_function()

#
print("=======================  1 =======================")

def outer_function():
    sum=0
    print("Sum in outer function scope ",sum)#0
    def inner_function():
        sum =12+90
        print("Sum in inner function scope ",sum)# 102
    inner_function()
    print("Sum in outer function scope ",sum)#102
outer_function()

    
