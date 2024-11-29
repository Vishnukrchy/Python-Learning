# WAP To  build list  input and check whether it is palandrome or not

list=[1,2,3,2,1]
# Way 1
copylist=list.copy()
if list==copylist:
    print("list is palandrome")
else:
    print("list is not palandrome")
# Way 2
if list==list[::-1]:
    print("list is palandrome")
else:
    print("list is not palandrome")

# Way3

while list:
    if list.pop(0)==list[-1]:
        print("list is palandrome")
    else:
        print("list is not palandrome")
        break
    
