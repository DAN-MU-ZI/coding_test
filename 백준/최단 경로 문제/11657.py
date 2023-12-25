import sys
from collections import defaultdict

input = sys.stdin.readline


def solution():
    n, m = map(int, input().split())

    edges = [list(map(int, input().split())) for _ in range(m)]

    INF = 10000000
    distance = [INF] * (n + 1)

    def func(start):
        distance[start] = 0

        for i in range(1, n + 1):
            for src_node, dst_node, cost in edges:
                if (
                    distance[src_node] != INF
                    and distance[src_node] + cost < distance[dst_node]
                ):
                    distance[dst_node] = distance[src_node] + cost
                    if i == n:
                        return False
        return True

    if func(1):
        for i in range(2, n + 1):
            if distance[i] == INF:
                print(-1)
            else:
                print(distance[i])
    else:
        print(-1)


solution()
