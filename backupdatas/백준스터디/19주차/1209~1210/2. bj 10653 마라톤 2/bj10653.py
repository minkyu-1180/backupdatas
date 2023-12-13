# 백준 10653. 마라톤 2
import sys
sys.stdin = open("bj10653input.txt")

# N : 체크포인트의 수(3 <= N <= 500)
# K : 건너뛸 체크포인트의 수(K < N)
# 1번 체크포인트와 N번 체크포인트는 건너뛰기 X
N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)

# dists[i][j] : (i+1)번 체크포인트와 (j+1)번 체크포인트 사이의 거리
dists = [[0] * N for _ in range(N)]

# 최대 거리
max_dist = 0
for i in range(N):
    check1 = arr[i]
    if i < N-1:
        max_dist += abs(arr[i+1][0] - arr[i][0]) + abs(arr[i+1][1] - arr[i][1])
    for j in range(N):
        check2 = arr[j]
        dists[i][j] = abs(check2[0] - check1[0]) + abs(check2[1] - check1[1])
# 총 거리
# print(max_dist)
# dp[N-1][K] : N개의 체크포인트 중 K개를 건너뛰었을 때의 거리 최소값
dp = [[max_dist] * (K+1) for _ in range(N)]
dp[0][0] = 0
# 건너뛰는 체크포인트가 존재 X -> 그냥 dists합
for i in range(1, N):
    # i개의 체크포인트 중, 0개의 체크포인트 건너뛰기
    dp[i][0] = dp[i-1][0] + dists[i][i-1]

# 건너뛰는 체크포인트가 존재 O -> ?
for j in range(1, K+1):
    # 0개 중 j개 : nocase
    dp[0][j] = 0
    # 1개 중 j개 : 1개중 j-1개(다음턴에 바로 1개 추가)
    dp[1][j] = dp[1][j-1]
    # j개 중 j개
    dp[j][j] = dists[j][0]

    for i in range(1, N):
        # 현재 dp[i][j]를 구하기 위해 배열 범위에 해당되는 값들에 대해 초기화
        for k in range(j, 0, -1):
            if i-k-1 >= 0:
                # case 1 : k번 전에 있는 위치의 dp값 + 뒤의 k개 다 건너뛰지 않기
                dist1 = dp[i-k-1][j-k] + dists[i-k-1][i]
                # case 2 : 직전 체크포인트까지 j개 다 씀 -> i번 위치로 올 때 건너뛰지 않기
                dist2 = dp[i-1][j] + dists[i][i-1]
                dp[i][j] = min(dp[i][j], dist1, dist2)

print(dp[-1][-1])


