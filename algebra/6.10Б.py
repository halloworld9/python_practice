from sympy.matrices import Matrix, eye, zeros, ones, diag, GramSchmidt

m = Matrix([[4, -1, 3, -2], [8, -2, 6, -4], [3, -1, 4, -2], [6, -2, 8, -4]])
print(*m.T.columnspace())