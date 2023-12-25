# 23 ~ 36줄의 if문 순서에 따라 정답 유무가 달라진다
# 같은 scope에서 유사한 문맥의 if문을 구분하는 것은 의도를 명시하지 않으면
# 가독성을 해친다고 생각한다.
# 하지만 안정성이 높은 코드에 비해 33%의 효율을 보여주기 때문에
# 주석과 같은 부가적인 설명으로 부족한 안정성을 보완한다면
# 채택할만하다고 본다.
import sys
from collections import deque

input = sys.stdin.readline


def solution():
    n, k = map(int, input().split())
    INF = 100001
    visited = [-1] * INF

    def is_out_of_range(p):
        return p < 0 or INF <= p

    stk = deque([n])
    visited[n] = 0
    while stk:
        x = stk.popleft()
        if x == k:
            break

        nx = x - 1
        if not is_out_of_range(nx) and visited[nx] == -1:
            visited[nx] = visited[x] + 1
            stk.append(nx)

        nx = x * 2
        if not is_out_of_range(nx) and visited[nx] == -1:
            visited[nx] = visited[x]
            stk.append(nx)

        nx = x + 1
        if not is_out_of_range(nx) and visited[nx] == -1:
            visited[nx] = visited[x] + 1
            stk.append(nx)

    print(visited[k])


solution()
