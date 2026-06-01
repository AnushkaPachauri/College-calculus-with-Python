x = -2
h = 0.0001

# for y = (3*x**2)/(x**2 - 4)

y_right = (3*(x+h)**2)/((x+h)**2 - 4)
y_left = (3*(x-h)**2)/((x-h)**2 - 4)

print("y_right = ", y_right)
print("y_left = ", y_left)

if round(y_right) != round(y_left):
    print("Limit does not exist at x = ", x)