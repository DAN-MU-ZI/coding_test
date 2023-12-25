import sys

input = sys.stdin.readline


def prime_list(n):
    array = [True] * n

    m = int(n**0.5)
    for i in range(2, m + 1):
        if array[i] == True:
            for j in range(i + i, n, i):
                array[j] = False

    return [i for i in range(2, n) if array[i] == True]


def solution():
    n = int(input())
    s, e = 0, 0

    primes = prime_list(n + 1)
    total = primes[0]

    answer = 0
    prime_len = len(primes)
    while s <= e:
        if total > n:
            total -= primes[s]
            s += 1
        else:
            if total == n:
                answer += 1
            e += 1
            if e == prime_len:
                break
            total += primes[e]

    print(answer)


solution()
