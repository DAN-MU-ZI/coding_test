import sys
from heapq import heappush, heappop

input = sys.stdin.readline


def solution():
    n = int(input())
    arr = []
    for _ in range(n):
        x = int(input())
        if x:
            heappush(arr, (-x, x))
        else:
            if arr:
                print(heappop(arr)[-1])
            else:
                print(0)


solution()
