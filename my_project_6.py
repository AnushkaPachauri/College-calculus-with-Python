#derivatives 
import sympy
from sympy import symbols
x,y = symbols('x,y')

eq = x**3
derivative = sympy.diff(eq,x)

print ("derivative = ",derivative)

x_value = 2
slope = derivative.subs(x,x_value)
print("slope at x = ",x_value,"is", slope)
