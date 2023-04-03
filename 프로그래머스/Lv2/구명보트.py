# https://school.programmers.co.kr/learn/courses/30/lessons/42885

from collections import deque
def solution(people, limit):
    answer = 0
    people = deque(sorted(people))
    
    while len(people)>1:
        a = people.pop()
        b = people.popleft()
        if a+b <= limit:
            pass
        else:
            people.appendleft(b)
        answer+=1
        
    if people:
        answer+=1
    return answer

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))