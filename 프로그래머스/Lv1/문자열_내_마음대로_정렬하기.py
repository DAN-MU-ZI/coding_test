# https://school.programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    answer = []
    
    for c in [chr(x) for x in range(97, 97+26)]:
        tmp = [s for s in strings if s[n]==c]
        answer.extend(sorted(tmp))
    return answer

print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))