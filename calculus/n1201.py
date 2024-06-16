from sympy import Symbol, sin, cos, trigsimp, diff

x = Symbol("x")
expr = sin(x)**4 + cos(x)**4
n = int(input("input n\n"))
print(trigsimp(diff(expr, x, n), method="combined"))