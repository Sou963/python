def f(x):
    return x**2 + 3


def bisection(a, b, n):
    i = 1
    condition = True
    while condition:
        x = (a + b) / 2
        if f(x) < 0:
            a = x
        else:
            b = x
            print("Iteration", i, "X", x, "F(x)=", f(x))
        if i == n:
            condition = False
        else:
            i = i + 1
            print("The root is=", x)


a = float(input("Enter the first value="))
b = float(input("Enter the second value="))
n = float(input("How many iteration do you want="))
if f(a) * f(b) > 0:
    print("Give another value.!")
    print("Try again thanks")
else:
    bisection(a, b, n)
