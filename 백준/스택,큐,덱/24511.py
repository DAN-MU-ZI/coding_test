import sys
from collections import deque

input = sys.stdin.readline


def solution():
    n = int(input())
    kind = list(map(int, input().split()))
    elements = list(map(int, input().split()))

    structures = deque()
    for k, e in zip(kind, elements):
        if k == 0:
            structures.append(e)

    answer = deque()
    m = int(input())
    nums = list(map(int, input().split()))
    for num in nums:
        structures.appendleft(num)
        answer.append(str(structures.pop()))
    print(" ".join(answer))


solution()
