# area between curves
import sympy 
from sympy import symbols, Eq

x,y,c = symbols('x,y,c')

eq_1 = x**2
eq_2 = x

x_points = sympy.solve(Eq(eq_1,eq_2)) # to get all the solutions of x's we have to use Eq from sympy 
print(x_points)

lower = x_points[0]
upper = x_points[1]
top = sympy.integrate(eq_1,(x,lower,upper))
bottom = sympy.integrate(eq_2,(x,lower,upper))
area = abs(top-bottom)
print ("area =",area)
sympy.plot (eq_1,eq_2,(x,-0.5,1.5))