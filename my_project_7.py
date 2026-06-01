import sympy
from sympy import symbols

x,y = symbols('x,y')

eq = sympy.sin(sympy.cos(x))
derivative = sympy.diff(eq,x)
print("derivative chain rule: ",derivative)