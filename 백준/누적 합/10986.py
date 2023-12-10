import sys

input = sys.stdin.readline


def solution():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    remain = [0] * m
    stk = 0
    for i in range(n):
        stk += arr[i]
        remain[stk % m] += 1

    answer = remain[0]
    for i in range(m):
        answer += remain[i] * (remain[i] - 1) // 2
    print(answer)


solution()
