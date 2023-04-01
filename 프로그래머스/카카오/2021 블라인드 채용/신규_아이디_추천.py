# https://school.programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    answer = ''
    allow_li = []
    allow_li.extend(chr(x+97) for x in range(26))
    allow_li.extend(str(x) for x in range(10))
    allow_li.extend(['-','_','.'])
    # 1단계
    new_id = new_id.lower()
    # 2단계
    for c in new_id:
        if c in allow_li:
            answer+=c
    # 3단계
    answer = '.'.join([x for x in answer.split('.') if x != ''])
    
    # 4단계
    if len(answer) and answer[0] == '.':
        answer = answer[1:]
    if len(answer) and answer[-1] == '.':
        answer = answer[:-1]
    # 5단계
    if answer == '':
        answer = 'a'
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7단계
    if len(answer) <= 2:
        while len(answer) <3:
            answer+=answer[-1]
    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))