from sympy import Matrix, Rational


a1 = [Rational(1, 2), Rational(1, 3), Rational(1, 2), 1]
a2 = [Rational(1, 3), Rational(1, 2), 1, Rational(1, 2)]
a3 = [Rational(1, 2), 1, Rational(1, 2), Rational(1, 3)]
a4 = [1, Rational(1, 2), Rational(1, 3), Rational(1, 2)]
m = Matrix([a1, a2, a3, a4])
print(m.det())
