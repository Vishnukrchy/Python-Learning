#Input => Good Is Morning
#Output => Morning Is Good

str1=input("Enter the string : ")
print("input => "+str1)
def reverseWords(input):
    list=input.split(" ")
    revesedStr=""
    for i in range(len(list)):
        revesedStr=list[i]+" "+revesedStr
    return revesedStr

print("Output => "+reverseWords(str1))