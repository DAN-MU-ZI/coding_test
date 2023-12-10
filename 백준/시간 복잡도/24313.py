import sys

input = sys.stdin.readline


def solution():
    a1, a2 = map(int, input().split())
    c = int(input())
    n0 = int(input())

    n = n0
    while n <= 100:
        if a1 * n + a2 > c * n:
            print(0)
            return
        n += 1
    print(1)


solution()
