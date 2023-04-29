# https://school.programmers.co.kr/learn/courses/30/lessons/42860#

def solution(name):
    answers = []
    
    # 이동, 변경
    def forward(answer, cur_idx, table, name, process):
        stk = 0
        while sum(process):
            if name[cur_idx]!="A":
                answer += min(abs(ord(name[cur_idx])-ord('A')), 26-abs(ord('A')-ord(name[cur_idx])))
                table[cur_idx] = name[cur_idx]
                answer+=stk
                stk=0
            process[cur_idx] = 0
            cur_idx = (cur_idx + 1)%len(name)
            stk+=1
        return answer

    def backward(answer, cur_idx, table, name, process):
        stk=0
        while sum(process):
            if name[cur_idx]!="A":
                answer += min(abs(ord(name[cur_idx])-ord('A')), 26-abs(ord('A')-ord(name[cur_idx])))
                table[cur_idx] = name[cur_idx]
                answer+=stk
                stk = 0
            process[cur_idx] = 0
            cur_idx = (cur_idx - 1)%len(name)
            stk+=1
        return answer

    for j in range(len(name)):
        answer = 0
        cur_idx = 0
        table = list('A'*len(name))
        name = list(name)
        process = [1]*len(name)
    
        backend = abs(len(name)-j)
        frontend = j
        answer+=min(frontend, backend)
        if backend > frontend:
            cur_idx = frontend
        else:
            cur_idx = len(name)-backend
        if name[cur_idx]!="A":
            answers.append(forward(answer, cur_idx, table.copy(), name.copy(), process.copy()))
            answers.append(backward(answer, cur_idx, table.copy(), name.copy(), process.copy()))
    if answers:
        return min(answers)
    else:
        return 0

print(solution('JEROEN'))
print(solution('JAN'))
print(solution("AAAAAAAA"))
print(solution("AAAAABBAAAAAAABAAA"))
print(solution("BBBBAAAABA"))