# input ="mohan and sohan is here"
# output="sohan and mohan is here"

input=input("enter the string : ")
def reverseWords(input):
    list = input.split(" ")
    str=""
    for i in list:
        str=i+" "+str
    print("Output => "+str)
reverseWords(input)  







# def reverseWords(input):
#     return " ".join(reversed(input.split()))

# def reverseWords(input):
#     return " ".join(reversed(input.split()))