import sys

input = sys.stdin.readline


def solution():
    s = input().strip()
    part = set()
    for i in range(len(s)):
        for j in range(len(s) - i):
            part.add(s[i : i + j + 1])
    print(len(part))


solution()
