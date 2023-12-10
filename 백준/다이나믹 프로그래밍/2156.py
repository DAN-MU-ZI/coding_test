import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    arr = [int(input()) for _ in range(n)]

    dp = [[0, 0, 0, 0] for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][0] = max(dp[i - 1][2], dp[i - 1][3]) + arr[i - 1]
        dp[i][1] = dp[i - 1][0] + arr[i - 1]
        dp[i][2] = max(dp[i - 1][:2])

        dp[i][3] = dp[i - 1][2]

    print(max(dp[-1]))


solution()
