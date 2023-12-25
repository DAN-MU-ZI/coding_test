import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    k = int(input())

    start = 1
    end = k
    while start <= end:
        mid = (start + end) // 2

        cnt = 0
        for i in range(1, n + 1):
            div = mid // i
            if mid // i > n:
                cnt += n
            else:
                cnt += div

        if cnt >= k:
            end = mid - 1
        else:
            start = mid + 1

    print(start)


solution()
