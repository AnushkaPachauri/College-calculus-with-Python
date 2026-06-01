#projectile application 
import sympy
from sympy import symbols

t = symbols('t')
v = 16.5
h = 3.9
position = -4.9*t**2 + v*t + h
print("y = ",position)

vel = sympy.diff(position)
print("vel = ",vel)

x_max_h = sympy.solve(vel,t)[0]
max_h = position.subs(t,x_max_h)
print("max height at ", x_max_h,"sec = ",max_h)

acc = sympy.diff(vel)
print("acc = ", acc)