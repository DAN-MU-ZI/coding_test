# https://school.programmers.co.kr/learn/courses/30/lessons/118667#

from collections import deque
def solution(queue1, queue2):
    sq1 = sum(queue1)
    sq2 = sum(queue2)
    mean = (sq1+sq2)/2
    
    if mean - int(mean) > 0:
        return -1
    
    limit = len(queue1)*3
    cnt = 0
    q1 = deque(queue1)
    q2 = deque(queue2)
    for cnt in range(limit):
        if sq1 > sq2:
            if q1:
                tmp = q1.popleft()
                q2.append(tmp)
                sq1 -= tmp
                sq2 += tmp
            else:
                return -1
        elif sq1 < sq2:
            if q2:
                tmp = q2.popleft()
                q1.append(tmp)
                sq1 += tmp
                sq2 -= tmp
            else:
                return -1
        else:
            return cnt
    return -1
        


print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
print(solution([1, 1], [1, 5]))
print(solution([1, 1, 1, 1, 1], [1, 1, 1, 9, 1]))
print(solution([1, 4], [4, 8]))