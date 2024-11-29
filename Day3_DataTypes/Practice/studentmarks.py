# take user input for 3 subjects marks 
subject={} # satrt with empty dictionary
sub1=str(input("Enter subject 1 name:  "))
marks=int(input("Enter marks: "))
subject[sub1]=marks

sub2=str(input("Enter subject 2 name:  "))
marks=int(input("Enter marks: "))
subject[sub2]=marks

sub3=str(input("Enter subject 3 name:  "))
marks=int(input("Enter marks: "))
subject[sub3]=marks

print(subject)



for i in range(3):
    subject_name=input("Enter subject name: ")
    marks=int(input("Enter marks: "))
    subject[subject_name]=marks

print(subject)