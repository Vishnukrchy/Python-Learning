# Tuples methods in python
# append()	Adds an element at the end of the tuple  ===>Error
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Returns the index of the first occurrence of a specified value in a tuple
# len()	Returns the length (the number of items) in a tuple
# pop()	Removes the element at the specified position ===>Error
# remove()	Removes the first item with the specified value
# sort()	Sort the tuple


tuple = (1, 2, 3, 4, 5)
# append()	Adds an element at the end of the tuple
#tuple.append(6) #======> error because tuple is immutable and append() method is not available
print(tuple)# it will print tuple => (1, 2, 3, 4, 5, 6)

# count()	Returns the number of times a specified value occurs in a tuple
tuple = (1, 2, 3, 4, 5)
count = tuple.count(2)
print(count) # it will print count => 1

list = [1, 2, 3, 4, 5]
count = list.count(2)
print(count) # it will print count => 1

# index()	Returns the index of the first occurrence of a specified value in a tuple   
tuple = (1, 2, 3, 4, 5)
index = tuple.index(3)
print(index) # it will print index => 2

# len()	Returns the length (the number of items) in a tuple
tuple = (1, 2, 3, 4, 5)
length = len(tuple) 
print(length) # it will print length => 5

# pop()	Removes the element at the specified position
tuple = (1, 2, 3, 4, 5)
#tuple.pop(0) #======> error because tuple is immutable and pop() method is not available
print(tuple) # it will print tuple => (2, 3, 4, 5)

# remove()	Removes the first item with the specified value
tuple = (1, 2, 3, 4, 5)
tuple.remove(3)
print(tuple) # it will print tuple => (1, 2, 4, 5)

# sort()	Sort the tuple
tuple = (1, 2, 3, 4, 5)
tuple.sort()
print(tuple) # it will print tuple => (1, 2, 3, 4, 5)   