# https://school.programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    answer = []
    p = len(stages)
    stage_fail = {}
    for i in range(1,N+1):
        n = stages.count(i)
        if n:
            stage_fail[i] = n/p
            p -= n
        else:
            stage_fail[i] = 0
        
    return sorted(stage_fail, key= lambda x:stage_fail[x], reverse=True)


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))