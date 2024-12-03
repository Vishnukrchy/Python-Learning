#Nth Term Of  Fabonacci Series
n = int (input("enter the Nth Postion: "))
a,b,c=0,1,0
for i in range(2,n):
    c=a+b
    a=b 
    b=c
print("Nth Term Of Fabonacci Series",c)  



