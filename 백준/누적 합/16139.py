import sys


input = sys.stdin.readline


def solution():
    s = input().strip()
    q = int(input())
    di = [[0] * 26 for _ in range(len(s) + 1)]
    for i in range(1, len(s) + 1):
        c = ord(s[i - 1]) - 97
        for j in range(26):
            di[i][j] = di[i - 1][j]
        di[i][c] += 1

    for _ in range(q):
        a, l, r = input().split()
        a, l, r = ord(a) - 97, int(l), int(r)
        print(di[r + 1][a] - di[l][a])


solution()
