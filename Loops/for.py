#  list iterartion
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x ,end=" ")
print(" ")   
# whith index
for f in range(len(fruits)):
    print(fruits[f],end=" ") 
print(" ")

# for loop in string
name="Mohan"
for x in name:
    print(x,end=" ")
print(" ")

# for loop in dictionary    
dict = {"name":"vishnu","age":30,"city":"Noida"}
for x in dict:
    print("key ",x,end=" ") # x will print key of dictionary
    print("value ",dict[x],end=" ") # dict[x] will print value of dictionary
    print(",")
print(" ")

# for loop in tuple
tuple = (1,2,3,4,5)
for x in tuple:
    print(x,end=" ")
print(" ")

# for loop in set
set = {1,2,3,4,5}
for x in set:
    print(x,end=" ")
print(" ")




   