x=0
for iteration in range(1,101):
    print(iteration,x)
    xnew=x-(2*x**2+3)/(4*x-1)
    if abs(x-xnew)<0.000001:
        break
    x=xnew
    print("Root= 0.5%f",xnew)
    print("iteration= %d",iteration)