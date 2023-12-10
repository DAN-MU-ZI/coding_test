import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    nodes = {}
    steps = list(map(int, input().split()))
    for i, step in zip(range(1, n + 1), steps):
        nodes[i] = {"next": i + 1, "prev": i - 1, "step": step}
    nodes[1]["prev"] = n
    nodes[n]["next"] = 1

    cur = 1
    answer = []
    for _ in range(n):
        answer.append(str(cur))

        node = nodes[cur]
        next = node["next"]
        prev = node["prev"]
        step = node["step"]

        nodes[next]["prev"] = prev
        nodes[prev]["next"] = next

        if step > 0:
            for _ in range(step):
                cur = nodes[cur]["next"]
        else:
            for _ in range(-step):
                cur = nodes[cur]["prev"]

    print(" ".join(answer))


solution()
