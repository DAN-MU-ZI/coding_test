import sys

sys.setrecursionlimit(100000)

def solution(n, m, x, y, r, c, k):    
    directions = ("d","l","r","u")
    delta = ((1,0),(0,-1),(0,1),(-1,0))

    def canReturn(x,y,d):
        if (d-(abs(r-x)+abs(c-y)))%2: return False
        else: return True
    def canArrive(x,y,d):
        if abs(r-x)+abs(c-y) > d: return False
        else: return True
    def isValid(x,y):
        if 1<=x and x<=n and 1<=y and y<=m: return True
        else: return False
    def isArrive(x,y):
        if x==r and y==c: return True
        else: return False

    def pathfinder(x,y,stk,state):
        if not isValid(x,y) or not canArrive(x,y,k-stk): return None
        if isArrive(x,y) and not canReturn(x,y,k-stk): return None
        if stk==k: return state
    
        res = None
        for i in range(4):
            dx,dy = delta[i]
            res = pathfinder(x+dx, y+dy, stk+1, state+directions[i])
            if res: return res
        return res

    def fillRemain(forward, backward, remain, max_dist):
        # 방향과 여유거리를 전달받고 완성해줌
        res = ''
        while remain:
            times = min(remain, max_dist)
            res = res + forward*times + backward*times
            remain = remain - times
        return res

    if not isValid(x,y) or not canArrive(x,y,k):
        return "impossible" # 현재 좌표가 유효하지 않은 경우
    if canReturn(x,y,k): pass # 도달하고 남은 거리가 짝수인 경우
    else: return "impossible"
    
    res = pathfinder(x,y,0,'')
    if res:
        return res
    else:
        return "impossible"

        
print(solution(3, 4, 2, 3, 3, 1, 5))
print()
print(solution(2, 2, 1, 1, 2, 2, 2))
print()
print(solution(3, 3, 1, 2, 3, 3, 4))
print()