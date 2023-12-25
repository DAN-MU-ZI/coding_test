import sys
from collections import defaultdict


input = sys.stdin.readline


def solution():
    n, m, r = map(int, input().split())
    visited = [0] * (n + 1)

    graph_dict = defaultdict(list)
    for _ in range(m):
        start, end = map(int, input().split())
        graph_dict[start].append(end)
        graph_dict[end].append(start)

    cnt = 0
    stk = [r]
    while stk:
        node = stk.pop()
        if visited[node]:
            continue

        cnt += 1
        visited[node] = cnt

        for next_node in sorted(graph_dict[node], reverse=True):
            if visited[next_node] == 0:
                stk.append(next_node)

    for order in visited[1:]:
        print(order)


solution()
