def f(x):
    return x**3 - 5 * x + 1


def bisection(a, b, n):
    i = 1
    condition = True
    while condition:
        x = (a + b) / 2
        if f(x) < 0:
            a = x
        else:
            b = x
        print("iteration", i, "x=", x, "f(x)=", f(x))
        if i == n:
            condition = False
        else:
            i = i + 1
        print("The root is =", x)


a = input("Enter the first value=")
b = input("Enter the second value=")
n = input("How many iteration do you want=")
a=float(a)
b=float(b)
n=float(n)
if f(a) * f(b) > 0:
    print("Give another value=")
    print("Try again thanks")
else:
    bisection(a, b, n)
