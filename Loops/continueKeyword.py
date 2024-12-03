#continue keyword in python
#The continue keyword is used to skip the current iteration of a loop and continue to the next iteration.
#The continue keyword is used to skip the current iteration of a loop and continue to the next iteration.

for i in range(10):
    if i == 5:
        print()
        print("i is 5 so continue skip the current iteration of the loop now \n")
        continue
    print(i,end=" ")

 #print odd no form 1 to 10
print("\n")
i=1
while i<=10  :
    if i%2==0:
        i+=1
        continue
    print(i,end=" ")
    i+=1
    
    
