#fabunacci series by recursion

def fab(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fab(n-1) + fab(n-2)

n = int(input("Enter the number: "))
for i in range(1,n+1):
    print(fab(i),end=" ")
        
