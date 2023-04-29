# https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []
    ptn1 = [1,2,3,4,5]
    ptn2 = [2,1,2,3,2,4,2,5]
    ptn3 = [3,3,1,1,2,2,4,4,5,5]
    
    cnt = [0]*3
    for i, a in enumerate(answers):
        if a == ptn1[i%len(ptn1)]:
            cnt[0]+=1
        if a == ptn2[i%len(ptn2)]:
            cnt[1]+=1
        if a == ptn3[i%len(ptn3)]:
            cnt[2]+=1
    
    m = max(cnt)
    for i, c in enumerate(cnt):
        if c==m:
            answer.append(i+1)
    return answer

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))