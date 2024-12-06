#*Get Keys and Values:** Given a dictionary, write a Python function to return a list of keys and a list of values.
dict = {"name":"John","age":30,"city":"New York"}
def get_keys_values(dict):
    kyes=list(dict.keys())
    values=list(dict.values())
    return kyes,values# in python we can return multiple values from a function its called tupple
kyes,values=get_keys_values(dict)
print(kyes,type(kyes))
print(values,type(values))

key_value=get_keys_values(dict)
print(key_value,type(key_value))
print(key_value[0],key_value[1])


#2nd Way
print(dict.keys())
print(dict.values())