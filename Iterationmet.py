x=0
for iteration in range(1,101):
    print(iteration,x)
    xnew=(2*x**2+3)/5
    if x==xnew:
        break
    x=xnew
    print(iteration,xnew)
