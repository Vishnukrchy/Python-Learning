#List Comprehension for Even Numbers: Given a list of numbers, use a list comprehension to return a new list containing only the even numbers.

list = [1,2,3,4,5,6,7,8,9,10]
print(' Original List is : '+str(list))
def evenNumberList(list):
    evenNumber=[]
    for i in list:
        if i%2==0:
            evenNumber.append(i)
    return evenNumber
print("Even No list is : ",evenNumberList(list))    