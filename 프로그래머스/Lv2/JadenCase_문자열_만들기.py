# https://school.programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    answer = ''
    prev = ' '
    s = s.lower()
    for c in s:
        if str.isalpha(c) and prev==' ':
            answer += c.upper()
        else:
            answer += c
        prev = c
    return answer

print(solution("3people unFollowed me"))
print(solution("for the last week"))