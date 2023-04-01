# https://school.programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    answer = [0 for x in range(len(id_list))]
    rep_dict = {x:{} for x in id_list}
    for rep in report:
        reporter, reported = rep.split()
        #if reporter not in rep_dict[reporter].keys():
        rep_dict[reported][reporter]=1
    for key,v in rep_dict.items():
        if len(v)>=k:
            for reporter in v.keys():
                answer[id_list.index(reporter)]+=1
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))
print(solution(	["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))