class Student:
    college_name="Supaul Engineering College"
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks

    def printDetails(self):
        print("Name: ",self.name)
        print("Roll No: ",self.roll_no)
        print("College Name: ",self.college_name)
    def avg_marks(self):
        sum=0
        for  i in self.marks:
            sum+=i
        print("Acerage marks is ",sum/len(self.marks))
        return sum/len(self.marks)



s1=Student("Vishnu",101,[90,30,40])
s1.printDetails()
s1.avg_marks()
s2=Student("Vikash",102,[102,30,40,20])
s2.printDetails()
s2.avg_marks()

