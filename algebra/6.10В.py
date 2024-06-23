from functools import reduce
from sympy.matrices import Matrix
from itertools import permutations
m = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7]]

perm = permutations(m)
l = []
for i in perm:
    l.append(Matrix(i).columnspace())

ans = reduce(lambda re, x: re+[x] if x not in re else re, l, [])
for i in ans:
    for j in i:
        print(j, end=' ')
    print()
