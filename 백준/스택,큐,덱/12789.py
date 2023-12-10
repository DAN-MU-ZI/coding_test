import sys
from collections import deque

input = sys.stdin.readline


def solution():
    n = int(input())
    queue = deque(map(int, input().split()))
    stk = deque()

    cur = 1
    answer = "Nice"
    while queue or stk:
        q, s = None, None
        if queue:  # 큐가 있으면
            q = queue.popleft()  # 큐에서 뽑고
            if cur == q:  # 찾는 값이 같다면 통과
                cur += 1
                continue
            else:  # 찾는 값이 아니라면
                if stk:  # 스택이 있을때
                    s = stk.pop()  # 스택에서 꺼내서
                    if cur == s:  # 같다면 큐는 복원
                        cur += 1
                        queue.appendleft(q)
                        continue
                    else:  # 아니라면 스택에 큐를 추가
                        stk.append(s)
                        stk.append(q)
                else:
                    stk.append(q)
        else:  # 큐가 없다면
            s = stk.pop()  # 스택에서 값을 가져와서
            if cur == s:
                cur += 1
                continue
            else:
                answer = "Sad"
                break

    print(answer)


solution()
