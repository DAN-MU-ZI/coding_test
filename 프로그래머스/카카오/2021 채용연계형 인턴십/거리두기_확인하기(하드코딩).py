# https://school.programmers.co.kr/learn/courses/30/lessons/81302


def solution(places):
    answer = []
    participant = "P"
    emptyTable = "O"
    partition = "X"

    def checkOutOfRange(x, y):
        return not (0 > x or x > 4 or 0 > y or y > 4)

    def checkWarning(place, x, y):
        oneSteps = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for step in oneSteps:
            new_x = x + step[0]
            new_y = y + step[1]
            if checkOutOfRange(new_x, new_y):
                if place[new_y][new_x] == participant:
                    return True

        twoStepsContainsHorAndVer = [(2, 0), (-2, 0), (0, 2), (0, -2)]
        for step in twoStepsContainsHorAndVer:
            new_x = x + step[0]
            new_y = y + step[1]
            if checkOutOfRange(new_x, new_y):
                if (
                    place[new_y][new_x] == participant
                    and place[y + step[1] // 2][x + step[0] // 2] != partition
                ):
                    return True

        twoStepsContainsDiagonal = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for step in twoStepsContainsDiagonal:
            new_x = x + step[0]
            new_y = y + step[1]
            if checkOutOfRange(new_x, new_y):
                if place[new_y][new_x] == participant:
                    if (
                        place[y + step[1]][x] != partition
                        or place[y][x + step[0]] != partition
                    ):
                        return True

        return False

    for place in places:
        isWarning = False
        for y, row in enumerate(place):
            for x, value in enumerate(row):
                if value == participant:
                    isWarning = checkWarning(place, x, y)
                    if isWarning:
                        break

            if isWarning:
                break
        answer.append(int(not isWarning))

    return answer


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
