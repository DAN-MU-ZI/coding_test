# https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    answer = []
    
    prev = -1
    for i in arr:
        if prev!=i:
            answer.append(i)
            prev = i
    
    return answer

print(solution([1, 1, 3, 3, 0, 1, 1]))
print(solution([4, 4, 4, 3, 3]))