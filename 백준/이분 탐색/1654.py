import sys

input = sys.stdin.readline


def solution():
    k, n = map(int, input().split())
    arr = [int(input()) for _ in range(k)]
    arr.sort()
    start = 1
    end = max(arr)

    while start <= end:
        mid = (start + end) // 2
        total = 0
        for a in arr:
            total += a // mid

        if total >= n:
            start = mid + 1
        else:
            end = mid - 1

    print(end)


solution()
