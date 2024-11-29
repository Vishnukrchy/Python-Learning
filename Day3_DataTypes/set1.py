#Opreation on set
set1={1,2,3,4,5}
# accessing set
print(set1) # it will print set => {1, 2, 3, 4, 5}

# adding element in set we can add this by using add method add(element)
set1.add(6)
set1.add(2)
set1.add
print(set1) # it will print set => {1, 2, 3, 4, 5, 6}

# remove(element) removing element in set we can remove this by using remove method we can  remove this by using remove method
set1.remove(2)
set1.remove(6)
print(set1) # it will print set => {1, 3, 4, 5}

# discard(element) removing element in set we can remove this by using discard method we can  remove this by using discard method
set1.discard(3)
print(set1) # it will print set => {1, 4, 5}

#Upadte(element) updating element in set we can update this by using update method we can  update this by using update method
companies ={"apple","google","microsoft"}
tech_companies = {"a","gle","rosoft"}
companies.update(tech_companies)
print(companies) # it will print set => {'a', 'apple', 'gle', 'google', 'microsoft', 'rosoft'}
tech_companies.update(companies)
print(tech_companies) # it will print set => {'a', 'apple', 'gle', 'google', 'microsoft', 'rosoft'}

companies = {'Lacoste', 'Ralph Lauren'}
tech_companies = ['apple', 'google', 'apple']
# using update() method
companies.update(tech_companies)
print(companies)
# Output: {'google', 'apple', 'Lacoste', 'Ralph Lauren'}


#Iterate Over a Set in Python
fruits = {'apple', 'banana', 'cherry'}
for i in fruits:
    print(i)

