import heapq


def solution(alp, cop, problems):
    SIZE = 150
    INF = SIZE + 1
    arr = [[INF for _ in range(SIZE + 1)] for _ in range(SIZE + 1)]

    for i in range(alp + 1):
        for j in range(cop + 1):
            arr[i][j] = 0

    target_alp = 0
    target_cop = 0
    for problem in problems:
        alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
        target_alp = max(target_alp, alp_req)
        target_cop = max(target_cop, cop_req)
    alp = min(alp, target_alp)
    cop = min(cop, target_cop)

    queue = []
    heapq.heappush(queue, (alp, cop))

    while queue:
        na, nc = heapq.heappop(queue)
        if SIZE > na >= target_alp and SIZE > nc >= target_cop:
            continue

        # learn algo
        if na + 1 <= target_alp:
            if arr[na + 1][nc] > arr[na][nc] + 1:
                arr[na + 1][nc] = arr[na][nc] + 1
                heapq.heappush(queue, (na + 1, nc))

        # learn coding
        if nc + 1 <= target_cop:
            if arr[na][nc + 1] > arr[na][nc] + 1:
                arr[na][nc + 1] = arr[na][nc] + 1
                heapq.heappush(queue, (na, nc + 1))

        # solve problem
        for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
            if alp_req <= na and cop_req <= nc:
                x = min(na + alp_rwd, target_alp)
                y = min(nc + cop_rwd, target_cop)
                if arr[x][y] > arr[na][nc] + cost:
                    arr[x][y] = arr[na][nc] + cost
                    heapq.heappush(queue, (x, y))

    return arr[target_alp][target_cop]


print(solution(10, 10, [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]))
print(solution(1, 1, [[0, 2, 1, 1, 100]]))
