# volume around x axis (3-D graph)
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as axes3d
# x range 
lower = 0
upper = 3

# set up the graph
fig = plt.figure()
ax = fig.add_subplot(1,1,1,projection = '3d') # necessary for 3d graph
points = 10*(upper-lower)
u = np.linspace(lower,upper,points)
v = np.linspace(0,2*np.pi,60)
U,V = np.meshgrid(u,v)
X = U
#defining function with capital U

fun = U**2
#this in 3-D is what plots it going around in a circle revolving around that axis
Y1 = (fun)*np.cos(V)
Z1 = (fun)*np.sin(V)

#ax.plot_surface(X,Y1,Z1,alpha = 0.4,color = 'blue')
#plt.show()

# for graphing a second function 
fun2 = 1
Y2 = (fun2)*np.cos(V)
Z2 = (fun2)*np.sin(V)

# calculating volume 
import sympy 
from sympy import symbols
x,y = symbols('x,y')
radius = x**2
area = sympy.pi*radius**2
lower = 0
upper = 2
vol = sympy.integrate(area,(x,lower,upper))
print (vol)

ax.plot_surface (X,Y1,Z1,alpha = 0.3,color = 'red')
ax.plot_surface (X,Y2,Z2,alpha = 0.2, color = 'blue')
plt.show()