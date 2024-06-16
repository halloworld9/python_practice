from sympy import *

x = Symbol("x")
exp = x ** 2 / (1 - x) ** 100
print(factor(integrate(exp)))
