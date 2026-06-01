#implicit differentiation
import sympy 
from sympy import symbols

x,y = symbols('x,y')

eq = x**2 + y**2 - 25
derivative = sympy.idiff(eq,y,x)
print (derivative)

from sympy.plotting import plot
sympy.plot_implicit(eq,ylim = (-5,5))
