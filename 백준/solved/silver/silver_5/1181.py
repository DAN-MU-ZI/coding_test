import sys
n = int(sys.stdin.readline())
arr = set()
for i in range(n):
    arr.add(sys.stdin.readline().strip())

arr = list(sorted(arr, key=lambda x:(len(x), x)))
for i in arr:
    print(i)