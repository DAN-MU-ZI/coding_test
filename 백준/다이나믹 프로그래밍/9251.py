import sys


def func():
    a = sys.stdin.readline()
    b = sys.stdin.readline()

    dp = [[0 for _ in range(len(b))] for _ in range(len(a))]

    for i in range(1, len(a)):
        for j in range(1, len(b)):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    print(dp[len(a) - 1][len(b) - 1])


func()
