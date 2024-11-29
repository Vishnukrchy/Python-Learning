#data Types in Python
#(1) Numbers and Mathematical => python supports two numeric data types: int and float and for mathical operations it complex number is not supported in python
# uses the built-in math module that provides access to a wide range of mathematical functions. like sqrt(), log(), exp(), etc. 

num1 = 10
num2 = 3.14 # desault its convert into float
sum = num1 + num2
print(sum)
print(type(sum))# we can explicitly cast  into int 


example = 1+2j
print(example)# it will print complex number => (1+2j)

#(2) String => string is a sequence of characters
# string is immutable, you can not change the value of a string after it is created.
# string is a collection of characters that can be accessed using indexing and slicing. 
# string is a sequence of characters that can be used to store text, such as words, sentences, or paragraphs.

example = "hello world"
print(example)  
print(type(example))

print(example[0])# it will print first characte => h
print(example[2:5])# it will print from index 2 to 4 => 
example[0] = "H" # we can not change the value of string on the based of index  becaused its immutable


#(3) List => list is a collection of items in a particular order
# list is mutable, you can change the value of a list after it is created. 
# list is a collection of items in a particular order that can be accessed using indexing and slicing. 
# list is a collection of items that can be used to store a group of values, such as numbers, strings, or other lists.

example = [1,2,3,4,5]
print(example)# it will print list => [1, 2, 3, 4, 5]
print(type(example))    
print(example[0])# it will print first element => 1
print(example[2:5])# it will print from index 2 to 4 => [3, 4, 5]

#(4) Tuple => tuple is a collection of items in a particular order
# tuple is immutable, you can not change the value of a tuple after it is created. 
# tuple is a collection of items in a particular order that can be accessed using indexing and slicing. 
# tuple is a collection of items that can be used to store a group of values, such as numbers, strings, or other tuples.  

example = (1,2,3,4,5)
print(example) # it will print tuple => (1, 2, 3, 4, 5)
print(type(example))
print(example[0])# it will print first element => 1
print(example[2:5])# it will print from index 2 to 4 => (3, 4, 5)     

#(5) Dictionary => dictionary is a collection of key-value pairs
# dictionary is mutable, you can change the value of a dictionary after it is created. 
# dictionary is a collection of key-value pairs that can be accessed using indexing and slicing. 
# dictionary is a collection of key-value pairs that can be used to store a group of values, such as numbers, strings, or other dictionaries.

example = {"name": "John", "age": 30, "city": "New York"}
print(example) # it will print dictionary => {'name': 'John', 'age': 30, 'city': 'New York'}
print(type(example))
print(example["name"])# it will print value of name => John
print(example["age"])# it will print value of age => 30


 
 