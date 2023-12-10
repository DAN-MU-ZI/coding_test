# https://school.programmers.co.kr/learn/courses/30/lessons/118669

import heapq


def solution(n, paths, gates, summits):
    path_dict = {}
    for path in paths:
        i, j, w = path
        if i not in path_dict:
            path_dict[i] = {j: w}
        else:
            path_dict[i][j] = w

        if j not in path_dict:
            path_dict[j] = {i: w}
        else:
            path_dict[j][i] = w

    summits.sort()
    summits_set = set(summits)

    answer = [0, 10000001]
    intensities = [10000001] * (n + 1)

    queue = []
    for gate in gates:
        intensities[gate] = 0
        heapq.heappush(queue, (intensities[gate], gate))

    while queue:
        print(queue)
        w, node = heapq.heappop(queue)
        if node in summits_set or w > intensities[node]:
            continue

        for k, v in path_dict[node].items():
            intensity = max(w, v)
            if intensity < intensities[k]:
                intensities[k] = intensity
                heapq.heappush(queue, (intensity, k))

    for summit in summits:
        if intensities[summit] < answer[1]:
            answer = [summit, intensities[summit]]

    return answer


print(
    solution(
        7,
        [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]],
        [1],
        [2, 3, 4],
    )
)

print(
    solution(
        6,
        [
            [1, 2, 3],
            [2, 3, 5],
            [2, 4, 2],
            [2, 5, 4],
            [3, 4, 4],
            [4, 5, 3],
            [4, 6, 1],
            [5, 6, 1],
        ],
        [1, 3],
        [5],
    )
)
