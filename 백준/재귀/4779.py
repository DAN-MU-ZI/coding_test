import sys

input = sys.stdin.readline


def solution():
    def vacate(p, r):
        for i in range(p, r):
            arr[i] = " "

    def func(p, r, depth):
        if p < r and depth:
            start = p
            first = p + (r - p) // 3
            second = p + (r - p) // 3 * 2
            end = r
            func(start, first, depth - 1)
            vacate(first, second)
            func(second, end, depth - 1)

    while True:
        try:
            n = int(input())
            arr = ["-" for _ in range(3**n)]
            func(0, 3**n, n)
            print("".join(arr))
        except:
            break


solution()
