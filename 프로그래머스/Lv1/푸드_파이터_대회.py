# https://school.programmers.co.kr/learn/courses/30/lessons/134240

def solution(food):
    answer = '0' # 0번째를 미리 대입
    food = food[1:] # 0번째 인덱스를 제외한다 = 0번째는 물이므로 항상 중간
    # 배열이 칼로리 오름차순 = 문자열은 바깥에서 안쪽으로 칼로리가 높아지는 구조
    # 오름차순 배열을 역순으로 대입 = reversed(list(enumerate()))
    for i, f in reversed(list(enumerate(food))): 
        for j in range(f//2): # 차피 짝수면 할거라서 2로 나눈 몫만큼 반복하기
            answer = str(i+1)+answer+str(i+1) # 양쪽에 해당 음식을 연결
    
    return answer

print(solution([1, 3, 4, 6]))
print(solution([1, 7, 1, 2]))
