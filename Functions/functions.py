#Functions in Pythons
#Functions are blocks of code that can be used to perform a specific task.
#Functions can be defined using the def keyword.
#Functions can be called using the function name followed by parentheses.
#Functions can return a value using the return keyword.

#Syntax =>
#def function_name(parameters):
#    statements
#    return value  

#example 1 =>   
def greating():
    print("Good Morning")
#calling  function  by function name folowed by parentheses
greating() # in first line we define function and in second line we call function by function name
# here first step funtion is called then outer body is printed and then  control   
print("this Outer Body Of Program")

#When the function greet() is called, the program's control transfers to the function definition.
#All the code inside the function is executed.
#The control of the program jumps to the next statement after the function call.
#example 2 =>

# Functions with Parameters
# Functions can accept parameters, which are variables that are passed to the function when it is called.
# Parameters can be used to pass data to the function and control its behavior.

def greating(name):
    print("Good Morning : "+name)
greating("sohan")
greating("vishnu")
print(greating("ram"))

##Retrun value in functions
def greating(name): 
    print("Good Morning : "+name)
    return "Hello "+name
print(greating("sohan"))
print(greating("vishnu"))
print(greating("ram"))

# Functions with Default Parameters
# Functions can have default parameters, which are variables that are assigned a default value when the function is called.

def power(a,b=2):
    power =1
    for i in range(b):
        power =power*a
    print("Power of ",a," and ",b," is ",power)
power(2)# 2 to the power of 2
power(5)
power(2,3)# 2 to the power of 3

# finctions With default values
def info(first_name,last_name,age=30):
    print("First Name : ",first_name)   
    print("Last Name : ",last_name)
    print("Age : ",age)
info(first_name="sohan",last_name="navish")    
info(first_name="mohan",last_name="kumar",age=20)
#info(last_name="rohan",first_name="choudhray",10)# error => SyntaxError: non-default argument follows default argument                                                  ^
