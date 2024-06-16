from sympy import limit, Symbol, sqrt, sin, cos, sympify

x = Symbol("x")
expr = sqrt(1 - (cos(x**2))) / (1 - cos(x))
print(limit(expr, x, 0))
