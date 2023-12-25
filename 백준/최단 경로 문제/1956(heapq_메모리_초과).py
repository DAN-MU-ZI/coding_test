import sys
from heapq import heappush, heappop

input = sys.stdin.readline


v, e = map(int, input().split())

INF = 10000000
edges = [[] for _ in range(v + 1)]
distance = [[INF] * (v + 1) for _ in range(v + 1)]
hq = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edges[a].append([b, c])
    distance[a][b] = c
    heappush(hq, [c, a, b])

answer = -1
while hq:
    c, src, dst = heappop(hq)
    if src == dst:
        answer = c
        break

    if distance[src][dst] < c:
        continue

    for nd, nc in edges[dst]:
        nc = c + nc
        if nc < distance[src][nd]:
            distance[src][nd] = nc
            heappush(hq, [nc, src, nd])

print(answer)
