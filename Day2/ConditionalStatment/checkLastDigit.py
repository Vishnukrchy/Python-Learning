# WAP to Check Last Digit Of A number
num = int(input("Enter a number: "))

latDigit = num % 10

if latDigit == 0:{
    print("Last digit is 0")
}
elif latDigit > 0:
   if latDigit % 2 == 0:
        print(latDigit, "Last digit is even")
   else:
        print(latDigit, "Last digit is odd")
else:
    print("Last digit is not present")