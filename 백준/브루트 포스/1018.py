import sys

input = sys.stdin.readline


def solution():
    n, m = map(int, input().split())
    board = []
    for _ in range(n):
        board.append(list(input()))

    def func(a, b):
        stk = 0
        for k in range(8):
            for l in range(8):
                if k % 2 == 0:
                    if l % 2 == 0:
                        if board[i + k][j + l] == a:
                            stk += 1
                    else:
                        if board[i + k][j + l] == b:
                            stk += 1
                else:
                    if l % 2 == 0:
                        if board[i + k][j + l] == b:
                            stk += 1
                    else:
                        if board[i + k][j + l] == a:
                            stk += 1
        return stk

    answer = 32
    for i in range(n - 7):
        for j in range(m - 7):
            answer = min(answer, func("W", "B"))
            answer = min(answer, func("B", "W"))

    print(answer)


solution()
