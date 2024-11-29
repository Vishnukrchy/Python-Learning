# ***List in Python***
#List is a collection of items in a particular order  (maitained insertion order)
# list is mutable, you can change the value of a list after it is created.(provides indexing and slicing)
# list is a collection of items in a particular order that can be accessed using indexing and slicing.
# in list we can store hetrogenous data type and duplicate value    
# list can strore any type of data type like int, float, string, boolean, list, tuple, dictionary
# list in python similar as array in java but diffence is in array we can store homogenous data type but in list we can store hetrogenous data type

# List Characteristics
# Lists are:

# Ordered - They maintain the order of elements.
# Mutable - Items can be changed after creation.
# Allow duplicates - They can contain duplicate values.

#Create List
example = [1,2,3,4,5]
print(example)# it will print list => [1, 2, 3, 4, 5]
print(type(example))# it will print list type => <class 'list'>

print(example[0])# it will print first element => 1
print(example[2:5])# it will print from index 2 to 4 => [3, 4, 5]

# list is mutable, you can change the value of a list after it is created.
example[0] = 10
print(example)# it will print list => [10, 2, 3, 4, 5]
# Note in string we can not change the value of string on the based of index but in list we can change the value of list

# list in python similar as array in java but diffence is in array we can store homogenous data type but in list we can store hetrogenous data type


marks=[10,20,30,40,50]

print("Marks are ",marks);#Marks are  [10, 20, 30, 40, 50]
print("Marks are ",marks[0]);#Marks are  10
print("Marks are ",marks[1]);#Marks are  20
print("type of marks list ",type(marks));#type of marks list  <class 'list'>

print("Marks are ",marks[0:3]);#Marks are  [10, 20, 30]
print("Marks ",marks[-1]);#Marks  50


x = "axz"
# convert to list
result = list(x)
print(result)  # ['a', 'x', 'z']

# a list containing strings and numbers
student = ['Jack', 32, 'Computer Science']
print(student)# it will print list => ['Jack', 32, 'Computer Science']

# an empty list
empty_list = []
print(empty_list)# it will print list => []
