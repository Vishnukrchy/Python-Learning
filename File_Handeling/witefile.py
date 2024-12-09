# how to read and wite file
# 1)open() -: It is a function that opens a file. and returns a file object. and need to specify the mode of the file.

# 2)write() -: It is a function that writes data to a file. and overwrites the contents of the file.

file=open("/sample.txt","w") # hwe to open file in write mode we can only write in file
file.write("i am vishnu\n")
file.read()#error permission denied
file.close()

# file=open("/sample.txt","r+") # here w+ means we can read and write in file
# file.write("i am vishnu i am writing in file\n")
# print(file.read())# read wole file at time and pointer at the end of the file
# file.close()



