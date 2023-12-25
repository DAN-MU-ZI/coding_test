import sys
from collections import deque

input = sys.stdin.readline


def solution():
    n, m = map(int, input().split())
    ladders = {}
    for _ in range(n):
        start, end = map(int, input().split())
        ladders[start] = end

    snakes = {}
    for _ in range(m):
        start, end = map(int, input().split())
        snakes[start] = end

    visited = [0] * 101
    stk = deque([1])
    while stk:
        num = stk.popleft()
        for i in range(1, 7):
            pos = num + i
            if pos <= 100 and not visited[pos]:
                if pos in ladders:
                    pos = ladders[pos]
                if pos in snakes:
                    pos = snakes[pos]
                if not visited[pos]:
                    stk.append(pos)
                    visited[pos] = visited[num] + 1

    print(visited[-1])


solution()
