import sys

input = sys.stdin.readline


def solution():
    n, m = map(int, input().split())

    dictionary = {}
    for _ in range(n):
        string = input().strip()
        if len(string) >= m:
            if string not in dictionary:
                dictionary[string] = 1
            else:
                dictionary[string] += 1

    words = sorted(
        dictionary.items(), key=lambda item: (-item[1], -len(item[0]), item[0])
    )
    for word, count in words:
        print(word)


solution()
