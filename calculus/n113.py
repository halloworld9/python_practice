from sympy import Symbol, sin, pi, limit_seq

n = Symbol("n")
expr = n / (n + 1) * (sin(pi / 4 * n)) ** 2
bounds = limit_seq(expr, n)
print(f"maximum {bounds.max}\nminimum {bounds.min}")
