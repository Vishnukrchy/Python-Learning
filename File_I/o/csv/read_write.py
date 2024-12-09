# Python CSV File I/O
# CSV (Comma Separated Values) is a file format used to store data in a tabular format. It is a text file that contains a series of values that are separated by commas or other delimiters.
# CSV is used to store data in a tabular format, such as a spreadsheet or database table. It is a text file that contains a series of values that are separated by commas or other delimiters.
# Python Provides a module called csv that can be used to read and write CSV files.\ 
# Import the csv module

# Read CSV File
import csv
# Open the CSV file 
# csv.reader => It is a function that reads a CSV file and returns a reader object.
with open('File_I\o\sample_people.csv', 'r') as file:
    reader = csv.reader(file)
    print("reader",reader)# <_csv.reader object at 0x000001B3B5B0C0D0>
    print(type(reader)) # <class '_csv.reader'>
    # print(list(reader)) # in list form
    for row in reader:
        print(row)
        # ['1', 'Alice', 'Engineer']
        # ['2', 'Bob', 'Doctor']
        # ['3', 'Charlie', 'Teacher']
        # ['4', 'Diana', 'Artist']
        # ['5', 'Ethan', 'Scientist']
        # ['6', 'Fiona', 'Musician']
        # ['7', 'George', 'Writer']
        # ['8', 'Hannah', 'Chef']
        # ['9', 'Ian', 'Architect']
        # ['10', 'Julia', 'Lawyer']
file=open("File_I\o\sample_people.csv","r")
reader=csv.reader(file)
# print(list(reader)) 
file.close()  

print('=========== Write CSV File ===========')
# Write CSV File
# csv.writer() => It is a function that writes data to a CSV file.
#  writerow() => It is a function that writes a single row of data to a CSV file.
#newline='' => It is a parameter that specifies the newline character to use in the CSV file.
file =open('File_I\o\write.csv','w+',newline='')
writer =csv.writer(file)
print("writer",writer) # <_csv.writer object at 0x000001B3B5B0C0D0>
print(type(writer)) # <class '_csv.writer'>

# writeing data in file
writer.writerow(['id','name','city'])
writer.writerow(['1','Vishnu','Noida']) 
writer.writerow(['2','ishnu','moida'])
writer.writerow(['3','shnu','lOIDAa'])

file.close()

# reading data from file

with open('File_I\o\write.csv','r') as file:
    reader=csv.reader(file)
    #print(list(reader))# in list form
    for row in reader:
        print(row)

print('=========== Redad CSV File and Write CSV File ===========')        
#  Redad CSV File and Write CSV File
with open('File_I\o\write.csv','r+',newline='') as file:
    reader=csv.reader(file)
    print(list(reader))
    writer=csv.writer(file)
    writer.writerow(['1','vishnu','Madhubani'])# write data in file new line added
#  Redad CSV File and Write CSV File
# In w+ mode  => read and truncate file     
with open('File_I\o\write.csv','w+',newline='') as file:    
    reader=csv.reader(file)
    print(list(reader))
    writer=csv.writer(file)
    writer.writerow(['1','vishnu','Madhubani'])
    writer.writerow(['2','ishnu','moida'])
    writer.writerow(['3','shnu','lOIDAa'])
    file.seek(0)
    print(file.read())

   
