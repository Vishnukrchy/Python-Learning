# append  into file
# 1)open() -: It is a function that opens a file. and returns a file object. and need to specify the mode of the file.  
#

# file = open("File_Handeling/ap.txt","a")# a means append only if file not exist then create file
# #print(file.read()) #not readble because itsa in a mode
# file.write("i am writing in file\n")
# file.seek(0)
# file.close
# file = open("File_Handeling/ap.txt","a+")
# print(file.read())# empty in a+ also its pointer are in end

file = open("File_Handeling/ap.txt","a+")# a means append only if file not exist then create file
file.write("i am writing in file\n")
file.seek(0)
print(file.read())
file.close


