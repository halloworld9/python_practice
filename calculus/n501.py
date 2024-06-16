from sympy import limit, Symbol, sqrt, sin, cos

x = Symbol("x")
expr = (sqrt(cos(x)) - (cos(x))**(1/3))/(sin(x))**2
print(limit(expr, x, 0))
