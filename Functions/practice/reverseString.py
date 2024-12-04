#reverse String 
str1=input("Enter the string : ")
print("reverse string is ",str1[::-1])


def reverse(str1):
    reversedStr=""
    for i in str1:
        reversedStr=i+reversedStr
    return reversedStr

print("reverse string is ",reverse(str1))
