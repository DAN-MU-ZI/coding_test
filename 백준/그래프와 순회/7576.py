import sys
from collections import deque

input = sys.stdin.readline


def solution():
    m, n = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    direction = ((1, 0), (-1, 0), (0, 1), (0, -1))

    def is_out_of_range(x, y):
        return x < 0 or n <= x or y < 0 or m <= y

    stk = deque()
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                stk.append((i, j))

    while stk:
        x, y = stk.popleft()
        arr[x][y] = 1

        for dx, dy in direction:
            nx = x + dx
            ny = y + dy

            if not is_out_of_range(nx, ny) and arr[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                stk.append((nx, ny))

    answer = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                print(-1)
                return
            if answer < visited[i][j]:
                answer = visited[i][j]

    print(answer)


solution()
