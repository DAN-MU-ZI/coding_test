from collections import deque


def solution(n, k, cmd):
    cells = [1 for _ in range(n)]
    delete_stack = deque()

    link_list = dict()
    for i in range(n):
        prev = i - 1
        next = i + 1
        link_list[i] = {"prev": prev, "next": next}
    link_list[0]["prev"] = -1
    link_list[n - 1]["next"] = -1

    global s
    s = k

    def up(x):
        global s
        for i in range(x):
            s = link_list[s]["prev"]

    def down(x):
        global s
        for i in range(x):
            s = link_list[s]["next"]

    def remove():
        global s
        delete_stack.append(s)
        cells[s] = 0
        prev = link_list[s]["prev"]
        next = link_list[s]["next"]
        if prev != -1:
            link_list[prev]["next"] = next
        if next != -1:
            link_list[next]["prev"] = prev

        if next != -1:
            s = next
        else:
            s = prev

    def undo():
        global s
        undo_num = delete_stack.pop()
        cells[undo_num] = 1
        prev = link_list[undo_num]["prev"]
        next = link_list[undo_num]["next"]

        if prev != -1:
            link_list[prev]["next"] = undo_num
        if next != -1:
            link_list[next]["prev"] = undo_num

    for command in cmd:
        argv = command.split()
        if argv[0] == "U":
            up(int(argv[1]))
        if argv[0] == "D":
            down(int(argv[1]))
        if argv[0] == "C":
            remove()
        if argv[0] == "Z":
            undo()

    return "".join(["O" if x else "X" for x in cells])


print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))

print(solution(8, 2, ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
