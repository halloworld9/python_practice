from sympy import Symbol, integrate

x = Symbol("x")
expr = (x ** 2 + 3) / (x ** 2 - 1)
print(integrate(expr))
