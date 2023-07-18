# https://school.programmers.co.kr/learn/courses/30/lessons/42626

from collections import deque
def solution(scoville, K):
    answer = 0
    scoville = deque(scoville)
    
    while scoville:
        s = scoville.popleft()
        if s>=K:
            break
        else:
            if scoville:
                s2 = scoville.popleft()
            else:
                answer = -1
                break
        scoville.appendleft(s+s2*2)
        answer+=1
        
        
    return answer