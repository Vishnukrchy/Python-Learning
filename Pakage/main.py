# import my_pakage.sub_pakage.anotherSubPakage.advanced_math as am
# # to access the function
# # my_pakage.sub_pakage.anotherSubPakage.advanced_math.advanced_add(2,3)
# print(am.advanced_add(2,3))

# or 
# from my_pakage.sub_pakage.anotherSubPakage.advanced_math import advanced_add # its only import the function
# print(advanced_add(2,3))

# from my_pakage.sub_pakage.anotherSubPakage.advanced_math import * # its import all the functions
# print(advanced_add(2,3))


# import my_pakage.sub_pakage.math 
# print(my_pakage.sub_pakage.math.add(2,3))
# import my_pakage.sub_pakage.math as m
# print(m.add(2,3))
# print(m.mul(2,3))

# from my_pakage.sub_pakage.math import *
# print(add(2,3)) 
# print(mul(2,3))

from my_pakage.sub_pakage.math import add , sub
print(add(2,3)) 
print(sub(2,3))
# print(mul(2,3)) Error => NameError: name 'mul' is not defined




# import my_pakage.String_operation
# print(my_pakage.String_operation.reverse("hello"))

