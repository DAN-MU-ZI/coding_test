# https://school.programmers.co.kr/learn/courses/30/lessons/92342

def solution(n, info):
    answer = []
    
    def generate_lists(k, current_list):
        if 0 == k:
            # 1의 개수가 k개가 된 리스트 출력
            lion = [0]*11
            stk = n
            for i in range(11):
                if current_list[i]:
                    if info[i] >= stk:
                        lion[i]=stk
                        stk = 0
                    else:
                        lion[i] = info[i]+1
                        stk -= info[i]+1
            return lion
        else:
            # n번째 원소를 1로 설정하는 경우
            res = []
            if k==1:
                res.append(generate_lists(k-1, current_list + [1]))
                # n번째 원소를 0으로 설정하는 경우
                res.append(generate_lists(k-1, current_list + [0]))
            else:
                [res.append(x) for x in generate_lists(k-1, current_list + [1])]
                [res.append(x) for x in generate_lists(k-1, current_list + [0])]
            return res

    
    apeach_score = 0
    for i in range(11):
        if info[i]:
            apeach_score += 10-i            
    
    score_li = generate_lists(11, [])
    
    scores = []
    records = []
    for s in score_li:
        score = apeach_score
        for i in range(11):
            if s[i] > info[i]:
                if info[i]:
                    score -= 2*(10-i)
                else:
                    score -= 10-i
        if score < 0:
            scores.append(score)
            records.append(s)
            
    if not scores:
        return [-1]
    
    highest = min(scores)
    records = [records[x] for x in range(len(scores)) if scores[x] == highest]
    for i in range(10,-1,-1):
        for r in records:
            if r[i]:
                return r
    return answer

print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(solution(9, [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]))
print(solution(10, [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]))
