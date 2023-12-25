import sys
from collections import deque

input = sys.stdin.readline


def solution():
    n, m = map(int, input().split())
    arr = [input().strip() for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1

    pos = ((1, 0), (-1, 0), (0, 1), (0, -1))
    global distance
    distance = 100 * 100

    def dfs(x, y, cnt):
        global distance
        print(x, y, cnt)
        if x == n - 1 and y == m - 1 and distance > cnt:
            distance = cnt
            return

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
                visited[nx][ny] = 1
                dfs(nx, ny, cnt + 1)
                visited[nx][ny] = 0

    dfs(0, 0, 1)

    print(distance)


solution()
