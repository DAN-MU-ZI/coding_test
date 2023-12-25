import sys

input = sys.stdin.readline


def solution():
    n, c = map(int, input().split())
    arr = [int(input()) for _ in range(n)]
    arr.sort()

    start = 1
    end = arr[-1] - arr[0]
    answer = 0

    while start <= end:
        mid = (start + end) // 2

        prev = arr[0]
        cnt = 1
        for i in range(1, n):
            if arr[i] - prev >= mid:
                cnt += 1
                prev = arr[i]

        if cnt >= c:
            start = mid + 1
            answer = mid
        else:
            end = mid - 1

    print(answer)


solution()
