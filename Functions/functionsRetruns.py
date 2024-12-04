#Retrun Keyword in python
 # add two nooumber and retrun By function
def add(num1,num2):
    sum=num1+num2
    return sum
# IF A FUNCTION RETURNS A VALUE THEN WE USE RETURN KEYWORD AND  WE CAN STORE THIS VALUE IN A VARIABLE OR DIRECTLY PRINT IT
sum=add(2,3)
print("Sum of 2 and 3 is ",sum)
print(add(2,3))

#Subtraction of two nooumber and retrun By function
def sub(a,b):
    sub=a-b
    return sub
print("Subtraction of 2 and 3 is ",sub(2,3))

#multiplication of two nooumber and retrun By function
def multiply(num1,num2):
    mul=num1*num2
    return mul
print("multiplication of 2 and 3 is ",multiply(2,3))    

#division of two nooumber and retrun By function
def divide(a,b):
    div= a/b
    print(" dividion round off is ",round(div))#it will print round off value like 2.0   
    print(" dividion  no decimals is ",a//b) #it will print no decimals value like 2
    return div
print("division of 2 and 3 is ",divide(10,3))   

#exponentiation of two nooumber and retrun By function
def power(a,b):
    pow=a**b
    return pow
print("power of 2 and 3 is ",power(2,3))

def power1(a,b):
    pow=a**b
    return pow
print("power of 2 and 3 is ",power(2,3))