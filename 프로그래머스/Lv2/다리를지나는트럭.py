from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 1
    truck_weights = deque(truck_weights)
    stk = deque()
    total_weight = 0
    while truck_weights or stk:
        if truck_weights:
            truck = truck_weights.popleft()
        
            # 대기중인 트럭이 들어갈 수 없다면 기다리기
            if total_weight+truck > weight or len(stk)>=bridge_length:
                truck_weights.appendleft(truck)
            else:
                stk.append([truck,0])
                total_weight+=truck
                
            
        length = len(stk)
        idx = 0
        answer+=1
        # print(truck_weights, stk)
        while idx<length and stk:
            s = stk.popleft()
            # print(s)
            s[1]+=1
            if s[1]==bridge_length:
                total_weight-=s[0]
            else:
                stk.append(s)
            idx+=1
        
    return answer