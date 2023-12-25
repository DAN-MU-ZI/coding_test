import sys

input = sys.stdin.readline


n, b = map(int, input().split())
op = [list(map(int, input().split())) for _ in range(n)]
div = 1000


def pow_dot(mat1, mat2):
    res = []
    for i in range(n):
        line = []
        for j in range(n):
            tmp = 0
            for l in range(n):
                tmp += mat1[i][l] % div * mat2[l][j] % div
                tmp = tmp % div
            line.append(tmp)
        res.append(line)
    return res


def dfs(mat, depth):
    if depth == 1:
        for i in range(n):
            for j in range(n):
                mat[i][j] = mat[i][j] % div
        return mat

    res = dfs(mat, depth // 2)
    if depth % 2:
        return pow_dot(pow_dot(res, res), mat)
    else:
        return pow_dot(res, res)


for line in dfs(op, b):
    print(" ".join([str(x) for x in line]))
