from sympy import *
n = Symbol('n')
x = Symbol('x')
print(summation((2*n+1) * x ** (2 * n) / factorial(n), (n, 0, oo)))