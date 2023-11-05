# 백준 17836. 공주님을 구해라
import sys
sys.stdin = open("bj17836input.txt")
from collections import deque

def bfs():
    min_dist = 10001
    visited = [[-1] * M for _ in range(N)]
    que = deque()
    que.append((0, 0))
    visited[0][0] = 0

    while que:
        i, j = que.popleft()
        # 만약 검을 발견 -> 그냥 공주까지 최소거리가 dist
        if arr[i][j] == 2:
            min_dist = (N - 1 - i) + (M - 1 - j) + visited[i][j]

        # 공주에게 도달 -> 검을 이용하여 뜷고 간 거리와 비교
        if i == N-1 and j == M-1:
            return min(min_dist, visited[i][j])

        for di, dj in dir:
            ni = i+di
            nj = j+dj
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] != 1:
                if visited[ni][nj] == -1:
                    visited[ni][nj] = visited[i][j] + 1
                    que.append((ni, nj))

    # que가 빌 때 까지 공주에게 도달 실패 -> 기존 min_dist 입력
    return min_dist
# 원래 T는 없음
T = int(input())
for tc in range(T):
    # N, M : 성의 크기(3 <= N, M <= 100)
    # T : 공주에게 걸린 저주의 제한 시간 (1 <= T <= 10000)
    N, M, T = map(int, input().split())

    # 성의 구조
    # 0 : 빈 공간 / 1 : 마법의 벽 / 2 : 그람이 놓여있는 공간
    # 그람을 집는 순간, 벽 있어도 뜷기 가능
    # (0, 0), (N-1, M-1)는 무조건 0
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    # 목적 : (0, 0)에 있는 용사가 T시간 내에 공주에게 도달 가능시
    # 공주에게 도달할 수 있는 최단 시간
    # 불가능하면 Fail 출력
    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    result = bfs()
    # 결과값이 제한시간을 넘을 경우 -> 공주 사망
    if result > T:
        print('Fail')
    else:
        print(result)