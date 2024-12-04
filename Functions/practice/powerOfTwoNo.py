num1=int(input("Enter a number 1 : ")) 
num2=int(input("Enter a number 2 : "))

def power(a,b):
    power =1
    for i in range(b):
        power =power*a
    return power
print("Power of ",num1," and ",num2," is ",power(num1,num2))    

def power(a,b):
    pw=a**b
    return pw
print("Power of ",num1," and ",num2," is ",power(num1,num2))    
