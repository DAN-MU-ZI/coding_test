def solution(n):
    answer = []

    def move(N, start, to):
        answer.append([start,to])

    def hanoi(N, start, to, via):
        if N == 1:
            move(1, start, to)
        else:
            hanoi(N-1, start, via, to)
            move(N, start, to)
            hanoi(N-1, via, to, start)
            
    hanoi(2, 1, 3, 2)
    
    return answer