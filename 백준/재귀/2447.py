import sys

input = sys.stdin.readline


def solution():
    n = int(input())

    arr = [["*" for _ in range(n)] for _ in range(n)]

    def clearCell(x_start, x_end, y_start, y_end):
        for i in range(x_start, x_end):
            for j in range(y_start, y_end):
                arr[i][j] = " "

    def func(n, x, y):
        if n == 0:
            return

        n = n // 3
        for i in range(3):
            for j in range(3):
                if i == j == 1:
                    clearCell(
                        x + n * i,
                        x + n * i + n,
                        y + n * j,
                        y + n * j + n,
                    )
                else:
                    func(n, x + n * i, y + n * j)

    func(n, 0, 0)
    for line in arr:
        print("".join(line))


solution()
