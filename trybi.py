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
        print("Iteration=", i, "x=", x, "f(x=)", f(x))
        if i == n:
            condition = False
        else:
            i = i + 1
        print("The root is=", x)


a = float(input("Enter the first element="))
b = float(input("Enter the second element="))
n = float(input("How many iteration do you want="))
if f(a) * f(b) > 0:
    print("Try again with another value")
else:
    bisection(a, b, n)
