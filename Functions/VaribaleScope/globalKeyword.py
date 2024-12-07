#Global Scope and Global Keyword In Python
# => In Python a variable is said to be global if it is defined outside of any function and its scope extends to the entire program. 
# => A global variable can be accessed from any part of the program by using the global keyword.

# example 1 =>
x=5
y=6
def func():
    global x
    x=9
    print(f"global  variable x inside the function : {x}")
    y=3
    print(f" variable y inside the function : {y}")
func()
print(f"global variable x  : {x}")
print(f"global variable y  : {y}")