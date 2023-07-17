import sys
sys.setrecursionlimit(100000)

t = int(sys.stdin.readline())
for i in range(t):
    m,n,k = map(int, sys.stdin.readline().split())
    arr = [[0 for x in range(m)] for y in range(n)]
    log = [[0 for x in range(m)] for y in range(n)]
    for i in range(k):
        xpos,ypos = map(int, sys.stdin.readline().split())
        arr[ypos][xpos] = 1

    def isOut(x,y):
        if x>=0 and x<m and y>=0 and y<n:
            return False
        else:
            return True

    stk = 0
    def func(x,y,prev,path):
        global stk
        if isOut(x,y):
            return path
        if path[y][x]:
            if not prev:
                stk+=1
            path[y][x]=0
            prev = True
            path = func(x-1,y,prev,path)
            path = func(x+1,y,prev,path)
            path = func(x,y-1,prev,path)
            path = func(x,y+1,prev,path)
        
        return path

    for y in range(n):
        for x in range(m):
            arr = func(x,y,False,arr)
    print(stk)