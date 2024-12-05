# WAP To pyhow many times each element is present in a list

list = [1,3,2,4,5,2,3]
dict = {}
for i in list:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
print(dict)

#WAP To pyhow many times each element is present in a list
n=len(list)
for i in range(0,n):
    count =1
    for j in range(i+1,n):
        if list[i] == list[j]:
            count+=1
            list[j] = -1
    if list[i] != -1:
        print(list[i],count)    
           
    