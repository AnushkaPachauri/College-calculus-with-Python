import sympy 
from sympy import symbols
from sympy.plotting import plot

x = symbols ('x')

eq = sympy.exp(x)

derivative = sympy.diff(eq,x)

print(derivative)

sympy.plot(eq)

"""import sympy
from sympy import symbols

x,y = symbols('x y')

eq = x**2*sympy.exp(2*x)
#eq = (x**3)*(x**2 +2*x)
derivative = sympy.diff(eq,x)
print (derivative)"""