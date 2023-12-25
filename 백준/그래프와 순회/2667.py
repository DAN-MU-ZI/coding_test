import sys
from collections import deque

input = sys.stdin.readline


def solution():
    n = int(input())
    arr = [list(map(int, input().strip())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]

    def is_out_of_range(x, y):
        if 0 <= x and x < n and 0 <= y and y < n:
            return False
        return True

    pos = ((1, 0), (-1, 0), (0, 1), (0, -1))
    cnt = 0
    answer = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0 and visited[i][j] == 0:
                cnt += 1
                scale = 0
                stk = deque([(i, j)])
                while stk:
                    x, y = stk.popleft()
                    if visited[x][y] != 0 or arr[x][y] == 0:
                        continue
                    visited[x][y] = 1
                    scale += 1

                    for dx, dy in pos:
                        nx = x + dx
                        ny = y + dy
                        if not is_out_of_range(nx, ny) and arr[nx][ny]:
                            stk.append((nx, ny))
                answer.append(scale)

    print(cnt)
    for a in sorted(answer):
        print(a)


solution()
