import sys


input = sys.stdin.readline


def solution():
    n, m = map(int, input().split())

    listeners = set()
    for _ in range(n):
        listeners.add(input().strip())

    witness = set()
    for _ in range(m):
        witness.add(input().strip())

    remain = listeners & witness
    print(len(remain))
    for person in sorted(list(remain)):
        print(person)


solution()
