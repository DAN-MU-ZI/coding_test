import sys

input = sys.stdin.readline


def solution():
    answer = 665
    n = int(input())
    while n:
        answer += 1
        if str(answer).find("666") != -1:
            n -= 1

    print(answer)


solution()
