# https://school.programmers.co.kr/learn/courses/30/lessons/160586

def solution(keymap, targets):
    answer = []
    # 최소값 찾기
    min_dict = {chr(key+65):101 for key in range(26)}
    for key in keymap:
        for i, k in enumerate(key):
            min_dict[k] = min([min_dict[k], i+1])
    
    for target in targets:
        total = 0
        for t in target:
            if min_dict[t]==101:
                total=-1
                break
            total+=min_dict[t]
        answer.append(total)
    return answer

print(solution(["ABACD", "BCEFD"], ["ABCD", "AABB"]))
print(solution(["AA"], ["B"]))
print(solution(["AGZ", "BSSS"], ["ASA", "BGZ"]))