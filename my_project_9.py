#Financial Applications 
# For max revenue 
x_price1 = 6
y_demand1 = 480
x_price2 = 7
y_demand2 = 476

#slope and Linear Equation 

slope = (y_demand2 - y_demand1)/(x_price2 - x_price1)
y_intercept = y_demand1 - slope*x_price1
print ("y = ", slope, "x + ", y_intercept )

import sympy 
from sympy import symbols

x,y = symbols ('x,y')

demand = slope*x + y_intercept 

revenue = x*demand 

# maximize a revenue 

max_revenue = sympy.diff (revenue, x)
max_x = sympy.solve(max_revenue, x)[0]
max_y = revenue.subs(x, max_x)

print("max revenue is", max_y)
print("when price is", max_x)

#checking 

print("rev 1= ", x_price1*y_demand1)
print("rev 2 = ", x_price2*y_demand2)
print("rev 3 = ", max_x*demand.subs(x,max_x))
print(demand.subs(x,max_x))
zero = sympy.solve(demand)
print(zero)