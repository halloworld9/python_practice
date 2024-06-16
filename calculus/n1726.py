from sympy import *

x = Symbol("x")
expr = (2 - x) ** 2 / (2 - x ** 2)
print(integrate(expr))
