#Recursion in python
 # Recursion is a function that calls itself
 # example 1 =>

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)   
print(factorial(5))
