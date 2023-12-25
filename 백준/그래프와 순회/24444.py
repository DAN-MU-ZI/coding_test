import sys
from collections import defaultdict, deque

input = sys.stdin.readline


def solution():
    n, m, r = map(int, input().split())
    visited = [0] * (n + 1)

    graph_dict = defaultdict(list)
    for _ in range(m):
        start, end = map(int, input().split())
        graph_dict[start].append(end)
        graph_dict[end].append(start)

    cnt = 1
    visited[r] = cnt
    stk = deque([r])
    while stk:
        node = stk.popleft()
        for next_node in sorted(graph_dict[node]):
            if visited[next_node] == 0:
                cnt += 1
                visited[next_node] = cnt
                stk.append(next_node)

    for order in visited[1:]:
        print(order)


solution()
