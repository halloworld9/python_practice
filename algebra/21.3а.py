from sympy import I, sqrt, Symbol, solve, Abs, symbols

a, b = symbols('a b', complex=True)
f = sqrt(a ** 2 + b ** 2) + a + b * I - 8 - 4 * I
print(f.simplify())
f1 = I * b - 4 * I
b = solve(f1)[0]
f2 = a + sqrt(a**2 + b**2) - 8
a = solve(f2)[0]
print(a + I * b)

