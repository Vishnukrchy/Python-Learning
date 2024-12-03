# Reverse The No Entered By User
num= int(input("Enter a number: "))
num1=num
reversedNo = 0
while num!=0:
    lastDigit = num % 10
    reversedNo = reversedNo * 10+lastDigit
    print("Reversed number is ",reversedNo)
    num = num//10

print("Final Reversed number is ",reversedNo) 


reversedNo = 0
for i in range(len(str(num1))):
    lastDigit = num1 % 10
    reversedNo = reversedNo * 10+lastDigit
    print("Reversed number is ",reversedNo)
    num1 = num1//10

print("Final Reversed number is ",reversedNo)
