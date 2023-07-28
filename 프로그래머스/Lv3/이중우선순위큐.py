# https://school.programmers.co.kr/learn/courses/30/lessons/42628

from heapq import *

def solution(operations):
    answer = []
    
    for op in operations:
        print(answer)
        num = int(op.split()[-1])
        
        if op.startswith('I'):
            # input
            heappush(answer, num)
        else:
            if answer:
                if num < 0:
                    # print('remove min')
                    heappop(answer)
                else:
                    # print('remove max')
                    answer = answer[:-1]

                
    # print(answer)
    if answer:
        min_heap = min(answer)
    else:
        min_heap = 0
    if answer:
        max_heap = max(answer)
    else:
        max_heap = min_heap
    
    return [max_heap, min_heap]