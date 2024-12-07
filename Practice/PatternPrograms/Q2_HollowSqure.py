print(" =========== Print trainale Pattern 1 ===========")
n=int(input("Enter a number: "))
for i in range(1,n+1):           
   if i==1 or i==n:
       for j in range(1,n+1):
           print("*",end=" ")
       print()
   else:
       for j in range(1,n+1):
           if j==1 or j==n:
               print("*",end=" ")
           else:
               print(" ",end=" ")
       print()