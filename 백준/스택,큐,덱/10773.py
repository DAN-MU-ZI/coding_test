import sys
from collections import deque

input = sys.stdin.readline


def solution():
    k = int(input())
    arr = deque()
    for _ in range(k):
        x = int(input())
        if x == 0:
            arr.pop()
            continue

        arr.append(x)

    print(sum(arr))


solution()
