import math
import sys
from itertools import permutations

def factorial(n):
    res = 1
    for i in range(1,n+1):
        res*=i
    return res

n = int(sys.stdin.readline())
lines = []
for i in range(n):
    lines.append(int(sys.stdin.readline()))
k = int(sys.stdin.readline())
lines = [x%k for x in lines]
cnt = 0
muls = [10**x for x in range(n)]

print(muls)
memo = []
for arr in permutations(lines, n):
    num = 0
    for i in range(n):
        num = (num*10**len(str(arr[i]))+arr[i])%k

    if num%k:
        pass
    else:
        cnt+=1

print(arr)
total_sum = cnt
total = factorial(n)
gcd = math.gcd(total_sum,total)
print(f'{total_sum//gcd}/{total//gcd}')
