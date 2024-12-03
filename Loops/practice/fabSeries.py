# WAP To Pprint the natural fabunacci series
n=int(input("Enter the number: "))
a,b=0,1
for i in range(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
else:
    print()
    print("Progam End")    



   