from sympy import limit, Symbol, sqrt, sin, cos

x = Symbol("x")
expr = x ** 2 / (sqrt(1 + x * sin(x)) - sqrt(cos(x)))
print(limit(expr, x, 0))
