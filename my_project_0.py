import sympy
from sympy import symbols
from sympy.solvers import solve

x = symbols('x')

# Put the equation here
eq = x**2 - 4

# solve() sets the equation equal to zero
print("x = ", solve(eq,x))