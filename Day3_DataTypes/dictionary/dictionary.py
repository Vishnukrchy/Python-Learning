#Dictionary in python
#Dictionary is a collection of key-value pairs
#Dictionary is mutable, you can change the value of a dictionary after it is created.
#Dictionary is a collection of key-value pairs that can be accessed using indexing and slicing.
#Dictionary is a collection of key-value pairs that can be used to store a group of values, such as numbers, strings, or other dictionaries.

#Create Dictionary => {key: value, key: value, key: value}
#We can also create a dictionary using a Python built-in function dict().
contyCapital = {
    "India": "Delhi",#element 1
    "Pakistan": "Islamabad",   #element 2 
    "Nepal": "Kathmandu"#element 3
}   
#Dictionary keys must be immutable, such as tuples, strings, integers, etc. We cannot use mutable (changeable) objects such as lists as keys.
# Here India is key and Delhi is value in  dictionary Key will be unique and value can be duplicate
print(contyCapital) # it will print dictionary => {'India': 'Delhi', 'Pakistan': 'Islamabad', 'Nepal': 'Kathmandu'}
print(type(contyCapital)) # it will print dictionary type => <class 'dict'>

#Accessing Dictionary Elements => 
#To access the value of a specific key in a dictionary, you can use the key name as an index.   
capital=contyCapital["India"] # it will retrun value of India => Delhi

print(capital)#

#example 2 =>
info = {
    "id": 1,
    "name": "John",
    "age": 30,
}
print(info)# it will print dictionary => {'id': 1, 'name': 'John', 'age': 30}

#accessing the value of a specific key in a dictionary
print(info["name"])# it will print value of name => John
#updating the value of a specific key in a dictionary
info["name"]="vishnu";
print(info["name"])# it will print value of name => vishnu
#adding a new key-value pair to a dictionary
info["cuntry"]="India";
print(info)# it will print dictionary => {'id': 1, 'name': 'vishnu', 'age': 30, 'cuntry': 'India'}
#addeing new List to dictionary
info["skills"]=["java","python","react"];
print(info)# it will print dictionary => {'id': 1, 'name': 'vishnu', 'age': 30, 'cuntry': 'India', 'skills': ['java', 'python', 'react']}
info["skills"].append("docker");
print(info)# it will print dictionary => {'id': 1, 'name': 'vishnu', 'age': 30, 'cuntry': 'India', 'skills': ['java', 'python', 'react', 'docker']}

#adding tupple to dictionary
info["address"]=("Noida","Madhubani","Patna","Bihar","India");
print(info)# it will print dictionary => {'id': 1, 'name': 'vishnu', 'age': 30, 'cuntry': 'India', 'skills': ['java', 'python', 'react', 'docker'], 'address': (1, 2, 3, 4, 5)}
#*** delete the value of a specific key in a dictionary
del info["address"]
print(info)# it will print dictionary => {'id': 1, 'name': 'vishnu', 'age': 30, 'cuntry': 'India', 'skills': ['java', 'python', 'react', 'docker']}
#adding dictionary to dictionary
info["address"]={
    "city":"Noida",
    "state":"Uttar Pradesh",
    "country":"India",
    "native":{
        "state":"Bihar",
        "city":"madhubani"
    }

}
print(info)






