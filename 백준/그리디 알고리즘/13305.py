import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    roads = [0] + list(map(int, input().split()))
    costs = list(map(int, input().split()))

    answer = 0
    stk = roads[0]
    min_cost = costs[0]
    for i in range(1, n):
        stk += roads[i]
        if min_cost >= costs[i]:
            answer += min_cost * stk
            stk = 0
            min_cost = costs[i]
        else:
            continue
    if stk != 0:
        answer += min_cost * stk
    print(answer)


solution()
