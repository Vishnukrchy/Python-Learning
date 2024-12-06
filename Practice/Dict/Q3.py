#*Merge Two Dictionaries:** Write a Python function that merges two dictionaries into one.

dict1={"a":1,"b":2,"c":3}
dict2={"d":4,"e":5,"f":6}

def merge_dictionaries(dict1,dict2):
    dict1.update(dict2)
    return dict1
print(merge_dictionaries(dict1,dict2)) 

# or 2nd Way 
dict3={**dict1,**dict2}
print(dict3)

