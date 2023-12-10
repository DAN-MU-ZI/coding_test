from collections import deque


def solution(rc, operations):
    answer = [[]]
    r = len(rc)
    c = len(rc[0])

    left_col = deque([rc[i][0] for i in range(r)])
    right_col = deque([rc[i][c - 1] for i in range(r)])
    rows = deque([deque(rc[i][1 : c - 1]) for i in range(r)])

    def rotate():
        top_row = rows.popleft()
        tail_row = rows.pop()

        if len(top_row) and len(tail_row):
            top_right_end = top_row.pop()
            right_col.appendleft(top_right_end)
            bottom_right_end = right_col.pop()
            tail_row.append(bottom_right_end)
            botom_left_end = tail_row.popleft()
            left_col.append(botom_left_end)
            top_left_end = left_col.popleft()
            top_row.appendleft(top_left_end)
        else:
            bottom_right_end = right_col.pop()
            left_col.append(bottom_right_end)
            top_left_end = left_col.popleft()
            right_col.appendleft(top_left_end)

        rows.appendleft(top_row)
        rows.append(tail_row)

    def shift_row():
        left_col.appendleft(left_col.pop())
        right_col.appendleft(right_col.pop())
        rows.appendleft(rows.pop())

    for op in operations:
        if op == "Rotate":
            rotate()
        if op == "ShiftRow":
            shift_row()

    for i in range(r):
        rows[i].appendleft(left_col.popleft())
        rows[i].append(right_col.popleft())

    return [list(row) for row in list(rows)]


# print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate", "ShiftRow"]))
print(solution([[1, 2], [3, 4]], ["Rotate", "ShiftRow"]))
