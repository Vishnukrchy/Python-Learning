# finaly block :
# => finally block is always executed irrespective of whether an exception is raised or not
# => finally block is used to clean up resources used by the program
# => finally block is used to perform cleanup operations that are required even if an exception is raised or not

try:
    numrator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    result = numrator // denominator
    print(result)
except Exception as e:
    print("You can't divide by zero")
finally:
    print("Program is finished")