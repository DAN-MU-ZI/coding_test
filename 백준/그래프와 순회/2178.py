import sys
from collections import deque

input = sys.stdin.readline


def solution():
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    pos = ((1, 0), (-1, 0), (0, 1), (0, -1))

    stk = deque([(0, 0)])
    visited[0][0] = 1
    while stk:
        x, y = stk.popleft()

        for dx, dy in pos:
            nx = x + dx
            ny = y + dy
            if (
                0 <= nx
                and nx < n
                and 0 <= ny
                and ny < m
                and arr[nx][ny] == "1"
                and visited[nx][ny] == 0
            ):
                visited[nx][ny] = visited[x][y] + 1
                stk.append((nx, ny))

    print(visited[n - 1][m - 1])


solution()
