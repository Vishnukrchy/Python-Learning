# Tuples in python
#A tuple is a collection similar to a Python list. The primary difference is that we cannot modify a tuple once it is created.similar to string
# Tuples are immutable, you can not change the value of a tuple after it is created.  (can not modify by using indexing) 
# Tuples are a collection of items in a particular order that can be accessed using indexing and slicing. (can access by using indexing)
# Tuples are a collection of items that can be used to store a group of values, such as numbers, strings, or other tuples.

# Tuple Characteristics
# ordered - They maintain the order of elements.(can access by using indexing)
# immutable - Items cannot be changed after creation.(can not modify by using indexing)
# allow duplicates - They can contain duplicate values.(we can store hetrogenous data type and duplicate value) 

#create tuple
tuple = (1, 2, 3, 4, 5)  # or tuple = 1, 2, 3, 4, 5
print(tuple)# it will print tuple => (1, 2, 3, 4, 5)
print(type(tuple))# it will print tuple type => <class 'tuple'>
#Create tuple using constructor
# tuple_constructor = tuple(['Jack', 'Maria', 'David'])
# print(tuple_constructor)# it will print tuple => ('Jack', 'Maria', 'David')

# Accessing Tuple Elements
print(tuple[0])# it will print first element => 1
print(tuple[2:5])# it will print from index 2 to 4 => (3, 4, 5)

# Tuple Length
print(len(tuple))# it will print length of tuple => 5   
#print(tuple_constructor.length())# it will print length of tuple => 3   

#tumple is immutable, you can not change the value of a tuple after it is created.
tup=(23,45,67,89)
print(tup)# it will print tuple => (23, 45, 67, 89)
tup[0]=90 #Error we can not change the value of tuple on the based of index


# tuple is immutable, you can not change the value of a tuple after it is created.
cars = ('BMW', 'Tesla', 'Ford', 'Toyota')
# trying to modify a tuple
cars[0] = 'Nissan'    # error    
print(cars)# it will print tuple => ('BMW', 'Tesla', 'Ford', 'Toyota')




