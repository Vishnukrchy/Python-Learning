#Funtcions whith parametrs

# Add two numbers
def add(num1,num2):
    sum =num1+num2
    print("Sum of ",num1," and ",num2," is ",sum)

add(2,3)  

# Add three numbers
def add(num1,num2,num3):
    sum =num1+num2+num3
    print("Sum of ",num1," and ",num2," and ",num3," is ",sum)
add(2,3,4)
# squrare of number a number
def square(num):
    sq=num*num
    print("Square of ",num," is ",sq)

square(2)
# power Of two Noumber
def power(a,b):
    power =1
    for i in range(b):
        power =power*a
    print("Power of ",a," and ",b," is ",power)
power(2,3)# 2 to the power of 3

#Funtion with default parametrs
def power(a,b=5):
    power =1
    for i in range(b):
        power =power*a
    print("Power of ",a," and ",b," is ",power)
power(2)# 2 to the power of 5=2*2*2*2*2=>32
power(2,3)# 2 to the power of 3=2*2*2=>8

#reverse of  a noumber

def reverse(num):
    reversedNo = 0
    while num!=0:
        lastdigit = num%10
        reversedNo=reversedNo*10+lastdigit
        num=num//10
    print("Reversed number is ",reversedNo)
reverse(1234)# 4321  

    



    