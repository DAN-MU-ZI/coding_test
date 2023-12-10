import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    my_cards = input().split()

    my_cards_set = set(my_cards)
    my_cards_dict = {k: 0 for k in my_cards_set}
    for card in my_cards:
        my_cards_dict[card] += 1

    m = int(input())
    cards = input().split()
    for card in cards:
        if card not in my_cards_set:
            print(0, end=" ")
        else:
            print(my_cards_dict[card], end=" ")


solution()
