# https://school.programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    words = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    for i in range(len(words)):
        s = s.replace(words[i],str(i))
    return int(s)

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution(	"2three45sixseven"))
print(solution("123"))