# newton rapsion method
import math

x = 0
for iteration in range(1, 101):
    print(iteration, x)
    f1 = 2 * x**2 - 5 * x + 3
    f2 = 4 * x - 5
    xnew = x - ((2 * x**2 - 5 * x + 3) / (4 * x - 5))
    if x == xnew:
        break
    x = xnew
    print(iteration, xnew)
