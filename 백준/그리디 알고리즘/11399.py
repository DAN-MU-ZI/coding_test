import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    answer = 0
    for i in range(n):
        answer += arr[i] * (n - i)

    print(answer)


solution()
