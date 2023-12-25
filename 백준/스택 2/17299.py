import sys
from collections import defaultdict

input = sys.stdin.readline


def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    cnt_dict = defaultdict(int)
    for e in arr:
        cnt_dict[e] += 1

    answer = [-1] * n
    stk = [0]
    for i in range(1, n):
        while stk and cnt_dict[arr[stk[-1]]] < cnt_dict[arr[i]]:
            answer[stk.pop()] = arr[i]
        stk.append(i)
    print(*answer)


solution()
