
#Way 1

import calculator #=>it will import all function
print((dir(calculator)))#=>['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'div', 'mul', 'power', 'square', 'sub']calculator)
print(calculator.add(2,3))#=>5
print(calculator.sub(2,3))#=>-1
print(calculator.mul(2,3))#=>6
print(calculator.div(2,3))#=>0.6666666666666666
print(calculator.power(2,3))#=>8
print(calculator.square(2))#=>4

#Way 2
from calculator import * #=>it will import all function
print(add(2,3))#=>5
print(sub(2,3))#=>-1
print(mul(2,3))#=>6
print(div(2,3))#=>0.6666666666666666
print(power(2,3))#=>8
print(square(2))#=>4

#Way 3
from calculator import add,sub,mul,div,power,square #=>it will import all function that are mentioned here only
print(add(2,3))#=>5
print(sub(2,3))#=>-1
print(mul(2,3))#=>6
print(div(2,3))#=>0.6666666666666666
print(power(2,3))#=>8
print(square(2))#=>4

#Way 4  
import calculator as cal
print(cal.add(2,3))#=>5
print(cal.sub(2,3))#=>-1
print(cal.mul(2,3))#=>6
print(cal.div(2,3))#=>0.6666666666666666
print(cal.power(2,3))#=>8
print(cal.square(2))#=>4
