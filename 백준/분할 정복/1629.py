import sys


input = sys.stdin.readline


def solution():
    print(pow(*map(int, input().split())))


solution()
