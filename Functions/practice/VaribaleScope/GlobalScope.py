# Vraible Glopal Scope In Python
# Gloal variable => variable that is defined outside of a function and can be accessed from any part of the program.
# example 1 =>
massege = 'Hello'
def greet():
    print("Local", massege)
print("Global", massege)
greet() 
# here we can access massege variable outside the function  and inside the function bescause its global variable
# its decalared outside the function and can be accessed from any part of the program
# example 2 =>
sume=12
print("sum",sume)
def add_numbers():
   print("Sum ",sume)# it will print sum 12 crrently it is global variable
#    sume=sume+20 it will give error becaused its local variable and can only be accessed within that function
   print("Sum is ",sume)# it will print sum 50 after adding 20 and 30 and its local variable because its decalared inside the function and can only be accessed within that function 
add_numbers()
# here we can access sume variable outside the function and inside the function because its local variable
print("sum",sume)   

