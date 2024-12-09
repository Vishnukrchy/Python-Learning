# File handeling in Python
# => A file is a container for data that is stored on the disk or in a database.
# pythone can be used to create, read, update, and delete files.

# type of file
# 1)Text File -: It is a file that contains text data. like  text file, csv file, json file, xml file, etc.
# 2)Binary File -: It is a file that contains binary data. like image file, audio file, video file, etc.


# diffrent operation on file
# 1)Read File -: It is a function that reads the contents of a file and returns it as a string.
# 2)Write File -: It is a function that writes data to a file. and overwrites the contents of the file.
# 3)Append File -: It is a function that appends data to the end of a file. and does not overwrite the contents of the file.
# 4)Delete File -: It is a function that deletes a file.
# 5)Rename File -: It is a function that renames a file.
# 6)Copy File -: It is a function that copies a file.
# 7)Move File -: It is a function that moves a file.

# charatwers and methods of file
# 1)read() -: It is a function that reads the contents of a file and returns it as a string.
# 2)write() -: It is a function that writes data to a file. and overwrites the contents of the file.
# 3)append() -: It is a function that appends data to the end of a file. and does not overwrite the contents of the file.
# 4)close() -: It is a function that closes a file.
# 5)seek() -: It is a function that moves the file pointer to a specific position in the file.
# 6)tell() -: It is a function that returns the current position of the file pointer.

# how to open a file
# 1)open() -: It is a function that opens a file. and returns a file object. and can be used to open a file in read mode, write mode, append mode, and binary mode. and need to specify the mode of the file. close() method can be used to close the file.
# 2)with open() -: It is a function that opens a file. and returns a file object. we can use it to open a file in read mode, write mode, append mode, and binary mode. and need to specify the mode of the file. not need to close the file.            


# open and read file
# we have to open a file before reading or writing to it.

# way 1
# f = open('file name', 'mode')
file = open("sample.txt","r")# r means read only
print(file.read())
file.close()

# way 2

with open("sample.txt","r") as file:
    print(file.read())
with open("Quetions.txt","r") as f:
    print(f.read())  
    