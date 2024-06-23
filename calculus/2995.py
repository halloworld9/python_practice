from sympy import *

n = Symbol('n')
x = Symbol('x')
expr = n**2 / factorial(n)
print(summation(expr, (n, 1, oo)))
