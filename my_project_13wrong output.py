# parametric equation 
import sympy 
from sympy import symbols
x,y,t = symbols('x,y,t')

y = sympy.sin(t)
x = sympy.cos(t)

import math
import matplotlib.pyplot as plt

x_val = []
y_val = []

for i in range (36):
    a = math.pi*i/12
    xt = x.subs(t,a)
    yt = y.subs(t,a)
    x_val.append(xt)
    y_val.append(yt)

# this plot works better for arrays 
#plt.plot(x_val, y_val)
#plt.show()

# sympy graph

from sympy.plotting import plot_parametric
sympy.plot_parametric(x,y) # check the problem

dydt = sympy.diff(y,t)
print(dydt)

dxdt = sympy.diff(x,t)
print(dxdt)

dydx = dydt/dxdt
print(dydx)

import math 
# math.pi and sympy.pi are used for different answers

slope = dydx.subs(t,math.pi/12)
print("slope = ", slope)
slope = dydx.subs(t,sympy.pi/12)
print(slope)