from sympy import *

n = Symbol('n')
x = Symbol('x')
print(summation(n * (n + 2) * x ** n, (n, 1, oo)))

print("x*(3-x)/(1-x)**3")
