import sys

dp = [[0 for _ in range(2)] for _ in range(41)]
dp[0][0] = 1
dp[1][1] = 1

for i in range(2, 41):
    dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
    dp[i][1] = dp[i - 1][1] + dp[i - 2][1]


def func():
    n = int(sys.stdin.readline())
    for i in range(n):
        num = int(sys.stdin.readline())
        print(dp[num][0], dp[num][1])


func()
