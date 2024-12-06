#**Add or Update a Key in a Dictionary:** Write a Python function that adds a new key-value pair to a dictionary or updates the value if the key already exists.

dict={
    "name":"mohan",
    "age":23,
 
    "City":"Noida"
}
print("original dictionary",dict)
def add_or_update_key(dict,key,value):
     if key in dict:
        dict[key]=value
     else:
        dict[key]=value  
     return dict

add_or_update_key(dict,"state","Uttar Pradesh")
print(" NEW dISTIONARY",dict)    
#WANT  UPDATE NEW VALUE
add_or_update_key(dict,"state","Bihar")
add_or_update_key(dict,"City","Patna")

print(" NEW dISTIONARY",dict)

value={
    "10th":"PDKG College Andhrathardhi",
    "Intermidiate":"PDKG College Andhrathardhi",
    "Diploma":"PDKG College Andhrathardhi",
    "Btech":"PDKG College Andhrathardhi"
}
key="education"
add_or_update_key(dict,key,value)
print(" NEW dISTIONARY",dict)
