from sympy import limit, Symbol, sqrt, sin, cos, sympify

x = Symbol("x")
expr = (1 - sqrt(cos(x))) / (1 - cos(sqrt(x)))
print(limit(expr, x, 0))
