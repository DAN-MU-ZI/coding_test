# https://school.programmers.co.kr/learn/courses/30/lessons/155652

def solution(s, skip, index):
    li = list(s)
    for idx, spell in enumerate(li):
        ch_cnt = index
        num = ord(spell) # 아스키 코드 숫자
        x = 1 # 추가할 숫자
        cnt = 0 # 넘어간 횟수
        while(True):
            if (num+x) > 122:
                num -= 26
                if chr(num+x) not in skip:
                    x += 1
                    ch_cnt -= 1
                else:
                    x += 1
                    cnt += 1
            else:
                if chr(num+x) not in skip:
                    x += 1
                    ch_cnt -= 1
                else:
                    x += 1
                    cnt += 1
            if ch_cnt == 0:
                li[idx] = chr(num+cnt+index)
                break
    answer = ''
    for s in li:
        answer += s
    return answer.strip()

print(solution("aukks", "wbqd", 5))