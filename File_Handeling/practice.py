c=open("File_Handeling\practice.txt","w")
c.close()

with open("File_Handeling\practice.txt","r+") as f:
   
     f.write("hello evryone\n") 
     f.write("i am vishnu\n")
     print(f.read())
     f.write("i am from madhubani\n")
     print(f.read())
     f.seek(0)#pointer at the start of the file
     print(f.read())

file =open("File_Handeling\practice.txt","r")
print(file.read())     
