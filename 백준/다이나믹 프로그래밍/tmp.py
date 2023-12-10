def func(tops):
    dp = [[0, 0] for _ in range(len(tops) + 1)]

    dp[0][0] = 1
    dp[0][1] = 0

    for i, top in zip(range(1, len(tops) + 1), tops):
        dp[i][0] = dp[i - 1][0] * 2 + dp[i - 1][1]
        if top == 1:
            dp[i][0] = dp[i][0] + dp[i - 1][0] + dp[i - 1][1]
        dp[i][1] = dp[i - 1][0] + dp[i - 1][1]

    print(sum(dp[len(tops)]))
    print(dp)


func([0, 1])
func([1, 0])
func([0, 0, 1, 1, 0])
func([0, 0, 0])
