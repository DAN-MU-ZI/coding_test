import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    arr = list(map(int, input().split()))

    arr.sort()

    def binary_find(num, start, end):
        if start > end:
            return False

        mid = (start + end) // 2

        if arr[mid] == num:
            return True
        elif arr[mid] < num:
            start = mid + 1
        else:
            end = mid - 1

        return binary_find(num, start, end)

    m = int(input())
    finds = list(map(int, input().split()))
    for f in finds:
        if binary_find(f, 0, n - 1):
            print(1)
        else:
            print(0)


solution()
