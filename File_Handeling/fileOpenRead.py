# Way to open and read a file
# 1)open() -: It is a function that opens a file. and returns a file object. and need to specify the mode of the file.
# 2 read() -: It is a function that reads the contents of a file and returns it as a string. and  pontinter at the end of the file.

file = open("File_Handeling\sample.txt","r")
print(file.read()) # read wole file at time and pointer at the end of the file

print(file.read()) # empty line because pointer at the end of the file in above line
file.close()
#print(file.read())# error because file is closed for this we have to open file again

# way 2
with open("File_Handeling\sample.txt","r") as file:
    print(file.read())
    print(file.read())# empty line because pointer at the end of the file in above line
# print(file.read())# error because file is closed for this we have to open file again

#read file line by line
with open("File_Handeling\sample.txt","r") as file:
    for line in file:
        print(line)
#readline() method => It is a function that reads a line from a file and returns it as a string.
print('=========== Readline Method ===========')
f=open("File_Handeling\sample.txt","r") 
print(f.readline())  # first line
print(f.readline())  # second line
print(f.readline())  # third line
print(f.readline())  # fourth line or if no more line then return empty string because pointer at the end of the file   
f.close()

# with 
with open("File_Handeling\sample.txt","r") as f:
    print(f.readline(),end="")
    print(f.readline(),end="")
    print(f.readline())


# method  charater and  means at time fie open
# 
open("File_Handeling\sample.txt","r")
# 'r' => open file in read mode default mode
# 'w' => open file  for writing ,the file will be created if it does not exist, or truncated if it does exist.
# 'a' => open file  for appending ,the file will be created if it does not exist.
# 'r+' => open file  for reading and writing.
# 'w+' => open file  for reading and writing, the file will be created if it does not exist, or truncated if it does exist.
# 'a+' => open file  for reading and writing, the file will be created if it does not exist.

#'x' => open file  for writing, creating the file if it does not exist.
#'b' => binary mode
#'t' => text mode
#'+' => open file  for reading and writing, the file will be created if it does not exist.

# seek() method => It is a function that moves the file pointer to a specific position in the file.
# tell() method => It is a function that returns the current position of the file pointer.





