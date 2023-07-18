# https://school.programmers.co.kr/learn/courses/30/lessons/42627

from heapq import *

def solution(jobs):
    answer = 0
    num = len(jobs)
    ready = []
    cur_time = 0
    cnt = 0
    while jobs or ready:
        tmp  = []
        while jobs:
            job = jobs.pop()
            if job[0] <= cur_time:
                heappush(ready, [job[1],job[0]])
            else:
                tmp.append(job)
        jobs = tmp

        if ready:
            run_time, request_at = heappop(ready)
            wait_to_end = cur_time-request_at+run_time
            answer+=wait_to_end
            cur_time+=run_time
            cnt+=1
        else:
            cur_time+=1

    # print(answer)
    return answer//num