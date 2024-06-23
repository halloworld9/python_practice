def check_matrix(matrix): #условия найденные в интернете
    height = len(matrix)
    f = False
    for i in range(height):
        row = matrix[i]
        row_len = len(row) - 1
        if row_len != height:
            return False
        elif row[i] == 0:
            return False
        s = 0
        for j in range(row_len):
            if i - 1 <= j <= i + 1:
                s += abs(row[j])
            elif row[j] != 0:
                return False
        if abs(row[i]) * 2 < s:
            return False
        elif abs(row[i]) * 2 > s:
            f = True
    return f


def input_matrix(matrix):
    line = input()

    while line.strip() != "":
        matrix.append([i for i in map(int, line.split())])
        line = input()


def solve(matrix): #алгоритм с википедии
    n = len(matrix)
    v = [0 for _ in range(n)]
    u = [0 for _ in range(n)]
    v[0] = -matrix[0][1] / matrix[0][0]
    u[0] = matrix[0][n] / matrix[0][0]

    for i in range(1, n - 1):
        v[i] = -matrix[i][i + 1] / (matrix[i][i] + matrix[i][i - 1] * v[i - 1])
        u[i] = (matrix[i][n] - matrix[i][i - 1] * u[i - 1]) / (matrix[i][i - 1] * v[i - 1] + matrix[i][i])

    v[n - 1] = 0
    u[n - 1] = (matrix[n - 1][n] - matrix[n - 1][n - 2] * u[n - 2]) / (
            matrix[n - 1][n - 2] * v[n - 2] + matrix[n - 1][n - 1])

    x = [0 for _ in range(n)]
    x[n - 1] = u[n - 1]
    for i in range(n - 1, 0, -1):
        x[i - 1] = v[i - 1] * x[i] + u[i - 1]

    return x


def main():
    print("input system")
    matrix = []
    input_matrix(matrix)
    if not check_matrix(matrix):
        print("invalid input")
        return
    x = solve(matrix)
    for i in range(len(x)):
        print(f"x{i + 1}={x[i]}")


if __name__ == '__main__':
    main()
