#Modues is a file that contains python code
#Modues can be imported into another python file
#  import module_name
 #> module_name.function_name


#  import module_name as mn
#  from module_name import function_name
#  from module_name import function_name as fn
#  from module_name import *


# expample 1 =>
import math
print(math.sqrt(9))

# expample 2 =>
from math import sqrt
print(sqrt(9))

# expample 3 =>
from math import sqrt as sq
print(sq(9))    

# expample 4 =>
from math import *
print(sqrt(9))
