#area above and below the axis
import sympy 
from sympy import symbols

x,y,c = symbols('x,y,c')

#graph
eq=sympy.sin(x)


zeros = sympy.solve(eq,x)
print(zeros)

import math
lower=0
upper=2*sympy.pi
one = abs(sympy.integrate(eq, (x,lower,zeros[0])))
two = abs(sympy.integrate(eq, (x,zeros[0],zeros[1])))
three = abs(sympy.integrate(eq, (x,zeros[1],upper)))
print("area = ",one+two+three)
print("one =",one)
print("two =",two)
print("three =",three)

sympy.plot(eq)