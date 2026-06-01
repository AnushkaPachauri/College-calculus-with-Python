#Rolle's Theorem 
import sympy 
from sympy import symbols,Eq
x,y = symbols('x,y')
eq = x**2

x1 = 4
y1 = eq.subs(x,x1)
x2 = -4
y2 = eq.subs(x,x2)

#for rolle's theorem

print("y1 = ",y1)
print("y2 = ",y2)

slope = (y2-y1)/x2-x1
der = sympy.diff(eq)
#comparing slopes
test = sympy.solve(Eq(der,slope))
test_slope = der.subs(x,test[0])
print("at x = ",test[0])
print(slope,"=",test_slope)