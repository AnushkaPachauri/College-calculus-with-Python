import matplotlib.pyplot as plt
import numpy as np
# value = 1
# y_value = x_value**2 #for eq y**2
x_value = 1
y_value = x_value**2

# change h to get better answer 
#h = 1
# a better version
for a in range (1,11):
 h=10**(-a)
y_value_2 = (x_value + h)**2
slope = (y_value_2-y_value)/h
print("slope = ", slope)

zoom =10
xmin = x_value - zoom
xmax = x_value + zoom
ymin = y_value - zoom
ymax = y_value +zoom
x = np.linspace(xmin,xmax,100)
y = x**2
plt.axis([xmin,xmax,ymin,ymax])# window size 
plt.plot(x,y)
plt.plot([x_value],[y_value],'ro')
plt.plot ([x_value+h],[y_value_2],'ro')
plt.axhline(y=0,color = 'k')
plt.axvline(x=0,color = 'k')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Graph of y = x^2")
plt.show()