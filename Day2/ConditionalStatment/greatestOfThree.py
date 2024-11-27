num1= int(input("Enter first number: "))
num2= int(input("Enter second number: "))   
num3= int(input("Enter third number: "))

if num1>num2 and num1>num3:
    print(num1,"is greatest")
elif num2>num3:
    print(num2,"is greatest")
elif num1==num2 and num2==num3:
    print("All are equal")
else:
    print(num3,"is greatest")