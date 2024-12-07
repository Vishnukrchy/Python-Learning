#Sum of 10 netural numbers by recursion

def add(n):
    if n==0:
        return 0
    else:
        sum= n+add(n-1)
        return sum
print(add(10))        

