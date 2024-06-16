from sympy import I, sqrt

a = (-1 + I * sqrt(3)) ** 15
b = (1 - I) ** 20
c = (-1 - I * sqrt(3))**15
d = (1 + I)**20
print((a/b + c/d).simplify())
