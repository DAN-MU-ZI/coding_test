import sys
from collections import deque

input = sys.stdin.readline


def solution():
    global k, answer, save_count
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    answer = -1
    save_count = 0

    def merge_sort(p, r):  # arr[p..r]을 오름차순 정렬한다.
        if p < r:
            q = (p + r) // 2  # q는 p, r의 중간 지점
            merge_sort(p, q)  # 전반부 정렬
            merge_sort(q + 1, r)  # 후반부 정렬
            merge(p, q, r)  # 병합

    def merge(p, q, r):
        global k, answer, save_count
        i = p
        j = q + 1

        if save_count == k:
            return

        tmp = deque()
        while i <= q and j <= r:
            if arr[i] <= arr[j]:
                tmp.append(arr[i])
                i += 1
            else:
                tmp.append(arr[j])
                j += 1

        while i <= q:  # 왼쪽 배열 부분이 남은 경우
            tmp.append(arr[i])
            i += 1
        while j <= r:  # 오른쪽 배열 부분이 남은 경우
            tmp.append(arr[j])
            j += 1
        i = p
        t = 0
        while i <= r and tmp:  # 결과를 arr[p..r]에 저장
            arr[i] = tmp.popleft()
            save_count += 1
            if save_count == k:
                answer = arr[i]
            i += 1
            t += 1

    merge_sort(0, n - 1)
    print(answer)


solution()
