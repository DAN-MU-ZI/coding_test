# https://school.programmers.co.kr/learn/courses/30/lessons/72412

from bisect import bisect_left

def solution(info, query):
    answer = []

    di = {}
    langs = ['cpp', 'java', 'python', '-']
    ends = ['backend', 'frontend', '-']
    careers = ['junior','senior', '-']
    foods = ['chicken','pizza', '-']
    
    for l in langs:
        di[l] = {}
        for e in ends:
            di[l][e] = {}
            for c in careers:
                di[l][e][c] = {}
                for f in foods:
                    di[l][e][c][f] = []
                    
    for i in info:
        lang, end, care, food, score = i.split()
        score = int(score)
        
        for l in [lang, '-']:
            for e in [end, '-']:
                for c in [care, '-']:
                    for f in [food, '-']:
                        di[l][e][c][f].append(score)
    
    for l in langs:
        for e in ends:
            for c in careers:
                for f in foods:
                    di[l][e][c][f].sort()
                    
    for q in query:
        lang, end, care, food, score = q.replace('and','').split()
        score = int(score)
        li = di[lang][end][care][food]
        answer.append(len(li)-bisect_left(li, score))
    return answer

print(solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]))