    #WAP to check how may student having A grade in class in following tuple

grade = ("A", "C", "D", "B", "E","A",2)
count = 0
# Way 1
count=grade.count("A")
print(count)#



# Way 2
for i in grade:
    if i == "A":
        count += 1
print(count)

# 
# list1=list(grade)#convert tuple to list
# print(list1)
list = [1,3,1,2,5]
list.sort()
print(list)
list = [1,3,1,2,5]
list.sort()

print(list)

