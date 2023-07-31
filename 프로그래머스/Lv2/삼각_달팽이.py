def solution(n):
    answer = []
    tmp = []
    [tmp.append([0 for y in range(x+1)]) for x in range(n)]
    
    x,y = -1,0
    direct = {'down':(1,0), 'up':(-1,-1), 'right':(0,1)}
    decoder = ['down','right','up']
    
    cnt=1
    for i in range(n):
        d = direct[decoder[i%3]]
        for j in range(n-i):
            x+=d[0]
            y+=d[1]
            tmp[x][y] = cnt
            cnt+=1
    [answer.extend(x) for x in tmp]
    return answer