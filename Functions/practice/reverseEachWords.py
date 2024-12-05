# Input = Mohan and sohan
# Output = nahoM dna noahs

str =input("Enter the string : ")
list = str.split(" ")
str1=""
for i in list:
    str1=i[::-1]+" "+str1
print("Output => "+str1)
