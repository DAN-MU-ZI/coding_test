import sys

input = sys.stdin.readline


def solution():
    dp = [1 for _ in range(101)]
    dp[4] = 2
    dp[5] = 2
    for i in range(6, 101):
        dp[i] = dp[i - 1] + dp[i - 5]

    n = int(input())
    for _ in range(n):
        print(dp[int(input())])


solution()
