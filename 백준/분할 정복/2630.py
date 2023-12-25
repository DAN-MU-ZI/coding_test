import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    global white, blue
    white, blue = 0, 0

    def checkArea(x1, y1, x2, y2):
        global white, blue
        if x1 == x2 == y1 == y2:
            if board[x1][y1]:
                blue += 1
            else:
                white += 1
            return

        total = sum([sum(line[y1:y2]) for line in board[x1:x2]])
        if total == 0:
            white += 1
            return
        elif total == (x2 - x1) ** 2:
            blue += 1
            return
        else:
            half_x = (x1 + x2) // 2
            half_y = (y1 + y2) // 2
            checkArea(x1, y1, half_x, half_y)
            checkArea(x1, half_y, half_x, y2)
            checkArea(half_x, y1, x2, half_y)
            checkArea(half_x, half_y, x2, y2)

    checkArea(0, 0, n, n)
    print(white)
    print(blue)


solution()
