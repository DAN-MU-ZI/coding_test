from collections import deque

def solution(progresses, speeds):
    answer = []
    predict = deque()
    
    for p, s in zip(progresses, speeds):
        remain = 100-p
        if remain%s:
            predict.append(remain//s+1)
        else:
            predict.append(remain//s)
            
    while predict:
        cnt = 1

        p1 = predict.popleft()
        while predict:
            p2 = predict.popleft()
            if p1<p2:
                predict.appendleft(p2)
                break
            else:
                cnt+=1
        answer.append(cnt)
        
    return answer