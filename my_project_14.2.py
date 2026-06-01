#related rates 
#ballon volume 
import sympy 
from sympy import symbols,Derivative

v,r,t = sympy.symbols('v,r,t')

expr = (4/3)*sympy.pi*r**3
print (expr)

dr = expr.diff(r)
drdt = Derivative (r,t)
der = dr*drdt
print(der)
dr_plugin = dr.subs(r,3)
plugin = dr_plugin*drdt
print(plugin)
dvdt = 9
eq = sympy.Eq(plugin,dvdt)
print(eq)
answer =sympy.solve(eq,dvdt)
print ("answer",answer)