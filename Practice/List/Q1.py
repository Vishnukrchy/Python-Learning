#**List Reversal:** Write a Python function that takes a list and returns the list reversed.
list=[1,2,3,4,5]
print("Original List : ",list)
def reversedList(list):
    reversedList=[]
    # iterate from last to first that meanis -1 beacued list index start from 0 and for loop  not include the last element
    for i in range(len(list)-1,-1,-1):
        reversedList.append(list[i])
    return reversedList  

print("Reversed List : ",reversedList(list))  

# def reverseList(list):
#     reversedList=[]
#     for i in range(len(list)-1,-1,-1):
#         reversedList.append(list[i])
#     return reversedList
# def reverseList2(list):
#     return list[::-1]


# print(reverseList(list))