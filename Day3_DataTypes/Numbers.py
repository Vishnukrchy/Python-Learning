num1 = 5
print(num1, 'is of type', type(num1))# it will print 5 is of type int
num2 = 5.42
print(num2, 'is of type', type(num2))# it will print 5.42 is of type float
num3 = 8+2j
print(num3, 'is of type', type(num3))# it will print (8+2j) is of type complex

#Number System in Python

#Binary Number System     0b => 0 or 1 base 2
#Octal Number System      0o    => 0 to 7 base 8
#Hexadecimal Number System 0x => 0 to 9 and A to F base 16

print(0b1101011)  # prints 107
print(0xFB + 0b10)  # prints 253
print(0o15)  # prints 13
print(0x1A)  # prints 26
print(0x1A + 0b10)  # prints 28 

# implsicit type Conversion ========================================================
print(1 + 2.0) # prints 3.0
# explicit type Conversion ========================================================
num1 = int(2.3)
print(num1)  # prints 2
num2 = int(-2.8)
print(num2)  # prints -2
num3 = float(5)
print(num3) # prints 5.0
num4 = complex('3+5j')
print(num4)  # prints (3 + 5j)

#Python Random Module==========================================
import random
print(random.randrange(10, 20))

list1 = ['a', 'b', 'c', 'd', 'e']
# get random item from list1
print(random.choice(list1))
# Shuffle list1
random.shuffle(list1)
# Print the shuffled list1
print(list1)
# Print random element
print(random.random())

#Mathamatical Operation in Python
import math

print(math.pi)# it will print 3.141592653589793
print(math.cos(math.pi))# it will print -1.0
print(math.exp(10))# it will print 22026.4657948068
print(math.log10(1000))# it will print 3.0
print(math.sqrt(9))# it will print 3.0  
print(math.sinh(1))# it will print 1.1752011936438014
print(math.factorial(6))# it will print 720

