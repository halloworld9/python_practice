from sympy import *
from sympy.simplify.radsimp import *

x = Symbol("x")
expr = x ** 5 / (x + 1)
print(integrate(expr))
