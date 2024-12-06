#Count Occurrences of an Element in a List: Write a Python function that counts the occurrences of a specific element in a list.

list=[1,4,5,1,3,5,6,3,5,8,9,0,2,0,4,23,6,]
def countFrequency(list):
    dict={}
    for i in list:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1

def countElement(list):
    for i in  list:
        count=1
        for j in list:
            if i==j:
                count+=1
        print("The element ",i," is repeated ",count," times")

countElement(list)        