#Reading csv files n python 

#Basic Usage of of csv.reader
import csv
with open('File_I\o\sample_people.csv', 'r') as file:
    reader =csv.reader(file)
    for row in reader:
        print(row)
# csv.reader() is used to read a CSV file into a list of lists. and its return am iterable object        
                