import sys
from collections import deque

input = sys.stdin.readline


def solution():
    n, m = map(int, input().split())
    board = [input().strip() for _ in range(n)]
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

    direction = ((1, 0), (-1, 0), (0, 1), (0, -1))
    visited[0][0][0] = 1
    visited[0][0][1] = 1
    stk = deque([[0, 0, 0]])
    while stk:
        x, y, is_break = stk.popleft()

        for dx, dy in direction:
            nx = x + dx
            ny = y + dy

            if nx < 0 or n <= nx or ny < 0 or m <= ny:
                continue

            if visited[nx][ny][is_break]:
                continue

            if board[nx][ny] == "1":
                if not is_break:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    stk.append([nx, ny, 1])
            elif board[nx][ny] == "0":
                visited[nx][ny][is_break] = visited[x][y][is_break] + 1
                stk.append([nx, ny, is_break])

    if visited[n - 1][m - 1][0] and visited[n - 1][m - 1][1]:
        print(min(visited[n - 1][m - 1]))
    elif not visited[n - 1][m - 1][0] and visited[n - 1][m - 1][1]:
        print(visited[n - 1][m - 1][1])
    elif not visited[n - 1][m - 1][1] and visited[n - 1][m - 1][0]:
        print(visited[n - 1][m - 1][0])
    else:
        print(-1)


solution()
