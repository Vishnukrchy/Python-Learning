#WAP to Check a no is Armstrong or not
#ex of Armstrong no => 153 => 1^3+5^3+3^3 = 1+125+27 = 153 is Armstrong no
num = int(input("Enter a number: "))

def count_digits(num):
    count=0
    while num !=0:
        count+=1
        num=num//10
    print("Total digit is ",count)
    return count
def sum_of_digits(num):
    temp = num
    total = 0
    digit_count = count_digits(num)
    while num != 0:
        last_digit = num % 10
        total += power(last_digit, digit_count)
        num //= 10
    return total == temp     

def power(a,b):
    power=1
    for i in range(b):
        power=power*a
    return power

if sum_of_digits(num):
    print(num, "is a Armstrong number")
else:   
    print(num, "is not a Armstrong number") 
# By while loop  ======================================================
temp = num
sum = 0
while temp > 0:
    lastDigit = temp % 10
    sum = sum + lastDigit ** 3
    temp = temp // 10
if num == sum:  
    print(num, "is a Armstrong number")
else:   
    print(num, "is not a Armstrong number")
