import sys

input = sys.stdin.readline


def solution():
    global board_sum
    arr = [list(map(int, input().split())) for _ in range(9)]
    blanks = [(r, c) for r in range(9) for c in range(9) if arr[r][c] == 0]

    board_sum = 0
    for line in arr:
        board_sum += sum(line)

    def checkRow(n, r):
        for j in range(9):
            if arr[r][j] == n:
                return False

        return True

    def checkCol(n, c):
        for i in range(9):
            if arr[i][c] == n:
                return False
        return True

    def checkCell(n, r, c):
        cell_x = r // 3 * 3
        cell_y = c // 3 * 3
        for i in range(3):
            for j in range(3):
                if arr[cell_x + i][cell_y + j] == n:
                    return False
        return True

    def dfs(depth=0):
        global board_sum
        if depth == len(blanks):
            for line in arr:
                for e in line:
                    print(e, end=" ")
                print()
            return

        r, c = blanks[depth]

        for n in range(1, 10):
            if checkRow(n, r) and checkCol(n, c) and checkCell(n, r, c):
                arr[r][c] = n
                board_sum += n
                dfs(depth + 1)
                if board_sum == 405:
                    return
                arr[r][c] = 0
                board_sum -= n

    dfs()


solution()
