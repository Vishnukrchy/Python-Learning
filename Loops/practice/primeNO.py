# Prime no 
num = int(input("Enter a number: "))

for i in range(2,int(num/2)):
    if num%i==0:
        print(num,"is not a prime number")
        break
else:
    print(num,"is a prime number")

print (" From while loop ")
i=2  # i satrt from 2  because 1 is not prime number
while i<int(num/2):
    if num%i==0:
        print(num,"is not a prime number")
        break
    i+=1
else:
    print(num,"is a prime number")
