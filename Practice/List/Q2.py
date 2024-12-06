#Find the Largest Number in a List: Write a function to find the largest number in a list of integers.
list = [1,2,3,9,4,5]
def maxNoumber(list):
    max = list[0]
    for i in range(len(list)):
        if list[i]>max:
            max=list[i]
    return max
print("max number is : ",maxNoumber(list))    
print(max(list))