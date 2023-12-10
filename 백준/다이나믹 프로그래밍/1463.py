import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    dp = [1000000 + 1 for _ in range(n + 1)]
    dp[0] = 0
    dp[1] = 0

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 1

        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i // 3] + 1)
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i // 2] + 1)

    print(dp[n])


solution()
