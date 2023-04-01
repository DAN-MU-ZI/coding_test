# https://school.programmers.co.kr/learn/courses/30/lessons/142086

def solution(s):
    answer = []
    alpha_dict = {chr(x+97):-1 for x in range(26)}
    
    for i, c in enumerate(s):
        if alpha_dict[c]==-1:
            answer.append(alpha_dict[c])
        else:
            answer.append(i-alpha_dict[c])
        alpha_dict[c]=i
    return answer

print(solution("banana"))
print(solution("foobar"))