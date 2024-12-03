#Break Keyword in Python
#The break keyword is used to exit a loop. It is used to stop the loop when a certain condition is met.
#The break keyword is used to stop the loop when a certain condition is met.

for i in range(10):
    if i == 5:
        print("i is 5 so break the loop now \n")
        break
    print(i,end=" ")
print("\n")

# Print Number  unti user enter 0
num = int(input("Enter a number: "))
while num !=0:
    print("Number is ",num)
    num = int(input("Enter a number: "))
    if num == 0:
        break
   
print("You entered 0 program is finished")