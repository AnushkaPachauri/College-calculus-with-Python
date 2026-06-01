#related rates
# 1. ladder
import sympy
from sympy import Derivative, symbols

x,y,t = symbols('x,y,t')

expr = x**2 + y**2
print(expr)
dx = expr.diff(x)
dy = expr.diff(y)
dxdt = Derivative(x,t)
dydt = Derivative(y,t)
der = dx*dxdt + dy*dydt
print(der)
der.subs(dxdt,3)

plugin = der.subs([(dx,6),(dy,8),(dxdt,2)])
print(plugin)

eq = sympy.Eq(plugin,0)
print(eq)
answer = sympy.solve(eq,dydt)[0]
print("answer = ",answer)