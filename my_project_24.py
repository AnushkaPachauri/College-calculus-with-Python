# centre of mass 
import sympy 
from sympy import symbols,Eq

x,y,c = symbols('x y c')
# x value range 
lower = 0
upper = sympy.pi
# for area bw eq_1 and x axis 
eq_1 = sympy.sin(x)
mass = sympy.integrate(eq_1, (x, lower, upper))
eq_2 = (eq_1**2)/2
mx = sympy.integrate(eq_2, (x, lower, upper))
eq_3 = eq_1*x
my = sympy.integrate(eq_3, (x, lower, upper))
x_cm = mx/mass
y_cm = my/mass
print("Centre of mass (x_cm, y_cm):")
print((sympy.N(x_cm), sympy.N(y_cm)))
sympy.plot(eq_1, (x, lower, upper), title="y=sin(x)", ylabel="y", xlabel="x", legend=True,markers=[{'args':[x_cm,y_cm,]}])