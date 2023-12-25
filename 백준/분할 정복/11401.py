import sys

input = sys.stdin.readline


def solution():
    n, k = map(int, input().split())
    div = 1000000007

    def factorial(a):
        res = 1
        for i in range(2, a + 1):
            res = res * i % div
        return res

    print(factorial(n) * pow((factorial(n - k) * factorial(k) % div), -1, div) % div)


solution()
