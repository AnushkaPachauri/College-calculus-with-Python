# mean value theorem
import sympy 
from sympy import symbols,Eq

x,y = symbols('x,y')
eq = x**3 + 2*x**2 - 5*x + 3

x1 = 0
y1 = eq.subs(x,x1)
x2 = 5
y2 = eq.subs(x,x2)
slope = (y2-y1)/(x2-x1)
der = sympy.diff(eq)
#comparing slopes
test =sympy.solve(Eq(der,slope))
test_slopes = der.subs(x,test[0])
print("at x =",sympy.N(test[0]))
print(slope,"=",sympy.N(test_slopes))