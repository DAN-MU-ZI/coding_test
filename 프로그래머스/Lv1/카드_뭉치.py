# https://school.programmers.co.kr/learn/courses/30/lessons/159994

def solution(cards1, cards2, goal):
    answer = 'Yes'
    for g in goal:
        if len(cards1) and cards1[0] == g:
            if len(cards1):
                cards1 = cards1[1:]
        elif len(cards2) and cards2[0] == g:
            if len(cards2):
                cards2 = cards2[1:]
        else:
            answer='No'
            return answer
    
    return answer

print(solution(["i", "drink", "water"], ["want", "to"], ["i", "want", "to", "drink", "water"]))
print(solution(["i", "water", "drink"], ["want", "to"], ["i", "want", "to", "drink", "water"]))