#simple iteration method
import math
x=0
for iteration in range(1,101):
    print(iteration,x)
    xnew= (2*x**2+3)/5
    if abs(xnew-x)<0.00001:
        break
    x=xnew
    print(iteration,xnew)
