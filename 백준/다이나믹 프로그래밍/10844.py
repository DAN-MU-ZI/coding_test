import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    dp = [1 for _ in range(10)]

    for i in range(1, n):
        tmp = [0 for _ in range(10)]

        for j in range(1, 9):
            tmp[j] = dp[j - 1] + dp[j + 1]
        tmp[0] = dp[1]
        tmp[9] = dp[8]
        dp = tmp

    print(sum(dp[1:]) % 1000000000)


solution()
