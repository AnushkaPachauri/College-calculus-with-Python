#tangent line 
import sympy 
from sympy import symbols 

x,y = symbols('x,y')

eq =  x**2

der = sympy.diff(eq)

x_val = 2
slope = der.subs(x,x_val)
y_val = eq.subs(x,x_val)

b_val = y_val - slope*x_val

print("tangent is : y = ",slope,"*x +",b_val)