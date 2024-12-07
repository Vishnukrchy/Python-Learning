
n=int(input("Enter a number: "))
for i in range(1,n+1):            # ****
    for j in range(1,n+1):        # ****
        print("*",end=" ")        # ****
    print()
print("====================================== 2nd Pattern")
for i in  range(1,n+1):
    for j in range(1,n+1):
        print(j,end=" ")
    print()
print("====================================== `")
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end=" ")
    print() 
print("====================================== 3rd Pattern")    
for i in range(1,n+1):
    for j in range(1,n+1):
        print(n-j+1,end=" ")
    print()
print("====================================== 4th Pattern" )

count =1
for i in range(1,n+1):
 
   for j in range(1,n+1):
       print(count,end=" ")
       count+=1
   print()
print("======================================")   
