#Tuple Swapping: Given two variables a and b with values, swap their values using tuples.

def swap_values(a, b):
    a, b = b, a
    return a, b

# Example
print(swap_values(5, 10))  # Output: (10, 5)



a = 10
b=20
a,b=b,a
print(a,b)