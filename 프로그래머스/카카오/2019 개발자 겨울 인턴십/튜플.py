# https://school.programmers.co.kr/learn/courses/30/lessons/64065


def solution(s):
    answer = []
    temp = s[2:-2].split("},{")
    temp.sort(key=lambda x: len(x))
    for num_set in [x.split(",") for x in temp]:
        for num in num_set:
            num = int(num)
            if num not in answer:
                answer.append(num)
    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
