import sys
from collections import deque

input = sys.stdin.readline


def solution():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    queue = deque(arr[:k])
    arr = deque(arr[k:])

    answer = sum(queue)
    tmp = answer
    while arr:
        tmp -= queue.popleft()
        a = arr.popleft()
        tmp += a
        queue.append(a)
        answer = max(answer, tmp)
    print(answer)


solution()
