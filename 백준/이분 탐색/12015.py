import sys
from bisect import bisect_left


input = sys.stdin.readline


def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    stk = [arr[0]]

    for a in arr:
        if a > stk[-1]:
            stk.append(a)
        else:
            stk[bisect_left(stk, a)] = a

    print(len(stk))


solution()
