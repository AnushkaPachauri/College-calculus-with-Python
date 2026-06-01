import matplotlib.pyplot as plt
import numpy as np

# for equation y=(3*x**2)/(x**2-4)
x_value=0
y_value = (3*x_value**2)/(x_value**2-4)

zoom = 20
xmin = x_value - zoom
xmax = x_value + zoom
ymin = y_value - zoom
ymax = y_value + zoom

x = np.linspace(xmin, xmax, 100)
y = (3*x**2)/(x**2-4)
# y=(3*x**2)/(x**2-4)

plt.axis([xmin, xmax, ymin, ymax]) #window size
plt.plot(x,y)
plt.plot([x_value], [y_value], 'ro')
#plt.plot([xmin, xmax], [3,3], 'r--')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Graph of y=(3*x**2)/(x**2-4)")
plt.show()