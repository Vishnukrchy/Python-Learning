# loops  in python

# for loop => used to iterate over a sequence of elements suach as list, tuple, string, dictionary  
# while loop => used to iterate over a condition till the condition is true

# for loop  ==>
# Syntax -: 
# for var in sequence:
#     statement or code block
langages=["c","c++","java","python"]
#access the elements of list
for i in langages:
    print(i)# here i is  variable i we can use any name is used to access the elements of list
#access the index of list
for i in range(len(langages)):
    print(langages[i]+" is at index ",i) # here i is used as index start form o to len of list and  acced by index

# Iddentation error => in python indentation is important its defines a block of code or block of statement
print("start of for loop")
for i in range(5):
    print(i)
    print(i+1)
 #print(i+2) # indentation error
print("end of for loop")

# explample  loops through a string
names ="Mohan is here!";
count=0
for  ch in names:
    print("char is ",ch+" at index ",count)
    count+=1
print ("another way to print")
for i in range(len(names)):# we can only used in this which can access the index like string,list,tuple
    print(names[i]+" is at index ",i)


#  Range function => RANGE function is used to generate a sequence of numbers in python
value = range(4) #=> it will print 0,1,2,3
print ("ex  range(4) => it will print 0,1,2,3")
for i in range(4):
    print(i) # it will print 0,1,2,3

# ex  value = range(2,10) => it will print 2,3,4,5,6,7,8,9
for i in range(2,10):
    print(i) # it will print 2,3,4,5,6,7,8,9

# ex  value = range(2,10,2) => it will print 2,4,6,8
#    by default step is 1 and stop is not included then it will start from 0 to stop-1 
print("ex  value = range(2,10,2) => it will print 2,4,6,8")
for i in range(2,10,2):
    print(i)# it will print 2,4,6,8    

# range function in python => range(start,stop,step) => default range is (0,stop)
#   by default step is 1 and stop is not included then it will start from 0 to stop-1 









