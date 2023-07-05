import sys
n, k = map(int, sys.stdin.readline().split())

stk = 0
cnt = 0

while format(n, 'b').count('1') > k:
    if n%2:
        stk+=2**cnt
        n+=1
    cnt+=1
    n = n>>1
print(stk)