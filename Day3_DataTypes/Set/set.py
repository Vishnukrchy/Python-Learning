#Sets in pythons
#Sets are collection of unique elements
#Sets are mutable, you can change the value of a set after it is created.
#Sets are a collection of items that can be used to store a group of values, such as numbers, strings, or other sets.
# notes set is mutable    insertion order is not preserved  and duplicate value is not allowed

# Create Set => we camn create a set using curly brackets {value, value, value}
# We can also create a set using a Python built-in function set(). 
# Not set is mutable but set should not be mutable 
#Note: We cannot create empty sets using { } syntax as it creates an empty dictionary. To create an empty set, we use set().
#A set can have any number of items and they may be of different types (integer, float, tuple, string, etc.). But a set cannot have mutable elements like lists, sets or dictionaries as its elements.
null_set = set()
print(null_set) # it will print set => set()
null_set.add(1)
null_set.add(2)
print(null_set) # it will print set => {1, 2}
# creating set integer type
std_id={1,2,3,4,5} # in this if we have duplicate value it will strore only one  times
print("Student ID : ",std_id) # it will print set => {1, 2, 3, 4, 5}
print(type(std_id))# it will print set type => <class 'set'>

# creating set string type  
vawels={'a','e','i','o','u'}
print("Vawels : ",vawels) # it will print set => {'a', 'e', 'i', 'o', 'u'}

# creating set mix type
mix_set={1,2,'hellow',True,(-1,2.4)}
print("Mix Set : ",mix_set) # it will print set => {1, 2, 'hellow', True, (-1, 2.4)}

# creating set using constructor
# set_constructor = set(['apple', 'banana', 'cherry'])
# print(set_constructor) # it will print set => {'apple', 'banana', 'cherry'}

# try to add duplicate value in set and list, tuple, dictioniary
set_id={1,2,3,4,5,2,3}
print(set_id) # it will print set => {1, 2, 3, 4, 5}

#mix_set={1,[12,12],2,'hellow',True,{"name":"vishnu","age":30}} # Error => TypeError: unhashable type: 'list'
# #A set can have any number of items and they may be of different types (integer, float, tuple, string, etc.). But a set cannot have mutable elements like lists, sets or dictionaries as its elements.



#Accessing Set Elements => 
std_id={1,2,3,4,5}
#std_id[0] # it will throw error => TypeError: 'set' object is not subscriptable
# we 

p




    