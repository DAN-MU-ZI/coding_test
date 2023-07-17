import sys
from collections import deque

n = int(sys.stdin.readline())
arr = deque(list(map(int, sys.stdin.readline().split())))
stk = []
res = []

cnt = 0
while arr:
    top = arr.popleft()
    find = False
    
    while stk:
        if stk[-1][1] < top:
            find = True
            stk.pop()
        else:
            break
    
    
    if find:
        if stk:
            res.append(stk[-1][0]+1)
        else:
            res.append(0)
    else:
        res.append(cnt)
    
    stk.append((cnt,top))
    cnt+=1

print(' '.join([str(x) for x in res]))
# print(*res)