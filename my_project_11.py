#derivative & differential

import sympy 
from sympy import symbols

x,y = symbols('x,y')

eq = x**2 #original function

der = sympy.diff(eq) #derivative
#point
x_val = 2 
dx = 0.00001
dy= eq.subs(x,x_val+dx) - eq.subs(x,x_val)
# der.subs to get slope 
slope = der.subs(x,x_val)

print("differnetial equation is written as: dy = ",der,"*dx")
print("slope = ",slope)
print("dy/dx = ", dy/dx)
print("dy = ", dy)
print("dy = ", slope*dx)