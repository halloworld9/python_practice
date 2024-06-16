from sympy import Matrix, Identity, eye

x = Matrix([
    [2, 1, 0],
    [0, 2, 0],
    [1, 1, 1]
])

print(x**3 - 2 * x**2 + eye(3))
