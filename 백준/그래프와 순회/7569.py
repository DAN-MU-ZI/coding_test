import sys
from collections import deque

input = sys.stdin.readline


def solution():
    m, n, h = map(int, input().split())
    arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
    visited = [[[0] * m for _ in range(n)] for _ in range(h)]

    stk = deque()
    for z in range(h):
        for x in range(n):
            for y in range(m):
                if arr[z][x][y] == 1:
                    stk.append((z, x, y))

    pos = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))

    def is_out_of_range(z, x, y):
        return x < 0 or n <= x or y < 0 or m <= y or z < 0 or h <= z

    while stk:
        z, x, y = stk.popleft()
        arr[z][x][y] = 1

        for dz, dx, dy in pos:
            nz = z + dz
            nx = x + dx
            ny = y + dy

            if (
                not is_out_of_range(nz, nx, ny)
                and arr[nz][nx][ny] == 0
                and not visited[nz][nx][ny]
            ):
                visited[nz][nx][ny] = visited[z][x][y] + 1
                stk.append((nz, nx, ny))

    answer = 0
    for z in range(h):
        for x in range(n):
            for y in range(m):
                if arr[z][x][y] == 0:
                    print(-1)
                    return
                if answer < visited[z][x][y]:
                    answer = visited[z][x][y]

    print(answer)


solution()
