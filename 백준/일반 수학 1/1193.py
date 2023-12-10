import sys


def solution():
    x = int(sys.stdin.readline())
    n = 1
    while True:
        remain = x - n * (n + 1) // 2
        if remain <= 0:
            a = n + remain
            b = 1 - remain
            if n % 2 == 0:
                print(f"{a}/{b}")
            else:
                print(f"{b}/{a}")
            break

        n += 1


solution()
