# area under the curve 
#eq y = x**2 from x=0 to x=3
dx = 0.1
start_x = 0
end_x = 3
rectangles = int((end_x-start_x)/dx)

sum = 0
for a in range(0,rectangles):
    x = start_x + dx +a
    y = x**2
    area = y*dx
    sum = sum + area

print(sum)