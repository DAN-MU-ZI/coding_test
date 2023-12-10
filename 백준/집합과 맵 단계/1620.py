import sys

input = sys.stdin.readline


def solution():
    n, m = map(int, input().split())
    monster_num_dict = {}
    num_monster_dict = {}
    for i in range(1, n + 1):
        name = input().strip()
        monster_num_dict[name] = i
        num_monster_dict[i] = name

    for _ in range(m):
        search = input().strip()
        if search.isnumeric():
            print(num_monster_dict[int(search)])
        else:
            print(monster_num_dict[search])


solution()
