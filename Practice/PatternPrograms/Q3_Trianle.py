#  Trianle Pattern
n=int(input("Enter a number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
#======================================
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")    
    print()   
print("======================= Reversed Trianle Pattern")
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()   
     
