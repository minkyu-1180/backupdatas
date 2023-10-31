# 백준 189. 점프
import sys
sys.stdin = open("bj1890input.txt")
import heapq
# N : 게임판의 가로 세로 길이(4 <= N <= 100)
N = int(input())

# 게임판
# 각 칸의 의미 : 현재 칸에서 갈 수 있는 거리(오른쪽으로 or 아래쪽으로만 이동 가능)
# 0 <= arr[i][j] <= 9
# 0 : 종착점
# 0,0 -> N-1, N-1로 갈 수 있는 경로 개수
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)] # dp[i][j] : 0, 0 -> i, j로 이동 가능한 경우의 수
dp[0][0] = 1 # (0, 0) -> (0, 0) : 1
visited = [[0] * N for _ in range(N)]

# last_visited[i][j] : (i, j)로 오기 위한 가장 최근 좌표 -> 이후 dp[i][j]에서 해당 좌표들의 dp값을 더해줄거임
last_visited = [[set() for _ in range(N)] for _ in range(N)]
visited[0][0] = 1 # 시작점 방문 처리
# print(visited)
que = []
dist = arr[0][0]
if dist < N:
    # que에 넣어주는 것 : (i+j, i, j)
    # heappop을 진행할 때, que 안에 들어있는 값들 중 (0, 0)과 가장 가까운 애들부터 뽑아내기 위해
    # 결국dp[i][j]를 확인하기 위해서는 (0, 0) ~ (i, j) 사이 값들을 봐야 하기 때문문
    que.append((dist, dist, 0))
    que.append((dist, 0, dist))
    last_visited[dist][0].add((0, 0))
    last_visited[0][dist].add((0, 0))

while que:
    # 가장 안쪽 범위에 있는 i, j 좌표 뽑아오기
    d, i, j = heapq.heappop(que)

    if visited[i][j]:
        continue
    # 방문 처리(뒤에서 dp값 갱신할 건데, 혹시 중복될까봐)
    visited[i][j] = 1
    # 뽑아온 값에 대해 dp 처리

    for y, x in last_visited[i][j]:
        dp[i][j] += dp[y][x]

    dist = arr[i][j]
    # dist = 0 --> 어차피 뒤에 과정은 최근 visited & que에 추가하는 과정이라 그냥 생략
    if dist == 0:
        continue

    # 범위 안에 포함 -> next (i, j)로 갈 수 있는 좌표로 포함시키고, 큐에 heappush
    if i + dist < N:
        last_visited[i+dist][j].add((i, j))
        heapq.heappush(que,(i+j+dist, i+dist, j))

    if j + dist < N:
        last_visited[i][j+dist].add((i, j))
        heapq.heappush(que, (i+j+dist, i, j+dist))


print(dp[N-1][N-1])

#
# for i in range(N):
#     for j in range(N):
#         dist = arr[i][j]
#         if dist == 0:
#             continue
#         if dist + i < N:
#             dp[dist+i][j] += dp[i][j]
#         if dist + j < N:
#             dp[i][dist+j] += dp[i][j]
# print(dp[N-1][N-1])
