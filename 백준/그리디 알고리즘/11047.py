import sys

input = sys.stdin.readline


def solution():
    n, k = map(int, input().split())
    coins = []
    for _ in range(n):
        coins.append(int(input()))
    coins.reverse()

    answer = 0
    for coin in coins:
        if k == 0:
            break
        if k // coin > 0:
            answer += k // coin
            k = k % coin
    print(answer)


solution()
