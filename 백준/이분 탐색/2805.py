import sys

input = sys.stdin.readline


def solution():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    start = 1
    end = max(arr)

    while start <= end:
        mid = (start + end) // 2
        total = 0
        for a in arr:
            if a >= mid:
                total += a - mid

        if total >= m:
            start = mid + 1
        else:
            end = mid - 1

    print(end)


solution()
