# 중복된 간선 경로에 대해서 더 낮은 가중치 정보만을 추가한다
# 처음에 계속 틀렸던 이유는 중복된 간선정보가 담기지 않는다는 전제를 했다
import sys
from collections import defaultdict
from heapq import heappush, heappop

input = sys.stdin.readline


def solution():
    nv, ne = map(int, input().split())
    k = int(input())

    graph = defaultdict(lambda: defaultdict(dict))
    for _ in range(ne):
        u, v, w = map(int, input().split())
        if v in graph[u].keys():
            if graph[u][v] > w:
                graph[u][v] = w
        else:
            graph[u][v] = w

    INF = 199991
    distance = [INF] * (nv + 1)
    q = []

    distance[k] = 0
    heappush(q, (0, k))

    while q:
        dist, now = heappop(q)

        if dist > distance[now]:
            continue

        for v, cost in graph[now].items():
            cost = dist + cost
            if cost < distance[v]:
                distance[v] = cost
                heappush(q, (cost, v))

    for c in distance[1:]:
        if c == INF:
            print("INF")
        else:
            print(c)


solution()
