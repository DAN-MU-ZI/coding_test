import sys
from collections import deque

input = sys.stdin.readline


def solution():
    n = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())

    visited = [[0] * n for _ in range(n)]

    pos = ((1, 2), (2, 1), (-1, 2), (-2, 1), (-1, -2), (-2, -1), (1, -2), (2, -1))

    stk = deque([[sx, sy]])
    visited[sx][sy] = 0
    while stk:
        x, y = stk.popleft()
        if x == ex and y == ey:
            continue

        for dx, dy in pos:
            nx = x + dx
            ny = y + dy

            if nx < 0 or n <= nx or ny < 0 or n <= ny:
                continue

            if visited[nx][ny]:
                continue

            visited[nx][ny] = visited[x][y] + 1
            stk.append([nx, ny])

    print(visited[ex][ey])


n = int(input())
for _ in range(n):
    solution()
