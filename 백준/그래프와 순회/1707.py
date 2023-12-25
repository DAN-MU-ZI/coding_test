import sys
from collections import defaultdict, deque

input = sys.stdin.readline


def solution():
    v, e = map(int, input().split())

    graph = defaultdict(list)
    for _ in range(e):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    visited = [0] * (v + 1)
    for i in range(1, v + 1):
        if not visited[i]:
            stk = deque([i])
            color = 1
            visited[i] = color
            while stk:
                cur = stk.popleft()

                for node in graph[cur]:
                    if not visited[node]:
                        visited[node] = visited[cur] * -1
                        stk.append(node)
                        continue
                    if visited[node] == visited[cur]:
                        print("NO")
                        return

    print("YES")


k = int(input())
for _ in range(k):
    solution()
