
checkBoard = [
    [set([1]),set([4,1]),set([])],
    [set([1,2,3,7]),set([0,1,2,3,4,5,6,7,8,9]),set([5,6])],
    [set([1,7]),set([0,1,7]),set([])],
    [set([1,3,4,5,7,9,]),set([0,1,2,3,4,5,6,6,7,8,9]),set([2])],
    [set([1,4,7]),set([1,4,7]),set([])]
]

import sys
n = int(sys.stdin.readline())
board = []
res = [set(range(0,10)) for x in range(n)]
is_false = False
for i in range(5):
    line = sys.stdin.readline().strip()
    spl = 0
    for j in range(n):
        for k in range(3):
            if line[j*3+k+spl]=='#':
                res[j] = res[j].difference(checkBoard[i][k])
                if res[j]:
                    pass
                else:
                    is_false = True
                    break
        spl += 1
        if is_false:
            break
    if is_false:
        break

# print(res)
if is_false:
    print(-1)
else:
    answer = 0
    stk = 1
    prev=1
    first=1
    for i in range(n):
        answer*=10
        answer+=sum(res[i])/len(res[i])
        prev=len(res[i])
        stk*=prev
    print(answer)