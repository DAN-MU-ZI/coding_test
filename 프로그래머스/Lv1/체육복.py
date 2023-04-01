# https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    answer = 0
    cls = [0]+[1]*(n)+[0]
    for j in lost:
        cls[j]=0
    print(cls)
    for j in reserve:
        cls[j]+=1
    print(cls)
    for i in range(1, n+1):
        if cls[i]==0:
            if cls[i-1]==2:
                cls[i] += 1
                cls[i-1]-=1
            elif cls[i+1]==2:
                cls[i+1]-=1
                cls[i] += 1
    print(cls)
    return len(cls) - cls.count(0)


print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(5, [2, 4], [5, 3, 1]))
print(solution(3, [3], [1]))