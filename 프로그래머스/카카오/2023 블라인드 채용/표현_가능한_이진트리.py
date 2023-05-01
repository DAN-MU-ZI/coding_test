# https://school.programmers.co.kr/learn/courses/30/lessons/150367

import math

def solution(numbers):
    answer = []
    
    def search(bin, depth, start, end):
        mid = (start+end)//2
        right = int((mid+end)/2)
        left = int((start+mid)//2)
        if bin[mid]:
            state = 1
        else:
            if bin[left] or bin[right]:
                state = 0
            else:
                state = 1
        if state:
            if depth > 2:
                state = search(bin, depth-1, start, mid) and search(bin, depth-1, mid, end)
        return state
                
    for num in numbers:
        bin = ''
        while num:
            bin=str(num%2)+bin
            num = num >> 1
        if 2**int(math.log2(len(bin)))-1 == len(bin):
            pass
        else:
            while 2**(int(math.log2(len(bin)))+1)-1 > len(bin):
                bin = '0'+bin
        bin = [int(x) for x in bin]
        answer.append(search(bin, int(math.log2(len(bin)+1)), 0, len(bin)))
    return answer

print(solution([7, 42, 5])) # [1, 1, 0]
print(solution([63, 111, 95])) # [1, 1, 0]
print(solution([1])) # [1]
print(solution([156]))