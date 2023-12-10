import sys

input = sys.stdin.readline


def solution():
    n, m = map(int, input().split())
    str_set = set()
    for _ in range(n):
        str_set.add(input())

    answer = 0
    for _ in range(m):
        if input() in str_set:
            answer += 1
    print(answer)


solution()
