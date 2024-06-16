from sympy import Symbol, sin, pi, limit_seq

n = Symbol("n")
expr = (1 + 2 ** (n * (-1) ** n)) ** (1 / n)
bounds = limit_seq(expr, n)
print(f"maximum {bounds.max}\nminimum {bounds.min}")
