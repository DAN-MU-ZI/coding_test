import sys
from math import *
n = int(sys.stdin.readline())

arr = [0 for x in range(10)]
cnt=0
while n:
    a = n%10
    b = n//10

    for i in range(10):
        arr[i]+=b*10**cnt
    
    if a:
        for i in range(1,a):
            arr[i]+=10**cnt
    if b:
        for c in str(b):
            arr[int(c)]+=a*10**cnt
    if a==0:
        arr[0]-=10**cnt
    arr[a]+=1
    n//=10
    cnt+=1
print(' '.join(map(str,arr)))