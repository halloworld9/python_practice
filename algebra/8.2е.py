from sympy import Symbol, Matrix, symbols, solve_undetermined_coeffs, solve_linear_system, solve

k = Symbol("k")
x1, x2, x3 = symbols('x1 x2 x3')
a1 = [k, 1, 1, 1]
a2 = [1, k, 1, 1]
a3 = [1, 1, k, 1]
m = Matrix([a1, a2, a3])
print(solve_linear_system(m, x1, x2, x3))
echelon = m.echelon_form()
for i in solve(echelon.row(-1)):
    for j in i.keys():
        k = i[j]
        a1 = [k, 1, 1, 1]
        a2 = [1, k, 1, 1]
        a3 = [1, 1, k, 1]
        m = Matrix([a1, a2, a3])
        print(solve_linear_system(m, x1, x2, x3))