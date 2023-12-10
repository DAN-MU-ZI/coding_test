import sys

input = sys.stdin.readline


def solution():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [False for _ in range(n)]
    global score_diff
    score_diff = 100 * n

    def dfs(depth=0, idx=0):
        global score_diff

        if depth == n // 2:
            score = 0
            for i in range(n):
                for j in range(i, n):
                    if visited[i] and visited[j]:
                        score += arr[i][j] + arr[j][i]
                    elif not visited[i] and not visited[j]:
                        score -= arr[i][j] + arr[j][i]
            score_diff = min(score_diff, abs(score))
            if score_diff == 0:
                print(score_diff)
                exit()
            return

        for i in range(idx, n):
            if not visited[i]:
                visited[i] = True
                dfs(depth + 1, i + 1)
                visited[i] = False

    dfs()
    print(score_diff)


solution()
