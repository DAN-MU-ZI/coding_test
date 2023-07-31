from collections import deque

def solution(s):
    answer = True
    
    s = deque(s)
    
    if s[0]==")" or s[-1]=="(":
        return False
    
    stk = deque()
    # 기준값이 ) 이면
    # 넣다가
    # 반대값 ( 이 나오면 넣은거 꺼내서 확인
    while s:
        t1 = s.pop()
        if t1==')':
            stk.append(t1)
        else:
            if stk:
                t2 = stk.pop()
                if t2==')':
                    pass
                else:
                    return False
            else:
                 return False
    if stk:
        return False

    return True