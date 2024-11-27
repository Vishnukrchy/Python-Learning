# Conditional Statments in python
# if-else-elf =>

a = 10
b = 20
#(1) if condition
if (a != b):{
  print("a is != b") # a is not equal to b")
}
# else condition
if (a > b):
 print("a is greater than b") 
else:
    print("b is greater than a")

# Note : The indentation is very important in python after if-else-elf we have to give Tab space
#Note -: we can also give {} in if-else-elf but its recommended to use indentation

# (2)if- eslse nested
#if- eslse nested
latter ="C"
if latter == "A":
    print("latter is A")
else:
    if latter=="B":
        print("latter is B")
    else:
        if latter=="C":
            print("latter is C")
        else:
            print("latter is  Not  A,B,C")
 # Note : The indentation is very important in python after if-else-elf we have to give Tab space  eslse we can also give {} in if-else-elf but its recommended to use indentation
 # if-elif statement example
letter = "A"

if letter == "B":
    print("letter is B")

elif letter == "C":
    print("letter is C")

elif letter == "A":
    print("letter is A")

else:
    print("letter isn't A, B or C")


# (3) if eslse-elif
a = 10
b ,c= 20,30   

if a>b:
    if a>c:
        print("{} is greater than {} and {}".format(a,b,c))
    else:
        print("{} is greater than {} and {}".format(c,a,b))
elif b>c:
    print("{} is greater than {} and {}".format(b,c,a))
else:
    print("{} is greater than {} and {}".format(c,b,a))

  





print("program ends")

