# https://school.programmers.co.kr/learn/courses/30/lessons/150369

def solution(cap, n, deliveries, pickups):
    answer = 0

    d = cap
    p = 0

    while deliveries or pickups:
        dl = 0
        pl = 0
        while d>=0 and deliveries:
            deli = deliveries.pop()
            if d==cap and deli:
                dl = len(deliveries)+1
            d-=deli
            if d<0: # 깔끔히 배달
                deliveries.append(-d)
                break
            elif len(deliveries)==0: # 남았지만 배달끝남
                break
        while p<=cap and pickups: # 아직걷을게 있고 걷을 수 있으면
            pick = pickups.pop()
            if p==0 and pick: # 
                pl = len(pickups)+1
            p+=pick
            if p>cap: # 전부 수거
                pickups.append(p-cap)
                break
            elif len(pickups)==0:
                break
        d=cap
        p=0
        answer+=2*max(dl,pl)
    return answer
print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
print(solution(2, 7, [1, 0, 2, 0, 1, 0, 2], [0, 2, 0, 1, 0, 2, 0]))