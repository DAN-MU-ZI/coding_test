import sys
from collections import deque

input = sys.stdin.readline


def func():
    n = int(input())
    stk = deque()

    for _ in range(n):
        com = list(map(int, input().split()))
        if com[0] == 1:
            stk.append(com[1])
        elif com[0] == 2:
            if len(stk):
                print(stk.pop())
            else:
                print(-1)
        elif com[0] == 3:
            print(len(stk))
        elif com[0] == 4:
            if len(stk) == 0:
                print(1)
            else:
                print(0)
        elif com[0] == 5:
            if len(stk):
                print(stk[-1])
            else:
                print(-1)


func()
