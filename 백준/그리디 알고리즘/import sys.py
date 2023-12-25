import sys

input = sys.stdin.readline


def solution():
    cal = input().strip().split("-")
    length = len(cal)

    for i in range(length):
        cal[i] = sum([int(x) for x in cal[i].split("+")])

    answer = cal[0]
    for i in range(1, length):
        answer -= cal[i]
    print(answer)


solution()
