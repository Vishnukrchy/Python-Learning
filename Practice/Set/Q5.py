# **Remove Duplicates from a List Using Set:** Given a list, write a Python function to remove duplicates by converting it into a set.

list1=[1,2,3,4,5,1,2,3,4,5]

def removeDuplicate(list1):
    set1=set(list1)
    list1=list(set1)
    return list1
    
set1=set(list1)
print(set1)