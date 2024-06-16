from sympy import Symbol, Matrix, symbols, solve_undetermined_coeffs, solve_linear_system

k = Symbol("k")
x1, x2, x3, x4 = symbols('x1 x2 x3 x4')
a1 = [2, 3, 1, 2, 3]
a2 = [4, 6, 3, 4, 5]
a3 = [6, 9, 5, 6, 7]
a4 = [8, 12, 7, k, 9]
m = Matrix([a1, a2, a3, a4])
print("Echelon form")
print(m.echelon_form())
print("\nif k != 8")
print(solve_linear_system(m, x1, x2, x3, x4))
k = 8
a1 = [2, 3, 1, 2, 3]
a2 = [4, 6, 3, 4, 5]
a3 = [6, 9, 5, 6, 7]
a4 = [8, 12, 7, k, 9]
m = Matrix([a1, a2, a3, a4])
print("\nif k == 8")
print(solve_linear_system(m, x1, x2, x3, x4))