# graph에 모든 간선정보를 담는다
# 중복된 경로에 대한 모든 가중치가 담긴다
# 그러므로 계산할 중복된 간선을 조회하는 중복이 발생한다
import sys
from heapq import heappush, heappop

input = sys.stdin.readline


def solution():
    nv, ne = map(int, input().split())
    k = int(input())

    graph = [[] for _ in range(nv + 1)]
    for _ in range(ne):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    INF = 1000000000
    distance = [INF] * (nv + 1)
    q = []

    distance[k] = 0
    heappush(q, (0, k))

    while q:
        dist, now = heappop(q)

        if dist > distance[now]:
            continue

        for v, cost in graph[now]:
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
