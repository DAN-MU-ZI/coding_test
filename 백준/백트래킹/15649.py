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
            if i in arr:
                continue
            arr.append(i)
            dfs()
            arr.pop()

    dfs()


solution()
