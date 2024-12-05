#factoreial of a number
n =int(input("Enter a number: "))

def findfactorial(n):
    fact =1
    for i in range(1,n+1):
        fact=fact*i
    return fact
print("factorial of",n,"is",findfactorial(n))    
