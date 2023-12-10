import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    nums = list(map(int, input().split()))
    op_counts = list(map(int, input().split()))
    global max_value, min_value, value
    max_value = int(-1e10)
    min_value = int(1e10)
    value = nums.pop(0)

    def dfs(depth=0):
        global max_value, min_value, value

        if sum(op_counts) == 0:
            max_value = max(max_value, value)
            min_value = min(min_value, value)
            return

        for i in range(4):
            if op_counts[i]:
                op_counts[i] -= 1
                save = value
                if i == 0:
                    value += nums[depth]
                elif i == 1:
                    value -= nums[depth]
                elif i == 2:
                    value *= nums[depth]
                elif i == 3:
                    if value < 0:
                        value = -(abs(value) // nums[depth])
                    else:
                        value = value // nums[depth]
                dfs(depth + 1)
                value = save
                op_counts[i] += 1

    dfs()

    print(max_value, min_value)


solution()
