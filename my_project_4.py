import sympy 
from sympy import symbols

x = symbols('x')
eq = (3*x**2)/(x**2-4) # the equation to be solved and plotted 

#critical values calculated in my_project.py
x_1 = 2
x_2 = -2
#limit (expression, variable, value)
# 1st critical point
right = sympy.limit(eq,x,x_1,dir='+') # eq in variable x = x_1,find limits (RHL & LHL)
left = sympy.limit(eq,x,x_1,dir='-')
print("At x = ",x_1)
print("RHL = ",right)
print("LHL = ",left)
# 2nd critical point
right = sympy.limit(eq,x,x_2,dir='+') # eq in variable x = x_2,find limits (RHL & LHL)
left = sympy.limit(eq,x,x_2,dir='-')
print("At x = ",x_2)
print("RHL = ",right)
print("LHL = ",left)
# limits as x approaches INFINITY (+ve and -ve)
right = sympy.limit(eq,x,sympy.oo)
left = sympy.limit(eq,x,-sympy.oo)
print ("As x approaches +ve infinity = ",right)
print ("As x approaches -ve infinity = ",left)
#plot the eq
sympy.plot(eq,ylim=(-8,8))