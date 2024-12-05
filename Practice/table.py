#Genrate Table of any no
num = int(input("Enter a number: "))

def genratetable(num):
    for i in  range(1,11):
        print(num,"*",i,"=",num*i)

genratetable(num)


#by while loop
num = int(input("Enter a number: "))

i=1
while i<=10:
    print(num,"*",i,"=",num*i)
    i=i+1