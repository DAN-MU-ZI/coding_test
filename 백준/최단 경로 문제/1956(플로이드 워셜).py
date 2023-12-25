import sys

input = sys.stdin.readline


def solution():
    v, e = map(int, input().split())

    INF = 1000000000
    distance = [[INF] * (v + 1) for _ in range(v + 1)]

    for _ in range(e):
        a, b, c = map(int, input().split())
        if distance[a][b] > c:
            distance[a][b] = c

    for k in range(1, v + 1):
        for i in range(1, v + 1):
            for j in range(1, v + 1):
                if distance[i][j] > distance[i][k] + distance[k][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

    answer = INF
    for i in range(1, v):
        if answer > distance[i][i]:
            answer = distance[i][i]

    if answer == INF:
        print(-1)
    else:
        print(answer)


solution()
