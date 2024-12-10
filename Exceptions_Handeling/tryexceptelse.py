# try except else block
# try:
#     numrator = int(input("Enter the numerator: "))
#     denominator = int(input("Enter the denominator: "))
#     result = numrator // denominator
#     print(result)
# except Exception as e:

#     print("You can't divide by zero")
# else:
#     print("Program is finished")

# print("Program is finished")  
  
# program to print the reciprocal of even numbers
try:
    num=int(input("Enter a number: "))
    assert num%2==0
except Exception as e:
   print(' Not an even number !')
else:
    resciprocals=1/num
    print(resciprocals)   
      
