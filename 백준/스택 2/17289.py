import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    cnt_dict = {}
    answer = [-1] * n
    stk = [0]
    for i in range(1, n):
        while stk and arr[stk[-1]] < arr[i]:
            answer[stk.pop()] = arr[i]
        stk.append(i)
    print(*answer)


solution()
