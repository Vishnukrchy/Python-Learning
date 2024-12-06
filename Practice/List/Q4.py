#Sum of Elements in a List: Write a Python function that takes a list of numbers and returns the sum of all elements.

list = [1,2,3,4,5,6,7,8,9,10]
def sumOfElements(list):
    #return sum(list)
    sum = 0
    for i in list:
        sum += i
    return sum

print(sumOfElements(list))