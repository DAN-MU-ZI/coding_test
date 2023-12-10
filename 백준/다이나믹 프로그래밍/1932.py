import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    for depth in range(n - 2, -1, -1):
        for i in range(len(arr[depth])):
            arr[depth][i] += max(arr[depth + 1][i], arr[depth + 1][i + 1])
    print(arr[0][0])


solution()
