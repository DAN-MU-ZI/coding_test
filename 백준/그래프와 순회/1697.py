import sys
from collections import deque

input = sys.stdin.readline


def solution():
    n, k = map(int, input().split())
    visited = [0] * 100001

    if n >= k:
        print(n - k)
        return

    stk = deque([n])
    while stk:
        x = stk.popleft()

        if x == k:
            break
        for i in (x + 1, x - 1, x * 2):
            if 0 <= i and i <= 100000 and visited[i] == 0:
                visited[i] = visited[x] + 1
                stk.append(i)
    print(visited[k])


solution()
