import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    my_cards = set(map(int, input().split()))
    m = int(input())
    cards = list(map(int, input().split()))

    for card in cards:
        print(int(card in my_cards), end=" ")
    print()


solution()
