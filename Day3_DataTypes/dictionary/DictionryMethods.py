#Dictionary Method in Pythons
# keys() => returns a list of all the keys in the dictionary
# values() => returns a list of all the values in the dictionary
# items() => returns a list of all the key-value pairs in the dictionary
# get(key) => returns the value of a specific key in the dictionary    
# pop(key) => removes a specific key-value pair from the dictionary  and returns removed key  value
# update() => updates the dictionary with the key-value pairs from another dictionary
# popitem() => removes the last key-value pair from the dictionary and returns removed key  value
# clear() => removes all the key-value pairs from the dictionary

dict={
    91:"country code",
    "name":"vishnu",
    "age":23,
    "score":{
        "maths":90,
        "science":80
    },
    "skills":["java","python","react"]
}
#keys() =>  its retrun a list of all the keys in the dictionary
print(dict.keys())# it will print keys => dict_keys([91, 'name', 'age', 'score', 'skills'])
keys=list(dict.keys())# its retrun a list of all the keys in the dictionary and store in list
print(keys) # it will print keys => [91, 'name', 'age', 'score', 'skills']

#values() =>  its retrun a list of all the values in the dictionary
print(dict.values())# it will print values => dict_values(['country code', 'vishnu', 23, {'maths': 90, 'science': 80}, ['java', 'python', 'react']]
values=list(dict.values())# its retrun a list of all the values in the dictionary and store in list
print(values) # it will print values => ['country code', 'vishnu', 23, {'maths': 90, 'science': 80}, ['java', 'python', 'react']]

#items() =>  its retrun a list of all the key-value pairs in the dictionary
print(dict.items())# it will print items => dict_items([(91, 'country code'), ('name', 'vishnu'), ('age', 23), ('score', {'maths': 90, 'science': 80}), ('skills', ['java', 'python', 'react'])]
items=list(dict.items())# its retrun a list of all the key-value pairs in the dictionary and store in list
print(items) # it will print items => [(91, 'country code'), ('name', 'vishnu'), ('age', 23), ('score', {'maths': 90, 'science': 80}), ('skills', ['java', 'python', 'react'])]

# get(key) => returns the value of a specific key in the dictionary
print(dict.get("name"))# it will print value of name => vishnu
print(dict.get("score"))# it will print value of score => {'maths': 90, 'science': 80}

# pop(key) => removes a specific key-value pair from the dictionary and returns removed key the value
removed_key=dict.pop(91)
print(removed_key)# it will print removed_key => country code
print("removed_key value",dict.pop("score"))# it will print removed_key => {'maths': 90, 'science': 80}

print(dict)# it will print dictionary => {'name': 'vishnu', 'age': 23, 'skills': ['java', 'python', 'react']}

# upate() => updates the dictionary with the key-value pairs from another dictionary 
 
dict2={
    "city":"Noida",
    "state":"Uttar Pradesh",
    "native":{
         "state":"Bihar",
         "city":"madhubani"
    }
}

dict.update(dict2) # in dist 1 add dict 2  key-value pairs
print(dict)# it will print dictionary => {'name': 'vishnu', 'age': 23, 'skills': ['java', 'python', 'react'], 'city': 'Noida', 'state': 'Uttar Pradesh', 'native': {'state': 'Bihar', 'city': 'madhubani'}}

# popitem() => removes the last key-value pair from the dictionary and returns removed key  value
removed_item=dict.popitem() 
print(removed_item) # it will print removed_item => ('native', {'state': 'Bihar', 'city': 'madhubani'})
print(dict) # it will print dictionary => {'name': 'vishnu', 'age': 23, 'skills': ['java', 'python', 'react'], 'city': 'Noida', 'state': 'Uttar Pradesh'}

# clear() => removes all the key-value pairs from the dictionary
dict.clear()
print(dict) # it will print dictionary => {}




