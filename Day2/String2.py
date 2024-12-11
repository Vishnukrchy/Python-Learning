#Basic opareations in string
#length of string
# name="ram"
# print(len(name));

str1='mohan';
str2='kumar';
str3=str1+str2;
print(str3+" is a good boy"+" ", len(str3));  

#Indexing in string
name="ram Kuma";
print(name[0]); #0 is index
print(name[1]); #1 is index
print(name[2]); #2 is index
print(name[3]); #3 is index
print(name[4]); #4 is index

#in python we can not reassign the value of string with the help of index that is possible in java
# name[0] = "R";

# in pytgon we can use negative indexing
print(name[-1]); #1 is index => 
print(name[-2]); #2 is index
print(name[-3]); #3 is index
print(name[-4]); #4 is index


# slicing in string
#=> we can slice the string in python with the help of index in this  satrting index is inclusive and ending index is exclusive
name="Mohan Kumar";
print(len(name));
print(name[0:4]);#0,1,2,3 => 0 is inclusive and 4 is exclusive ==> Moha
print(name[0:9]);#0,1,2,3,4,5,6,7,8 => 0 is inclusive and 9 is exclusive ==> Mohan Kum
print(name[0:11]);#0,1,2,3,4,5,6,7,8,9,10,11,12 => 0 is inclusive and 13 is exclusive ==> Mohan Kumar

print(name[1:5]);#1,2,3,4 => 1 is inclusive and 5 is exclusive ==>ohan
print(name[1:9]);#1,2,3,4,5,6,7,8 => 1 is inclusive and 9 is exclusive ==>ohan Kum
print(name[1:11]);#1,2,3,4,5,6,7,8,9,10,11,12 => 1 is inclusive and 13 is exclusive ==>ohan Kumar
# if ending indix is not given then it will take the length of string==================================================
print(name[0:]);#0,1,2,3,4,5,6,7,8,9,10,11,12 => 0 is inclusive and 13 is exclusive ==> Mohan Kumar  
print(name[1:]);#1,2,3,4,5,6,7,8,9,10,11,12 => 1 is inclusive and 13 is exclusive ==>ohan Kumar
# if starting index is not given then it will take 0 index==============================================================
print(name[:4]);#0,1,2,3 => 0 is inclusive and 4 is exclusive ==> Moha
print(name[:9]);#0,1,2,3,4,5,6,7,8 => 0 is inclusive and 9 is exclusive ==> Mohan Kum
print(name[:11]);#0,1,2,3,4,5,6,7,8,9,10,11,12 => 0 is inclusive and 13 is exclusive ==> Mohan Kumar
# if ending index is not given then it will take the length of string==================================================
print(name[:]);#0,1,2,3,4,5,6,7,8,9,10,11,12 => 0 is inclusive and 13 is exclusive ==> Mohan Kumar

name1="sohan";
#slicing in reverse or negative indexing in this satrting index is inclusive and ending index is exclusive
print(name1[-1:-3]);#-1,-2,-3,-4 => -1 is inclusive and -5 is exclusive ==> 
print(name1[-3:-1]);#-1,-2,-3,-4 => -1 is inclusive and -5 is exclusive ==> oh
print(name1[-1:]);#-1,-2,-3,-4 => -1 is inclusive and -5 is exclusive ==> ohan

str1="Apple";
print(str1[0:4]);#0,1,2,3 => 0 is inclusive and 4 is exclusive ==> App  
print(str1[-3:-1]);#-1,-2,-3,-4 => -1 is inclusive and -5 is exclusive ==> pl
print(str1[-3:]);#-1,-2,-3,-4 => -1 is inclusive and -5 is exclusive ==> ple







