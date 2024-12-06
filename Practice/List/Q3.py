#List Slicing: Given a list of numbers, return a new list containing the first three elements, and then another with the last three elements.

list = [1,2,3,4,5,6,7,8,9,10]
print("Original List : ",list)
print("First Three Elements : ",list[0:3])
print("Last Three Elements : ",list[7:])


def first_three(list):
     first_three=[]
     for i in range(0,3):
         first_three.append(list[i])
     return first_three

def last_three(list):    
     last_three=[]
     for i in range(7,10):
         last_three.append(list[i])
     return last_three




