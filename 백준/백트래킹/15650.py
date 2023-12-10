import sys

input = sys.stdin.readline


def solution():
    n, m = map(int, input().split())
    arr = []

    def dfs():
        if len(arr) == m:
            print(" ".join([str(x) for x in arr]))
            return

        for i in range(1, n + 1):
            if arr and i <= arr[-1]:
                continue
            arr.append(i)
            dfs()
            arr.pop()

    dfs()


solution()
