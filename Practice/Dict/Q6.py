#**Check if a Key Exists in a Dictionary:** Write a Python function to check if a specific key exists in a dictionary.

dict = {"name": "John", "age": 30, "city": "New York"}
print("name" in dict)

def check_key(dict,key):
    if key in dict:
        return True
    else:
        return False
print(check_key(dict,"name"))        
