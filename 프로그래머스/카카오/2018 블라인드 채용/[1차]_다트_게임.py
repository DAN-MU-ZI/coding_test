# https://school.programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    answer = 0
    score_di = {
        'S':1,
        'D':2,
        'T':3
    }
    opt = {
        '*':2,
        '#':-1
    }

    scores = []
    dartResult = list(dartResult)
    num = 0
    while len(dartResult):
        c = dartResult.pop(0)
        if str.isdigit(c):
            num*=10
            num+=int(c)
        elif c in score_di.keys():
            scores.append(num**score_di[c])
            num=0
            if len(scores) == 3:
                answer+=scores.pop(0)
        elif c == '*':
            for i, s in enumerate(scores):
                scores[i]=s*opt[c]
        elif c == '#':
            scores[-1]=scores[-1]*opt[c]
        print(scores, answer)
            
        
    for s in scores:
        answer+=s
            
    return answer

print(solution("1S2D*3T"))
print(solution("1D2S#10S"))
print(solution("1D2S0T"))
print(solution("1S*2T*3S"))
print(solution("1D#2S*3S"))
print(solution("1T2D3D#"))
print(solution("1D2S3T*"))