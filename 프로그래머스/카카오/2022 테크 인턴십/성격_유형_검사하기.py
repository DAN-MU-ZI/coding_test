# https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    answer = ''
    mbti_dict = {
        "R":0,
        "T":0,
        "C":0,
        "F":0,
        "J":0,
        "M":0,
        "A":0,
        "N":0
    }
    stat_dict = {
        0:'RT',
        1:'CF',
        2:'JM',
        3:'AN'
    }
    for m, c in zip(survey, choices):
        values = [3,2,1,0,1,2,3]
        keys = [m[0],m[0],m[0],None,m[1],m[1],m[1]]
        if keys[c-1]:
            mbti_dict[keys[c-1]]+=values[c-1]
    for i in range(4):
        stat  = stat_dict[i]
        if mbti_dict[stat[0]] == mbti_dict[stat[1]]:
            answer+=stat[0]
        elif mbti_dict[stat[0]] > mbti_dict[stat[1]]:
            answer+=stat[0]
        elif mbti_dict[stat[0]] < mbti_dict[stat[1]]:
            answer+=stat[1]
        
    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))
print(solution(	["TR", "RT", "TR"], [7, 1, 3]))