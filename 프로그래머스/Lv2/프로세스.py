from collections import deque

def solution(priorities, location):
    answer = 0
    
    cnt = 0
    priorities = deque([(i,p) for i,p in enumerate(priorities)])
    while priorities:
        
        p1 = priorities.popleft()
        is_high = True
        for p2 in priorities:
            if p2[1] > p1[1]:
                priorities.append(p1)
                is_high = False
                break
        if is_high:
            cnt+=1
            if p1[0]==location:
                return cnt
        
    return answer