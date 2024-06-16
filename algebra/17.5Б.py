from sympy import Matrix, eye

x = Matrix([
    [2, 1, 1],
    [1, 2, 1],
    [1, 1, 2]
])

print(x**3 - 3 * x + 2*eye(3))
