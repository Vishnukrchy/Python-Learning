# Find Grade Of Student
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Yor grade is A")
elif marks <90 and marks >=80:
    print("Yor grade is B")
elif(marks<80 and marks>70):
    print("Yor grade is C")
elif marks <70 and marks >=60:
    print("Yor grade is D")
elif marks <60 and  marks >=30: 
    print("Yor grade is E")
else:
    print("Yor grade is F")

# WAP to take input marks of 5 subject and print grade and percentage
# find percentage of 5 subject  
marks1 = int(input("Enter your marks: "))
marks2 = int(input("Enter your marks: "))   
marks3 = int(input("Enter your marks: "))   
marks4 = int(input("Enter your marks: "))       
markss5 =int(input("Enter your marks: "))    

total = marks1+marks2+marks3+marks4+markss5
print("Total marks are: ",total)
percentage = (total/500)*100    # total *0.5
print("Percentage is: ",percentage)
