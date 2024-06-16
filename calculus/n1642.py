from sympy import *
from sympy.simplify.radsimp import *

x = Symbol("x")
exp = 1 / sqrt(1 - x**2) + 1 / sqrt(1 + x**2)
print(integrate(exp))
