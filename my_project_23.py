# volume revolved around y 
import numpy as np
import matplotlib.pyplot as plt 
import mpl_toolkits.mplot3d.axes3d as axes3d
# y range 
lower = 0
upper = 3
# graph set up 
fig = plt.figure()
ax = fig.add_subplot(1,1,1,projection = '3d')
points = 10*(upper-lower)
u = np.linspace(lower,upper,points)
v = np.linspace(0,2*np.pi,60)
U,V = np.meshgrid(u,v)
Z = U
# define function with capital U
fun = U**2 + 1
X1 = (fun)*np.cos(V)
Y1 = (fun)*np.sin(V)
# 2nd function 
fun2 = 1
X2 = (fun2)*np.cos(V)
Y2 = (fun2)*np.sin(V)

import sympy 
from sympy import symbols
x,y = symbols('x,y')
# same bound for both function 
lower = 0
upper = 3
# outer volume 
outer_radius = y**2+2
outer_area = sympy.pi*outer_radius**2
outer_vol = sympy.integrate(outer_area,(y,lower,upper))
#inner volume
inner_radius = 1
inner_area = sympy.pi*inner_radius**2
inner_vol = sympy.integrate(inner_area,(y,lower,upper))

vol = outer_vol - inner_vol
print(vol)

ar = sympy.N(vol)
print(ar) 
#graph
ax.plot_surface(X1,Y1,Z,alpha=0.3,color='red')
ax.plot_surface(X2,Y2,Z,alpha=0.3,color='blue')
plt.show()