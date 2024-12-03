# Plaindome No 
num=int(input("Enter a number: "))
num1=num
reversedNo = 0
while num!=0:
    lastDigit = num % 10
    reversedNo = reversedNo * 10+lastDigit
    print("Reversed number is ",reversedNo)
    num = num//10
if num1==reversedNo:
    print("Number is plaindrome")
else:
    print("Number is not plaindrome")

print("From for loop")

   