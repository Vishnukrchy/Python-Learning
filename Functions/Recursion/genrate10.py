# genrated 0 to 10 by using recursion

def genrate(n):
    if n==10:
        return
    print(n,end=" ")
    genrate(n+1)

genrate(0)
print(" ")

print("Genrate 10 to 0")
def genrate_10_to_0(n):
    if n==-1:
        return
    print(n,end=" ")
    genrate_10_to_0(n-1)

genrate_10_to_0(10)    