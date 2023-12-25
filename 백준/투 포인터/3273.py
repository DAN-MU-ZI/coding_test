import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    arr = list(map(int, input().split()))
    x = int(input())
    arr.sort()

    s, e = 0, n - 1
    answer = 0
    while s < e:
        if (arr[s] + arr[e]) > x:
            e -= 1
        elif (arr[s] + arr[e]) < x:
            s += 1
        else:
            s += 1
            e -= 1
            answer += 1

    print(answer)


solution()
