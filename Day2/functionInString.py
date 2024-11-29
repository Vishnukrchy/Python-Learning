#importants Functions in string
# 1)len() function = providise the length of string
# 2)upper() function = convert the string into upper case
# 3)lower() function = convert the string into lower case
# 4)title() function = convert the first letter of each word into upper case
#   capitalize() function = convert the first letter of the string into upper case
# 5)count() function = count the number of occurence of a character in a string 
# 6)find() function = find the index of a character in a string
# 7)index() function = find the index of a character in a string
# 8)replace() function = replace the character in a string
# 9)split() function = split the string into a list
# 10)join() function = join the list into a string  

#     


#len() function = providise the length of string
name="ram";
print(len(name));#3

#upper() function = convert the string into upper case
name="ram";
print(name.upper());#RAM
print(name);#ram
name=name.upper();
print(name);#RAM

#lower() function = convert the string into lower case
name="RAM";
print(name.lower());#ram

#title() function = convert the first letter of each word into upper case   
name="mohan kumar";
print(name.title());#Mohan Kumar    

#capitalize() function = convert the first letter of the string into upper case 
name="mohan kumar";
print(name.capitalize());#Mohan kumar
print(name);#mohan kumar

#count() function = count the number of occurence of a character in a string
name="mohan kumar"; 
print(name.count("a"));#2
print(name.count("k"));#1

#find() function = find the index of a character in a string returns -1 if not found
name="mohan kumar"; 
print("index of "+name[3]+" is ",name.find("a"))#3
print(name.find("k"))#6
print(name.find("z"))#-1

#index() function = find the index of a character in a string returns error if not found
name="mohan kumar";
print("index of "+name[3]+" is ",name.index("a"))#3
print(name.index("k"))#6

#replace() function = replace the character in a string 
name="mohan kumar";
age="23";
print(name.replace("mohan","sohan"));#sohan kumar
age=age.replace("23","24");
print("{} is my age {}".format(name,age));#sohan is my age 24

#split() function = split the string into a list  
name="mohan kumar";
print(name.split(" "));#['mohan', 'kumar']
arr = name.split("a");
print(arr);#['moh', 'n kum', 'r']
print(type(arr));#<class 'list'>
print(type(name));#<class 'str'>
name=name.split(" ");
print(name);#['mohan', 'kumar']
print(type(name));#<class 'list'>

#join() function = join the list into a string  
name="mohan kumar";
print(" ".join(name));#m o h a n   k u m a r    
print("-".join(name));#m-o-h-a-n---k-u-m-a-r    



