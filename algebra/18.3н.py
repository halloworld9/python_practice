from sympy import Matrix, MatrixSymbol

m1 = Matrix([
    [1, 2, 3],
    [2, 3, 1],
    [3, 1, 2]
])

m2 = Matrix([
    [0, 0, 1],
    [1, 0, 0],
    [0, 1, 0]
])

print(m1 ** (-1) * m2)