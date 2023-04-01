# https://school.programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    answer = 0
    stk = []
    for m in moves:
        for i, r in enumerate(board):
            if board[i][m-1]:
                stk.append(board[i][m-1])
                board[i][m-1] = 0
                break
    
    i = 0
    while i<len(stk):
        if stk[i]==stk[i+1]:
            answer+=2
            stk = stk[:i]+stk[i+2:]
            i = 0
        else:
            i+=1
        if i+1 >= len(stk):
            break
        
            
    return answer

print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]))