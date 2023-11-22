# https://school.programmers.co.kr/learn/courses/30/lessons/150366#


def solution(commands):
    answer = []
    SIZE = 50
    EMPTY = "EMPTY"
    cells = [[EMPTY for y in range(SIZE)] for x in range(SIZE)]
    merged = [[(x, y) for y in range(SIZE)] for x in range(SIZE)]

    def clearCell(x, y):
        cells[x][y] = EMPTY

    def updateCell(r, c, value):
        x, y = merged[r][c]
        cells[x][y] = value

    def updateValue(value1, value2):
        for x, row in enumerate(cells):
            for y, value in enumerate(row):
                if value == value1:
                    cells[x][y] = value2

    def merge(r1, c1, r2, c2):
        x1, y1 = merged[r1][c1]
        x2, y2 = merged[r2][c2]

        if cells[x1][y1] == EMPTY:
            cells[x1][y1] = cells[x2][y2]
            clearCell(x2, y2)

        for x, row in enumerate(merged):
            for y, value in enumerate(row):
                if value == (x2, y2):
                    merged[x][y] = (x1, y1)

    def unmerge(r, c):
        x1, y1 = merged[r][c]
        temp = cells[x1][y1]
        for x, row in enumerate(merged):
            for y, value in enumerate(row):
                if value == (x1, y1):
                    merged[x][y] = (x, y)
                    clearCell(x, y)
        cells[r][c] = temp

    def printCell(r, c):
        x, y = merged[r][c]
        return cells[x][y]

    for commandLine in commands:
        command = commandLine.split()
        if command[0] == "UPDATE":
            if len(command) == 3:
                updateValue(command[1], command[2])
            if len(command) == 4:
                updateCell(int(command[1]) - 1, int(command[2]) - 1, command[3])
        if command[0] == "MERGE":
            merge(
                int(command[1]) - 1,
                int(command[2]) - 1,
                int(command[3]) - 1,
                int(command[4]) - 1,
            )
        if command[0] == "UNMERGE":
            unmerge(int(command[1]) - 1, int(command[2]) - 1)
        if command[0] == "PRINT":
            answer.append(printCell(int(command[1]) - 1, int(command[2]) - 1))

    return answer
