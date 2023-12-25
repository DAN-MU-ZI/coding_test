import sys
from collections import defaultdict
from heapq import heappush, heappop

input = sys.stdin.readline


def solution():
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    edges = defaultdict(lambda: defaultdict(dict))
    for _ in range(m):
        a, b, d = map(int, input().split())
        edges[a][b] = d
        edges[b][a] = d

    targets = [int(input()) for _ in range(t)]

    INF = 1000000000

    def bfs(start):
        distance = [INF] * (n + 1)
        q = []

        distance[start] = 0
        heappush(q, (0, start))

        while q:
            dist, now = heappop(q)

            if dist > distance[now]:
                continue

            for b, cost in edges[now].items():
                cost = dist + cost
                if cost < distance[b]:
                    distance[b] = cost
                    heappush(q, (cost, b))

        return distance

    s_pipe = bfs(s)
    g_pipe = bfs(g)
    h_pipe = bfs(h)

    answer = []
    for target in targets:
        if (
            s_pipe[target] == s_pipe[h] + h_pipe[g] + g_pipe[target]
            or s_pipe[target] == s_pipe[g] + g_pipe[h] + h_pipe[target]
        ):
            answer.append(target)
    answer.sort()
    print(*answer)


T = int(input())
for _ in range(T):
    solution()
