# https://school.programmers.co.kr/learn/courses/30/lessons/42890

from itertools import combinations

def solution(relation):
    col_len = len(relation[0])
    def generate_lists(k, current_list):
        if 0 == k:
            # 1의 개수가 k개가 된 리스트 출력
            return current_list
        else:
            # n번째 원소를 1로 설정하는 경우
            res = []
            if k==1:
                res.append(generate_lists(k-1, current_list))
                res.append(generate_lists(k-1, current_list + [col_len-k]))
                # n번째 원소를 0으로 설정하는 경우
            else:
                [res.append(x) for x in generate_lists(k-1, current_list)]
                [res.append(x) for x in generate_lists(k-1, current_list + [col_len-k])]
            return res
    
    col_len = len(relation[0])
    table = {x:[] for x in range(col_len)}
    
    for r in relation:
        for i, v in enumerate(r):
            table[i].append(v)
    
    cases = generate_lists(col_len, [])
    cases = cases[1:]
    
    unique_cases = []
    for case in cases:
        lines = list(zip(*[table[x] for x in case]))
        uniq = set(lines)
        if len(lines) == len(uniq):
            unique_cases.append(tuple(case))
    
    answer = set(unique_cases)
    for x, y in combinations(unique_cases,2):
        if len(set(x)) == len(set(x)&set(y)):
            answer.discard(y)
    return len(answer)

print(solution([["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"], ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]))