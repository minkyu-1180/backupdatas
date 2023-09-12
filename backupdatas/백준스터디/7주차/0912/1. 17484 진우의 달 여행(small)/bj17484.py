import sys
sys.stdin = open("bj17484input.txt")
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 현재 row / 현재 col / 최근 dir / 현재 root에서 작은 값으로 인지하는 것 /
def dfs(i, j, last_dir, min_v, now):
    if i == N-1:
        return min(min_v, now)

    for k in [-1, 0, 1]:
        if last_dir != k:
            ni = i + 1
            nj = j + k
            if 0 <= ni < N and 0 <= nj < M:
                min_v = dfs(ni, nj, k, min_v, now + arr[ni][nj])

    return min_v

result = 600
for j in range(M):
    if result > dfs(0, j, 100, result, arr[0][j]):
        result = dfs(0, j, 100, result, arr[0][j])

print(result)