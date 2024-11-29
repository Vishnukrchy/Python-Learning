# Method Of List in Python   
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list  
# copy()	Returns a copy of the list

list = [1,3,2,4,5]


#1. append()	Adds an element at the end of the list retrun none
list.append(6)
print(list)#[1, 2, 3, 4, 5, 6]
# 2 *****sort()  =>	Sorts the list assending order and its retrun none 
list.sort()
print(list.sort())#None
print(list)#[1, 2, 3, 4, 5, 6]
 # To sort in decending order
list.sort(reverse=True)
print(list)#[6, 5, 4, 3, 2, 1]
# sorting is also for string
list1=["bnana","apple","mango"]
list1.sort()
print(list1)#['apple', 'bnana', 'mango']

# 3 reverse()	Reverses the list and its retrun none
list.reverse()
print(list)#[6, 5, 4, 3, 2, 1]
# 4 clear()	Removes all the elements from the list and its retrun none
list.clear()
print(list) #[]
# insert()	Adds an element at the specified position in the list iriginal list will be changed retrun none
list = [1,3,2,4,5]
list.insert(2,6) # here it will replace index 2 by 6 and then from  index 3 rest elements will be added
print(list)#[1, 3, 6, 2, 4, 5]
list.insert(0,0)
print(list)#    [0, 1, 3, 6, 2, 4, 5]

# remove()	Removes the first occurrence of the specified element from the list and its retrun nonere
remo=list.remove(6)# 6  is element to be removed and return none
print(list)#[0,1, 3, 2, 4, 5]
print(remo)# none

# pop()	Removes the element at the specified index from the list and returns the removed element and its retrun none
list1 = [1,3,2,4,5,2,3]
list1.pop(2)# index 2 is element to be removed and retrun the removed element
print("List 1",list1)#[1, 3, 4, 5, 2, 3]
removedElement=list1.pop(3)
print("Removed Element from list1",removedElement)# 5
# Difference between pop and remove is that pop will return the removed element and remove will not return any thing

# index()	Returns the index of the first occurrence of the specified element in the list and its retrun none
print(list)#[0, 1, 3, 2, 4, 5]
print(list.index(5))#5
list.append(3)
print(list)#[0, 1, 3, 2, 4, 5, 3]
firstOrderIndex=list.index(3)
print(firstOrderIndex) #2

# count()	Returns the number of times the specified element appears in the list and its retrun none
print(list.count(5))#1
print(list.count(3))#2

# **copy()***	Returns a copy of the list 
list = [1,3,2,4,5]
list1 = list.copy()
print(list1)#[1, 3, 2, 4, 5]  

# extend()	Adds the elements of a list (or any iterable), to the end of the current list and its retrun none
list1 = [1,3,2,4,5]
list2 = [6,7,8,9]
list1.extend(list2)
print(list1)#[1, 3, 2, 4, 5, 6, 7, 8, 9]

# ***len()***	Returns the length of the list 
list1 = [1,3,2,4,5]
print(len(list1))#5



# create a list with square values
numbers = [n**2 for n in range(1, 6)]
print(numbers)    

# Output: [1, 4, 9, 16, 25]



