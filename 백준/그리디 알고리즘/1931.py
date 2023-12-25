import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(n)]
    arr.sort(key=lambda x: (x[0], x[1]))

    start, end = arr[0]
    arr = arr[1:]
    answer = 1
    for ns, ne in arr:
        if start < ns < end and ne <= end:
            start = ns
            end = ne
        elif end <= ns:
            answer += 1
            start = ns
            end = ne
    print(answer)


solution()
