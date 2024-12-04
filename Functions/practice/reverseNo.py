#Reverse a Noumber
num=int(input("Enter a number: "))

def reverse(num):
    reversedNo = 0
    while num!=0:
        lastdigit = num%10
        reversedNo=reversedNo*10+lastdigit
        num=num//10
    return reversedNo
print("Reversed number is ",reverse(num))