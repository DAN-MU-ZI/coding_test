# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    answer = 0
    w = 0
    h = 0
    for x,y in sizes:
        if w>=x and h>=y:
            pass
        elif w>=y and h>=x:
            pass
        elif w>=h:
            if x>=y:
                if w<x:
                    w=x
                if h<y:
                    h=y
            else:
                if w<y:
                    w=y
                if h<x:
                    h=x
    
    return w*h

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))