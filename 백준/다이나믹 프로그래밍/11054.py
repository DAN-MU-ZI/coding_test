import sys


def solution():
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))

    left_dp = [1 for _ in range(n)]
    left_start = 1
    left_end = n
    for select in range(left_start, left_end):
        for left in range(select):
            if nums[select] > nums[left]:
                left_dp[select] = max(left_dp[select], left_dp[left] + 1)

    right_dp = [1 for _ in range(n)]
    right_start = n - 1
    right_end = -1
    for select in range(right_start, right_end, -1):
        for right in range(right_start, select, -1):
            if nums[select] > nums[right]:
                right_dp[select] = max(right_dp[select], right_dp[right] + 1)

    print(max([l + r for l, r in zip(left_dp, right_dp)]) - 1)


solution()
