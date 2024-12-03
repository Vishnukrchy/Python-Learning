# For Else Loop min python
#=Else used with for loop to execute a block of code when the loop is finished

for i in range(10):
    print(i,end=" ")
else:
    print("loop is finished")
# it will print 0 to 9 and then it will print loop is finished

digit=[1,6,5,0,9,0]
for  i in digit:
    print(i, end="")
else:
    print("loop is finished")
# it will print 1,6,5,0,9,0 and then it will print loop is finished

# Loops Without accseing  items 
languages=["c","c++","java","python"]
 # Loops iterratiog over a sequence
count =0
for lang in languages:
    print (" Itreration is ",count)
    count+=1

# Nested Loops 
for i in range(3):
    for j in range(3):
        print("i is {i} and j is {j}".format(i=i,j=j))
