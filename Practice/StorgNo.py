# WAP to check a noumber is storng number or not
#ex of strong number => 145 => 1!+4!+5! = 1+24+120 = 145 is strong number
# 153 = 1!+5!+3! = 1+120+6 = 153 is strong number

num = int(input("Enter a number: "))

temp = num
sum = 0
while temp > 0:
    lastDigit = temp % 10
    fact = 1
    for i in range(1, lastDigit + 1):
        fact = fact * i
    sum = sum + fact
    temp = temp // 10
if num == sum:
    print(num, "is a strong number")
else:
    print(num, "is not a strong number")  

 # by Functions 
 #ex of strong number => 145 => 1!+4!+5! = 1+24+120 = 145 is strong number
def fact(num):
    fact = 1
    # here we are using for loop and we want itrate from 1 to num  so we use range and range(1,num+1)
    for i in range(1, num + 1):
        fact = fact * i
    return fact
def isStrong(num):
    temp = num
    sum = 0
    while temp>0:
        lastDigit=temp%10
        sum=sum+fact(lastDigit)
        temp=temp//10  
    return sum==num
n = int(input("Enter a number: "))
if isStrong(n):
    print(n, "is a strong number")
else:
    print(n, "is not a strong number")          