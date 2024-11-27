# WAP To calculate electricity bill and provides the total electricity bill to the user with discount
units = int(input("Enter the number of units consumed: "))
perUnit = int(input("Enter the rate per unit: "))
bill = 0
 
if units <= 100:
    bill = units * perUnit
    print("Not eligible for discount")
    print("The total electricity bill is:", bill)
elif units > 100 and units <= 200:  
    bill = 100 * perUnit + (units - 100) * perUnit * 0.3
    print("eligible for discount of 30%")
    print("The total electricity bill is:", bill)
elif units > 200:
    bill = 100 * perUnit + 100 * perUnit * 0.5 + (units - 200) * perUnit * 0.5
    print("eligible for discount of 50%")    
    print("The total electricity bill is:", bill)

