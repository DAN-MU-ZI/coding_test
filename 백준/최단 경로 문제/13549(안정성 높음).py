import sys
from collections import deque

input = sys.stdin.readline


def solution():
    n, k = map(int, input().split())
    INF = 100001
    visited = [0] * INF
    costs = [INF] * (INF)

    def is_out_of_range(p):
        return p < 0 or INF <= p

    stk = deque([n])
    costs[n] = 0
    while stk:
        x = stk.popleft()
        if visited[x]:
            continue
        visited[x] = 1

        nx = x + 1
        if not is_out_of_range(nx):
            costs[nx] = min(costs[nx], costs[x] + 1)
            stk.append(nx)

        nx = x - 1
        if not is_out_of_range(nx):
            costs[nx] = min(costs[nx], costs[x] + 1)
            stk.append(nx)

        nx = x * 2
        if not is_out_of_range(nx):
            costs[nx] = min(costs[nx], costs[x])
            stk.append(nx)
    print(costs[k])


solution()
