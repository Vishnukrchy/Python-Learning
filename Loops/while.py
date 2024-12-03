# While Loops In Python
# while loop => used to iterate over a condition till the condition is true
# Syntax :
# while condition:
#     statement
i=1
while i<=10:
    print(i,end=" ")
    i+=1
print("\n")
i=10
while i>=1:
    print(i,end=" ")
    i-=1
print("\n")
# Print Number  unti user enter 0
num = int(input("Enter a number: "))
while num !=0:
    print("Number is ",num)
    num = int(input("Enter a number: "))
else: 
    print("You entered 0 program is finished")   
     