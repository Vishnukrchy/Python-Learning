# assert statement
# assert statement is used to check if a condition is True or False. If the condition is False, then assert statement raises an AssertionError.

# expample 1

def average(marks):
    assert len(marks) != 0 
    return sum(marks) / len(marks)
# marks = []
# print(average(marks))# AssertionError: len(marks) != 0
marks = [10, 20, 30]
print(average(marks))

# assert with print statement
# expample 2 =>
def average(marks):
    assert len(marks) != 0, "List is empty"
    return sum(marks) / len(marks)
marks = []
print(average(marks))# AssertionError: List is empty