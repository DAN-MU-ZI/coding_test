from itertools import combinations

dice = [
    [1, 2, 3, 4, 5, 6],
    [3, 3, 3, 6, 6, 6],
    [5, 5, 5, 6, 6, 6],
    [1, 1, 1, 1, 1, 1],
    [1, 2, 3, 4, 5, 6],
    [3, 3, 3, 6, 6, 6],
    [5, 5, 5, 6, 6, 6],
    [1, 1, 1, 1, 1, 1],
    [5, 5, 5, 6, 6, 6],
    [4, 4, 4, 4, 4, 4],
]

d1 = sorted(dice[0])
d2 = sorted(dice[1])
tmp = []
for i in range(len(d1)):
    tmp.append(len([x for x in d2 if x < i]))
print(tmp)
arr_set = set(range(len(dice)))
print(arr_set)
comb_di = {}


# def calculate_number_of_cases(ds):
#     arr = ds.pop()
#     for d in ds:
#         res = []
#         temp = arr
#         for i in d:
#             for j in temp:
#                 res.append(i + j)
#         arr = res
#     return sorted(arr)


# for c in combinations(arr_set, len(arr_set) // 2):
#     c = sorted(c)
#     calculate_number_of_cases([dice[x] for x in c])
