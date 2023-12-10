import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    arr = [int(input()) for _ in range(n)]

    if n == 1:
        print(arr[0])
        return
    if n == 2:
        print(sum(arr))
        return

    dp = [[0, 0, 0] for _ in range(n)]

    arr.reverse()
    dp[0][0] = arr[0]
    dp[0][1] = arr[0]
    dp[0][2] = arr[0]

    dp[1][1] = dp[0][2] + arr[1]
    dp[1][2] = arr[0]

    for i in range(2, n):
        dp[i][0] = dp[i - 1][2] + arr[i]
        dp[i][1] = dp[i - 1][0] + arr[i]
        dp[i][2] = max(dp[i - 1][:2])

    print(max(dp[-1]))


solution()
