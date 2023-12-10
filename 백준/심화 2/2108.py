import sys
from heapq import heappush, heappop

input = sys.stdin.readline


def solution():
    n = int(input())
    arr_di = {}
    arr = []
    total = 0
    max_num = -4001
    min_num = 4001
    for _ in range(n):
        num = int(input())
        if num not in arr_di:
            arr_di[num] = 1
        else:
            arr_di[num] += 1
        arr.append(num)
        total += num
        max_num = max(max_num, num)
        min_num = min(min_num, num)

    print(round(total / n))

    sorted_keys = sorted(arr)
    print(sorted_keys[n // 2])

    max_count = max(arr_di.values())
    tmp = sorted([k for k, v in arr_di.items() if v == max_count])
    if len(tmp) > 1:
        print(tmp[1])
    else:
        print(tmp[0])

    print(max_num - min_num)


solution()
