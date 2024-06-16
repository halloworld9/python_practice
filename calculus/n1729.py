from sympy import *
from sympy.simplify.radsimp import *

x = Symbol("x")
expr = 1 / (sqrt(x+1) + sqrt(x-1))
print(integrate(expr))
