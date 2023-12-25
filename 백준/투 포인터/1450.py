import sys

input = sys.stdin.readline


def solution():
    n, c = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    s, e = 0, 0
    total = 0

    answer = 0
    while s <= e:
        if total > c:
            total -= arr[s]
            s += 1
        else:
            answer += 1

            total += arr[e]
            e += 1

    print(answer + 1)


solution()
