# https://school.programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = ''
    left_di = [1,4,7]
    right_di = [3,6,9]
    l = '*'
    r = '#'
    dist_di = {
        '*':{
            2:4,
            5:3,
            8:2,
            0:1
        },
        '#':{
            2:4,
            5:3,
            8:2,
            0:1
        },
        0:{
            2:3,
            5:2,
            8:1,
            0:0
        }, 
        1:{
            2:1,
            5:2,
            8:3,
            0:4
        },
        2:{
            2:0,
            5:1,
            8:2,
            0:3
        },
        3:{
            2:1,
            5:2,
            8:3,
            0:4
        },
        4:{
            2:2,
            5:1,
            8:2,
            0:3
        },
        5:{
            2:1,
            5:0,
            8:1,
            0:2
        },
        6:{
            2:2,
            5:1,
            8:2,
            0:3
        },
        7:{
            2:3,
            5:2,
            8:1,
            0:2
        },
        8:{
            2:2,
            5:1,
            8:0,
            0:1
        },        
        9:{
            2:3,
            5:2,
            8:1,
            0:2
        }
    }
    for n in numbers:
        if n in left_di:
            l = n
            answer+='L'
        elif n in right_di:
            r = n
            answer+='R'
        else:
            if dist_di[l][n] < dist_di[r][n]:
                l = n
                answer+='L'
            elif dist_di[r][n] < dist_di[l][n]:
                r = n
                answer+='R'
            else:
                if hand == 'right':
                    r = n
                    answer+='R'
                else:
                    l = n
                    answer+='L'
                
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))