#Method of sets
# add(element)	Adds an element to the set
# remove(element)	Removes an element from the set if element is not found then it will throw error
# discard(element)	Removes an element from the set if it is a member
# clear()	Removes all elements from the set
# pop()	Removes an element from the set and returns it
# update(set)	Updates the set with another set, or any other iterable
# intersection(set)	Returns the intersection of two sets as a new set
# difference(set)	Returns the difference of two sets as a new set
# symmetric_difference(set)	Returns the symmetric difference of two sets as a new set
# union(set)	Returns the union of two sets as a new set
# issubset(set)	Returns whether another set contains this set
# issuperset(set)	Returns whether this set contains another set


set1={1,2,3,4,5}
print(set1) # it will print set => {1, 2, 3, 4, 5}

# add(element)	Adds an element to the set
set1.add(6)
print(set1) # it will print set => {1, 2, 3, 4, 5, 6}
# remove(element)	Removes an element from the set if element is not found then it will throw error
set1.remove(6)
print(set1) # it will print set => {1, 2, 3, 4, 5}
#print(set1.remove(6)) # error => set.remove(x): x not in set

#discard(element)	Removes an element from the set if it is a member
set1.discard(5)
print(set1) # it will print set => {1, 2, 3, 4}

# pop()	Removes an element from the set and returns it
set1.pop()#pop() will remove random element
print(set1) # it will print set => set()

# update(set)	Updates the set with another set, or any other iterable
set2={3,6,9,12}
set1.update(set2)
print(set1) # it will print set => {1, 2, 3, 4, 6, 9, 12}

# intersection(set)	Returns the intersection of two sets as a new set
set1={1,2,3,4,5}
set2={3,6,9,12}
set3=set1.intersection(set2)
print(set3) # it will print set => {3}

# difference(set)	Returns the difference of two sets as a new set
set1={1,2,3,4,5}
set2={3,6,9,12}
set3=set1.difference(set2)
print(set3) # it will print set => {1, 2, 4, 5} 

# symmetric_difference(set)	Returns the symmetric difference of two sets as a new set
set1={1,2,3,4,5}
set2={3,6,9,12}
set3=set1.symmetric_difference(set2)
print(set3) # it will print set => {1, 2, 4, 5, 6, 9, 12}   

# union(set)	Returns the union of two sets as a new set
set1={1,2,3,4,5}
set2={3,6,9,12}
set3=set1.union(set2)
print(set3) # it will print set => {1, 2, 3, 4, 5, 6, 9, 12}    

# issubset(set)	Returns whether another set contains this set
set1={1,2,3,4,5}
set2={3,6,9,12}
print(set1.issubset(set2)) # it will print set => False

# issuperset(set)	Returns whether this set contains another set
set1={1,2,3,4,5}
set2={3,6,9,12}
print(set1.issuperset(set2)) # it will print set => False


