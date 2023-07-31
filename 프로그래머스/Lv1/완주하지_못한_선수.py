def solution(participant, completion):
    answer = ''
    part_di = {}
    for p in participant:
        if p not in part_di.keys():
            part_di[p]=1
        else:
            part_di[p]+=1
    for c in completion:
        if part_di[c]==1:
            del part_di[c]
        else:
            part_di[c]-=1
    
    return list(part_di.keys())[0]