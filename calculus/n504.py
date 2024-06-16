from sympy import limit, Symbol, sqrt, sin, cos, sympify

x = Symbol("x")
expr = (1 - cos(x) * sqrt(cos(2 * x)) * (cos(3 * x)) ** (1 / 3)) / x ** 2
print(limit(expr, x, 0))
