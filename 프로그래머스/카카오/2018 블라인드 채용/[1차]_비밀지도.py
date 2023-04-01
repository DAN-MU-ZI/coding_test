# https://school.programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer = []
    for a,b in zip(arr1, arr2):
        tmp = a|b
        res = ''
        print(tmp)
        while tmp:
            if tmp%2:
                res = '#' + res
            else:
                res = ' ' + res
            tmp = tmp>>1
        while not len(res)==n:
            res = ' ' + res
        answer.append(res)
    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))