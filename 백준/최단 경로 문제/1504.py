import sys
from collections import defaultdict
from heapq import heappush, heappop

input = sys.stdin.readline


def solution():
    n, e = map(int, input().split())

    graph = defaultdict(lambda: defaultdict(dict))
    for _ in range(e):
        a, b, c = map(int, input().split())
        graph[a][b] = c
        graph[b][a] = c

    v1, v2 = map(int, input().split())
    INF = 8000000

    def bfs(start):
        distance = [INF] * (n + 1)
        q = []

        distance[start] = 0
        heappush(q, (0, start))

        while q:
            dist, now = heappop(q)

            if dist > distance[now]:
                continue

            for b, cost in graph[now].items():
                cost = dist + cost
                if cost < distance[b]:
                    distance[b] = cost
                    heappush(q, (cost, b))

        return distance

    def cal_result():
        from_start = bfs(1)
        if from_start[v1] >= INF and from_start[v2]:
            return -1
        from_v1 = bfs(v1)
        if from_v1[v2] >= INF and from_v1[n] >= INF:
            return -1
        from_v2 = bfs(v2)
        if from_v2[v1] >= INF and from_v2[n] >= INF:
            return -1
        ptn1 = from_start[v1] + from_v1[v2] + from_v2[n]
        ptn2 = from_start[v2] + from_v2[v1] + from_v1[n]

        res = min(ptn1, ptn2)
        if res < INF:
            return res
        else:
            return -1

    print(cal_result())


solution()
