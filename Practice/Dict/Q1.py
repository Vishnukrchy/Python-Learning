#*Accessing Dictionary Values:** Write a Python function to get the value of a given key in a dictionary.

dict = {"name":"John","age":30,"city":"New York"}

def get_value(key):
    return dict[key]

print(get_value("name"))
print(get_value("age"))
print(get_value("city"))