import sys

input = sys.stdin.readline


def solution():
    k = int(input())

    def hanoi(n, src, dst, via):
        if n == 1:
            print(src, dst)
            return
        hanoi(n - 1, src, via, dst)
        print(src, dst)
        hanoi(n - 1, via, dst, src)

    print(2**k - 1)
    hanoi(k, 1, 3, 2)


solution()
