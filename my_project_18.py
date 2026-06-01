#fundamental theorem of calculus 
import sympy 
from sympy import symbols

x,y,c = symbols('x,y,c')

eq= x**2
eq
integral = sympy.integrate(eq) + c
print (integral)

integral_x = integral.subs(c,100)# any c value will do 
derivative = sympy.diff(integral_x)
print(derivative)

integral2 = sympy.integrate(derivative)+c
print(integral2)