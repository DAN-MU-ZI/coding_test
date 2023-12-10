import sys

input = sys.stdin.readline


def solution():
    n, m = map(int, input().split())
    arr = [0] + list(map(int, input().split()))

    for i in range(2, n + 1):
        arr[i] += arr[i - 1]

    for _ in range(m):
        a, b = map(int, input().split())
        print(arr[b] - arr[a - 1])


solution()
