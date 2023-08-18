# sw academy 미로의 거리
import sys
sys.stdin = open("미로의거리input.txt")

# 시작 좌표의 row_idx, col_idx를 배열로 담아 반환하는 함수
def find_start(N, arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':  # 출발지점
                return [i, j]

# 시작점에서 끝점으로 가는 경로가 있을 경우, 경로의 최단거리를 반환하는 함수
# 없을 경우 0반환
def bfs(start, N):
    dists = [] # 3으로 가는 경로의 거리를 담을 배열
    visited = [[0] * N for _ in range(N)] # visited 생성(거리정보가 담김)
    queue = [] # 큐 생성
    # 시작점 enqueue & visited 표시
    queue.append(start)
    visited[start[0]][start[1]] = 1
    while queue:
        i, j = queue.pop(0)
        if arr[i][j] == '3':
            # 경로가 있을 경우, dists에 추가
            dists.append(visited[i][j] - 2) # 지나온 칸의 개수(start의 visited값은 1이라서)
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj] != '1': # 미로 내의 인덱스 / 벽이 아닌 경우
                queue.append([ni, nj])
                visited[ni][nj] = visited[i][j] + 1
    # 3으로 갈 수 있는 경로가 존재할 경우
    if dists:
        min_dist = 100 # 3까지의 거리를 담을 리스트

        # 모든 경로중 최단거리 구하기
        for dist in dists:
            if min_dist > dist:
                min_dist = dist
        return min_dist
    # 큐가 빌 때 까지 return되지 않은 경우(3에 도달할 수 없는 경우)
    return 0


T = int(input())
for test_case in range(1, T+1):
    N = int(input()) # 미로의 행/열 개수(5 <= N <= 100)
    arr = list(input() for _ in range(N)) # N x N 미로 정보
    '''
    '0' : 통로
    '1' : 벽
    '2' : 출발
    '3' : 도착
    '''

    # 시작좌표 구하기

    start = find_start(N, arr)
    # print(start, end)
    print(f'#{test_case} {bfs(start, N)}')





