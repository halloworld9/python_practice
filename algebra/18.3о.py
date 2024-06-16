from sympy import Matrix, MatrixSymbol

m1 = Matrix([
    [1, 1, 0],
    [2, 1, 2],
    [0, 1, 1]
])

m2 = Matrix([
    [5, -1, 2],
    [-6, 4, 6],
    [-2, 0, 7]
])

print(m1 ** (-1) * m2)
