#Local variable => variable that is defined inside a function and can only be accessed within that function.
#example 1 =>

x=5
def  func():
    x=6#Local variable here are we are decalaaring local variable x for this function scope only and if we try to access this variable outside the function it will give error
    y=4
    print(f"local variable x : {x}")#it will print 6
    print(f"local variable y : {y}")#it will print 4
func()

print(f"global variable x : {x}")#it will print 5
# if we try to access local variable outside the function it will give error
print(f"global variable y : {y}")#NameError: name 'y' is not defined