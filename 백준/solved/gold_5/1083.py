import sys

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
s = int(sys.stdin.readline())

for i in range(n):
    max_num = max(arr[i:min(n,i+s+1)])
    start = arr.index(max_num)
    
    for j in range(start,i,-1):
        tmp = arr[j]
        arr[j] = arr[j-1]
        arr[j-1] = tmp

    s -= (start - i)
    if s==0:
        break

print(' '.join(map(str, arr)))