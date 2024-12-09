# write into file 
# in w+ mode  => read and truncate file
file = open("File_Handeling/write.txt","w")# w means write only if file not exist then create file and truncate
file.write("i am vishnu\n")
file.write("i am writing in file\n")
#file.read()# error not readeble
file.close
# write into file and read
file = open("File_Handeling/write.txt","w+")# w means write only if file not exist then create file truncate
print(file.read())# read wole data beacuse itsa in w+ mode 
file.write("i am vishnu\n")
print("after write",file.read())# empty line because pointer at the end of the file
file.write("i am writing in file") 
print(file.read())# readble but print empty line because pointer at the end of the file 
file.close


# r+ mode => read and write no trucnacte data
with open("File_Handeling/write.txt","r+") as f: 
    print(f.read())
    f.write("i a software developer\n")
    f.write("i live in Noida")
    # print('after write',f.read())
  

