# Count No Of Dogot  in  noumber 
num=int(input("Enter a number: "))
count =0 
num1 =num
while num>0:
     count+=1
     lastDigit = num % 10
     num = num//10 # Whwn you divide the number by 10 the last digit will be removed
  
     print("number  is ",num, "removed digit is ",lastDigit)

print("Total digit is ",count)

print("From for loop")

count1 =0
for i in range(len(str(num1))):
    count1+=1
    print(" count ",count1)
print("Total digit is ",count1)

