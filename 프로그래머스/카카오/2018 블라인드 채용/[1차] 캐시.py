# https://school.programmers.co.kr/learn/courses/30/lessons/17680
from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cities = deque(cities)
    stk = deque()
    spare = deque()
    
    while cities:
        city = cities.popleft().upper()
        if cacheSize:
            #print(stk)
            if stk:
                while len(spare)<cacheSize:
                    s = stk.pop()
                    #print('compare {} == {}'.format(city, s))
                    if city == s: # hit
                        while spare:
                            stk.append(spare.pop())
                        stk.append(city)
                        answer+=1
                        break
                    else:
                        #print(spare, cacheSize-1)
                        if len(spare) == cacheSize-1: # spare is full = miss
                            #print('miss')
                            #print('spare is full')
                            while spare:
                                stk.append(spare.pop())
                            stk.append(city)
                            answer+=5
                            break
                        elif len(spare) < cacheSize-1:
                            #print('spare is not full')
                            #print(stk, spare, s)
                            if stk:
                                #print('stk is not empty')
                                #print('add spare s, city')
                                spare.append(s)
                                #spare.append(city)
                                #print(spare)
                            else:
                                #print('stk is empty')
                                #print('add stk spare, city ')
                                stk.append(s)
                                while spare:
                                    stk.append(spare.pop())
                                stk.append(city)
                                #print('miss')
                                answer+=5
                                break
            else:
                #print('miss')
                stk.append(city)
                answer+=5
        else: # miss
            #print('miss')
            stk.append(city)
            answer+=5
        #print('check stk')
        #print(stk, answer)
        #print()
        
    return answer