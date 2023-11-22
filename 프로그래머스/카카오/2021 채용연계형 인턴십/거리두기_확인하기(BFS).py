# https://school.programmers.co.kr/learn/courses/30/lessons/81302


def solution(places):
    answer = []

    for place in places:
        answer.append(checkPlace(place))

    return answer


def checkPlace(place):
    for y, row in enumerate(place):
        for x, value in enumerate(row):
            if value == "P":
                if checkWarning(place, x, y):
                    return 0
    return 1


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def isOutOfRange(x, y):
    return 0 > x or x > 4 or 0 > y or y > 4


def checkWarning(place, x, y):
    visited = [[False for _ in range(5)] for _ in range(5)]
    queue = []
    queue.append((x, y, 0))
    visited[y][x] = True

    while queue:
        x, y, distance = queue.pop(0)

        if distance <= 1:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                nd = distance + 1
                if not isOutOfRange(nx, ny) and not visited[ny][nx]:
                    if place[ny][nx] == "P":
                        return True
                    if place[ny][nx] == "O":
                        queue.append((nx, ny, nd))
                        visited[y][x] = True

    return False


print(
    solution(
        [
            ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
            ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
            ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
            ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
            ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
        ]
    )
)
